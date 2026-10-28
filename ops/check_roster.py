#!/usr/bin/env python3
"""Roster-consistency check for finance-research-agents.

Verifies, against the repo on disk (default: the sibling
finance-research-agents directory, overridable with --repo):
  1. Every agent file in agents/ is listed in agents.json, and vice versa.
  2. Every runbook file in runbooks/ is listed in agents.json, and vice versa.
  3. The README roster table lists every agent slug (by file link).
  4. The README runbook table lists every runbook slug (by file link).

Exit 0 only if all four checks pass; otherwise prints each mismatch
and exits 1. No network, no GitHub API — this is a disk check, so it
can run in CI on every push and catch the Phase 1 drift (7 vs 10 agents,
3 vs 4 runbooks) before it ships again.
"""

import argparse
import json
import re
import sys
from pathlib import Path


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo",
        default=None,
        help="Path to finance-research-agents (default: ../finance-research-agents)",
    )
    args = parser.parse_args(argv)
    repo = Path(args.repo) if args.repo else Path(__file__).resolve().parent.parent / "finance-research-agents"
    errors = []

    agents_json = json.loads((repo / "agents.json").read_text(encoding="utf-8"))
    json_agents = {a["file"] for a in agents_json.get("agents", [])}
    json_runbooks = {r["file"] for r in agents_json.get("runbooks", [])}
    disk_agents = {f"agents/{p.name}" for p in (repo / "agents").glob("*.md")}
    disk_runbooks = {f"runbooks/{p.name}" for p in (repo / "runbooks").glob("*.md")}

    for label, disk, listed in (
        ("agents", disk_agents, json_agents),
        ("runbooks", disk_runbooks, json_runbooks),
    ):
        for f in sorted(disk - listed):
            errors.append(f"{label}: on disk but missing from agents.json: {f}")
        for f in sorted(listed - disk):
            errors.append(f"{label}: in agents.json but missing on disk: {f}")

    readme = (repo / "README.md").read_text(encoding="utf-8")
    for f in sorted(disk_agents):
        if f"({f})" not in readme:
            errors.append(f"README roster table missing agent link: {f}")
    for f in sorted(disk_runbooks):
        if f"({f})" not in readme:
            errors.append(f"README runbook table missing runbook link: {f}")

    print(f"agents on disk: {len(disk_agents)}, in agents.json: {len(json_agents)}")
    print(f"runbooks on disk: {len(disk_runbooks)}, in agents.json: {len(json_runbooks)}")
    if errors:
        print("FAIL:")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("PASS: roster consistent (agents, runbooks, README tables all match).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
