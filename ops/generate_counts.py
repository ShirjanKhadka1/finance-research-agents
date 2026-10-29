#!/usr/bin/env python3
"""Round 3 counter for finance-research-agents (Markdown pack, no tests).

Counts real files, never a typed constant:
- agents = agents/*.md excluding WHEN-TO-USE.md (the guide, not an agent)
- runbooks = runbooks/*.md
- templates = templates/*.md
- agents_json_entries = entries in agents.json (agents + 1 guide file)
Writes ops/status.json.
"""
import argparse
import json
from datetime import date
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=str(Path(__file__).resolve().parent.parent))
    root = Path(ap.parse_args().root)
    agents = [f for f in (root / "agents").glob("*.md") if f.name != "WHEN-TO-USE.md"]
    runbooks = list((root / "runbooks").glob("*.md"))
    templates = list((root / "templates").glob("*.md"))
    roster = json.loads((root / "agents.json").read_text(encoding="utf-8"))
    status = {
        "repo": "finance-research-agents",
        "agents": len(agents),
        "runbooks": len(runbooks),
        "templates": len(templates),
        "agents_json_entries": len(roster.get("agents", [])),
        "guide_files_excluded_from_agents": ["WHEN-TO-USE.md"],
        "generated_by": "ops/generate_counts.py (Round 3: file counts from disk)",
        "generated_at": date.today().isoformat(),
        "method": "agents counted as agents/*.md minus WHEN-TO-USE.md; "
                  "runbooks/templates counted as *.md in their folders; "
                  "agents.json entries counted from the file",
    }
    (root / "ops" / "status.json").write_text(json.dumps(status, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(status, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
