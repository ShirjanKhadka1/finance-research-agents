# Structured debate runbook

> Research only, not investment advice. This runbook ends in a publication
> gate (publish / publish with limits / hold), never in a buy/sell/hold
> recommendation, never in a position size, never in a trade.

## Team, in order
Research Orchestrator → Ledger Controller → analysts (in parallel) →
Debate Analyst → Risk Stance Analyst → Reality Checker → Accuracy Auditor
(for any forecast the debate touches).

## The synchronisation rule (the whole point)
Analysts run **in parallel**, each on its own sources, and the debate
**does not start until every analyst has reported**. A missing report
blocks the debate — it is not skipped, and the debate is not held with
a placeholder. The Orchestrator records which reports landed, which are
missing, and what blocks them. This is the discipline borrowed, as a
pattern, from multi-agent debate frameworks: parallel analysis first,
structured disagreement second, verdict last.

## Steps
1. **Freeze.** Ledger Controller certifies the inputs (control totals,
   cut-off, restatement log) and the Orchestrator stamps the as-of date.
   No analyst starts on uncertified inputs.
2. **Parallel analysis.** Fundamentals, news/sentiment, technicals, and
   Nepal/world context (as the study needs them) each produce a report
   with sourced numbers + periods. Analysts do not read each other's
   drafts mid-run — independence is the point.
3. **Bull vs Bear debate.** Debate Analyst stages the debate: each side
   states its case with toolkit numbers, each argument is answered by
   the other side or marked unanswered. The losing side's best argument
   survives in the record.
4. **Risk-stance pass.** Risk Stance Analyst writes the risky, safe, and
   neutral downside scenarios with observable triggers (see its agent
   file). Scenarios are analysis, not advice.
5. **Risk Veto.** Debate Analyst + Reality Checker issue the gate:
   **Publish** (claims check out), **Publish with stated limits**
   (claims check out within named limits), or **Hold** (a claim fails
   its source, a scenario has no trigger, or a debate argument stands
   unanswered). A Hold sends the report back to the failing step, not out.
6. **Ledger.** Accuracy Auditor logs any forecast the debate touched,
   before outcomes, with n and horizon — pending never counts as a win.

## Done when
- Every analyst reported, or the run is honestly reported as blocked.
- Debate record shows answered and unanswered arguments separately.
- Three risk scenarios exist, each with a trigger.
- The veto verdict is one of the three gates, with reasons tied to claims.
- The report carries its falsifier and its downside, and no recommendation.
