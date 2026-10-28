# Runbook: Macro to company

**Team, in order:** World Market Researcher → Nepal Market Researcher
(for NEPSE names) → Investment Researcher → Statement Reconciler →
Financial Analyst → Valuation Analyst → Reality Checker

**Purpose:** a full top-down study — place a company in world context,
then in its home market, then in its own thesis, statements, and
valuation, with every step checked before anything is shared.

## Step 1 — World Market Researcher
- Global markets, regimes, and cross-border themes relevant to the
  subject, with a local test: what does the world picture actually
  imply for this market and company, and what does it not imply?
- Output: global context + local test, every number sourced with
  source + period or labelled UNKNOWN.

## Step 2 — Nepal Market Researcher (for NEPSE names)
- Sourced Nepal market research for the subject. Exchange always
  stated; NEPSE tickers always labelled NEPSE and never confused
  with same-letter tickers on other exchanges.
- Output: Nepal market context for the company study.

## Step 3 — Investment Researcher
- Thesis in one paragraph, business, industry.
- Output: initiation template, sections 1–3 filled, rest empty.

## Step 4 — Statement Reconciler
- Tie out the statements before any analysis trusts them: balance
  sheet, cash flow, equity, segments, comparatives. Verdict: TIED /
  TIED WITH EXPLAINED DIFFERENCES / NOT TIED, with safe, flagged,
  and excluded lines listed.
- If the verdict is NOT TIED on a material section, stop and resolve
  it before Step 5 — analysis on the affected lines does not proceed.

## Step 5 — Financial Analyst
- Ratios, DuPont, trends, cash vs profit, drivers, using only safe
  or flagged lines from Step 4.
- Output: initiation template, section 4 filled.

## Step 6 — Valuation Analyst (only if inputs allow)
- Method fit first. If no method fits, write that and stop — do not
  force a DCF.
- Inputs, build, implied test, peer check, downside, one-sentence test.
- Output: initiation template, section 5 filled, or "Valuation not
  built, because…".
- **Accuracy Auditor ledger rule on forecasts:** any forecast in
  this chain is logged before its outcome is known, with its horizon
  and a named naive baseline, so it can be settled later and its
  failures retained — a forecast that is never scored is not a track
  record. Apply the Accuracy Auditor's prediction-ledger discipline
  (see `runbooks/prediction-accuracy-loop.md`) to every forecast
  this runbook produces; a forecast with no ledger entry, horizon,
  and baseline is not shared.

## Step 7 — Reality Checker
- Number audit, claim audit, logic audit.
- Output: fixes list, line by line. Apply the fixes. Re-run this step
  if a fix changed a number.

## Done when
Thesis + financials + risks with triggers + downside + falsifier +
open questions are all present, every number is sourced or labelled
UNKNOWN, every forecast in the chain has a ledger entry with horizon
and baseline, and the Reality Checker verdict is Pass. Anything less
is labelled In progress.

**Research only, not investment advice.** This runbook analyses and
explains. It never recommends buying or selling a security, never
presents an unfinished study as a valuation, and never invents a
number.
