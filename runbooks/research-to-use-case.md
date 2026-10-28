# Runbook: Research to use case

**Team, in order:** Completed research (input) → Use-Case Generator →
Data Scout (licence check) → Reality Checker

**Purpose:** turn finished research into honest applied next steps —
a short list of killable proposals, each with evidenced problem,
named beneficiary, checked data terms, feasibility verdict, and kill
criterion. This runbook generates proposals; it never replaces the
research, and it never promises a build, a sale, or an outcome.

## Step 0 — Input: completed research
- The input is a completed research report (thesis, findings, risks,
  falsifier, open questions), with every number sourced + period or
  labelled UNKNOWN.
- If the report's numbers are unsourced, send it back to the Reality
  Checker first — use cases are not generated from unsourced research.

## Step 1 — Use-Case Generator
- For each finding that genuinely suggests follow-on work, write one
  use case, at most five, in the fixed shape: evidenced problem,
  named beneficiary and how they would know, proposed study or build,
  data needed, feasibility verdict (Feasible / Feasible with stated
  gaps / Not feasible), kill criterion, and what it is NOT.
- Kill candidates that fail feasibility, data, or kill-criterion
  tests. Report every killed candidate in one line each — killed
  candidates are part of the deliverable, not a failure.
- Output: surviving use cases (ranked by evidenced problem size and
  data availability) plus the killed-candidate list.

## Step 2 — Data Scout (licence check)
- For every dataset each surviving use case needs, check existence
  and licence/terms: source, URL, terms, retrieval date, period,
  freshness verdict.
- A dataset whose licence forbids the proposed use is a blocker; a
  dataset that does not exist is a kill, not a gap to wave past.
- **Licence UNKNOWN if not cleared:** if a dataset's terms cannot be
  established, record its licence as UNKNOWN — never as permission —
  and carry that UNKNOWN label into the use case. No dataset is
  presented as available until its existence and terms are checked.
- Output: DATA_SOURCES entries (or UNKNOWN labels) attached to each
  use case, with any newly killed use cases added to the killed list.

## Step 3 — Reality Checker
- Number audit, claim audit, logic audit, plus a hype and
  advice-shape check: a use case flagged as hype, unsourced, or
  advice-shaped is dropped, not reworded into acceptability.
- Output: fixes list, line by line. Apply the fixes. Re-run this step
  if a fix changed a number.

## Done when
Every surviving use case has an evidenced problem, a named
beneficiary, dataset terms checked or marked UNKNOWN, a feasibility
verdict, and a kill criterion; killed candidates are reported; and
the Reality Checker verdict is Pass. Anything less is labelled
In progress.

**Research only, not investment advice.** This runbook proposes
studies and tools for further research. It never recommends buying,
selling, or holding any security, never promises a return, and never
presents a use case as something that will be built, sold, or
adopted.
