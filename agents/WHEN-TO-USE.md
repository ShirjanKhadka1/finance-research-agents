# When to use which agent

**This file is a guide, not an agent.** It exists to cut the overlap
complaint: for each of the 18 agents, one line stating when to use it
and how it differs from its nearest neighbour. Scopes below are taken
from each agent file's own frontmatter and mission — no capability
has been added here. If this guide and an agent file disagree, the
agent file wins.

> Roster note, stated honestly: the roster check
> (`ops/check_roster.py`) counts every `.md` file in `agents/`, so
> this guide file is listed in `agents.json` and linked in the README
> only so that unmodified check still passes. It is **not** a 19th
> agent. The pack has **18 agents** plus this 1 guide file, and
> **10 runbooks**. See the note under the README roster table.

| Agent | Use it when… (vs its nearest neighbour) |
|---|---|
| [Research Orchestrator](research-orchestrator.md) | You are running any multi-agent runbook and need the contract, as-of date, synchronisation, checkpoint/resume, and thesis-log settlement — vs every analyst: it runs the run, it does no analysis itself. |
| [Data Scout](data-scout.md) | You need data you do not already hold and must name its source, licence/terms, freshness, and schema first — vs Ledger Controller: the Scout finds and vets sources, the Controller freezes and certifies the inputs chosen. |
| [Investment Researcher](investment-researcher.md) | You are starting a company study and need a sourced thesis plus downside — vs Financial Analyst: the Researcher owns the thesis, the Analyst owns the statement ratios and drivers behind it. |
| [News & Sentiment Analyst](news-sentiment-analyst.md) | You are inside a deep dive or market study, before the debate step, and need what is being said counted by source, date, and stance — vs Investment Researcher: sentiment is a read of coverage, never evidence about fundamentals. |
| [Forensic Analyst](forensic-analyst.md) | You are about to trust a set of numbers and need profit quality tested (cash vs profit, one-offs, tax items, funding) — vs Statement Reconciler: Forensic judges quality, Reconciler mechanically ties statements. |
| [Statement Reconciler](statement-reconciler.md) | You have any set of statements and need the mechanical tie-out (balance sheet, cash flow, equity, segments, comparatives) before analysis starts — vs Forensic Analyst: a tie-out proves the numbers add up, not that the profit is good. |
| [Financial Analyst](financial-analyst.md) | You are reading financials or building a model (three statements, ratios, DuPont, drivers) — vs Valuation Analyst: Financial explains what happened and what drives it, Valuation attaches a value and its implied assumptions. |
| [FP&A Analyst](fpa-analyst.md) | A plan, budget, or rolling forecast exists and must be tested against actuals, variance decomposed by driver — vs Financial Analyst: FP&A tests a plan, Financial reads reported statements. |
| [Valuation Analyst](valuation-analyst.md) | Any value or target discussion is on the table (DCF, multiples, Gordon growth, sanity checks) — vs Financial Analyst: Valuation comes only after the financial picture exists, and multiples go on normalised earnings, not a depressed or one-off year. |
| [Nepal Market Researcher](nepal-market-researcher.md) | The subject is NEPSE-listed or the question is Nepal market structure, with exchange always stated and fiscal years kept as BS years — vs World Market Researcher: Nepal sourcing never substitutes for, and is never replaced by, world context. |
| [World Market Researcher](world-market-researcher.md) | You are comparing markets, tracking a global theme, or placing a local story in world context, regime first and like-for-like — vs Nepal Market Researcher: world context frames the local story, it does not source it. |
| [Portfolio & Forecast Analyst](portfolio-forecast-analyst.md) | You are building a portfolio, judging a model, or forecasting from price/return data with benchmarks and walk-forward tests — vs FP&A Analyst: Portfolio forecasts returns and models, FP&A forecasts company operating lines against a plan. |
| [Debate Analyst](debate-analyst.md) | A single verdict would be too easy, so the thesis must survive Bull vs Bear plus a Risk Veto publication gate — vs Reality Checker: Debate stages the disagreement and issues the veto, Reality Checker is the independent last pass on the draft. |
| [Accuracy Auditor](accuracy-auditor.md) | A run carried forecasts and the report must not go out until the prediction ledger is audited (accuracy with n stated, failures logged, failing models demoted) — vs Reality Checker: the Auditor gates the prediction record, the Checker gates the draft. |
| [Reality Checker](reality-checker.md) | Anything is about to be shared and needs the last pass for invented numbers, unsourced claims, missing falsifier, or missing downside — vs Accuracy Auditor: the Checker audits draft truthfulness, the Auditor audits forecast accuracy. |
| [Use-Case Generator](use-case-generator.md) | A research report already exists and you need honest applied next steps, each with a kill criterion — vs Investment Researcher: use cases follow completed research, they never replace it. |
| [Ledger Controller](ledger-controller.md) | No analyst has touched the numbers yet, or a restatement has landed, and inputs need freezing with control totals, cut-off, and a restatement log — vs Data Scout: the Controller certifies frozen inputs, the Scout found them. |
| [Risk Stance Analyst](risk-stance-analyst.md) | The Bull/Bear debate is done and the veto needs concrete downside: risky, safe, and neutral scenarios, each with an observable trigger — vs Debate Analyst: Risk Stance supplies the scenarios, Debate issues the veto; it never sizes a position and never recommends a trade. |

## The overlap rule in one paragraph

If two agents could both do the job, pick by **stage, not by topic**:
contract → sources → frozen inputs → tie-out → statements →
profit quality → thesis → value → debate → scenarios → veto →
last pass → ledger audit. An agent used out of stage is the overlap
complaint happening in real time; an agent used in stage is the
pack working as designed.
