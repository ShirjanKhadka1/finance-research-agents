# Runbook: Data first

**Team, in order:** Data Scout → Statement Reconciler → Financial
Analyst → Reality Checker

**Purpose:** no analysis starts on unvalidated, untied data. The scout
proves where the data came from and whether it may be used; the
reconciler proves whether the statements add up; only then does the
analyst interpret anything.

## Step 1 — Data Scout
- State each dataset needed: fields, period, granularity, exchange
  (NEPSE tickers always labelled NEPSE).
- Find a free, public, documented source for each dataset, or prove
  none exists. Record licence/terms, retrieval date, period covered,
  and a freshness verdict (fresh / stale / unknown) in a DATA_SOURCES
  entry per dataset.
- Validate schema on arrival (dates strictly increasing, closes
  positive, no missing required fields). Refuse a failing dataset as
  a whole, or drop the failing symbol with its reason logged.
- A paywalled, login-locked, or undocumented source is refused for
  the free path and recorded as refused — never bypassed. A 403 or
  429 is a recorded failure, not an invitation to retry harder.
- Output: DATA_SOURCES table, validation note per dataset, rejection
  list. If no legitimate free source exists for a needed dataset,
  say so plainly and stop — do not fill the gap with an invented,
  locked, or stale series relabelled as fresh.

## Step 2 — Statement Reconciler
- Normalise units, currency, fiscal year, and consolidation basis
  first; fix data errors and re-run, recording every fix.
- Tie out: balance sheet (assets = liabilities + equity), cash flow
  (operating + investing + financing = change in cash; closing cash
  ties to the balance sheet), equity (opening + profit + other
  comprehensive income − dividends + other movements = closing),
  segments and share counts, and prior-period comparatives
  (restatements quantified, both versions shown).
- Every check is listed as pass, fail, or NOT RUN with the reason —
  never silently skipped.
- Output: tie-out table and verdict — TIED / TIED WITH EXPLAINED
  DIFFERENCES / NOT TIED — plus a handoff note naming which lines
  are safe, which are flagged, and which are excluded. If a check
  fails materially, analysis on the affected lines stops until the
  difference is explained or the lines are excluded with the reason
  stated.

## Step 3 — Financial Analyst
- Ratios, DuPont, trends, cash vs profit, drivers — using only the
  lines the reconciler marked safe or flagged (flagged lines carried
  with their flag, excluded lines not used).
- Output: ratios, drivers, and cash-vs-profit read, every number
  sourced with source + period or labelled UNKNOWN.

## Step 4 — Reality Checker
- Number audit, claim audit, logic audit.
- Output: fixes list, line by line. Apply the fixes. Re-run this step
  if a fix changed a number.

## Done when
Every dataset has a DATA_SOURCES entry, the tie-out verdict is TIED
or TIED WITH EXPLAINED DIFFERENCES, every number is sourced or
labelled UNKNOWN, and the Reality Checker verdict is Pass. Anything
less is labelled In progress.

**Research only, not investment advice.** This runbook analyses and
explains. It never recommends buying or selling a security, never
presents an unfinished study as a valuation, and never invents a
number.
