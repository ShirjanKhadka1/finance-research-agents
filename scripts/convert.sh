#!/usr/bin/env bash
# Convert finance-research-agents into per-tool integration dirs.
# Pattern adapted from agency-agents (MIT) convert.sh: one source file,
# many tool formats — but this pack converts, it does not rewrite content.
# No network, no API key, no server, no data sent anywhere.
# Usage:
#   ./scripts/convert.sh [--out DIR] [--agent <slug> ...] [--dry-run]
#   ./scripts/convert.sh --list
#
# Default out: integrations/ (generated; do not hand-edit what lands there).
# Outputs, per agent:
#   claude-code/agents/<slug>.md   native Markdown agent file (copied as-is)
#   copilot/agents/<slug>.md       same
#   gemini/agents/<slug>.md        same
#   codex/agents/<slug>.md         same
#   cursor/agents/<slug>.mdc       Cursor rule file: description frontmatter
#                                  + the agent body (frontmatter stripped)
#   <tool>/skills/<slug>/SKILL.md  skill copy, for every tool above
# A file is never converted into a claim: the Cursor .mdc carries the
# agent's own description line only, and nothing is added or reworded.
set -euo pipefail

OUT="integrations"
AGENTS=()
DRY_RUN=0
SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
TOOLS="claude-code copilot cursor gemini codex"

while [ $# -gt 0 ]; do
  case "$1" in
    --out) OUT="$2"; shift 2 ;;
    --agent) AGENTS+=("$2"); shift 2 ;;
    --dry-run) DRY_RUN=1; shift ;;
    --list)
      echo "Agents:"
      ls "$REPO_DIR/agents"
      echo "Skills:"
      ls "$REPO_DIR/skills"
      exit 0
      ;;
    *) echo "Unknown option: $1" >&2; exit 1 ;;
  esac
done

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

# A path that is not under the repo is refused: the converter only ever
# writes inside the chosen out dir.
case "$OUT" in
  /*) OUT_DIR="$OUT" ;;
  *) OUT_DIR="$REPO_DIR/$OUT" ;;
esac

emit() {
  if [ "$DRY_RUN" -eq 1 ]; then echo "  [dry-run] would write $1";
  else mkdir -p "$(dirname "$1")"; echo "  wrote $1"; fi
}

echo "Converting finance-research-agents -> $OUT_DIR"
for f in "${FILES[@]}"; do
  slug="$(basename "$f" .md)"
  [ "$slug" = "WHEN-TO-USE" ] && continue  # guide, not an agent: never converted
  desc="$(sed -n 's/^description: //p' "$f" | head -n 1)"
  for tool in $TOOLS; do
    case "$tool" in
      cursor)
        dest="$OUT_DIR/cursor/agents/$slug.mdc"
        emit "$dest"
        if [ "$DRY_RUN" -eq 0 ]; then
          { printf -- '---\ndescription: %s\n---\n' "$desc";
            awk '/^---$/ && c < 2 {c++; next} c == 2' "$f"; } > "$dest"
        fi
        ;;
      *) dest="$OUT_DIR/$tool/agents/$slug.md"
        emit "$dest"
        [ "$DRY_RUN" -eq 0 ] && cp "$f" "$dest"
        ;;
    esac
    skill="$REPO_DIR/skills/$slug/SKILL.md"
    if [ -f "$skill" ]; then
      sdest="$OUT_DIR/$tool/skills/$slug/SKILL.md"
      emit "$sdest"
      [ "$DRY_RUN" -eq 0 ] && cp "$skill" "$sdest"
    fi
  done
done
echo "Done. Generated files only — edit agents/ or skills/, then re-run."
