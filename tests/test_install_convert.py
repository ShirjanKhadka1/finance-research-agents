"""Tests for scripts/install.sh and scripts/convert.sh (Engine 1.8).

Both scripts are exercised offline with temp dirs: install.sh with a
temp HOME (it copies into $HOME/.<tool>/agents), convert.sh with a
temp --out dir. No network, no real home directory touched.
"""

import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
TOOLS = {
    "claude-code": ".claude/agents",
    "copilot": ".github/agents",
    "cursor": ".cursor/agents",
    "gemini": ".gemini/agents",
    "codex": ".codex/agents",
}
CONVERT_TOOLS = ["claude-code", "copilot", "cursor", "gemini", "codex"]


def _run(cmd, env=None):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=120,
                          env=env, check=False)


@pytest.mark.parametrize("tool", TOOLS)
def test_install_dry_run_names_right_dest(tool, tmp_path):
    proc = _run(["bash", str(ROOT / "scripts" / "install.sh"),
                 "--tool", tool, "--agent", "nepse-bank-analyst", "--dry-run"])
    assert proc.returncode == 0, proc.stderr
    assert TOOLS[tool] in proc.stdout
    assert "nepse-bank-analyst.md" in proc.stdout


@pytest.mark.parametrize("tool", TOOLS)
def test_install_copies_one_agent_to_tool_dir(tool, tmp_path, monkeypatch):
    home = tmp_path / "home"
    home.mkdir()
    monkeypatch.setenv("HOME", str(home))
    proc = _run(["bash", str(ROOT / "scripts" / "install.sh"),
                 "--tool", tool, "--agent", "nepse-bank-analyst"])
    assert proc.returncode == 0, proc.stderr
    dest = home / TOOLS[tool] / "nepse-bank-analyst.md"
    assert dest.is_file()
    assert dest.read_text(encoding="utf-8") == (
        ROOT / "agents" / "nepse-bank-analyst.md").read_text(encoding="utf-8")


def test_install_unknown_tool_fails():
    proc = _run(["bash", str(ROOT / "scripts" / "install.sh"),
                 "--tool", "not-a-tool", "--dry-run"])
    assert proc.returncode != 0
    assert "Unknown tool" in proc.stderr


def test_install_unknown_agent_fails():
    proc = _run(["bash", str(ROOT / "scripts" / "install.sh"),
                 "--agent", "no-such-agent", "--dry-run"])
    assert proc.returncode != 0
    assert "No such agent" in proc.stderr


def test_convert_places_files_per_tool(tmp_path):
    out = tmp_path / "integrations"
    proc = _run(["bash", str(ROOT / "scripts" / "convert.sh"),
                 "--out", str(out), "--agent", "nepse-bank-analyst"])
    assert proc.returncode == 0, proc.stderr
    for tool in CONVERT_TOOLS:
        if tool == "cursor":
            agent_file = out / "cursor" / "agents" / "nepse-bank-analyst.mdc"
            assert agent_file.is_file()
            text = agent_file.read_text(encoding="utf-8")
            assert text.startswith("---\ndescription: ")
            # Body is the agent file with frontmatter stripped, unchanged.
            body = (ROOT / "agents" / "nepse-bank-analyst.md").read_text(
                encoding="utf-8")
            body = body.split("---", 2)[2].lstrip("\n")
            assert text.split("---", 2)[2].lstrip("\n") == body
        else:
            agent_file = out / tool / "agents" / "nepse-bank-analyst.md"
            assert agent_file.is_file()
            assert agent_file.read_text(encoding="utf-8") == (
                ROOT / "agents" / "nepse-bank-analyst.md"
            ).read_text(encoding="utf-8")
        skill = out / tool / "skills" / "nepse-bank-analyst" / "SKILL.md"
        assert skill.is_file()
        assert skill.read_text(encoding="utf-8") == (
            ROOT / "skills" / "nepse-bank-analyst" / "SKILL.md"
        ).read_text(encoding="utf-8")


def test_convert_skips_the_guide(tmp_path):
    out = tmp_path / "integrations"
    proc = _run(["bash", str(ROOT / "scripts" / "convert.sh"),
                 "--out", str(out)])
    assert proc.returncode == 0, proc.stderr
    assert not list(out.rglob("*WHEN-TO-USE*"))


def test_convert_unknown_agent_fails():
    proc = _run(["bash", str(ROOT / "scripts" / "convert.sh"),
                 "--out", "/tmp/never-created-by-this-test",
                 "--agent", "no-such-agent"])
    assert proc.returncode != 0
    assert "No such agent" in proc.stderr
