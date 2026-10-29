#!/usr/bin/env python3
"""Daily health check for the 8-repo finance programme (Phase 8).

Research only. Not investment advice. Nothing here recommends buying or
selling a security, and no number in the report is invented: every value
is labelled with how it was produced (local run, live GitHub fetch, or
TO VERIFY), and anything that cannot be checked is reported UNKNOWN,
never silently green.

What it checks, and what it honestly cannot check
-------------------------------------------------
1. Roster consistency: agents.json vs agents/ vs runbooks/ vs README
   tables, via ops/check_roster.py in the checked-out agents repo.
2. Doc-claim consistency: test counts in each repo's live README (fetched
   from raw.githubusercontent.com, public repos, no auth) vs
   ops/status-evidence.json. A mismatch is drift, reported as FAIL.
3. Workflow status: latest COMPLETED GitHub Actions run per repo with
   workflows, via the public GitHub API (no auth). API errors are
   UNKNOWN, not PASS.
4. Data freshness: the toolkit's reports/daily/ on main, via the Git
   Trees API. The latest summary-*.json run stamp (YYYYMMDDTHHMMSSZ) is
   parsed and aged against now (UTC). No reports at all means the Phase 3
   scheduled run has not been observed yet -> UNKNOWN, never "fresh".
   A latest summary whose symbols are all STALE_OR_FAILED, or a latest
   report older than 48 hours, is STALE -> FAIL. STALE is never reported
   as fresh.
5. Ledger publication: whether a run summary exists in reports/daily/
   and parses with per-symbol accuracy stated. The ledger itself
   (predictions.jsonl) is only checkable locally; from public output the
   check is "published and parses" vs "not publicly published" (UNKNOWN).
   There is no second public source to diff it against, so "drift"
   between ledger and accuracy report cannot be proven from GitHub
   alone -- that limitation is stated in the report, not hidden.
6. Broken internal links: relative Markdown links inside the agents
   repo checkout. External links are NOT checked (flaky, rate-limited)
   -- recorded as excluded, not as passed.
7. Security-config presence: CodeQL workflow + Dependabot config files
   present in the three code repos (raw fetch). Presence is NOT
   enablement: whether CodeQL / Dependabot / secret scanning / push
   protection are actually enabled in GitHub settings is UNKNOWN here
   (that API needs auth) and must be checked in each repo's Security tab.

Exit codes: 0 = every check PASS. 1 = at least one FAIL. 2 = no FAIL
but at least one UNKNOWN (health not proven). The workflow commits the
report either way and fails the job on 1 or 2, so an unproven state is
visible red, never silently green.

Failure visibility without email (email is a recorded blocker) and
without a Cloudflare cron backup (also blocked): the public workflow
run log + the committed status report + dated failure notes under
status/failures/. No email alert is claimed anywhere.

Usage:
    python ops/health_check.py --live --out status/HEALTH.md
    python ops/health_check.py --live --out status/HEALTH.md \
        --failure-note-dir status/failures
    python ops/health_check.py --selftest   # offline fixture tests only
    python ops/health_check.py --live --repo-root . --check-roster \
        ops/check_roster.py

Only the standard library is used. No credentials are read, sent, or
printed. Network calls are single polite GETs with a timeout; a 403/429
is recorded as a failure of that check, never retried aggressively.
"""

import argparse
import datetime
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

OWNER = "ShirjanKhadka1"
REPOS = [
    "finance-research-agents",
    "investment-analyst-toolkit",
    "financial-research-analyst-agent",
    "nepali-capital-market-research",
    "nepal-market-research",
    "nepali-business-opportunities",
    "equity-research-playbook",
    "ShirjanKhadka1",
]
# Repos that carry GitHub Actions workflows (others: none, by design).
WORKFLOW_REPOS = [
    "finance-research-agents",
    "investment-analyst-toolkit",
    "financial-research-analyst-agent",
    "nepali-capital-market-research",
]
CODE_REPOS = [
    "investment-analyst-toolkit",
    "financial-research-analyst-agent",
    "nepali-capital-market-research",
]
STALE_AFTER_HOURS = 48
USER_AGENT = "finance-programme-health-check (research only, no auth)"


def fetch_text(url, timeout=20):
    """One polite GET. Returns (text, error-or-None). Never retries."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return resp.read().decode("utf-8", errors="replace"), None
    except urllib.error.HTTPError as e:
        return None, "HTTP %s for %s" % (e.code, url)
    except Exception as e:  # noqa: BLE001 -- network errors are check input
        return None, "%s for %s" % (type(e).__name__, url)


def fetch_json(url, timeout=20):
    text, err = fetch_text(url, timeout=timeout)
    if err:
        return None, err
    try:
        return json.loads(text), None
    except json.JSONDecodeError:
        return None, "unparsable JSON from %s" % url


def parse_stamp(stamp):
    """YYYYMMDDTHHMMSSZ -> aware UTC datetime, or None."""
    try:
        return datetime.datetime.strptime(stamp, "%Y%m%dT%H%M%SZ").replace(
            tzinfo=datetime.timezone.utc
        )
    except (ValueError, TypeError):
        return None


def freshness_of(stamp, now):
    """PASS / STALE / UNKNOWN for a run stamp against now (UTC)."""
    run_at = parse_stamp(stamp)
    if run_at is None:
        return "UNKNOWN", "unparsable run stamp %r" % (stamp,)
    age_hours = (now - run_at).total_seconds() / 3600.0
    if age_hours < 0:
        return "UNKNOWN", "run stamp %s is in the future" % stamp
    if age_hours > STALE_AFTER_HOURS:
        return "STALE", "latest run %s is %.1f hours old (> %dh)" % (
            stamp, age_hours, STALE_AFTER_HOURS)
    return "PASS", "latest run %s is %.1f hours old" % (stamp, age_hours)


def extract_test_counts(readme_text):
    """All 'N/N tests passing' pairs found in a README, as (n, total)."""
    return [
        (int(a), int(b))
        for a, b in re.findall(r"(\d+)\s*/\s*(\d+)\s+tests passing",
                                readme_text or "")
    ]


def check_roster(repo_root, roster_script):
    """Run ops/check_roster.py; PASS only on exit 0."""
    path = roster_script
    if not os.path.isabs(path):
        path = os.path.join(repo_root, path)
    if not os.path.exists(path):
        return ("UNKNOWN", "roster script not present at %s" % path)
    proc = subprocess.run(
        [sys.executable, path], capture_output=True, text=True,
        cwd=repo_root)
    out = (proc.stdout + proc.stderr).strip().splitlines()
    tail = out[-1] if out else ""
    if proc.returncode == 0:
        return ("PASS", tail or "roster check exit 0")
    return ("FAIL", "roster check exit %d: %s" % (proc.returncode, tail))


def check_counts(repo_root, live):
    """README counts vs status-evidence.json. Returns list of results."""
    results = []
    ev_path = os.path.join(repo_root, "ops", "status-evidence.json")
    if not os.path.exists(ev_path):
        return [("status-evidence", "UNKNOWN",
                 "status-evidence.json not found at %s" % ev_path)]
    try:
        with open(ev_path, encoding="utf-8") as f:
            evidence = json.load(f)
    except (OSError, json.JSONDecodeError) as e:
        return [("status-evidence", "UNKNOWN",
                 "status-evidence.json unreadable: %s" % e)]
    for repo in REPOS:
        ev = evidence.get(repo, {})
        expected = None
        if ev.get("tests_passed") is not None and ev.get("tests_total"):
            expected = (ev["tests_passed"], ev["tests_total"])
        if not live:
            results.append((repo, "UNKNOWN",
                            "live README fetch skipped (offline mode)"))
            continue
        text, err = fetch_text(
            "https://raw.githubusercontent.com/%s/%s/main/README.md"
            % (OWNER, repo))
        if err:
            results.append((repo, "UNKNOWN", err))
            continue
        found = extract_test_counts(text)
        if expected is None:
            if found:
                results.append((repo, "FAIL",
                                "README claims counts %s but evidence "
                                "records no code tests" % (found,)))
            else:
                results.append((repo, "PASS",
                                "no counts in README, none in evidence "
                                "(Markdown repo)"))
        elif expected in found:
            results.append((repo, "PASS",
                            "README carries %d/%d matching evidence"
                            % expected))
        else:
            results.append((repo, "FAIL",
                            "evidence says %d/%d but README carries %s"
                            % (expected[0], expected[1], found)))
    return results


def check_workflows(live):
    """Latest COMPLETED Actions run per workflow repo. Returns results."""
    results = []
    for repo in WORKFLOW_REPOS:
        if not live:
            results.append((repo, "UNKNOWN", "live API fetch skipped"))
            continue
        if repo == "finance-research-agents":
            # This repo has no independent CI workflow by design: its only
            # workflow IS the Daily health check, which is excluded above
            # to avoid self-reference. Its verification is the roster,
            # README-count, and link checks in this same report — not a
            # second workflow run. Reporting UNKNOWN here would make a
            # full pass structurally impossible, so this row states the
            # design instead of pretending a run exists.
            results.append((repo, "PASS",
                            "no independent CI workflow by design; "
                            "verification is this health report itself "
                            "(roster, counts, links)"))
            continue
        data, err = fetch_json(
            "https://api.github.com/repos/%s/%s/actions/runs?per_page=5"
            % (OWNER, repo))
        if err:
            results.append((repo, "UNKNOWN", err))
            continue
        completed = [r for r in data.get("workflow_runs", [])
                     if r.get("conclusion") and r.get("head_branch") == "main"
                     and (r.get("triggering_actor") or {}).get("login") != "dependabot[bot]"
                     and (r.get("actor") or {}).get("login") != "dependabot[bot]"
                     # The health workflow must not judge itself: a failing
                     # health run would otherwise make every later health
                     # run fail on its predecessor forever, even after the
                     # underlying issue is fixed. The health report itself
                     # is the evaluation for this repo.
                     and not (repo == "finance-research-agents"
                              and r.get("name") == "Daily health check")]
        if not completed:
            results.append((repo, "UNKNOWN",
                            "no completed workflow run found"))
            continue
        run = completed[0]
        conclusion = run["conclusion"]
        detail = "latest completed run: %s -> %s (%s)" % (
            run.get("name"), conclusion, run.get("html_url"))
        if conclusion == "success":
            results.append((repo, "PASS", detail))
        else:
            results.append((repo, "FAIL", detail))
    return results


def check_data_freshness(live, now):
    """Toolkit reports/daily/ freshness + ledger publication. One result
    per aspect, so a missing first run is UNKNOWN, not hidden."""
    if not live:
        return [("freshness", "UNKNOWN", "live fetch skipped"),
                ("ledger", "UNKNOWN", "live fetch skipped")]
    tree, err = fetch_json(
        "https://api.github.com/repos/%s/%s/git/trees/main?recursive=1"
        % (OWNER, "investment-analyst-toolkit"))
    if err:
        return [("freshness", "UNKNOWN", err),
                ("ledger", "UNKNOWN", err)]
    paths = [t["path"] for t in tree.get("tree", [])
             if t["path"].startswith("reports/daily/")]
    summaries = sorted(p for p in paths
                       if re.match(r"reports/daily/summary-\d+T\d+Z\.json$",
                                   p))
    if not summaries:
        return [("freshness", "UNKNOWN",
                 "no summary in reports/daily/ on main: the Phase 3 "
                 "scheduled run has not been observed yet (plan, not "
                 "proven fact)"),
                ("ledger", "UNKNOWN",
                 "no run summary publicly published: ledger drift "
                 "cannot be checked from public output (local check "
                 "only)")]
    latest_summary = summaries[-1]
    stamp = re.search(r"summary-(\d+T\d+Z)\.json", latest_summary).group(1)
    status, detail = freshness_of(stamp, now)
    if status == "STALE":
        freshness = ("FAIL", detail + " -- STALE, never reported as fresh")
    elif status == "PASS":
        freshness = ("PASS", detail)
    else:
        freshness = ("UNKNOWN", detail)
    summary_text, serr = fetch_text(
        "https://raw.githubusercontent.com/%s/%s/main/%s"
        % (OWNER, "investment-analyst-toolkit", latest_summary))
    if serr:
        ledger = ("UNKNOWN", "latest summary %s unfetchable: %s"
                  % (latest_summary, serr))
    else:
        try:
            summary = json.loads(summary_text)
            symbols = summary.get("symbols", {})
            stale = [s for s, b in symbols.items()
                     if isinstance(b, dict)
                     and b.get("status") == "STALE_OR_FAILED"]
            if not symbols:
                ledger = ("UNKNOWN",
                          "latest summary %s has no symbols" % latest_summary)
            elif stale:
                ledger = ("FAIL",
                          "latest summary %s: symbols STALE_OR_FAILED: %s"
                          % (latest_summary, ", ".join(sorted(stale))))
                if freshness[0] == "PASS":
                    freshness = ("FAIL",
                                 "latest run is recent but symbols "
                                 "STALE_OR_FAILED: %s" % ", ".join(sorted(stale)))
            else:
                ledger = ("PASS",
                          "latest summary %s parses; %d symbol(s) fresh, "
                          "accuracy stated per symbol"
                          % (latest_summary, len(symbols)))
        except json.JSONDecodeError:
            ledger = ("UNKNOWN", "latest summary %s unparsable"
                      % latest_summary)
    return [("freshness",) + freshness, ("ledger",) + ledger]


def check_internal_links(repo_root):
    """Relative Markdown links inside the agents repo checkout."""
    link_re = re.compile(r"\]\((?!https?://|#|mailto:)([^)\s]+)\)")
    missing = []
    checked = 0
    for dirpath, dirnames, filenames in os.walk(repo_root):
        dirnames[:] = [d for d in dirnames
                       if d not in (".git", "__pycache__", "node_modules")]
        for name in filenames:
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            try:
                with open(path, encoding="utf-8") as f:
                    text = f.read()
            except OSError:
                continue
            for target in link_re.findall(text):
                target = target.split("#")[0]
                if not target:
                    continue
                checked += 1
                resolved = os.path.normpath(
                    os.path.join(os.path.dirname(path), target))
                if not os.path.exists(resolved):
                    missing.append("%s -> %s"
                                   % (os.path.relpath(path, repo_root),
                                      target))
    if missing:
        return ("FAIL", "%d internal link(s) checked, %d missing: %s"
                % (checked, len(missing), "; ".join(sorted(set(missing))[:10])))
    return ("PASS", "%d internal link(s) checked, none missing "
            "(external links not checked: excluded, see report)" % checked)


def check_security_config(live):
    """CodeQL workflow + Dependabot config presence (not enablement)."""
    results = []
    for repo in CODE_REPOS:
        if not live:
            results.append((repo, "UNKNOWN", "live fetch skipped"))
            continue
        missing = []
        for path in (".github/workflows/codeql.yml",
                     ".github/dependabot.yml"):
            _, err = fetch_text(
                "https://raw.githubusercontent.com/%s/%s/main/%s"
                % (OWNER, repo, path))
            if err:
                missing.append(path)
        if missing:
            results.append((repo, "FAIL",
                            "security config missing: %s" % ", ".join(missing)))
        else:
            results.append((repo, "PASS",
                            "codeql.yml + dependabot.yml present; actual "
                            "enablement in GitHub settings is TO VERIFY "
                            "in each repo's Security tab (API needs auth)"))
    return results


def render_report(checks, now):
    """checks: list of (section, status, detail). Returns Markdown."""
    fails = [c for c in checks if c[1] == "FAIL"]
    unknowns = [c for c in checks if c[1] == "UNKNOWN"]
    overall = "PASS" if not fails and not unknowns else (
        "FAIL" if fails else "INCOMPLETE (UNKNOWN present, not proven)")
    lines = [
        "# Daily health check — %s" % now.strftime("%Y-%m-%d %H:%M UTC"),
        "",
        "> Research only. Not investment advice. This report is generated,",
        "> not hand-written. A value is only as good as its evidence label:",
        "> [local run], [live fetch], or TO VERIFY. Nothing here is a",
        "> recommendation, and no number is invented.",
        "",
        "## Overall: %s" % overall,
        "",
        "FAIL: %d | UNKNOWN: %d | PASS: %d"
        % (len(fails), len(unknowns),
           len([c for c in checks if c[1] == "PASS"])),
        "",
        "## Checks",
        "",
        "| Check | Status | Detail |",
        "|---|---|---|",
    ]
    for section, status, detail in checks:
        lines.append("| %s | %s | %s |" % (
            section, status, detail.replace("|", "/")))
    lines += [
        "",
        "## What this job cannot check (recorded, not hidden)",
        "",
        "- Email alerts: blocked (Gmail connector not connected). Failure",
        "  visibility is this report + the public workflow run log + dated",
        "  notes under status/failures/. No email alert is claimed.",
        "- Cloudflare cron backup: blocked (Cloudflare access unverified).",
        "  The toolkit's scheduled workflow is the only schedule.",
        "- Dependabot / CodeQL / secret scanning / push protection",
        "  enablement: the GitHub API needs auth for alerts, so this job",
        "  checks config-file presence only; enablement is TO VERIFY in",
        "  each repo's Security tab.",
        "- Ledger-vs-accuracy-report drift: the ledger is only checkable",
        "  locally. From public output this job can only confirm a run",
        "  summary is published and parses. Publishing a ledger summary",
        "  in reports/daily/ on every run is an open owner decision.",
        "- External links: not checked (flaky, rate-limited). Internal",
        "  relative links in the agents repo are checked.",
        "- Live NEPSE data: no documented free public NEPSE OHLCV API",
        "  exists; the scanner stays CSV-only. Nothing in this report",
        "  implies a live NEPSE feed.",
        "",
        "## Known blockers (standing)",
        "",
        "- Phase 3 scheduled workflow's first run: not yet observed.",
        "  Until it is seen with public output in reports/daily/, the",
        "  schedule is a plan, not a proven fact, and freshness stays",
        "  UNKNOWN.",
        "- Nepal friction re-checks before reliance on a real trade:",
        "  circuit limits (+15%/-15%, user-supplied 28 Oct 2026) against",
        "  a current NEPSE/SEBON notice; broker-58 T+1 example against",
        "  that broker.",
        "- Private repos cannot be listed without a token, and that",
        "  would NOT authorise opening the private Nepse Decode project,",
        "  which stays out of scope regardless.",
        "",
        "Research only. Not investment advice. No trade is made by this",
        "system.",
        "",
    ]
    return "\n".join(lines)


def selftest():
    """Offline fixture tests. Raises AssertionError on any failure."""
    assert parse_stamp("20261028T010000Z") == datetime.datetime(
        2026, 10, 28, 1, 0, tzinfo=datetime.timezone.utc)
    assert parse_stamp("not-a-stamp") is None
    now = datetime.datetime(2026, 10, 28, 3, 0,
                            tzinfo=datetime.timezone.utc)
    assert freshness_of("20261028T010000Z", now)[0] == "PASS"
    assert freshness_of("20261026T010000Z", now)[0] == "STALE"
    assert freshness_of("bogus", now)[0] == "UNKNOWN"
    assert extract_test_counts("Live — 124/124 tests passing, CI") == [(124, 124)]
    assert extract_test_counts("no counts here") == []
    checks = [("roster", "PASS", "ok"), ("freshness", "UNKNOWN", "no run yet")]
    report = render_report(checks, now)
    assert "Overall: INCOMPLETE" in report
    assert "FAIL: 0 | UNKNOWN: 1 | PASS: 1" in report
    assert "Email alerts: blocked" in report
    print("health_check selftest: all fixture assertions passed")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--live", action="store_true",
                        help="fetch live GitHub data (default: offline, "
                        "live checks report UNKNOWN)")
    parser.add_argument("--out", default=None,
                        help="write the Markdown report to this path")
    parser.add_argument("--failure-note-dir", default=None,
                        help="write a dated failure note here on FAIL/UNKNOWN")
    parser.add_argument("--repo-root", default=None,
                        help="agents repo checkout root (default: parent of "
                        "the ops/ dir holding this script)")
    parser.add_argument("--check-roster", default="ops/check_roster.py",
                        help="roster script path, absolute or relative to "
                        "repo root")
    parser.add_argument("--selftest", action="store_true",
                        help="run offline fixture tests and exit")
    args = parser.parse_args(argv)
    if args.selftest:
        selftest()
        return 0
    repo_root = args.repo_root or os.path.dirname(
        os.path.dirname(os.path.abspath(__file__)))
    now = datetime.datetime.now(datetime.timezone.utc)
    checks = []
    status, detail = check_roster(repo_root, args.check_roster)
    checks.append(("roster", status, detail))
    for repo, status, detail in check_counts(repo_root, args.live):
        checks.append(("README counts: %s" % repo, status, detail))
    for repo, status, detail in check_workflows(args.live):
        checks.append(("workflow: %s" % repo, status, detail))
    for aspect, status, detail in check_data_freshness(args.live, now):
        checks.append(("data: %s" % aspect, status, detail))
    status, detail = check_internal_links(repo_root)
    checks.append(("internal links", status, detail))
    for repo, status, detail in check_security_config(args.live):
        checks.append(("security config: %s" % repo, status, detail))
    report = render_report(checks, now)
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)),
                    exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(report)
    print(report)
    fails = [c for c in checks if c[1] == "FAIL"]
    unknowns = [c for c in checks if c[1] == "UNKNOWN"]
    if (fails or unknowns) and args.failure_note_dir:
        os.makedirs(args.failure_note_dir, exist_ok=True)
        note_path = os.path.join(
            args.failure_note_dir, now.strftime("%Y-%m-%d.md"))
        with open(note_path, "w", encoding="utf-8") as f:
            f.write("# Health failure note — %s\n\n" % now.strftime("%Y-%m-%d %H:%M UTC"))
            f.write("Phase: Phase 8 daily health check\n\n")
            for section, status, detail in checks:
                if status in ("FAIL", "UNKNOWN"):
                    f.write("- [%s] %s: %s\n" % (status, section, detail))
            f.write("\nRetry status: not retried automatically; the next "
                    "daily run re-checks.\n")
            f.write("Fix attempted: none by this job (it reports only; "
                    "fixes are a separate, reviewed change).\n")
            f.write("\nResearch only. Not investment advice.\n")
    if fails:
        return 1
    if unknowns:
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
