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

18 agents. `agents.json` is the machine-readable roster; this table
mirrors it.

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

Guide (not an agent, not counted in the 18): [When to use which agent](agents/WHEN-TO-USE.md) — one line per agent on when to use it vs its nearest neighbour. It is listed in `agents.json` only because the roster check counts every `.md` file in `agents/`; the pack remains 18 agents + 1 guide file.

## 🎯 Runbooks — teams that work together

A runbook is a team for one job, in order. See `runbooks/`.
10 runbooks.

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
templates/         initiation report, earnings review, forensic checklist, valuation sanity check
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

