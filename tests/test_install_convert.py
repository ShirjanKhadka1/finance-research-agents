"""Tests for scripts/install.sh and scripts/convert.sh (Engine 1.8).

Both scripts are exercised offline with temp dirs: install.sh with a
temp HOME (it copies into $HOME/.<tool>/agents), convert.sh with a
temp --out dir. No network, no real home directory touched.

Paths are passed to bash in POSIX form (``Path.as_posix()``): on a
Windows runner the same paths are native backslash paths, and Git
Bash's ``dirname`` treats '\\' as a plain character, so ``dirname``
on the script path returns '.' and the scripts resolve the repo dir
wrongly — every test then fails with "No such agent" (exit 1). The
``--out`` dir and HOME get the same treatment: convert.sh's
absolute-path check only recognises '/'-prefixed paths. as_posix()
is a no-op on Linux/macOS, so local behaviour is unchanged.

Windows note (found 8 Nov 2026, Tests #7): bare `bash` on a
windows-latest runner resolves to WSL's bash, and WSL has no distro
installed there, so every invocation dies before the script runs
('Windows Subsystem for Linux has no installed distributions').
The tests therefore call Git Bash explicitly on Windows
(C:\\Program Files\\Git\bin\bash.exe), which is on every runner.
"""

import os
import subprocess
import sys
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


def _bash():
    """Bash to invoke: plain `bash` everywhere except Windows, where
    bare `bash` is WSL bash with no distro installed (see module
    docstring) — use Git Bash, which is on every windows runner."""
    if sys.platform == "win32":
        for candidate in (
                r"C:\Program Files\Git\bin\bash.exe",
                r"C:\Program Files\Git\usr\bin\bash.exe"):
            if os.path.exists(candidate):
                return candidate
    return "bash"


def _assert_ok(proc):
    """Fail with both streams: stderr alone hid the death point on
    the Windows runner (exit 1, empty stderr, stdout swallowed)."""
    assert proc.returncode == 0, (
        "stderr:" + chr(10) + proc.stderr
        + "stdout:" + chr(10) + proc.stdout)


@pytest.mark.parametrize("tool", TOOLS)
def test_install_dry_run_names_right_dest(tool, tmp_path):
    proc = _run([_bash(), (ROOT / "scripts" / "install.sh").as_posix(),
                 "--tool", tool, "--agent", "nepse-bank-analyst", "--dry-run"])
    _assert_ok(proc)
    assert TOOLS[tool] in proc.stdout
    assert "nepse-bank-analyst.md" in proc.stdout


@pytest.mark.parametrize("tool", TOOLS)
def test_install_copies_one_agent_to_tool_dir(tool, tmp_path, monkeypatch):
    home = tmp_path / "home"
    home.mkdir()
    monkeypatch.setenv("HOME", home.as_posix())
    proc = _run([_bash(), (ROOT / "scripts" / "install.sh").as_posix(),
                 "--tool", tool, "--agent", "nepse-bank-analyst"])
    _assert_ok(proc)
    dest = home / TOOLS[tool] / "nepse-bank-analyst.md"
    assert dest.is_file()
    assert dest.read_text(encoding="utf-8") == (
        ROOT / "agents" / "nepse-bank-analyst.md").read_text(encoding="utf-8")


def test_install_unknown_tool_fails():
    proc = _run([_bash(), (ROOT / "scripts" / "install.sh").as_posix(),
                 "--tool", "not-a-tool", "--dry-run"])
    assert proc.returncode != 0
    assert "Unknown tool" in proc.stderr


def test_install_unknown_agent_fails():
    proc = _run([_bash(), (ROOT / "scripts" / "install.sh").as_posix(),
                 "--agent", "no-such-agent", "--dry-run"])
    assert proc.returncode != 0
    assert "No such agent" in proc.stderr


def test_convert_places_files_per_tool(tmp_path):
    out = tmp_path / "integrations"
    proc = _run([_bash(), (ROOT / "scripts" / "convert.sh").as_posix(),
                 "--out", out.as_posix(), "--agent", "nepse-bank-analyst"])
    _assert_ok(proc)
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
    proc = _run([_bash(), (ROOT / "scripts" / "convert.sh").as_posix(),
                 "--out", out.as_posix()])
    _assert_ok(proc)
    assert not list(out.rglob("*WHEN-TO-USE*"))


def test_convert_unknown_agent_fails():
    proc = _run([_bash(), (ROOT / "scripts" / "convert.sh").as_posix(),
                 "--out", "/tmp/never-created-by-this-test",
                 "--agent", "no-such-agent"])
    assert proc.returncode != 0
    assert "No such agent" in proc.stderr
