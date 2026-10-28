#!/usr/bin/env python3
"""Generate a status table from EVIDENCE, never from hand-typed claims.

Usage:
    python3 ops/generate_status.py --evidence ops/status-evidence.json

The evidence file is a JSON object with one entry per repo, each entry
carrying ONLY facts that were observed (a test run, a CI run, a live
repo listing), each with its date and source, e.g.:

    {
      "investment-analyst-toolkit": {
        "version": "0.5.0",
        "tests_passed": 47, "tests_total": 47,
        "tests_date": "2026-10-28",
        "tests_evidence": "pytest run in a fresh venv, 28 Oct 2026",
        "ci": "GitHub Actions Tests, run #4 succeeded 28 Oct 2026",
        "live": "public, main"
      }
    }

Rules:
- A repo with no evidence entry is listed as UNKNOWN, never guessed.
- A count is printed only if tests_passed and tests_total are both
  present; otherwise the tests column reads "not evidenced".
- The script never invents a version, a count, or a live status.
- Output is a Markdown table on stdout, plus a one-line summary.
  The caller is responsible for saving it where it is published and
  for re-running it whenever the evidence changes.

This is the hybrid architecture's answer to the Phase 1 drift problem:
hardcoded numbers in READMEs rot; a generated table, fed only by
observed evidence, does not — provided nobody edits the output by hand
and then calls it generated.
"""

import argparse
import json
import sys


def render(evidence):
    lines = [
        "| Repo | Version | Tests | CI | Live status |",
        "|---|---|---|---|---|",
    ]
    for repo in sorted(evidence):
        e = evidence[repo] or {}
        version = e.get("version") or "—"
        if e.get("tests_passed") is not None and e.get("tests_total") is not None:
            tests = f"{e['tests_passed']}/{e['tests_total']}"
            if e.get("tests_date"):
                tests += f" ({e['tests_date']})"
        else:
            tests = "not evidenced"
        ci = e.get("ci") or "not evidenced"
        live = e.get("live") or "UNKNOWN"
        lines.append(f"| `{repo}` | {version} | {tests} | {ci} | {live} |")
    known = sum(1 for e in evidence.values() if e)
    lines.append("")
    lines.append(
        f"Repos listed: {len(evidence)}; with evidence: {known}; "
        f"without evidence (UNKNOWN): {len(evidence) - known}."
    )
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--evidence", required=True, help="JSON evidence file")
    args = parser.parse_args(argv)
    with open(args.evidence, encoding="utf-8") as fh:
        evidence = json.load(fh)
    if not isinstance(evidence, dict):
        print("evidence file must contain a JSON object", file=sys.stderr)
        return 2
    print(render(evidence))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
