# TEMPLATE — Nepal Market (NEPSE) Research Digest

> **STATUS: DESIGN ONLY — NOT A LIVE PUBLICATION, NOT A SCHEDULED RUN.**
>
> This is a template (a shape for a future digest), not a digest, not a
> claim that any digest is published or scheduled. **No agent-digest
> schedule exists live.** The ONLY schedule in the programme is the
> Phase 3 toolkit workflow (`.github/workflows/scheduled-update.yml`
> in `investment-analyst-toolkit`): daily at 01:00 UTC (06:45 NPT),
> writing generated reports to `reports/daily/` — and even that
> schedule is a plan until its first run is observed on GitHub with
> public output in `reports/daily/`. Do not cite this template as
> evidence that a digest runs, ran, or will run on any cadence.
> If a digest schedule is ever added, it needs its own approval and
> its own observed run before anyone may claim it exists.
>
> **Research only, not investment advice.** This digest analyses,
> compares, and explains. It never recommends buying, selling, or
> holding any security, never promises or implies guaranteed returns,
> and never presents an unfinished study as a valuation.
>
> **Agents that own this discipline:** Nepal Market Researcher
> (NEPSE-only labelling, fiscal years, sourced figures, status label),
> Reality Checker (last pass: number audit, claim audit, logic audit),
> Accuracy Auditor (ledger and freshness audit — see §7).
> A digest that has not passed §7 is a draft, not a digest.
> **The review gate blocks publishing on ANY failed check.**
> There is no "publish anyway with a caveat" path for a failed check:
> fix the item, drop the item, or hold the whole digest.

## NEPSE-only labelling (non-negotiable)

- **Exchange always stated: NEPSE, every time, for every ticker.**
  A ticker without its exchange is not publishable in this digest.
- **NEPSE tickers are never confused with other exchanges' same
  letters.** The standing collision is BNT: NEPSE BNT (Bottlers
  Nepal (Terai)) ≠ NYSE BNT (a different company). Confirm the
  ticker is NEPSE before writing it, every time.
- **Fiscal years are Nepalese** (e.g. FY 2081/82) and are never
  silently converted to calendar years.
- **Study status, honestly:** a company study is labelled Inputs
  only / In progress / Completed — and only "Completed" may carry
  a valuation conclusion. This digest carries no valuation
  conclusion for any Inputs-only or In-progress study.

## Data note — CSV only, no live-feed claim

- **NEPSE data in this programme is user-supplied CSV only.**
  No documented free public NEPSE OHLCV API has been verified as of
  28 Oct 2026; the licensed feed is paid and not started (see
  `investment-analyst-toolkit/DATA_SOURCES.md` and
  `ops/ARCHITECTURE.md`). This template therefore claims NO live
  feed, NO streaming prices, and NO real-time NEPSE data.
- Every NEPSE figure in a filled digest must name its CSV (file +
  retrieval/provision date + period covered) or its primary document
  (annual report / filing, with period + page/section). A figure
  without that provenance is deleted or labelled UNKNOWN.
- **No scraped data presented as official. No invented prices,
  volumes, or ratios.** A paywalled, login-locked, or undocumented
  source is recorded as refused in §6 and never bypassed.
- **No credentials.** No API key, login, or credential belongs in,
  or is needed by, a digest file. This digest does not use, link
  to, or publish from any Nepse Decode GitHub repo (out of scope
  for this pack by the pack author's rule).

## How to use this template

1. Copy this file. Fill every bracket. Delete nothing from §7.
2. One digest = one as-of date, one period, NEPSE only.
3. Every item follows the item block in §4. An item without a primary
   source + period is not an item; it goes in §6 (Open questions /
   TO VERIFY), not in the digest body.
4. **Deduplication rule:** the same event reported by two sources =
   ONE item, BOTH sources cited in that item. Do not run the same
   event twice under two headlines. If two sources disagree on a
   fact, say so inside the single item and mark the disputed fact
   UNKNOWN until a primary source settles it.
5. **Unknown = UNKNOWN, never filled.** No estimate, no interpolation,
   no gap filled from a stale CSV relabelled as fresh. A stale input
   invalidates the item that depends on it, even if the item looks
   good.
6. **No fake metrics.** No accuracy rate without n (number of scored
   predictions). Pending predictions never count as wins. Failures
   stay in the record with a reason and an action.

## 1. Header (fill every field; UNKNOWN where unknown)

| Field | Value |
|---|---|
| Digest date (as-of) | [YYYY-MM-DD — the date the data is as of, not the date of writing, if they differ] |
| Period covered | [YYYY-MM-DD to YYYY-MM-DD, plus Nepalese fiscal year where applicable, e.g. FY 2081/82] |
| Exchange | NEPSE (Nepal Stock Exchange) — every ticker in this digest is NEPSE |
| CSV / primary documents used | [file + provision/retrieval date + period covered, per dataset, or "None yet — TO VERIFY"] |
| Sources refused | [paywalled / login-locked / undocumented — with reason, or "None"] |
| Status | DRAFT — review gate (§7) NOT YET PASSED |
| Previous digest | [link or "None — no previous digest published"] |

## 2. Market snapshot (NEPSE only — no live-feed claim)

One short paragraph each, sourced and dated, or UNKNOWN. Nothing
here is a live price: every figure names its CSV or document.

- **Breadth / turnover (CSV or document only):** [figure + source +
  period, or UNKNOWN]
- **Sector read (CSV or document only):** [figure + source + period,
  or UNKNOWN]
- **What is NOT covered:** [sectors, symbols, or periods absent from
  the CSV/documents used — stated, not hidden]

## 3. Company / sector table (NEPSE tickers only)

| Company | Ticker (exchange) | Period / FY | Figure | Primary source (CSV or document + page/section) | Freshness |
|---|---|---|---|---|---|
| [TO VERIFY] | [TO VERIFY, NEPSE] | [TO VERIFY] | [TO VERIFY] | [TO VERIFY] | [FRESH / STALE / UNKNOWN] |

Study status per company (Inputs only / In progress / Completed):
[TO VERIFY — only "Completed" may carry a valuation conclusion, and
this digest carries none for Inputs-only or In-progress studies.]

## 4. Digest items (deduplicated — one event = one item)

Copy this block per item. Every field is required.

### Item [N]: [one-line headline — the event, not a verdict]

- **Primary source + period:** [CSV file + period, or annual report /
  filing + period + page/section. If a second source reported the
  same event, cite it here too — deduplication rule, §"How to use",
  rule 4.]
- **Ticker + exchange:** [e.g. XXXX, NEPSE — exchange stated every time]
- **What changed:** [the fact, with its number, its unit, and its
  currency (NPR where applicable). Every number carries source +
  period on the same page as the number, or the number is deleted.]
- **What did NOT change:** [the counterweight — what stayed flat,
  what the headline does not imply. If nothing is known, write
  UNKNOWN, not a reassurance.]
- **Downside / falsifier:** [the trigger that would change this
  reading. No falsifier → the item does not ship. A downside that
  is just a haircut on the headline number is not a downside case.]
- **Nepal-specific checks (where applicable):** [dividend history
  including nil years; bonus vs cash split; shareholding
  concentration; disclosed tax dispute vs equity — or "Not
  applicable / UNKNOWN" with the reason.]
- **Freshness:** [FRESH / STALE / UNKNOWN, with last data date and age]
- **Status:** [READY FOR GATE / HELD — reason]

## 5. Risks and what would change the picture

Ranked, each with a trigger that would confirm it:

1. [Risk] — trigger: [TO VERIFY]
2. [Risk] — trigger: [TO VERIFY]

## 6. Open questions / TO VERIFY / refused sources

[List everything that could NOT be verified, every disputed fact,
every refused source, every CSV gap, and every item held from §4.
A digest that hides its gaps is worse than a digest that lists them.
Include here, explicitly: any NEPSE figure whose CSV or document
provenance is missing.]

## 7. Review-gate checklist — Reality Checker + Accuracy Auditor (MUST ALL PASS)

Copy the verdict table. **Any FAIL blocks publishing of the whole
digest.** "Pass with fixes" means: apply the fixes line by line,
then re-run this checklist. No vague "looks good".

| # | Check | Pass / Fail | Evidence / line |
|---|---|---|---|
| 1 | Reality Checker — number audit: every number traces to a source + period (CSV or document + page/section), or is deleted / labelled UNKNOWN | | |
| 2 | Reality Checker — claim audit: no completion or experience claim beyond what actually exists; study statuses honest (Inputs only / In progress / Completed) | | |
| 3 | Reality Checker — every thesis/item has a falsifier and a downside case (not a haircut) | | |
| 4 | Reality Checker — advice audit: no buy / sell / hold recommendation, in any wording; no guaranteed or implied return | | |
| 5 | Reality Checker — NEPSE labelling: every ticker carries "NEPSE"; no cross-exchange ticker confusion (BNT check done); fiscal years Nepalese, never silently converted | | |
| 6 | Accuracy Auditor — freshness: every input carries source + last date + age; no stale CSV presented as fresh; no live-feed claim | | |
| 7 | Accuracy Auditor — metrics honesty: any accuracy rate states n (scored predictions); pending never counted as a win; failures logged with reason + action, none deleted | | |
| 8 | Deduplication: same event from two sources appears once, both sources cited; disagreements flagged, disputed facts UNKNOWN | | |
| 9 | No paywalled / login-locked / undocumented source used or bypassed; no credential in or required by this file; no Nepse Decode repo used, linked, or published from | | |
| 10 | Unknown = UNKNOWN throughout; no gap filled, estimated, or smoothed over; no scraped data presented as official | | |

**Gate verdict:** [PASS — publishable as research only / PASS WITH FIXES
(list them) / FAIL — HELD (list blocking items)] — signed:
[reviewer role + date, or "Not yet reviewed"].

## 8. Worked example — FORMAT ONLY, on verified synthetic demo data

This section demonstrates the item block's shape. It is NOT NEPSE
market news, NOT a real company, and NOT publishable content. Every
number below is marked EXAMPLE next to the number, per the template
rule. The symbol DEMO is a synthetic placeholder, not a NEPSE ticker.

### Item EXAMPLE: Scanner demo series movement (format demonstration only)

- **Primary source + period:** Scanner synthetic demo file
  (`nepali-capital-market-research/scanner/examples/demo_prices.csv`),
  symbol DEMO, sector Hydro Power (EXAMPLE sector label from the
  demo file). Period: TO VERIFY as a market period — the demo file
  is synthetic, so no real market period is claimed for it.
- **Ticker + exchange:** DEMO, SYNTHETIC DEMO ONLY — not NEPSE, not
  any real exchange. Never copy this symbol into a real digest item.
- **What changed:** In the demo file, the DEMO close falls from
  200.00 (EXAMPLE) on the file's first row to 170.00 (EXAMPLE) on
  its later flat rows, with volume at 13000 (EXAMPLE) on one such
  later row (volume starts at 10000 (EXAMPLE) on the first row).
  That is a shape
  demonstration only; it describes no real NEPSE company.
- **What did NOT change:** UNKNOWN — a synthetic series has no real
  market context, so nothing about a real NEPSE company can be
  claimed as unchanged from it.
- **Downside / falsifier:** Not applicable to demo data — and that
  is the point: a real item without a falsifier does not ship.
- **Nepal-specific checks:** Not applicable — DEMO is synthetic, so
  dividend history, bonus/cash split, shareholding, and tax-dispute
  checks are all UNKNOWN, not assumed.
- **Freshness:** NOT APPLICABLE — synthetic demo data, never fresh
  market data. Never present it as fresh, and never present a
  user-supplied CSV as a live feed.
- **Status:** FORMAT EXAMPLE ONLY — never publish as a digest item.

## TO VERIFY before any digest could publish

- [ ] A real as-of date, period, and Nepalese fiscal year — none exists in this template.
- [ ] Real user-supplied NEPSE CSV(s) with file + provision date + period, or real primary documents with page/section — none is claimed here.
- [ ] Every ticker confirmed as NEPSE (BNT collision check done per ticker).
- [ ] A schedule, if one is ever claimed: separate approval + an
  observed run with public output. Until then, no schedule claim.
- [ ] Review-gate §7 fully passed and signed — currently unreviewed.
- [ ] Deduplication actually performed across the real source set
  (cannot be pre-filled; it depends on the day's sources).
- [ ] Any Nepal-specific check (dividends, bonus/cash, concentration,
  tax dispute) evidenced from a real source, or left UNKNOWN.
