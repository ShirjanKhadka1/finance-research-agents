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

## 🎨 The roster

| Agent | Specialty | When to use |
|---|---|---|
| 🔍 [Investment Researcher](agents/investment-researcher.md) | Due diligence, thesis, market research | Starting any company study |
| 📊 [Financial Analyst](agents/financial-analyst.md) | Three-statement analysis, ratios, forecasting drivers | Reading financials, building a model |
| 🔬 [Forensic Analyst](agents/forensic-analyst.md) | Profit quality, red flags, cash vs profit | Before you trust the numbers |
| 💎 [Valuation Analyst](agents/valuation-analyst.md) | DCF, multiples, sanity checks, implied assumptions | Before any target price is discussed |
| 🇳🇵 [Nepal Market Researcher](agents/nepal-market-researcher.md) | NEPSE, sourced Nepal market research | Nepal-listed companies, with exchange always stated |
| 🛡️ [Reality Checker](agents/reality-checker.md) | Review, falsifiers, downside, accuracy audit | Last pass before anything is shared |
| 🌍 [World Market Researcher](agents/world-market-researcher.md) | Global markets, regimes, cross-border themes | Comparing markets, placing a local story in world context |
| 📈 [Portfolio & Forecast Analyst](agents/portfolio-forecast-analyst.md) | Portfolio, performance, walk-forward forecasting, free API data | Building a portfolio, judging a model, forecasting honestly |
| ⚔️ [Debate Analyst](agents/debate-analyst.md) | Bull vs Bear debate + Risk Veto, toolkit numbers for every argument | When a single verdict would be too easy |
| 🎯 [Accuracy Auditor](agents/accuracy-auditor.md) | Prediction ledger audit, failure logging, model demotion | After every autonomous run, before any report is shared |

## 🎯 Runbooks — teams that work together

A runbook is a team for one job, in order. See `runbooks/`.

| Runbook | Team | Job |
|---|---|---|
| [Company deep dive](runbooks/company-deep-dive.md) | Researcher → Forensic → Financial → Valuation → Reality Checker | One company, fully checked, thesis + downside + open questions |
| [Earnings review](runbooks/earnings-review.md) | Financial → Reality Checker | One quarter, what actually moved, what to ask next |

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
scripts/           install.sh — copies agent files to your tool's agent directory, nothing else
agents.json        machine-readable roster: every agent, its file, its specialty
```

## 🤝 Contributing

Add a new agent, improve an existing one, or share a worked example:

1. One agent = one file in `agents/`, following the format in
   `agents/investment-researcher.md` (frontmatter + identity + workflow +
   deliverables + rules + example prompt).
2. Add it to `agents.json` and to the roster table above.
3. No real company data without a source. No investment recommendations.
4. Test the install script with `--dry-run` before submitting.

## 📜 License

MIT. Use it, fork it, teach with it, build a business on it — just keep the
accuracy rules, because those are what make it useful.
