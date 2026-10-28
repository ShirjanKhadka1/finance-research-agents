#!/usr/bin/env bash
# Install finance-research-agents locally. Copies .md agent files only.
# No network, no API key, no server, no data sent anywhere.
# Usage:
#   ./scripts/install.sh --tool claude-code [--agent <slug> ...] [--dry-run] [--list]
#   ./scripts/install.sh --tool copilot [--agent <slug> ...] [--dry-run]
#   ./scripts/install.sh --list
#
# Runbook-team install pattern: a runbook names a team, it does not
# install itself. Install the agents the runbook names, one --agent
# flag per agent, in runbook order. For example, the data-first
# runbook (runbooks/data-first.md) team:
#   ./scripts/install.sh --tool claude-code \
#     --agent data-scout --agent statement-reconciler \
#     --agent financial-analyst --agent reality-checker
# The macro-to-company team:
#   ./scripts/install.sh --tool claude-code \
#     --agent world-market-researcher --agent nepal-market-researcher \
#     --agent investment-researcher --agent statement-reconciler \
#     --agent financial-analyst --agent valuation-analyst \
#     --agent reality-checker
# The research-to-use-case team:
#   ./scripts/install.sh --tool claude-code \
#     --agent use-case-generator --agent data-scout \
#     --agent reality-checker
# Run ./scripts/install.sh --list to see every agent and runbook.
set -euo pipefail

TOOL="claude-code"
AGENTS=()
DRY_RUN=0
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

while [ $# -gt 0 ]; do
  case "$1" in
    --tool) TOOL="$2"; shift 2 ;;
    --agent) AGENTS+=("$2"); shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    --list)
      echo "Agents:"
      ls "$REPO_DIR/agents"
      echo "Runbooks:"
      ls "$REPO_DIR/runbooks"
      exit 0
      ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

case "$TOOL" in
  claude-code) DEST="$HOME/.claude/agents" ;;
  copilot) DEST="$HOME/.github/agents" ;;
  *) echo "Unknown tool: $TOOL (use claude-code or copilot)" >&2; exit 1 ;;
esac

if [ "${#AGENTS[@]}" -gt 0 ]; then
  FILES=()
  for slug in "${AGENTS[@]}"; do
    f="$REPO_DIR/agents/$slug.md"
    [ -f "$f" ] || { echo "No such agent: $slug" >&2; exit 1; }
    FILES+=("$f")
  done
else
  FILES=("$REPO_DIR"/agents/*.md)
fi

echo "Installing finance-research-agents -> $DEST"
for f in "${FILES[@]}"; do
  if [ "$DRY_RUN" -eq 1 ]; then
    echo "  [dry-run] would copy $(basename "$f") -> $DEST/"
  else
    mkdir -p "$DEST"
    cp "$f" "$DEST/"
    echo "  copied $(basename "$f")"
  fi
done
echo "Done. These are Markdown agent files — they run inside your own AI tool."
