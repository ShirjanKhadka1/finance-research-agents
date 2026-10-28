# TEMPLATE — International Macro / Markets Research Digest

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
> **Agents that own this discipline:** World Market Researcher
> (regime first, like-for-like, currency and period stated),
> Reality Checker (last pass: number audit, claim audit, logic audit),
> Accuracy Auditor (ledger and freshness audit — see §7).
> A digest that has not passed §7 is a draft, not a digest.
> **The review gate blocks publishing on ANY failed check.**
> There is no "publish anyway with a caveat" path for a failed check:
> fix the item, drop the item, or hold the whole digest.

## How to use this template

1. Copy this file. Fill every bracket. Delete nothing from §7.
2. One digest = one as-of date, one period, one currency basis
   (or the differences stated in the table notes — World Market
   Researcher rule: like-for-like or nothing).
3. Every item follows the item block in §4. An item without a primary
   source + period is not an item; it is a note, and it goes in §6
   (Open questions / TO VERIFY), not in the digest body.
4. **Deduplication rule:** the same event reported by two sources =
   ONE item, BOTH sources cited in that item. Do not run the same
   event twice under two headlines. If two sources disagree on a
   fact, say so inside the single item and mark the disputed fact
   UNKNOWN until a primary source settles it.
5. **Unknown = UNKNOWN, never filled.** No estimate, no interpolation,
   no "probably", no gap filled from a stale series relabelled as
   fresh. A stale input invalidates the item that depends on it
   (Accuracy Auditor freshness rule), even if the item looks good.
6. **No paywalled scraping, no credentials.** Only public sources the
   digest may lawfully use, cited with retrieval date. A paywalled,
   login-locked, or undocumented source is recorded as refused in §6
   and never bypassed. No API key, login, or credential belongs in,
   or is needed by, a digest file.
7. **No fake metrics.** No accuracy rate without n (number of scored
   predictions). Pending predictions never count as wins. Failures
   stay in the record with a reason and an action; they are never
   deleted or edited away.

## 1. Header (fill every field; UNKNOWN where unknown)

| Field | Value |
|---|---|
| Digest date (as-of) | [YYYY-MM-DD — the date the data is as of, not the date of writing, if they differ] |
| Period covered | [YYYY-MM-DD to YYYY-MM-DD] |
| Currency basis | [e.g. USD, or "as stated per item" — never mix currencies silently] |
| Markets in scope | [e.g. TO VERIFY — list benchmarks by name, market, and currency] |
| Primary sources consulted | [list, with retrieval dates] |
| Sources refused | [paywalled / login-locked / undocumented — with reason, or "None"] |
| Status | DRAFT — review gate (§7) NOT YET PASSED |
| Previous digest | [link or "None — no previous digest published"] |

## 2. Regime map (World Market Researcher: regime first)

One short paragraph each, sourced and dated. A market move without
its regime is noise. If a paragraph cannot be sourced, write UNKNOWN
for that paragraph — do not write it from impression.

- **Rates:** [direction, primary source + period, or UNKNOWN]
- **Dollar / major currencies:** [direction, primary source + period, or UNKNOWN]
- **Energy / commodities:** [direction, primary source + period, or UNKNOWN]
- **Risk appetite:** [on / off / mixed, primary source + period, or UNKNOWN]

## 3. Comparison table (same period, same currency basis — or differences stated)

| Market / benchmark | Market + currency | Period | Change | Primary source | Freshness |
|---|---|---|---|---|---|
| [TO VERIFY] | [TO VERIFY] | [TO VERIFY] | [TO VERIFY] | [TO VERIFY] | [FRESH / STALE / UNKNOWN] |

Notes on any like-for-like break (different period, different
currency, different benchmark type): [state them here, or "None"].

## 4. Digest items (deduplicated — one event = one item)

Copy this block per item. Every field is required.

### Item [N]: [one-line headline — the event, not a verdict]

- **Primary source + period:** [source name, publication date, period
  the data covers. If a second source reported the same event, cite
  it here too — deduplication rule, §"How to use", rule 4.]
- **What changed:** [the fact, with its number, its unit, and its
  currency where applicable. Every number carries source + period
  on the same page as the number, or the number is deleted.]
- **What did NOT change:** [the counterweight — what stayed flat,
  what the headline does not imply, what a reader might wrongly
  assume changed. If nothing is known about what did not change,
  write UNKNOWN, not a reassurance.]
- **Downside / falsifier:** [the trigger that would change this
  reading. No falsifier → the item does not ship. A downside that
  is just a haircut on the headline number is not a downside case.]
- **Local test (if any):** [does this theme reach Nepal, through
  which channel — exports, imports, remittances, rates, sentiment —
  and with what lag? Or "No channel evidenced — UNKNOWN". Never
  assert a Nepal effect from a world headline alone.]
- **Freshness:** [FRESH / STALE / UNKNOWN, with last data date and age]
- **Status:** [READY FOR GATE / HELD — reason]

## 5. Risks and what would change the picture

Ranked, each with a trigger that would confirm it:

1. [Risk] — trigger: [TO VERIFY]
2. [Risk] — trigger: [TO VERIFY]

## 6. Open questions / TO VERIFY / refused sources

[List everything that could NOT be verified, every disputed fact,
every refused source, and every item held from §4. A digest that
hides its gaps is worse than a digest that lists them.]

## 7. Review-gate checklist — Reality Checker + Accuracy Auditor (MUST ALL PASS)

Copy the verdict table. **Any FAIL blocks publishing of the whole
digest.** "Pass with fixes" means: apply the fixes line by line,
then re-run this checklist. No vague "looks good".

| # | Check | Pass / Fail | Evidence / line |
|---|---|---|---|
| 1 | Reality Checker — number audit: every number traces to a source + period, or is deleted / labelled UNKNOWN | | |
| 2 | Reality Checker — claim audit: no completion or experience claim beyond what actually exists | | |
| 3 | Reality Checker — every thesis/item has a falsifier and a downside case (not a haircut) | | |
| 4 | Reality Checker — advice audit: no buy / sell / hold recommendation, in any wording; no guaranteed or implied return | | |
| 5 | Reality Checker — tickers carry their exchange; fiscal years labelled as such; currencies and periods stated | | |
| 6 | Accuracy Auditor — freshness: every input carries source + last date + age; no stale input presented as fresh | | |
| 7 | Accuracy Auditor — metrics honesty: any accuracy rate states n (scored predictions); pending never counted as a win; failures logged with reason + action, none deleted | | |
| 8 | Deduplication: same event from two sources appears once, both sources cited; disagreements flagged, disputed facts UNKNOWN | | |
| 9 | No paywalled / login-locked / undocumented source used or bypassed; no credential in or required by this file | | |
| 10 | Unknown = UNKNOWN throughout; no gap filled, estimated, or smoothed over | | |

**Gate verdict:** [PASS — publishable as research only / PASS WITH FIXES
(list them) / FAIL — HELD (list blocking items)] — signed:
[reviewer role + date, or "Not yet reviewed"].

## 8. Worked example — FORMAT ONLY, on verified demo data

This section demonstrates the item block's shape. It is NOT market
news, NOT a real event, and NOT publishable content. Every number
below is marked EXAMPLE next to the number, per the template rule.

### Item EXAMPLE: Demo series movement (format demonstration only)

- **Primary source + period:** Toolkit bundled demo series
  (`investment-analyst-toolkit/toolkit/data.py`, `demo_series()`),
  described in code as "synthetic, labelled DEMO in every use".
  Period: TO VERIFY — the demo series carries no market dates, so
  no period is claimed for it.
- **What changed:** The demo series starts at 100.0 (EXAMPLE) and
  ends at 136.0 (EXAMPLE) across 20 (EXAMPLE) values. That is a
  shape demonstration only; it describes no real market.
- **What did NOT change:** UNKNOWN — a synthetic series has no
  regime, no currency, and no market, so nothing about a real
  market can be claimed as unchanged from it.
- **Downside / falsifier:** Not applicable to demo data — and that
  is the point: a real item without a falsifier does not ship.
- **Local test:** No channel evidenced — UNKNOWN. Demo data cannot
  evidence a Nepal effect.
- **Freshness:** NOT APPLICABLE — synthetic demo data, never fresh
  market data. Never present it as fresh.
- **Status:** FORMAT EXAMPLE ONLY — never publish as a digest item.

> The toolkit's other verified demo figures (demo company revenue
> 1000 (EXAMPLE), gross profit 400 (EXAMPLE), DCF value 1668.03
> (EXAMPLE) — see `investment-analyst-toolkit/examples/demo_company.py`
> and `finance-research-agents/examples/demo-deep-dive.md`) are
> company-format examples, not digest items, and are NOT reused as
> market news here.

## TO VERIFY before any digest could publish

- [ ] A real as-of date, period, and currency basis — none exists in this template.
- [ ] Real primary sources with retrieval dates for every item.
- [ ] A schedule, if one is ever claimed: separate approval + an
  observed run with public output. Until then, no schedule claim.
- [ ] Review-gate §7 fully passed and signed — currently unreviewed.
- [ ] Deduplication actually performed across the real source set
  (cannot be pre-filled; it depends on the day's sources).
- [ ] Any Nepal local-test channel evidenced from a real source,
  or left UNKNOWN.
