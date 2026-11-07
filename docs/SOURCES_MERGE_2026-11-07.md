# Sources — merge of 2026-11-07

Date: 2026-11-07. Scope: this repo only
(`finance-research-agents`). A parallel merge landed the toolkit and
scanner parts of the same plan in their own repos; this file records
only what changed here.

> Research only, not investment advice. Nothing in this merge adds a
> recommendation, a signal, or a trade. Every addition below is a
> research discipline, a checklist, or a design note.

## Source repos

| Source | Licence | Commit inspected | Head date |
|---|---|---|---|
| [FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) (Fincept Corporation) | GNU AGPL-3.0-or-later | `7716ee8` | 2026-10-26 |
| [day-trader-skill](https://github.com/Jakeschincariol/day-trader-skill) (Jake Schincariol) | MIT | `3d0f4ef` | 2026-10-20 |

Inspection record (full local clones, read-only, nothing modified):
`~/workspace/github-repos/ops/fincept-daytrader-merge-plan.md`,
2026-11-07. FinceptTerminal is ~534,600 lines C++/Qt6 + ~337,300
lines Python, 201 connectors (141 keyless, 60 key-required), no
NEPSE/Nepal coverage. day-trader-skill is 11 skills, each one
SKILL.md + one stdlib-only Python tool, v2.0.0, 315 tests passing at
inspection.

## Licence rule (binding)

- **FinceptTerminal (AGPL-3.0): ideas and formulas ONLY.** No Fincept
  code, text, layouts, command syntax, branding, or trade dress was
  copied into this MIT repo. Anything adapted from it was rewritten
  from scratch in the pack's own words, and is attributed here and in
  the file that uses it with repo + commit.
- **day-trader-skill (MIT): arithmetic and discipline may be adapted**
  with attribution (repo + commit + "adapted from"). Its execution
  skill is excluded in full (see Rejected).
- Every merged file records source repo, licence, commit, and
  adopted/adapted status, in the file itself and in this document.

## What was adopted / adapted in this repo

| # | Capability | Source | Verdict | Landed in |
|---|---|---|---|---|
| F3 | DCF pipeline checklist (WACC → unlever/relever beta → FCF from EBIT → projected FCFs → terminal value → EV → equity value → price/share → sensitivity + scenarios) + football-field range summary (DCF / trading comps / precedent transactions, each with sources & vintage, normalised-vs-LTM check) | FinceptTerminal DCF model method list | ADAPT (Markdown structure, ideas only) | `agents/valuation-analyst.md` |
| F7 | Keyless sentiment pipeline design (lexicon score + keyword fallback → BULLISH/BEARISH/NEUTRAL + confidence + headline counts) | FinceptTerminal news-sentiment pipeline | ADAPT (design only, no code in this repo) | `agents/news-sentiment-analyst.md` ("Optional local sentiment step") |
| D5 | Risk gate as PASS/BLOCK checklist with fingerprinting (16 named checks, verdict matches the exact plan + date only) | day-trader-skill trader-risk | ADAPT (research context; no orders, no real money, shorts blocked, US day-trading rules replaced by a stated research analogue, Nepal market hours TO VERIFY) | `runbooks/hypothetical-position-review.md` |
| D6 | News discipline (dedup, filings beat headlines, tag every item, material-item mapping, MOVING threshold, "headlines are leads, not facts") | day-trader-skill trader-news | ADAPT (8-K mapping replaced by the Nepal analogue table, TO VERIFY where unsourced; MOVING = 3% vs prior close) | `agents/news-sentiment-analyst.md` (core rules 8–13) |
| D7 | Analyst discipline (filed-numbers-first, YoY + TTM tables, DERIVED marking, lag/one-off flags, blank-not-zero) | day-trader-skill trader-analyst | ADAPT (research-only: no value language, no recommendation) | NEW `agents/filings-analyst.md` (19th agent) |

## What was explicitly rejected (not in this repo)

| # | Capability | Reason |
|---|---|---|
| R1 | Fincept live brokerage / order execution (`src/trading/`, 22 broker adapters, OrderMatcher, SmartOrderEngine, DeploymentRunner) | Real-money trading; this programme is research-only by user rule. **No live trading, no broker code.** |
| R2 | Fincept algo-trading / RL / auto-execution (`algo_engine`, LEAN templates, agno_trading, ai_quant_lab RL) | Signals + auto-execution; out of scope. |
| R3 | day-trader-skill trader-broker (Alpaca MCP order placement, IBKR connector, ticket approve/fill/flatten) | The only execution skill; excluded in full. |
| R4 | Order-shaped files (`orders.json` bracket orders, flatten/close-all, options/crypto/margin/short) | Execution artefacts; not kept even as "paper". |
| R5 | trader-pelosi / 13F copying as a signal | Disclosure is weeks old; never a setup; no inside-information implication. **No Pelosi/13F copying as a signal.** |
| R6 | Fincept paid-data dependence (Fincept Data API credits, QuantLib cloud endpoints, Pro/Enterprise, 60 key-required connectors) | This pack runs on sources the user provides or free public sources. |
| R7 | Fincept branding / layouts / command syntax / trade dress; QuantLib cloud suite | AGPL + trademark/trade-dress assertions; ideas only. |
| R8 | Day-trading-specific / US-specific material as if general (TSLA example as evidence, NYSE holidays, PDT rules, Yahoo as NEPSE coverage) | Wrong market, wrong jurisdiction; Nepal equivalents labelled TO VERIFY. |
| R9 | Any implication a scanner hit, entry trigger, or simulation odds is a prediction | Both source repos say so themselves; walk-forward honesty is the programme rule. |

## Roster change in this merge

- Agents: 18 → **19** (new: Filings Analyst, `agents/filings-analyst.md`).
- Runbooks: 10 → **11** (new: Hypothetical position review,
  `runbooks/hypothetical-position-review.md`).
- `agents.json`, `agents/WHEN-TO-USE.md`, `README.md`, and
  `ops/status.json` (regenerated by `ops/generate_counts.py`) updated
  to match; `ops/check_roster.py` and `ops/check_numbers.py` pass.
- `ops/SYSTEM-MAP.md` current-count lines updated to 19 agents /
  11 runbooks (7 Nov 2026). Dated historical records were left
  untouched: `docs/RUBRIC.md` and `docs/SCORES-2026-10-29.md`
  (29 Oct 2026 scoring), `docs/worked-example/README.md` (frozen
  worked example, 16 Oct 2026), `status/STATUS.md` and
  `status/HEALTH.md` (regenerated by the daily health job), and
  `ops/status-evidence.json` (28 Oct 2026 evidence string).
  `ops/programme-status.json` was updated by hand for this repo's
  entry only (19 agents, 11 runbooks, 7 Nov 2026), because its
  generator needs every programme checkout under one repos-root
  and the merge folder holds only this round's checkouts.
- `INTEGRATION.md` is superseded and was not edited, per the rule
  in `ops/SYSTEM-MAP.md`.

## TO VERIFY (left open by this merge, not asserted)

- The Nepal material-disclosure mapping in
  `agents/news-sentiment-analyst.md` (SEBON / NEPSE disclosures,
  AGM / dividend / book-closure notices) — labelled TO VERIFY in
  the file until sourced.
- NEPSE trading hours for the entry-window check in
  `runbooks/hypothetical-position-review.md`, and whether any
  NEPSE/SEBON rule governs same-day round-trip frequency
  (check 16) — both labelled TO VERIFY in the file.

## Phase 1 engines 1.3–1.5 (2026-11-07)

### TradingAgents — patterns adapted, NO code copied

- Repo: https://github.com/TauricResearch/TradingAgents
- Licence: **Apache-2.0**
- What was taken, as patterns only, reimplemented from scratch in
  this pack's own words: the multi-agent role split (4 analysts in
  parallel → Bull/Bear debate → Trader → three-way risk debate →
  Portfolio Manager), the decision-memory loop (log every call
  before its outcome, settle against realised return and alpha vs a
  benchmark, feed a reflection into the next run), and the
  point-in-time discipline (decisions scored from the first close
  *after* the analysis date). No TradingAgents code, text, branding,
  or model names were copied.
- Where it landed: nine NEW agents (`agents/nepse-*.md`) + the
  orchestrator runbook `runbooks/nepse-agent-team.md`; the
  Portfolio Manager agent's reflections section; the decision-log
  design mirrored in the toolkit (`toolkit/decision_log.py`).
- Rejected from the same source: the five-tier
  Buy/Overweight/Hold/Underweight/Sell rating (NOT adopted — this
  programme is research-only and never issues a rating), the
  paper's backtest return/Sharpe figures (not this programme's
  results, never quoted as such), and any live-data vendor chain
  (NEPSE stays CSV-only).

## Phase 1 engine 1.8 — agent + skill library (2026-11-07)

### agency-agents — install/convert pattern adapted, NO text copied

- Repo: https://github.com/msitarzewski/agency-agents
- Licence: **MIT** (Copyright (c) 2025 AgentLand Contributors)
- What was taken, as a pattern only, reimplemented from scratch in
  this pack's own words: the agent-file template (frontmatter +
  Identity / Mission / Rules / Deliverables / Workflow / Success
  Metrics), the installer that copies agent files into per-tool
  config dirs (`scripts/install.sh`, extended here to Claude Code,
  GitHub Copilot, Cursor, Gemini CLI, Codex), and the converter that
  generates per-tool integration dirs (`scripts/convert.sh`,
  including a Cursor `.mdc` file and `SKILL.md` mirrors under
  `skills/<slug>/SKILL.md`). No agency-agents agent text, persona
  backstory, or claim was copied — all eight new agent personas are
  original, written for NEPSE sectors from this programme's own
  sector guidance and sourced Nepal frictions.
- Where it landed: eight NEW agents (`agents/nepse-bank-analyst.md`,
  `agents/nepse-hydropower-analyst.md`,
  `agents/nepse-insurance-analyst.md`,
  `agents/nepse-microfinance-analyst.md`,
  `agents/nepse-mutual-fund-nav-analyst.md`,
  `agents/nepse-ipo-analyst.md`,
  `agents/nepse-fees-and-tax-analyst.md`,
  `agents/nepse-content-writer.md`) + eight SKILL.md mirrors +
  `scripts/convert.sh` + the install.sh tool extension.
- Rejected from the same source: the 15-tool converter matrix
  (overkill for this pack's five tools), the desktop app (separate
  repo, out of scope), and any invented persona backstory
  ("200+ companies diligenced", "5x returns" — not this programme's
  evidence, never quoted as such).

### augur — persona YAML pattern (noted, not copied)

- Repo: see ops/teardown/augur.md. Licence: **MIT**.
- The persona-YAML pattern was reviewed; the eight new agents keep
  this pack's existing Markdown-frontmatter format instead, so no
  augur text or structure was copied.

### Duplicates checked and NOT added (2026-11-07, live roster)

- Corporate actions — already `agents/nepse-corporate-actions-analyst.md`.
- Macro — already `agents/nepse-macro-analyst.md`.
- Risk analyst — already covered by `agents/nepse-risk-team.md` and
  `agents/risk-stance-analyst.md`.
- Orchestrator — already `agents/research-orchestrator.md`.
