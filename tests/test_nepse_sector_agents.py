"""Structural tests for the Engine 1.8 NEPSE sector-agent library (Phase 1).

Eight new agents deepen the NEPSE Fundamentals sector guidance into one
agent per sector/topic (bank, hydropower, insurance, microfinance, mutual
funds/NAV, IPO, fees & tax, content writing). Four requested roles were
NOT added because the pack already covers them — corporate actions
(nepse-corporate-actions-analyst), macro (nepse-macro-analyst), risk
(nepse-risk-team + risk-stance-analyst), orchestrator
(research-orchestrator) — and the tests below assert those duplicates
were not created.

No LLM is needed: these check the agent files' own structure, the
SKILL.md mirrors, and the roster counts.
"""

import json
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

NEW_AGENTS = [
    "nepse-bank-analyst",
    "nepse-hydropower-analyst",
    "nepse-insurance-analyst",
    "nepse-microfinance-analyst",
    "nepse-mutual-fund-nav-analyst",
    "nepse-ipo-analyst",
    "nepse-fees-and-tax-analyst",
    "nepse-content-writer",
]

# Requested roles already covered by an existing agent: the covering file
# must exist exactly once in the roster — no second file was created.
COVERED_BY_EXISTING = {
    "nepse-corporate-actions-analyst": "nepse-corporate-actions-analyst.md (engine 1.3)",
    "nepse-macro-analyst": "nepse-macro-analyst.md (engine 1.3)",
    "nepse-risk-analyst": "covered by nepse-risk-team.md + risk-stance-analyst.md",
    "nepse-orchestrator": "covered by research-orchestrator.md",
}
# Slugs that must not exist at all (no covering agent file of that name).
NOT_CREATED = ["nepse-risk-analyst", "nepse-orchestrator"]

REQUIRED_SECTIONS = [
    "## Identity", "## Mission", "## Core rules", "## Workflow",
    "## Deliverable format", "## Example prompt", "## Inputs",
    "## Outputs", "## Success metrics", "## Falsifier",
    "## LLM flexibility",
]


@pytest.mark.parametrize("slug", NEW_AGENTS)
def test_agent_file_has_required_sections(slug):
    text = (ROOT / "agents" / f"{slug}.md").read_text(encoding="utf-8")
    assert text.startswith("---\nname: " + slug + "\n")
    for section in REQUIRED_SECTIONS:
        assert section in text, f"{slug} missing {section}"
    assert "```yaml" in text, f"{slug} has no structured-output schema"
    assert "Research only, not investment advice" in text


@pytest.mark.parametrize("slug", NEW_AGENTS)
def test_agent_states_llm_flexibility_and_rules_mode(slug):
    text = (ROOT / "agents" / f"{slug}.md").read_text(encoding="utf-8")
    assert "Ollama" in text
    assert "rules_mode" in text or "rules mode" in text
    assert "API key" in text
    assert "never" in text.lower()  # never a recommendation / never an order


@pytest.mark.parametrize("slug", NEW_AGENTS)
def test_workflow_is_not_a_copy_of_core_rules(slug):
    text = (ROOT / "agents" / f"{slug}.md").read_text(encoding="utf-8")
    workflow = text.split("## Workflow")[1].split("## Deliverable")[0].strip()
    rules = text.split("## Core rules")[1].split("## Workflow")[0].strip()
    assert workflow != rules, f"{slug}: Workflow duplicates Core rules"


def test_fees_agent_carries_sourced_friction_figures():
    text = (ROOT / "agents" / "nepse-fees-and-tax-analyst.md").read_text(encoding="utf-8")
    for figure in ("0.36", "0.015", "25", "3.75", "T+2"):
        assert figure in text, f"fees agent missing sourced figure {figure}"
    assert "2026-10-28" in text  # user-supplied frictions, as-of date


def test_ipo_agent_never_uses_grey_market_numbers():
    text = (ROOT / "agents" / "nepse-ipo-analyst.md").read_text(encoding="utf-8")
    assert "grey_market_flags" in text
    assert "never quotes one" in text.lower()


def test_mutual_fund_agent_marks_premium_discount_derived():
    text = (ROOT / "agents" / "nepse-mutual-fund-nav-analyst.md").read_text(encoding="utf-8")
    assert "premium_discount_to_nav_pct" in text
    assert "DERIVED" in text


def test_content_writer_forbids_value_language():
    text = (ROOT / "agents" / "nepse-content-writer.md").read_text(encoding="utf-8")
    assert "value_language_found" in text
    assert "cheap" in text.lower()


@pytest.mark.parametrize("slug", NEW_AGENTS)
def test_skill_mirror_exists_and_matches_agent(slug):
    skill = ROOT / "skills" / slug / "SKILL.md"
    assert skill.is_file(), f"missing skills/{slug}/SKILL.md"
    text = skill.read_text(encoding="utf-8")
    assert text.startswith("---\nname: " + slug + "\n")
    agent = (ROOT / "agents" / f"{slug}.md").read_text(encoding="utf-8")
    # Same content: identity paragraph and mission appear in both files.
    identity = agent.split("## Identity")[1].split("## Mission")[0].strip()
    assert identity in text, f"{slug}: SKILL.md identity differs from agent"
    assert "agents/" + slug + ".md" in text  # canonical-file pointer


@pytest.mark.parametrize("slug", COVERED_BY_EXISTING)
def test_requested_role_not_duplicated(slug):
    roster = json.loads((ROOT / "agents.json").read_text(encoding="utf-8"))
    entries = [a for a in roster["agents"] if a["slug"] == slug]
    if slug in NOT_CREATED:
        assert not (ROOT / "agents" / f"{slug}.md").exists(), (
            f"{slug} must not exist: {COVERED_BY_EXISTING[slug]}")
        assert entries == [], f"{slug} must have no roster entry"
    else:
        # The covering agent exists (that is the point); exactly one
        # roster entry, no second file created for the same role.
        assert (ROOT / "agents" / f"{slug}.md").is_file()
        assert len(entries) == 1, f"{slug}: want exactly 1 roster entry"
    assert not (ROOT / "skills" / slug).exists(), (
        f"no skill mirror for skipped role {slug}")


def test_roster_counts_36_agents():
    disk = [f for f in (ROOT / "agents").glob("*.md") if f.name != "WHEN-TO-USE.md"]
    assert len(disk) == 36, f"agents on disk: {len(disk)}, want 36"
    roster = json.loads((ROOT / "agents.json").read_text(encoding="utf-8"))
    assert len(roster["agents"]) == 37, "agents.json: 36 agents + 1 guide"
    for slug in NEW_AGENTS:
        assert any(a["slug"] == slug for a in roster["agents"]), slug
    status = json.loads((ROOT / "ops" / "status.json").read_text(encoding="utf-8"))
    assert status["agents"] == 36
    assert status["agents_json_entries"] == 37


def test_readme_and_guide_list_new_agents():
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    assert "36 agents" in readme
    guide = (ROOT / "agents" / "WHEN-TO-USE.md").read_text(encoding="utf-8")
    for slug in NEW_AGENTS:
        assert f"(agents/{slug}.md)" in readme, f"README missing {slug}"
        assert slug in guide, f"WHEN-TO-USE.md missing {slug}"
