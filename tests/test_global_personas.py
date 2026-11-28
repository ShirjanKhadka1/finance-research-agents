"""Structural tests for the Round 9.3 global personas (Phase 1).

Five agent files mirror the five deterministic personas in the companion
toolkit's rules mode (`investment-analyst-toolkit/toolkit/rules_mode.py`,
GLOBAL_TEAM): US large-cap fundamentals, ETF/index, FX/macro, crypto,
earnings. Each persona has an agent file, a SKILL.md mirror, a roster
entry, and a README roster-table row.

No LLM is needed: these check the agent files' own structure —
frontmatter, required sections, structured-output schema, LLM
flexibility + no-LLM rules-mode statements — plus the cross-repo
match against the toolkit's GLOBAL_TEAM dict, read from that file
(not hardcoded here twice).
"""

import ast
import json
import os
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]

GLOBAL_PERSONAS = [
    "us-large-cap-fundamentals",
    "etf-index",
    "fx-macro",
    "crypto",
    "earnings",
]

REQUIRED_SECTIONS = [
    "## Identity", "## Mission", "## Core rules", "## Workflow",
    "## Deliverable format", "## Example prompt", "## Inputs",
    "## Outputs", "## Success metrics", "## Falsifier",
    "## LLM flexibility",
]


def _find_rules_mode():
    """Locate the toolkit's rules_mode.py: env var first, then a sibling
    checkout of investment-analyst-toolkit next to this repo."""
    env = os.environ.get("TOOLKIT_RULES_MODE")
    candidates = [Path(env)] if env else []
    candidates += [
        ROOT.parents[1] / "investment-analyst-toolkit" / "toolkit" / "rules_mode.py",
        ROOT.parents[2] / "investment-analyst-toolkit" / "toolkit" / "rules_mode.py",
        Path.home() / "workspace" / "github-repos"
        / "investment-analyst-toolkit" / "toolkit" / "rules_mode.py",
    ]
    for path in candidates:
        if path.is_file():
            return path
    return None


def _global_team_keys(rules_mode_path):
    """Parse the GLOBAL_TEAM dict keys out of rules_mode.py with ast —
    the dict itself is the source of truth, not a copy of it here."""
    tree = ast.parse(rules_mode_path.read_text(encoding="utf-8"))
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "GLOBAL_TEAM":
                    return {k.value for k in node.value.keys
                            if isinstance(k, ast.Constant)}
    raise AssertionError(f"GLOBAL_TEAM not found in {rules_mode_path}")


def _rules_mode_functions(rules_mode_path):
    """Top-level function names defined in rules_mode.py."""
    tree = ast.parse(rules_mode_path.read_text(encoding="utf-8"))
    return {n.name for n in tree.body if isinstance(n, ast.FunctionDef)}


@pytest.mark.parametrize("slug", GLOBAL_PERSONAS)
def test_agent_file_has_required_sections(slug):
    text = (ROOT / "agents" / f"{slug}.md").read_text(encoding="utf-8")
    assert text.startswith("---\nname: " + slug + "\n")
    assert text.split("---", 2)[1].strip().startswith("name: " + slug)
    assert "description: " in text.split("---", 2)[1]
    for section in REQUIRED_SECTIONS:
        assert section in text, f"{slug} missing {section}"
    assert "```yaml" in text, f"{slug} has no structured-output schema"
    assert "Research only, not investment advice" in text
    assert "Runs under runbooks/agent-execution-contract.md" in text


@pytest.mark.parametrize("slug", GLOBAL_PERSONAS)
def test_agent_states_llm_flexibility_and_rules_mode(slug):
    text = (ROOT / "agents" / f"{slug}.md").read_text(encoding="utf-8")
    assert "Ollama" in text
    assert "rules_mode" in text or "rules mode" in text
    assert "API key" in text
    assert "never" in text.lower()  # never a recommendation / never a prediction


@pytest.mark.parametrize("slug", GLOBAL_PERSONAS)
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
    assert "LLM flexibility" in text


def test_persona_slugs_match_global_team_keys():
    rules_mode = _find_rules_mode()
    if rules_mode is None:
        pytest.skip("toolkit rules_mode.py not found next to this repo; "
                    "set TOOLKIT_RULES_MODE to its path to run this check")
    keys = _global_team_keys(rules_mode)
    for slug in GLOBAL_PERSONAS:
        assert slug.replace("-", "_") in keys, (
            f"{slug} has no GLOBAL_TEAM key in {rules_mode}")


def test_agent_names_its_rules_mode_function():
    rules_mode = _find_rules_mode()
    if rules_mode is None:
        pytest.skip("toolkit rules_mode.py not found next to this repo; "
                    "set TOOLKIT_RULES_MODE to its path to run this check")
    functions = _rules_mode_functions(rules_mode)
    for slug in GLOBAL_PERSONAS:
        text = (ROOT / "agents" / f"{slug}.md").read_text(encoding="utf-8")
        match = re.search(r"toolkit/rules_mode\.py` \(`(\w+)`\)", text)
        assert match, f"{slug}: agent names no rules-mode function"
        assert match.group(1) in functions, (
            f"{slug}: {match.group(1)} is not defined in {rules_mode}")


def test_us_fundamentals_mirrors_rules_mode_metrics_and_flags():
    text = (ROOT / "agents" / "us-large-cap-fundamentals.md").read_text(encoding="utf-8")
    for metric in ("revenue_growth_pct", "net_margin_pct",
                   "free_cash_flow_margin_pct", "debt_to_equity",
                   "interest_coverage", "return_on_invested_capital_pct"):
        assert metric in text, f"missing metric {metric}"
    assert "2.0x" in text and "debt_to_equity" in text
    assert "1.5x" in text and "interest_coverage" in text
    assert "EDGAR" in text


def test_etf_index_mirrors_rules_mode_metrics():
    text = (ROOT / "agents" / "etf-index.md").read_text(encoding="utf-8")
    for metric in ("expense_ratio_pct", "tracking_error_pct",
                   "assets_under_management_usd", "premium_discount_pct",
                   "index_return_1y_pct", "etf_return_1y_pct"):
        assert metric in text, f"missing metric {metric}"
    assert "etf_minus_index_1y_pct" in text
    assert "0.50%" in text  # expense-ratio discussion flag


def test_fx_macro_mirrors_rules_mode_inputs():
    text = (ROOT / "agents" / "fx-macro.md").read_text(encoding="utf-8")
    for metric in ("policy_rate_base_pct", "policy_rate_quote_pct",
                   "inflation_base_pct", "inflation_quote_pct",
                   "pair_change_1y_pct", "pair_volatility_annualised_pct"):
        assert metric in text, f"missing input {metric}"
    assert "rate_differential_bps" in text
    assert "20%" in text  # one-year-move discussion flag
    assert "predicts nothing" in text


def test_crypto_mirrors_rules_mode_metrics_and_no_predictions():
    text = (ROOT / "agents" / "crypto.md").read_text(encoding="utf-8")
    for metric in ("price_usd", "market_cap_usd", "volume_24h_usd",
                   "all_time_high_usd", "mean_200d_usd",
                   "realised_vol_30d_daily_pct", "circulating_supply",
                   "max_supply"):
        assert metric in text, f"missing metric {metric}"
    assert "drawdown_from_ath_pct" in text
    assert "circulating_share_of_max_supply" in text
    assert "never predicts a price" in text.lower()


def test_earnings_surprise_needs_both_sides_and_says_nothing_next_quarter():
    text = (ROOT / "agents" / "earnings.md").read_text(encoding="utf-8")
    for field in ("reported_eps", "expected_eps", "eps_surprise_pct",
                  "reported_revenue", "expected_revenue",
                  "revenue_surprise_pct"):
        assert field in text, f"missing field {field}"
    assert "a beat says nothing about the next quarter" in text.lower()
    assert "UNKNOWN" in text


def test_roster_consistent_for_new_personas():
    roster = json.loads((ROOT / "agents.json").read_text(encoding="utf-8"))
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    guide = (ROOT / "agents" / "WHEN-TO-USE.md").read_text(encoding="utf-8")
    for slug in GLOBAL_PERSONAS:
        assert (ROOT / "agents" / f"{slug}.md").is_file()
        assert any(a["slug"] == slug for a in roster["agents"]), slug
        assert f"(agents/{slug}.md)" in readme, f"README missing {slug}"
        assert slug in guide, f"WHEN-TO-USE.md missing {slug}"


def test_roster_counts_41_agents():
    disk = [f for f in (ROOT / "agents").glob("*.md") if f.name != "WHEN-TO-USE.md"]
    assert len(disk) == 41, f"agents on disk: {len(disk)}, want 41"
    roster = json.loads((ROOT / "agents.json").read_text(encoding="utf-8"))
    assert len(roster["agents"]) == 42, "agents.json: 41 agents + 1 guide"
    for slug in GLOBAL_PERSONAS:
        assert any(a["slug"] == slug for a in roster["agents"]), slug
    status = json.loads((ROOT / "ops" / "status.json").read_text(encoding="utf-8"))
    assert status["agents"] == 41
    assert status["agents_json_entries"] == 42
