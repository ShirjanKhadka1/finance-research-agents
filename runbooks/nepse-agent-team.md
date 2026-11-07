# Runbook: NEPSE agent team

> Research only, not investment advice. This runbook ends in a
> publication gate (publish / publish with stated limits / hold),
> never in a buy/sell/hold recommendation, never in a position size,
> never in a trade.

## Team, in order

Research Orchestrator → Ledger Controller → six NEPSE analysts (in
parallel: Fundamentals, Technical, News & Sentiment, Broker-flow,
Macro, Corporate Actions) → Bull vs Bear debate (Debate Analyst,
structured-debate runbook) → Trader → Risk team (Aggressive /
Neutral / Conservative) → Portfolio Manager → Reality Checker →
Accuracy Auditor (for any forecast the run touches).

## The synchronisation rule (the whole point)

Analysts run **in parallel**, each on its own sources, and the debate
**does not start until every analyst has reported**. A missing report
blocks the debate — it is not skipped, and the debate is not held
with a placeholder. The Orchestrator records which reports landed,
which are missing, and what blocks them. This is the discipline
borrowed, as a pattern, from multi-agent debate frameworks:
parallel analysis first, structured disagreement second, verdict
last. The pattern is adapted from TradingAgents (Apache-2.0) —
reimplemented in this pack's own words, with its five-tier
Buy/Overweight/Hold/Underweight/Sell rating NOT adopted.

## LLM flexibility — any model, or none

Every agent in this team is a Markdown persona: it runs in the
reader's own AI tool with whatever LLM that tool already uses,
including a free local model via Ollama. No provider, model, or API
key is required or hard-coded. With no LLM at all, the core runs in
the toolkit's deterministic no-LLM rules mode
(`investment-analyst-toolkit/toolkit/rules_mode.py`,
`run_rules_team()`): sector checklists, technical read, Nepali +
English lexicon sentiment, indicative broker flow, macro checklist,
corporate-action flags — same structured output shape, zero API
keys, offline. A rules-mode run is labelled as such in the report.

## Steps

1. **Freeze.** Ledger Controller certifies the inputs (control
   totals, cut-off, restatement log) and the Orchestrator stamps
   the as-of date. No analyst starts on uncertified inputs.
2. **Parallel analysis.** The six NEPSE analysts each produce a
   report in their structured format, with sourced numbers +
   periods. Analysts do not read each other's drafts mid-run —
   independence is the point. Broker-flow claims carry the
   INDICATIVE ONLY label throughout.
3. **Bull vs Bear debate.** Debate Analyst stages the debate
   (runbooks/structured-debate.md, templates/structured-debate.md):
   each side states its case with toolkit numbers, each argument
   is answered by the other side or marked unanswered. The losing
   side's best argument survives in the record.
4. **Trader.** The Trader turns the debate into one written
   hypothetical plan — exit before entry, size as the minimum of
   limits — and runs the risk gate (16 checks, then the 19-check
   extended gate with per-idea limits: max loss per idea, sector
   concentration, exit liquidity). A plan that has not passed is
   labelled "not reviewed" and goes no further.
5. **Risk team.** Aggressive, Neutral, and Conservative debate the
   plan in writing (one round each), argue the per-idea limits
   explicitly, and issue a joint verdict: VETO / SCALE DOWN /
   PASS WITH STATED LIMITS.
6. **Portfolio Manager.** Reads the decision-memory reflections
   for the symbol first (or records honestly that there are none —
   the scoreboard starts at n=0), then the debate, plan, and risk
   verdict, and issues the publication gate: PUBLISH / PUBLISH WITH
   STATED LIMITS / HOLD. The decision is logged to the decision log
   (`toolkit/decision_log.py`) before it is shared, with its
   horizon and confidence, so it can be settled and scored later.
7. **Last pass.** Reality Checker reads the draft for invented
   numbers, unsourced claims, missing falsifier, or missing
   downside. Accuracy Auditor logs any forecast the run touched,
   before outcomes, with n and horizon — pending never counts as a
   win.

## Done when

- Every analyst reported, or the run is honestly reported as blocked.
- Debate record shows answered and unanswered arguments separately.
- Trader plan carries its gate verdict and fingerprint; a PASS is
  labelled "not a recommendation".
- Risk verdict exists, with per-idea limits argued explicitly.
- Portfolio Manager gate is one of the three gates, with reasons
  tied to claims, and the decision is logged to the decision log.
- The report carries its falsifier and its downside, and no
  recommendation.
