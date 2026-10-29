#!/usr/bin/env python3
"""Round 3 programme-wide status generator (ops host repo).

Counts real things across programme checkouts, never a typed constant.
Usage:
    python3 ops/generate_programme_status.py [--repos-root DIR]
    # default repos-root: the parent of this repo (the usual
    # ~/workspace/github-repos layout, one folder per repo).

For each code repo it runs pytest --collect-only and parses the real
collected count (with PYTHONPATH set for the toolkit, whose tests import
the package); for Markdown repos it counts real files. A repo whose
checkout is missing from --repos-root is recorded as TO VERIFY (null),
never guessed. Writes ops/status.json -- but note ops/status.json as
shipped by ops/generate_counts.py covers THIS repo only; this script
writes ops/programme-status.json so the two never overwrite each other.
"""
import argparse
import json
import re
import subprocess
import sys
from datetime import date
from pathlib import Path


def collect_pytest(repo_dir, test_subdir, use_pythonpath=False):
    env = {"PYTHONPATH": str(repo_dir)} if use_pythonpath else None
    import os
    e = dict(os.environ)
    if env:
        e.update(env)
    r = subprocess.run([sys.executable, "-m", "pytest", test_subdir, "--collect-only", "-q"],
                       cwd=repo_dir, env=e, capture_output=True, text=True)
    m = re.search(r"(\d+) tests? collected", r.stdout + r.stderr)
    return int(m.group(1)) if m else None


def count_files(d, pattern):
    return len(list(d.glob(pattern))) if d.is_dir() else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--repos-root", default=None)
    args = ap.parse_args()
    here = Path(__file__).resolve().parent.parent
    root = Path(args.repos_root) if args.repos_root else here.parent
    out = {}

    def entry(name, **kw):
        d = {"repo": name, "generated_at": date.today().isoformat()}
        d.update(kw)
        out[name] = d

    agents = root / "finance-research-agents"
    if agents.is_dir():
        entry("finance-research-agents",
              agents=len([f for f in (agents / "agents").glob("*.md")
                          if f.name != "WHEN-TO-USE.md"]),
              runbooks=count_files(agents / "runbooks", "*.md"))
    else:
        entry("finance-research-agents", agents=None, runbooks=None,
              note="TO VERIFY: checkout not present under --repos-root")
    tk = root / "investment-analyst-toolkit"
    if tk.is_dir():
        ver = None
        try:
            import tomllib
            ver = tomllib.loads((tk / "pyproject.toml").read_text())["project"]["version"]
        except Exception:
            pass
        entry("investment-analyst-toolkit", version=ver,
              tests=collect_pytest(tk, "tests", use_pythonpath=True))
    else:
        entry("investment-analyst-toolkit", version=None, tests=None,
              note="TO VERIFY: checkout not present under --repos-root")
    an = root / "financial-research-analyst-agent"
    entry("financial-research-analyst-agent",
          tests=collect_pytest(an, "tests") if an.is_dir() else None)
    cap = root / "nepali-capital-market-research"
    # scanner tests live in scanner/tests; collect from the scanner dir
    if (cap / "scanner").is_dir():
        entry("nepali-capital-market-research",
              scanner_tests=collect_pytest(cap / "scanner", "tests"))
    else:
        entry("nepali-capital-market-research", scanner_tests=None,
              note="TO VERIFY: checkout not present under --repos-root")
    pb = root / "equity-research-playbook"
    if pb.is_dir():
        entry("equity-research-playbook", tests=collect_pytest(pb, "tests"),
              templates=count_files(pb / "templates", "*.md"))
    else:
        entry("equity-research-playbook", tests=None, templates=None,
              note="TO VERIFY: checkout not present under --repos-root")
    nm = root / "nepal-market-research"
    if nm.is_dir():
        entry("nepal-market-research",
              case_studies=len([d for d in (nm / "case-studies").iterdir() if d.is_dir()]),
              datasets=count_files(nm / "data", "*.csv"))
    else:
        entry("nepal-market-research", case_studies=None, datasets=None,
              note="TO VERIFY: checkout not present under --repos-root")
    bo = root / "nepali-business-opportunities"
    if bo.is_dir():
        entry("nepali-business-opportunities",
              sectors=count_files(bo / "sectors", "*.md"))
    else:
        entry("nepali-business-opportunities", sectors=None,
              note="TO VERIFY: checkout not present under --repos-root")
    doc = {
        "generated_by": "ops/generate_programme_status.py (Round 3)",
        "generated_at": date.today().isoformat(),
        "method": "pytest --collect-only counts and file counts from the checkouts "
                  "under --repos-root; missing checkouts are null/TO VERIFY, never guessed",
        "repos": out,
    }
    (here / "ops" / "programme-status.json").write_text(json.dumps(doc, indent=2) + "\n")
    print(json.dumps(doc, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
