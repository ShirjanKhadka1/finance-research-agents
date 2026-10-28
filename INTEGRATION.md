# Integration — finance-research-agents

## Role in the system
The thinking layer. These agents decide what to research, in what order,
and what counts as a trustworthy answer. They do not calculate (that is
the toolkit) and they do not invent structure (that is the playbook) —
they call on both. `agents.json` is the single source of truth for the
roster: 16 agents, 8 runbooks (counts live there, not here).

## How to use (free, local)
- Claude Code: `./scripts/install.sh --tool claude-code`
- Copilot: `./scripts/install.sh --tool copilot`
- Any other tool: copy `agents/*.md` into its agent folder, or paste one
  agent file into a chat as a system prompt. No server, no API key.

## Connections
| Agent | Uses | Produces |
|---|---|---|
| research-orchestrator | runbook + team, as-of date | run contract, step state, run log entry |
| data-scout | documented free sources | DATA_SOURCES entries, validated dataset or no-source finding |
| investment-researcher | playbook initiation template | thesis, business, industry |
| news-sentiment-analyst | named news + public sentiment sources | item list, stance counts, news read, sentiment read, limits |
| forensic-analyst | playbook forensic checklist | verdict: Clean / Watch / Flagged |
| statement-reconciler | reported statements, source + period | tie-out table, TIED / TIED WITH EXPLAINED DIFFERENCES / NOT TIED |
| financial-analyst | toolkit ratios + DuPont | ratios, drivers, cash vs profit |
| fpa-analyst | plan/forecast + actuals, same basis | variance table, driver decomposition, restated forward view |
| valuation-analyst | toolkit DCF + multiples, playbook sanity check | valuation + downside + implied test |
| nepal-market-researcher | nepal-market-research case studies | sourced Nepal company research |
| nepali-capital-market-researcher* | nepali-capital-market-research guide | market-structure research |
| world-market-researcher | regime map, comparison table | global context + local test |
| reality-checker | every deliverable above | fixes list, Pass / Send back |
| use-case-generator | completed research report | killable use cases + killed-candidate list |

*The capital-market agent lives in its own repo; this pack links to it.
## Workflow order (never skip the checker)
Researcher → Forensic → Financial → Valuation → Reality Checker.
See `runbooks/company-deep-dive.md` for the full team order.
Other teams: `runbooks/data-first.md` (Data Scout → Statement
Reconciler → Financial → Reality Checker),
`runbooks/macro-to-company.md` (World → Nepal → Investment →
Reconciler → Financial → Valuation → Reality, Accuracy Auditor ledger
rule on forecasts), and `runbooks/research-to-use-case.md` (completed
research → Use-Case Generator → Data Scout licence check → Reality
Checker).
## Extending
One new agent = one `.md` file + `agents.json` entry + roster row +
its own connections listed here. Test with `--dry-run`.
