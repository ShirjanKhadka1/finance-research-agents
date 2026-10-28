# Runbook: Agent Execution Contract

**Applies to:** every agent run in this pack, single-agent or
multi-agent, whether or not the agent file itself already carries
Inputs, Outputs, and Success metrics sections.

**Purpose:** make any agent run executable and checkable without
rewriting the agent. The Research Orchestrator writes the run
contract before any analyst starts; the Reality Checker (and the
checks in §5–§6 below) is the last pass before anything is shared.
Where an agent file and this contract disagree, this contract
governs the run output — the agent file is left unchanged in this
slice, and the gap is recorded for the follow-up retrofit (see §8).

**Research only, not investment advice.** This contract governs
research. No run under it recommends buying, selling, or holding
any security, presents a forecast as a promise, or guarantees a
return. A thesis, a valuation, a forecast, and a use case are
research outputs, not instructions to act.

## 1. Required Inputs — every run, before any analyst starts

No run starts without this section written down. If a field cannot
be supplied, it is recorded as UNKNOWN (see §7) — except the
as-of date and the exchange, which the Orchestrator refuses to
start without.

- **Subject:** company / market / question, named exactly as it
  appears in its source (company name, not ticker alone).
- **Exchange:** stated every time a ticker or a market appears.
  NEPSE tickers are always labelled NEPSE, and are never confused
  with same-letter tickers on another exchange. Where no exchange
  applies (for example a methods question), write
  "Exchange: not applicable, because…" — never leave it blank.
- **As-of date:** the single point-in-time date for the run.
  Only data published on or before the as-of date may be used in
  a historical run. A figure restated after the as-of date is read
  as first reported, or withheld if its first-reported value cannot
  be established. A dataset whose publication date is unknown is
  withheld for historical runs and labelled UNKNOWN for current
  runs. No as-of date → the run does not start.
- **Datasets:** each dataset the run will use, with source +
  period + licence/terms, or UNKNOWN where any of those is not
  known. Datasets are sourced through the Data Scout's rules:
  primary sources first (see §2); a paywalled, login-locked, or
  undocumented source is refused for the free path and recorded
  as refused, never bypassed; a 403 or 429 is a recorded failure,
  not an invitation to retry harder.
- **Team:** the agents in the run, in order, as named in the
  runbook (or the single agent, for a single-agent run). A missing
  report blocks the debate step; it is never silently skipped, and
  a debate held on a partial analyst set is labelled partial in
  the verdict.
- **Agent-specific inputs:** the inputs already named in the
  agent file (for example the plan and actuals for the FP&A
  Analyst, the statements for the Statement Reconciler, the
  completed report for the Use-Case Generator) sit under this
  contract section. They do not replace it.

## 2. Required sources rule — primary sources first

1. **Primary sources first.** Prefer the issuer's filing or
   annual report, the exchange's publication, and official
   statistics over secondary summaries, news reports, and social
   posts. A secondary source may point to a primary source; it
   never replaces it. Where only a secondary source exists, say
   so, and the claim carries that limit.
2. **Every number needs source + period, or UNKNOWN.** A number
   without a source and a period on the same page as the number
   is not a fact in this run: it is labelled UNKNOWN, listed
   under Open Questions, and excluded from any total, ratio,
   valuation, or stance count that would otherwise use it.
   "UNKNOWN" is a verdict about the evidence, not a placeholder
   to be filled later by guessing.
3. **Fiscal years and units are stated with the number.**
   Nepalese fiscal years (for example FY 2081/82) are never
   silently converted to calendar years; currency, units
   (thousands vs millions), and consolidation basis are stated
   wherever a figure appears. A comparison across different
   fiscal years, currencies, or consolidations is reconciled
   first, or the comparison is labelled UNKNOWN.
4. **No invented numbers, dates, or sources.** No figure, date,
   URL, page reference, or source name is written unless it was
   supplied or verified in a cited source. Demo or fixture data
   is labelled DEMO / FIXTURE, never presented as market data.
   No fake metrics: a rate always carries its denominator and
   its n; a count always carries its period and its total.

## 3. Output schema — every agent run

Every run output contains these sections, in this order. A
section that does not apply to an agent says
"Not applicable, because…" — nothing structural is deleted, and
no section is silently skipped. Agent-specific deliverables (a
variance table, a tie-out table, a DATA_SOURCES table, a use-case
list) sit inside the matching section below; they do not replace
it.

1. **Thesis.** One paragraph, before any numbers, stating the
   run's claim. For a non-thesis agent, this is its verdict in
   one paragraph: the Data Scout's verdict is which datasets are
   usable and which are refused; the Statement Reconciler's
   verdict is TIED / TIED WITH EXPLAINED DIFFERENCES / NOT
   TIED; the Accuracy Auditor's verdict is its scored accuracy
   with n. If no claim can be stated, the thesis section says
   so and the status is Inputs only (see §3, item 6).
2. **Evidence table.** Claim → number → source → period →
   denominator / basis. Every number in the output appears here
   or traces to a row here. A number with no row is an orphan
   number and fails the §6 check.
3. **Downside.** The bear case, in numbers where the data
   allows, with changed inputs — not a flat haircut to a total.
   It states what breaks first (demand, margin, funding,
   regulation, data availability, or the driver named by the
   agent) and what the downside value or outcome is on those
   changed inputs. For a non-thesis agent, the downside is its
   failure mode stated plainly: refused datasets, excluded
   lines, thin coverage, or stale series — carried with the
   reason, not dropped.
4. **Falsifier.** The single observation that would end or
   overturn the thesis, stated before the outcome is known:
   what would be observed, from which source type, over which
   period. A falsifier that cannot be observed, or that restates
   the thesis, is not a falsifier — rewrite it or label the
   thesis "no falsifier stated" and do not present it as a
   conclusion.
5. **What would change my mind.** One paragraph, distinct from
   the falsifier: the evidence, short of full falsification,
   that would materially change the thesis, the verdict, or the
   forward view — and the direction it would change it in.
   This section is where a restated figure, a corrected unit,
   or a new primary source lands; it is never rewritten after
   the outcome arrives to pretend the thesis survived.
6. **Status.** Exactly one of: Inputs only / In progress /
   Completed. Inputs only means inputs were collected but no
   analysis was built; it never carries a valuation conclusion.
   A study with a failed tie-out, unsourced numbers, or a
   missing falsifier is In progress at best, never Completed.
   The status is stated at the top of the output as well as
   here, so a reader skimming the first page cannot mistake an
   unfinished study for a finished one.

## 4. House rules — every run

- Research only. Never a buy, sell, or hold recommendation, in
  any wording. Never a guaranteed return, a promised outcome, or
  a price direction presented as a prediction.
- NEPSE exchange always stated where relevant; same-letter
  tickers on other exchanges are never confused with NEPSE
  tickers.
- No invented numbers, dates, or sources; no fake metrics (a
  rate without its denominator and n is not a result).
- No claim of completion or experience the author does not
  have: coursework is coursework, a personal project is a
  personal project, professional experience is neither.
- No credentials in any output. A user-supplied free key lives
  in environment variables only, never in a file or a report.

## 5. Citation checker rules

Run this check on every output before delivery. The checker is
the Reality Checker role; it does not rewrite the draft to make
it pass — it lists fixes line by line, or sends the draft back.

1. **Every cited source exists.** Each source named in the
   evidence table is checked: it was actually supplied or
   retrieved in the run, under the name given. A source that
   cannot be located is struck, and every number that rested
   on it becomes UNKNOWN.
2. **Date matches period.** Each citation's date (publication
   date, retrieval date, or period covered, as stated) is
   checked against the period the number claims to cover. A
   citation dated after the as-of date in a historical run is
   look-ahead and is excluded. A citation whose date cannot be
   established is labelled UNKNOWN and cannot support a
   period-specific claim.
3. **No dropped denominator.** Every rate, share, ratio, and
   stance count is checked for its denominator: the total it
   is a share of, the base period, the n behind a rate, the
   number of items behind a stance count. A figure whose
   denominator was dropped in writing is sent back, not
   repaired by guessing the denominator.
4. **Primary-source preference is audited, not assumed.** For
   each material claim, the checker notes whether the citation
   is primary or secondary. A material claim resting only on a
   secondary source is flagged with that limit in the output;
   it is not silently upgraded.
5. **Verdict.** Pass / Pass with fixes (list them, line by
   line) / Send back (list the blocking items). No vague
   "looks good". If there are no fixes, say so in one line —
   do not invent fixes to look busy.

## 6. Number-provenance checker rules

Run this check alongside §5, on every output, before delivery.

1. **Trace every number.** Each number traces to exactly one
   of: (a) an input dataset row (source + period), or
   (b) a calculation shown in the output (inputs + formula +
   result). A number that traces to neither is an orphan
   number: delete it or label it UNKNOWN.
2. **Recompute spot-checks.** Recompute, by hand or by
   re-running the stated calculation, at least: every total
   that feeds a verdict, every ratio in the ratios table, the
   DuPont components against ROE where DuPont is used, and
   one line per table. A recomputation that does not match is
   a blocking failure, not a rounding note, unless the
   difference is stated as rounding with its size.
3. **Flag restated figures.** If a prior period was restated,
   both versions are shown, the output states which version
   it uses and why, and the as-of-date rule in §1 decides
   which version a historical run may use. A restated figure
   presented as if it were the first-reported figure fails
   this check.
4. **Units, currency, and fiscal year are re-checked.** A
   failure caused by mixing thousands with millions, NPR with
   another currency, or a Nepalese fiscal year with a
   calendar year is a data error: fix the units and re-run
   the affected checks, recording every fix.
5. **UNKNOWN is never filled, never smoothed.** Unknown is
   stated as UNKNOWN, never filled, never smoothed. An
   UNKNOWN value is never interpolated, averaged away,
   replaced by a peer value, carried forward as if known, or
   folded into a total. A total that includes an UNKNOWN
   component is itself UNKNOWN for that component, with the
   component named — or the component is excluded with the
   reason stated and the total labelled partial.
6. **Verdict.** Same Pass / Pass with fixes / Send back
   scale as §5. A failed provenance check stops the run at
   that step; the run may resume after the failure is fixed,
   it may not skip the failed step and continue as if it
   passed.

## 7. UNKNOWN-handling rule

Unknown is stated as UNKNOWN, never filled, never smoothed.

That sentence is the whole rule, applied everywhere: in the
Inputs section (§1), in the evidence table (§3), in a
DATA_SOURCES entry, in a tie-out table (a check not run is
NOT RUN with the reason, never silently skipped), in a stance
count (an unclear item keeps the stance "unclear", never
forced into positive or negative), and in a forecast (a driver
with no source is UNKNOWN, and a forward view built on it says
so). UNKNOWN is listed under Open Questions with what would
resolve it — the single document, dataset, or source that
would turn it into a sourced figure. UNKNOWN is not a failure
of the run; filling it in is.

## 8. Scope note — retrofit still owed (deferred, not done here)

This contract is new. The six newest agents (fpa-analyst,
data-scout, statement-reconciler, research-orchestrator,
news-sentiment-analyst, use-case-generator) already carry
Inputs, Outputs, and Success metrics sections, and were patched
in this slice only with a contract pointer and, where missing,
a falsifier section. The ten original agents do not yet carry
this contract's sections in their own files; they are run under
this contract by supplying the missing sections in the run
output, and their files are retrofitted in a follow-up slice —
not silently rewritten here. The gap table for that retrofit is
held in the Phase 5 deliverable, not in this runbook, so this
file stays a contract, not a status report.

## 9. Done when

Every run under this contract is done when: the §1 Inputs
section is complete or explicitly UNKNOWN; every number is
sourced with source + period or labelled UNKNOWN; the §3
output schema is present in full (with "Not applicable,
because…" where a section genuinely does not apply); the §5
citation check and the §6 number-provenance check both read
Pass; a falsifier and a what-would-change-my-mind paragraph
are stated before the outcome is known; and the status is
stated honestly. Anything less is labelled In progress.
