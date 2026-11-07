# Runbook: Hypothetical position review

**Team, in order:** Research Orchestrator → Risk Stance Analyst →
Reality Checker

**Purpose:** a pre-publication / pre-simulation risk gate for a
hypothetical plan. Nothing in this runbook places, suggests, or
executes a trade. It checks a written hypothetical plan against 16
named checks and returns PASS or BLOCK. A PASS only means the
hypothetical plan passed the checklist; it is not a recommendation,
not an approval to act, and not a prediction that the plan would
have worked.

**Research only, not investment advice.** No run under this runbook
recommends buying, selling, or holding any security, sizes a real
position, or presents a simulation as a forecast. The plan under
review is hypothetical: its prices, sizes, and outcomes are
illustrative, labelled as such, and never presented as real.

**Applies to:** any hypothetical plan that will be published in a
report or run in a simulation. A plan that has not passed this gate
is labelled "not reviewed" and is not published or simulated.

## The plan under review

The plan is a single written document, dated, naming: the subject
(company + exchange, tickers never confused across exchanges), the
hypothetical entry and exit levels with their sources, the
hypothetical size and its basis, the stop / review trigger, the
maximum hypothetical loss, the reward:risk arithmetic, the entry
window, and the simulation day it belongs to. A plan missing any of
those fields is BLOCK on check 1 and is not reviewed further until
it is complete.

## The 16 checks

Each check is PASS or BLOCK, with one evidence line. A single BLOCK
blocks the plan. Checks are run in order; a plan that fails an early
check is not carried forward to hide the failure behind later
passes.

1. **Format.** The plan is complete, in the standard shape above,
   dated, with every field present. Missing field → BLOCK.
2. **Asset.** The subject is named with its exchange, the ticker is
   verified against its source, and no namesake ticker on another
   exchange is confused with it. Unverified or namesake subject →
   BLOCK.
3. **Short blocked.** Any short leg in the plan is blocked outright.
   This pack is research-only; a hypothetical plan never includes a
   short position. Short leg present → BLOCK.
4. **Blocked list.** The subject is not on the run's blocked list
   (namesakes, subjects under review, subjects with no usable
   source). On the list → BLOCK.
5. **Size.** The hypothetical size is within the research size cap
   stated in the run contract, and is stated as a hypothetical
   notional, never as money to be committed. Over the cap, or size
   stated as real money → BLOCK.
6. **Position cap.** The single hypothetical position is within its
   cap share of the hypothetical portfolio, stated in the plan.
   Over the cap → BLOCK.
7. **Cash buffer.** The hypothetical cash buffer retained after the
   plan is stated and meets the minimum in the run contract. Buffer
   unstated or below the minimum → BLOCK.
8. **Stop required.** An exit / stop level and the condition that
   triggers review are stated before any entry level is used. No
   stop, or a stop stated after the fact → BLOCK.
9. **Loss per trade.** The maximum hypothetical loss for this plan
   is stated in numbers and within the per-plan limit in the run
   contract. Unstated or over the limit → BLOCK.
10. **Reward:risk minimum.** The plan states its target and its
    stop, shows the reward:risk arithmetic, and the ratio meets the
    minimum the run set in advance and stated in the plan. No
    minimum stated, arithmetic not shown, or ratio below the stated
    minimum → BLOCK.
11. **Daily loss.** The cumulative hypothetical daily loss limit for
    the simulation day is stated, and this plan keeps the day
    within it. Limit unstated, or the plan would breach it → BLOCK.
12. **Trades/day.** The maximum number of hypothetical trades for
    the simulation day is stated, and this plan is within it.
    Over the daily count → BLOCK.
13. **Entry window.** Entry is only inside the stated window. For a
    Nepal subject the window is NEPSE market hours — TO VERIFY:
    the exact NEPSE trading hours for the simulation date have not
    been sourced in this run, so the window must be sourced and
    stated in the plan before this check can pass. Window unstated
    or outside market hours → BLOCK.
14. **Duplicate.** No identical plan has already been reviewed for
    the same subject and date. A duplicate is BLOCK, not a second
    PASS — it is re-reviewed only if a field changed, and then it
    is a new plan with a new fingerprint (see below).
15. **Daily limit.** The daily limit on the number of plans reviewed
    (or on total hypothetical exposure for the day) is stated and
    not exceeded by this plan. Over the daily limit → BLOCK.
16. **PDT-equivalent.** The research analogue of the pattern-day-
    trading limit: a cap on same-day round-trip hypothetical trades
    for one subject, stated in the run contract. TO VERIFY: whether
    any NEPSE or SEBON rule applies to the frequency of same-day
    hypothetical round trips — no such rule is asserted here, and
    the run's own cap governs until one is sourced. Over the run's
    cap → BLOCK.

## Verdicts and fingerprinting

- **PASS:** all 16 checks pass, each with its evidence line. The
  verdict is recorded with a fingerprint: the plan's exact text
  (or its hash) plus the review date. The verdict matches that
  exact plan and that exact date only.
- **BLOCK:** any check blocks, with the blocking check named and
  the evidence line shown. A blocked plan is not published or
  simulated. Fixing it creates a new plan, which is reviewed from
  check 1 with a new fingerprint — a BLOCK is never edited into a
  PASS on the same fingerprint.
- **Fingerprint rule:** any change to the plan — a level, a size, a
  date, a single word in a field — voids the verdict. The changed
  plan is a different plan and is reviewed again in full. A PASS
  is never carried across to a changed plan.

## What a PASS does and does not mean

A PASS means one thing: this hypothetical plan, exactly as written
and dated, passed these 16 checks. It does not mean the plan is
good, the subject is sound, the levels would have held, or anyone
should act on it. It is not a recommendation, not a rating, and
not a prediction. The Reality Checker step below audits the
verdict itself; a PASS with a missing evidence line is sent back,
not published.

## Steps

1. **Research Orchestrator:** writes the run contract — the plan,
   its date, the caps and limits the 16 checks use (size cap,
   position cap, cash-buffer minimum, loss limits, reward:risk
   minimum, daily counts, entry window, PDT-equivalent cap) — and
   confirms the plan is complete (check 1) before review starts.
2. **Risk Stance Analyst:** runs checks 1–16 in order, one evidence
   line each, and records PASS or BLOCK with the fingerprint
   (exact plan + date).
3. **Reality Checker:** audits the verdict — every PASS has an
   evidence line, every BLOCK names its check, the fingerprint
   matches the plan as written, and no value language (cheap,
   buy, sell) appears anywhere. Verdict: Pass / Pass with fixes /
   Send back, line by line.
4. **Done when:** all 16 checks are recorded with evidence lines,
   the verdict and fingerprint are recorded, the Reality Checker
   verdict is Pass, and the plan is labelled with its verdict and
   date wherever it is published or simulated. Anything less is
   labelled In progress — never "reviewed".

## The extended gate (Engine 1.5, 2026-11-07)

Where the run needs per-idea limits, the plan is also run through
the toolkit's `extended_risk_gate()` (`toolkit/position_plan.py`),
which adds three checks to the 16 above — 19 in total:

17. **Max loss per idea.** This plan's max loss must be at most the
    per-idea cap in the run contract. Over the cap → BLOCK.
18. **Sector concentration.** Existing exposure to the plan's sector
    plus this plan's cost, as a share of the hypothetical portfolio,
    must be at most the sector cap in the run contract. Over the
    cap → BLOCK. Context missing (portfolio value, sector exposure)
    → BLOCK, never passed silently.
19. **Exit liquidity.** The plan's shares must be at most the
    maximum participation (default 10%) of typical daily volume,
    reusing the Time Machine's exit-liquidity guard. Over it →
    BLOCK. Volume missing → BLOCK.

The extended gate's verdict is PASS only when all 19 pass; its
`base_gate` field holds the original 16-check result unchanged, so
a 16-check review and a 19-check review of the same plan can be
compared. The plan is recorded in the paper ledger
(`toolkit/paper_ledger.py`) with its verdict and fingerprint —
paper only, no orders. **A PASS is not a recommendation**, under
either gate.

## Attribution
- Checklist adapted from day-trader-skill, trader-risk (MIT
  licence, commit `3d0f4ef`): 16 named checks with PASS/BLOCK
  verdicts and fingerprinting. Adapted to a research-only pack:
  no orders, no broker, no real money, no shorting, no
  recommendation; US day-trading rules replaced by a stated
  research analogue (check 16) and Nepal market hours labelled
  TO VERIFY where unsourced. See
  `docs/SOURCES_MERGE_2026-11-07.md`.
