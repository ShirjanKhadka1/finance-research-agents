"""Structural tests for the Engine 1.3 NEPSE agent team (Phase 1).

No LLM is needed: these check the agent files' own structure —
frontmatter, required sections, structured-output schema, LLM
flexibility + no-LLM rules-mode statements — plus roster counts.
"""

import json
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

NEPSE_AGENTS = [
    "nepse-fundamentals-analyst",
    "nepse-technical-analyst",
    "nepse-news-sentiment-analyst",
    "nepse-broker-flow-analyst",
    "nepse-macro-analyst",
    "nepse-corporate-actions-analyst",
    "nepse-trader",
    "nepse-risk-team",
    "nepse-portfolio-manager",
]

REQUIRED_SECTIONS = [
    "## Identity", "## Mission", "## Core rules", "## Workflow",
    "## Deliverable format", "## Example prompt", "## Inputs",
    "## Outputs", "## Success metrics", "## Falsifier",
    "## LLM flexibility",
]


@pytest.mark.parametrize("slug", NEPSE_AGENTS)
def test_agent_file_has_required_sections(slug):
    text = (ROOT / "agents" / f"{slug}.md").read_text(encoding="utf-8")
    assert text.startswith("---\nname: " + slug + "\n")
    for section in REQUIRED_SECTIONS:
        assert section in text, f"{slug} missing {section}"
    assert "```yaml" in text, f"{slug} has no structured-output schema"
    assert "Research only, not investment advice" in text


@pytest.mark.parametrize("slug", NEPSE_AGENTS)
def test_agent_states_llm_flexibility_and_rules_mode(slug):
    text = (ROOT / "agents" / f"{slug}.md").read_text(encoding="utf-8")
    assert "Ollama" in text
    assert "rules_mode" in text or "rules mode" in text
    assert "API key" in text
    assert "never" in text.lower()  # never a recommendation / never an order


def test_broker_flow_labelled_indicative():
    text = (ROOT / "agents" / "nepse-broker-flow-analyst.md").read_text(encoding="utf-8")
    assert "INDICATIVE ONLY" in text
    assert "smart money" in text.lower()
    assert "never proven" in text.lower()


def test_fundamentals_has_sector_guidance():
    text = (ROOT / "agents" / "nepse-fundamentals-analyst.md").read_text(encoding="utf-8")
    for sector in ("banks", "hydropower", "insurance", "microfinance"):
        assert sector in text.lower()


def test_portfolio_manager_uses_reflections():
    text = (ROOT / "agents" / "nepse-portfolio-manager.md").read_text(encoding="utf-8")
    assert "reflections" in text
    assert "no prior calls" in text
    assert "decision log" in text
    assert "PUBLISH WITH STATED LIMITS" in text
    assert "How to use reflections" in text


def test_runbook_exists_and_orders_team():
    text = (ROOT / "runbooks" / "nepse-agent-team.md").read_text(encoding="utf-8")
    assert "Bull vs Bear" in text
    assert "Risk team" in text
    assert "Portfolio Manager" in text
    assert "Trader" in text
    assert "rules mode" in text
    for name in ("Fundamentals", "Trader", "Risk team", "Portfolio Manager"):
        assert name in text


def test_roster_counts_match_status():
    status = json.loads((ROOT / "ops" / "status.json").read_text(encoding="utf-8"))
    agents = [f for f in (ROOT / "agents").glob("*.md") if f.name != "WHEN-TO-USE.md"]
    runbooks = list((ROOT / "runbooks").glob("*.md"))
    assert status["agents"] == len(agents) == 36
    assert status["runbooks"] == len(runbooks) == 12
    roster = json.loads((ROOT / "agents.json").read_text(encoding="utf-8"))
    assert len(roster["agents"]) == 37  # 36 agents + 1 guide
    assert len(roster["runbooks"]) == 12
    for slug in NEPSE_AGENTS:
        assert any(a["slug"] == slug for a in roster["agents"]), slug
