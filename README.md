# 💰 Finance Research Agents — free, local, yours

A proper research agent pack for investment and research analysis — modelled
on the way great agent repos are published, but finance-only, and free to run
on your own machine.

**No app. No subscription. No server. No data sent anywhere by this repo.**

These agents are Markdown files. You copy them into your own AI tool
(Claude Code, GitHub Copilot, Gemini CLI, Cursor, and others that read agent
files), and they run inside *your* tool, on *your* machine, using *your*
existing AI access. If your tool is free, the agents are free. This repo never
asks for an API key, a login, or a payment.

> **Research only, not investment advice.** These agents analyse, compare,
> and explain. They never recommend buying or selling a security, never
> present an unfinished study as a valuation, and never invent a number.
> Every number in an output must carry its source and its period, or it
> must be labelled UNKNOWN.

## ⚡ Quick start (2 minutes)

```bash
git clone <this-repo-url>
cd finance-research-agents

# Install all agents for Claude Code (default)
./scripts/install.sh --tool claude-code

# Or install just one team
./scripts/install.sh --tool claude-code --agent investment-researcher

# Or use as reference — no install at all
# Open agents/investment-researcher.md, copy it into any AI chat, and go.
```

Then, in your AI tool:

```
Activate Investment Researcher mode and deep-dive [company, exchange]
using only sources I provide, with every number sourced.
```

## 🏥 Programme health

The whole 8-repo programme is checked daily by
[`.github/workflows/health.yml`](.github/workflows/health.yml)
(02:00 UTC, after the toolkit's 01:00 UTC daily update). It reports
roster consistency, README counts vs evidence, workflow runs, data
freshness, ledger publication, internal links, and security-config
presence — and it fails visibly on any FAIL or UNKNOWN, never silently
green. The latest report lives in [`status/HEALTH.md`](status/HEALTH.md)
once the job has run; [`status/STATUS.md`](status/STATUS.md) is the
human-readable status page. There are no email alerts (blocked) and no
Cloudflare backup (blocked): failure visibility is the report itself
plus the public workflow log plus dated notes under `status/failures/`.

## 🎨 The roster

36 agents. `agents.json` is the machine-readable roster; this table
mirrors it. Generated counts: see `ops/status.json` (produced by
`ops/generate_counts.py`, checked by `ops/check_numbers.py`).

| Agent | Specialty | When to use |
|---|---|---|
| 🎛️ [Research Orchestrator](agents/research-orchestrator.md) | Run contract, as-of date, synchronisation, checkpoint/resume, thesis-log settlement | Running any multi-agent runbook, before the first analyst starts |
| 🔍 [Data Scout](agents/data-scout.md) | Free public data sources, licence/terms, freshness, schema validation | Before any analysis that needs data you do not already hold |
| 🔍 [Investment Researcher](agents/investment-researcher.md) | Due diligence, thesis, market research | Starting any company study |
| 📰 [News & Sentiment Analyst](agents/news-sentiment-analyst.md) | News + public sentiment, source + date + stance counts | Inside a deep dive or market study, before the debate step |
| 🔬 [Forensic Analyst](agents/forensic-analyst.md) | Profit quality, red flags, cash vs profit | Before you trust the numbers |
| 🧾 [Statement Reconciler](agents/statement-reconciler.md) | Mechanical tie-out: balance sheet, cash flow, equity, segments, comparatives | On every set of statements, before the Financial Analyst starts |
| 📊 [Financial Analyst](agents/financial-analyst.md) | Three-statement analysis, ratios, forecasting drivers | Reading financials, building a model |
| 📈 [FP&A Analyst](agents/fpa-analyst.md) | Operating plans, rolling forecasts, driver-decomposed variance analysis | Testing a plan, budget, or forecast against actuals |
| 💎 [Valuation Analyst](agents/valuation-analyst.md) | DCF, multiples, sanity checks, implied assumptions | Before any target price is discussed |
| 🇳🇵 [Nepal Market Researcher](agents/nepal-market-researcher.md) | NEPSE, sourced Nepal market research | Nepal-listed companies, with exchange always stated |
| 🛡️ [Reality Checker](agents/reality-checker.md) | Review, falsifiers, downside, accuracy audit | Last pass before anything is shared |
| 🌍 [World Market Researcher](agents/world-market-researcher.md) | Global markets, regimes, cross-border themes | Comparing markets, placing a local story in world context |
| 📈 [Portfolio & Forecast Analyst](agents/portfolio-forecast-analyst.md) | Portfolio, performance, walk-forward forecasting, free API data | Building a portfolio, judging a model, forecasting honestly |
| ⚔️ [Debate Analyst](agents/debate-analyst.md) | Bull vs Bear debate + Risk Veto, toolkit numbers for every argument | When a single verdict would be too easy |
| 🎯 [Accuracy Auditor](agents/accuracy-auditor.md) | Prediction ledger audit, failure logging, model demotion | After every autonomous run, before any report is shared |
| 🧩 [Use-Case Generator](agents/use-case-generator.md) | Completed research into killable applied proposals | After a research report exists, never instead of one |
| 🧾 [Ledger Controller](agents/ledger-controller.md) | Input-ledger integrity: control totals, cut-off, restatements, frozen inputs | Before any analyst touches the numbers, and after any restatement |
| 🛡️ [Risk Stance Analyst](agents/risk-stance-analyst.md) | Downside scenarios in risky/safe/neutral stances, triggers, never sizing | After the Bull/Bear debate, before the Risk Veto |
| 📄 [Filings Analyst](agents/filings-analyst.md) | Filed numbers first: audited filings, YoY + TTM, DERIVED marking, lag and one-off flags | Before any press-release or headline claim is trusted |
| 🇳🇵 [NEPSE Fundamentals Analyst](agents/nepse-fundamentals-analyst.md) | NEPSE fundamentals by sector: banks, hydropower, insurance, microfinance — filed numbers first | A NEPSE-listed company, by sector |
| 📈 [NEPSE Technical Analyst](agents/nepse-technical-analyst.md) | NEPSE technicals: momentum, trend, volatility, RSI, circuit limits, exit liquidity — past bars only | A past-bars read on a NEPSE subject |
| 📰 [NEPSE News & Sentiment Analyst](agents/nepse-news-sentiment-analyst.md) | NEPSE news + sentiment in Nepali and English, counted by source, date, stance | Inside a NEPSE study, before the debate step |
| 🔀 [NEPSE Broker-Flow Analyst](agents/nepse-broker-flow-analyst.md) | NEPSE broker flow — indicative only, never proven smart money | When broker buy/sell rows exist for the subject |
| 🏛️ [NEPSE Macro Analyst](agents/nepse-macro-analyst.md) | Nepal macro for NEPSE: NRB policy, liquidity, rates, remittances, inflation | Placing a NEPSE subject in Nepal macro context |
| 🎁 [NEPSE Corporate Actions Analyst](agents/nepse-corporate-actions-analyst.md) | NEPSE corporate actions: bonus, rights, dividends, splits, mergers — filing first | When an action affects the subject |
| 🧑‍💼 [NEPSE Trader](agents/nepse-trader.md) | NEPSE Trader step: debate into one gated hypothetical plan — research only, never an order | After the Bull/Bear debate, before the Risk team |
| 🛡️ [NEPSE Risk Team](agents/nepse-risk-team.md) | NEPSE Risk team: Aggressive / Neutral / Conservative debate + joint verdict | After the Trader's plan, before the gate |
| 🎯 [NEPSE Portfolio Manager](agents/nepse-portfolio-manager.md) | NEPSE Portfolio Manager step: reflections, debate, plan, risk verdict → publication gate | Last step: the publication gate, with the decision logged |
| 🏦 [NEPSE Bank Analyst](agents/nepse-bank-analyst.md) | NEPSE banks: CAR, NPL, NIM, cost-to-income, CD ratio, provisioning cover | A NEPSE-listed bank needs a sector read in depth |
| ⚡ [NEPSE Hydropower Analyst](agents/nepse-hydropower-analyst.md) | NEPSE hydropower: PPA, plant load factor, generation vs capacity, construction vs operating | A NEPSE-listed hydropower company needs a sector read in depth |
| 🛡️ [NEPSE Insurance Analyst](agents/nepse-insurance-analyst.md) | NEPSE insurance: solvency margin, combined ratio, premium growth, claim ratio | A NEPSE-listed insurer needs a sector read in depth |
| 🌱 [NEPSE Microfinance Analyst](agents/nepse-microfinance-analyst.md) | NEPSE microfinance: NPL, cost of funds, opex ratio, portfolio yield vs funding cost | A NEPSE-listed microfinance institution needs a sector read in depth |
| 📈 [NEPSE Mutual Fund & NAV Analyst](agents/nepse-mutual-fund-nav-analyst.md) | NEPSE mutual funds: NAV per unit, premium/discount to NAV, expense ratio, holdings | A NEPSE-listed fund needs a NAV-and-discount read |
| 🚀 [NEPSE IPO Analyst](agents/nepse-ipo-analyst.md) | NEPSE IPOs: prospectus, issue price vs book value, promoter holding, allotment, lock-in | An IPO or recent listing needs a prospectus read |
| 🧾 [NEPSE Fees & Tax Analyst](agents/nepse-fees-and-tax-analyst.md) | NEPSE costs: broker slabs, SEBON fee, DP charge, CGT, circuit limits, settlement | Any cost, tax, or settlement question on a NEPSE trade |
| ✍️ [NEPSE Content Writer](agents/nepse-content-writer.md) | Nepali & English research writing: plain language, sourced numbers, no value language | A completed study needs plain-language writing |

Guide (not an agent, not counted in the 36): [When to use which agent](agents/WHEN-TO-USE.md) — one line per agent on when to use it vs its nearest neighbour. It is listed in `agents.json` only because the roster check counts every `.md` file in `agents/`; the pack remains 36 agents + 1 guide file.


## 🇳🇵 NEPSE sector agents (Engine 1.8, 2026-11-07)

Eight new agents deepen the NEPSE Fundamentals sector guidance into one
agent per sector or topic (see the roster above): Bank (CAR, NPL, NIM,
cost-to-income, credit-deposit ratio, provisioning cover), Hydropower
(PPA rate and years, plant load factor, generation vs capacity,
construction vs operating), Insurance (solvency margin, combined ratio,
premium growth, claim ratio, underwriting vs investment kept apart),
Microfinance (NPL, cost of funds, operating expense ratio, portfolio
yield vs funding cost), Mutual Fund & NAV (NAV per unit, premium/discount
to NAV marked DERIVED, expense ratio, holdings, distributions as history
only), IPO (prospectus first; grey-market numbers are never quoted),
Fees & Tax (broker slabs, SEBON fee, DP charge, CGT by holding period,
circuit 15% from 2026-04-20, 10% before; T+2 settlement, transition date
unverified — every figure sourced, or UNKNOWN), and Content Writer
(Nepali- and English-language plain-language write-ups of completed
studies only, no value language).

Four requested roles were checked against the live roster and NOT added
as duplicates: corporate actions (nepse-corporate-actions-analyst),
macro (nepse-macro-analyst), risk analyst (nepse-risk-team plus
risk-stance-analyst), and orchestrator (research-orchestrator).

Every new agent has a SKILL.md mirror under `skills/<slug>/SKILL.md`
(same content, skill format; the agent file is canonical). The
installer now covers five tools — Claude Code, GitHub Copilot, Cursor,
Gemini CLI, Codex (`./scripts/install.sh --tool cursor|gemini|codex`)
— and `./scripts/convert.sh` generates per-tool integration dirs
(`integrations/<tool>/agents/`, plus `skills/` copies; Cursor gets a
`.mdc` file carrying the agent's own description line). The agent-file
template pattern is adapted from agency-agents (MIT, see
`docs/SOURCES_MERGE_2026-11-07.md`); no agency-agents text was copied.

## 🎯 Runbooks — teams that work together

A runbook is a team for one job, in order. See `runbooks/`.
12 runbooks.

| Runbook | Team | Job |
|---|---|---|
| [Company deep dive](runbooks/company-deep-dive.md) | Researcher → Forensic → Financial → Valuation → Reality Checker | One company, fully checked, thesis + downside + open questions |
| [Earnings review](runbooks/earnings-review.md) | Financial → Reality Checker | One quarter, what actually moved, what to ask next |
| [Portfolio forecast](runbooks/portfolio-forecast.md) | Portfolio & Forecast → Reality Checker | Portfolio, performance, walk-forward forecasting |
| [Prediction accuracy loop](runbooks/prediction-accuracy-loop.md) | Accuracy Auditor → Reality Checker | Audit the prediction ledger, log failures, demote failing models |
| [Data first](runbooks/data-first.md) | Data Scout → Statement Reconciler → Financial → Reality Checker | No analysis on unvalidated, untied data |
| [Macro to company](runbooks/macro-to-company.md) | World → Nepal → Investment → Reconciler → Financial → Valuation → Reality | Full top-down study, with the Accuracy Auditor ledger rule on forecasts |
| [Research to use case](runbooks/research-to-use-case.md) | Completed research → Use-Case Generator → Data Scout licence check → Reality Checker | Finished research into killable proposals, killed candidates reported |
| [Agent execution contract](runbooks/agent-execution-contract.md) | Orchestrator → Reality Checker → Accuracy Auditor | Inputs, sources, output schema, citation + provenance checks, falsifier rule for every run |
| [Structured debate](runbooks/structured-debate.md) | Orchestrator → Ledger Controller → parallel analysts → Debate → Risk Stance → Reality Checker | Parallel analysis, Bull/Bear debate, risk scenarios, publication gate |
| [Nepal research to use case](runbooks/nepal-research-to-use-case.md) | Nepal Researcher → Data Scout → Ledger Controller → Use-Case Generator → Reality Checker | Completed Nepal research into killable proposals, sectors alphabetical unless evidence ≥ 3 |
| [Hypothetical position review](runbooks/hypothetical-position-review.md) | Orchestrator → Risk Stance → Reality Checker | Pre-publication / pre-simulation risk gate for a hypothetical plan: 16 checks, PASS/BLOCK, never a recommendation |
| [NEPSE agent team](runbooks/nepse-agent-team.md) | Orchestrator → Ledger Controller → six NEPSE analysts (parallel) → Debate → Trader → Risk team → Portfolio Manager → Reality Checker → Accuracy Auditor | Full NEPSE study: parallel analysts, Bull/Bear debate, gated hypothetical plan, three-way risk debate, publication gate with decision logging |

## 🇳🇵 NEPSE agent team (Engine 1.3, 2026-11-07)

Nine new agents form the NEPSE team (see the roster above), run by
`runbooks/nepse-agent-team.md`: six analysts in parallel
(Fundamentals with sector guidance for banks, hydropower, insurance,
and microfinance; Technical; News & Sentiment in Nepali and English;
Broker-flow, labelled INDICATIVE ONLY throughout; Macro on NRB
policy, liquidity, rates, and remittances; Corporate Actions), then
a Bull vs Bear debate (existing Debate Analyst + structured-debate
runbook), then Trader (one gated hypothetical plan), Risk team
(Aggressive / Neutral / Conservative), and Portfolio Manager (reads
the decision-memory reflections first, issues the publication gate,
logs the decision). The pattern is adapted from TradingAgents
(Apache-2.0) — reimplemented in this pack's own words, with its
five-tier Buy/Overweight/Hold/Underweight/Sell rating NOT adopted.

Every NEPSE agent states it works with any LLM, including a free
local Ollama — and with no LLM at all, via the toolkit's
deterministic no-LLM rules mode
(`investment-analyst-toolkit/toolkit/rules_mode.py`, zero API keys,
offline). No API keys or key-requiring endpoints are hard-coded
anywhere in the pack.

Decision memory (Engine 1.4) lives in the toolkit
(`toolkit/decision_log.py`): every call logged before its outcome,
settled after its horizon against realised return and alpha vs the
NEPSE index (index source named, never invented), and scored on the
public track record — which starts at **n=0, no calls settled yet**
(see the toolkit's `docs/track-record.md`).

## 🌍 Global rules-mode personas (companion toolkit)

The world side of this pack is not NEPSE-only. The companion toolkit
([`investment-analyst-toolkit`](https://github.com/ShirjanKhadka1/investment-analyst-toolkit),
`toolkit/rules_mode.py` v1.4.0) carries a 5-persona market-agnostic
rules-mode team that mirrors the NEPSE team's structure — deterministic
rules over caller-supplied inputs, nothing fetched, nothing guessed,
UNKNOWN for anything not supplied:

- `us_large_cap_fundamentals` — US large-cap fundamentals (EDGAR XBRL metrics)
- `etf_index` — ETF / index reads
- `fx_macro` — FX / macro reads
- `crypto` — crypto reads
- `earnings` — earnings events

These five personas live in the toolkit repo, not this one; this pack's
own world-side agent is the World Market Researcher in the roster above.
To run a full top-down study — world context first, then the home market,
then the company — use
[runbooks/macro-to-company.md](runbooks/macro-to-company.md)
(World → Nepal → Investment → Reconciler → Financial → Valuation →
Reality).

## 📝 Templates — 8, with a completeness checker

`templates/` holds the reusable research templates: initiation report,
earnings review, forensic checklist, valuation sanity check,
data-first checklist, structured debate, ledger-control checklist,
and research to use case. The last four moved here from
[`equity-research-playbook`](https://github.com/ShirjanKhadka1/equity-research-playbook)
on 7 Nov 2026 (content merge approved by the owner; that repo is
retained for history with a pointer to this pack). The four that were
already here are byte-identical to the playbook's copies — no
duplication remains. Templates are not agents: the pack stays
36 agents + 8 templates.

`examples/bottlers-nepal-terai-initiation-example.md` is a filled
initiation template for Bottlers Nepal (Terai) (BNT, NEPSE) —
labelled on its first lines as an **illustrative filled template,
NOT a valuation**: no DCF, no target price, no rating, no
recommendation. Every figure carries its source and period, or is
labelled UNKNOWN.

`scripts/check_template.py` is the stdlib-only template-completeness
checker (moved with the templates): it reports missing or empty
required sections and exits 1 in that case. Its tests live in
`tests/test_check_template.py` (6 tests):

```sh
python scripts/check_template.py examples/bottlers-nepal-terai-initiation-example.md
python -m pytest tests/ -v
```

### Quality gates (Phase 4)

```bash
pip install -r requirements-dev.txt   # pinned pytest, identical to CI
python scripts/qa.py                  # every gate in order; stops at the first failure
```

`scripts/qa.py` runs the test suite, the roster check
(`ops/check_roster.py`), the counts check (`ops/generate_counts.py` +
`ops/check_numbers.py`), the licence check, the secret scan (tree +
git history), and the link check (internal links must resolve;
external links best-effort). Run one gate with
`python scripts/qa.py --only <gate>` (`--list` shows the names). The
same gates run in CI via `.github/workflows/test.yml`; the Phase 4
workflow is staged for deployment via the browser route and is not
live until its first run is observed.

## 📋 What every agent in this pack does (and refuses to do)

**Every agent:**
- States its thesis in one paragraph before any numbers.
- Sources every number (source + period, on the same page as the number).
- Shows the downside case and what would change its mind (the falsifier).
- Lists open questions and unverified items instead of hiding them.
- Works only from sources the user provides, or from public sources it cites.

**Every agent refuses to:**
- Recommend buy / sell / hold as investment advice.
- Invent a price, a forecast, a growth rate, or a peer multiple.
- Present coursework, a personal project, or an unfinished study as
  professional experience or as a completed valuation.
- Confuse tickers across exchanges (NEPSE BNT ≠ NYSE BNT — exchange always stated).
- Touch real credentials, real accounts, or non-public data.

## 🆕 v0.4 improvements

- **Debate Analyst (new, 9th agent):** every thesis is argued Bull vs Bear from computed numbers, and the Risk Manager can veto to zero.
- **Toolkit v0.4 companion:** options, Monte Carlo, costed backtests, CLI, fresh-data fallback chain (no stale data), predictive auto-selection + ensemble, and an autonomous updater that re-runs reports daily with a hash-chained audit log — see [investment-analyst-toolkit](https://github.com/ShirjanKhadka1/investment-analyst-toolkit).

## 🎯 Accuracy Auditor (new, 10th agent)

Audits the prediction ledger, logs failures, demotes failing models, and checks archive completeness and data freshness before any report goes out. Runbook: `runbooks/prediction-accuracy-loop.md`.

## 🧰 How this repo is organised (the agency-agents pattern, finance-only)

```
agents/            one .md file per agent: identity, mission, workflow, deliverables, rules
runbooks/          teams of agents for one job, in order
templates/         8 templates (see Templates below): initiation report, earnings review, forensic checklist, valuation sanity check, data-first checklist, structured debate, ledger-control checklist, research to use case, data-first checklist, structured debate, ledger-control checklist, research to use case (8 templates; the last four moved here from `equity-research-playbook` on 7 Nov 2026 — see Templates below)
examples/          worked examples on DEMO data only, plus one inputs-only Nepal case study
docs/worked-example/  full worked example on a real subject: Bottlers Nepal (Terai), NEPSE: BNT, via the structured-debate runbook (research only; frozen as of 2026-10-16; not a runbook, not counted in the 10)
scripts/           install.sh — copies agent files to your tool's agent directory, nothing else
agents.json        machine-readable roster: every agent, its file, its specialty
```

## 🤝 Contributing

Add a new agent, improve an existing one, or share a worked example:

1. One agent = one file in `agents/`, following the format in
   `agents/investment-researcher.md` (frontmatter + identity + workflow +
   deliverables + rules + example prompt). New agents also carry two
   template sections: **Inputs/Outputs** (the handoff contract — what
   the agent takes in and what it hands on) and **Success metrics**
   (how "done" is judged). The 10 original agents have not yet been
   retrofitted with those two sections — that is a follow-up pass,
   not part of this slice.
2. Add it to `agents.json` and to the roster table above.
3. No real company data without a source. No investment recommendations.
4. Test the install script with `--dry-run` before submitting.

## 📜 License

MIT. Use it, fork it, teach with it, build a business on it — just keep the
accuracy rules, because those are what make it useful.

## Limitations

- These agents are Markdown files: they run inside the reader's own AI
  tool, on the reader's own machine. This repo itself executes nothing
  and fetches no live data.
- An agent's output is only as good as the sources it is given. A number
  without a source and a period in the output must be treated as UNKNOWN.
- No live NEPSE feed is provided or claimed anywhere in this repo.

> Research only, not investment advice; never a buy/sell recommendation

See `CONTRIBUTING.md` for how to contribute and `SECURITY.md` for how to
report a security issue privately.

