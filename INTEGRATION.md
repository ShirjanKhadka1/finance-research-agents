# Integration — finance-research-agents

## Role in the system
The thinking layer. These 10 agents decide what to research, in what order,
and what counts as a trustworthy answer. They do not calculate (that is
the toolkit) and they do not invent structure (that is the playbook) —
they call on both.

## How to use (free, local)
- Claude Code: `./scripts/install.sh --tool claude-code`
- Copilot: `./scripts/install.sh --tool copilot`
- Any other tool: copy `agents/*.md` into its agent folder, or paste one
  agent file into a chat as a system prompt. No server, no API key.

## Connections
| Agent | Uses | Produces |
|---|---|---|
| investment-researcher | playbook initiation template | thesis, business, industry |
| forensic-analyst | playbook forensic checklist | verdict: Clean / Watch / Flagged |
| financial-analyst | toolkit ratios + DuPont | ratios, drivers, cash vs profit |
| valuation-analyst | toolkit DCF + multiples, playbook sanity check | valuation + downside + implied test |
| nepal-market-researcher | nepal-market-research case studies | sourced Nepal company research |
| nepali-capital-market-researcher* | nepali-capital-market-research guide | market-structure research |
| world-market-researcher | regime map, comparison table | global context + local test |
| reality-checker | every deliverable above | fixes list, Pass / Send back |

*The capital-market agent lives in its own repo; this pack links to it.
## Workflow order (never skip the checker)
Researcher → Forensic → Financial → Valuation → Reality Checker.
See `runbooks/company-deep-dive.md` for the full team order.
## Extending
One new agent = one `.md` file + `agents.json` entry + roster row +
its own connections listed here. Test with `--dry-run`.
