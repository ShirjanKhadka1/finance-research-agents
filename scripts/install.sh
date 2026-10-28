#!/usr/bin/env bash
# Install finance-research-agents locally. Copies .md agent files only.
# No network, no API key, no server, no data sent anywhere.
# Usage:
#   ./scripts/install.sh --tool claude-code [--agent <slug>] [--dry-run] [--list]
#   ./scripts/install.sh --tool copilot [--agent <slug>] [--dry-run]
set -euo pipefail

TOOL="claude-code"
AGENT=""
DRY_RUN=0
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

while [ $# -gt 0 ]; do
  case "$1" in
    --tool) TOOL="$2"; shift 2 ;;
    --agent) AGENT="$2"; shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    --list) ls "$REPO_DIR/agents"; exit 0 ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

case "$TOOL" in
  claude-code) DEST="$HOME/.claude/agents" ;;
  copilot) DEST="$HOME/.github/agents" ;;
  *) echo "Unknown tool: $TOOL (use claude-code or copilot)" >&2; exit 1 ;;
esac

if [ -n "$AGENT" ]; then
  FILES="$REPO_DIR/agents/$AGENT.md"
  [ -f "$FILES" ] || { echo "No such agent: $AGENT" >&2; exit 1; }
else
  FILES="$REPO_DIR"/agents/*.md
fi

echo "Installing finance-research-agents -> $DEST"
for f in $FILES; do
  if [ "$DRY_RUN" -eq 1 ]; then
    echo "  [dry-run] would copy $(basename "$f") -> $DEST/"
  else
    mkdir -p "$DEST"
    cp "$f" "$DEST/"
    echo "  copied $(basename "$f")"
  fi
done
echo "Done. These are Markdown agent files — they run inside your own AI tool."
