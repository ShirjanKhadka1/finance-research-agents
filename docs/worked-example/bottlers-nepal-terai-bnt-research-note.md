# Worked example: Bottlers Nepal (Terai) — NEPSE: BNT

> **Research only, not investment advice. Never a buy / sell / hold
> recommendation, never a target price, never a position size.**
> This note proves the pack in use: it was built by applying the
> agents and the `structured-debate` runbook to one real, sourced
> subject. It is **not a valuation** — no DCF value and no valuation
> conclusion are built here — and it is not a live price source.

## 0. Run contract (Research Orchestrator)

| Contract field | Value |
|---|---|
| Subject | Bottlers Nepal (Terai) — **NEPSE: BNT** (NEPSE BNT ≠ NYSE BNT, a different company; exchange stated every time) |
| Runbook | `runbooks/structured-debate.md`: Orchestrator → Ledger Controller → parallel analysts → Debate Analyst → Risk Stance Analyst → Reality Checker → Accuracy Auditor (for any forecast touched) |
| As-of / freeze date | **2026-10-16** — the date of the frozen input ledger below. Prices and quotes in this note are October 2026 session prints, **not** current prices. The current BNT price is **UNKNOWN** in this example. |
| Currency / calendar | NPR; Nepalese fiscal years (FY 2081/82), never silently converted to calendar years |
| Team that reported | Ledger Controller, Investment Researcher, Financial Analyst, Forensic Analyst, Nepal Market Researcher, Valuation Analyst (sanity checks only), Debate Analyst, Risk Stance Analyst, Reality Checker, Accuracy Auditor. Data Scout's source record is §1; News & Sentiment Analyst did **not** report (no dated news/sentiment count was sourced for this run) — the debate therefore makes no claim about news or sentiment, and that gap is carried as a limit, not filled. |

## 1. Frozen input ledger (Ledger Controller) — verdict: Complete with stated gaps

Sources, exactly as frozen. No mid-run source swap; a new source
version would start a new ledger entry, never a quiet edit.

| # | Input | Source + period | Control total / count |
|---|---|---|---|
| 1 | BNT audited financials | BNT 39th annual report, FY 2081/82, year ended 16 July 2025, as consolidated in the sprint verified-inputs ledger prepared 2026-10-16 | 13 audited line items frozen below (§2); every recomputation in §3 ties to them |
| 2 | BNT unaudited quarterlies, FY 2082/83 | Unaudited quarterly results, Q1–Q4 FY 2082/83, via the same 2026-10-16 ledger | 4 quarters; used **only** as normalisation evidence, never as the anchor — the audited FY 2081/82 year stays the anchor |
| 3 | Peer session closes | NEPSE session prints, 13–15 Oct 2026, via the same ledger | 6 peers listed in §5; BNL stale since 9 Oct 2026 and UNL thin — both flagged, not smoothed over |
| 4 | WACC / multiple anchors | Damodaran Jan 2026 (US Beverage (Soft); country-premium page); PDMO FY 2081/82 auction series (22 auctions); World Bank Nepal Development Update, Oct 2026 | Anchors quoted in §5 with their own caveats; EM beta vintage **unverified** — stated, not hidden |
| 5 | Nepal trading frictions | User-supplied Nepal market frictions set, 2026-10-28 (broker slabs, SEBON, DP, CGT, circuit, settlement) | Schedule reproduced in §6; any rate not in that set is UNKNOWN |

**Cut-off check.** FY 2081/82 audited figures stay in FY 2081/82;
FY 2082/83 unaudited quarterlies stay in FY 2082/83 and are never
averaged into the audited year. The Rs 32,042,935 current lease
liability (ledger: Rs 32.0M) sits inside working capital (ledger
note); it is not double-counted.

> Provenance (Round 3, R7, 29 Oct 2026): every FY 2081/82 figure in
> §2 matches the programme's single source,
> `nepal-market-research/data/bnt-verified-figures.md`, exactly
> (cross-checked figure by figure; no numeric mismatch found).
> Page reference for every figure: TO VERIFY — no copy of the 39th
> annual report PDF is on file; see that file's verification status.

**Restatement log.** Two retired figures from the sprint ledger are
**not** used here: stake "~92%" (superseded by 90.78%) and the Day 6
P/E close 11,751 (superseded by the 11,888 Oct 12 close). No other
restatement is on file for this run.

**Stated gaps (the run proceeds with these limits, it does not hide
them).** (a) The ~Rs 81M bridge gap (§3) is unresolved. (b) What
happened to the Rs 763M prior-period tax provision is UNKNOWN until
the 40th annual report lands (not published as of 2026-10-16).
(c) No dated news/sentiment count was sourced. (d) BNT's own beta is
not regressed — thin trading forbids it (see §5).

## 2. The frozen audited year (Financial Analyst + Statement Reconciler)

BNT, FY 2081/82 audited (39th annual report), NPR. Prior-year
comparatives in brackets.

| Item | FY 2081/82 | Prior year |
|---|---|---|
| Revenue from Operations | 7,527,297,984 | 8,771,297,424 |
| Profit from Operations (EBIT face label) | 407,359,078 | 721,109,708 |
| D&A (646,041,660 + 4,829,940) | 650,871,600 | — (not frozen for this run) |
| Profit before tax | 218,422,271 | — |
| Current tax 53,371,085; deferred tax 15,934,615 | 69,305,700 combined | — |
| Prior-period tax adjustment | 763,054,705 | — |
| Net profit / (loss) | −613,938,134 | +339,681,626 |
| EPS | −507 | +281 |
| Operating cash flow (OCF) | 1,497,212,819 | 1,108,364,321 |
| Capex (PPE acquisition) | 197,522,182 | — |
| Working capital ex-cash/ex-borrowings | 1,478,090,828 | 1,937,911,582 |
| Borrowings — all current, nil non-current | 2,344,466,783 | — |
| Cash | 36,531,377 | — |

Tie-out notes (Statement Reconciler): the working-capital release
reconciles exactly, 1,937,911,582 − 1,478,090,828 = 459,820,754.
Borrowings minus cash = 2,307,935,406 net debt on the frozen
balance sheet. No balance-sheet tie-out beyond these frozen lines
was attempted — full-statement tie-out tables are UNKNOWN in this
example, and no analyst below claims otherwise.

## 3. What the numbers say (Financial Analyst, recomputed — not copied)

Every percentage below is recomputed from §2 and shows its
arithmetic, so a reader can rebuild it without trusting this note.

- **Revenue fell 14.2%**: (7,527,297,984 − 8,771,297,424) /
  8,771,297,424 = −14.18%.
- **EBIT fell 43.5%**: (407,359,078 − 721,109,708) / 721,109,708
  = −43.51%. EBIT margin compressed from 8.22% to **5.41%**
  (407,359,078 / 7,527,297,984).
- **EBITDA (EBIT + D&A)** = 407,359,078 + 650,871,600 =
  1,058,230,678; EBITDA margin **14.06%** (≈14.1% in the ledger).
- **Cash did not follow profit down.** OCF of 1,497,212,819 is a
  3-year high (prior year 1,108,364,321) while net profit is
  negative — the forensic question of §4, not a contradiction to
  be smoothed over.
- **OCF − capex** = 1,497,212,819 − 197,522,182 = **1,299,690,637**
  (≈Rs 1,299.7M). The EBIT-based bridge in the sprint build is
  ≈Rs 1,218.7M, leaving an **~Rs 81M gap** (cash taxes / interest
  classification) that this run does **not** resolve. It is carried
  as an open question and as a limit on the veto (§8), not
  explained away.
- **Headline add-back (arithmetic, not a judgement)**:
  −613,938,134 + 763,054,705 = **+149,116,571**. Reported profit
  understates the repeatable business by exactly this arithmetic
  *if* the prior-period tax item is genuinely one-off — which is
  the Bear's challenge in §7, not an assumption this note grants.

## 4. Forensic pass (Forensic Analyst) — flags are questions, not accusations

1. **The Rs 763M prior-period tax adjustment is the whole net-loss
   story.** At 763,054,705 it is larger than the year's EBIT
   (407,359,078) and larger than the reported loss it creates.
   Per the agent's rule, a material item bigger than normal profit
   leads — it is not a footnote. Its fate (settled, provided,
   reversed) is UNKNOWN until the 40th annual report.
2. **Cash vs profit divergence.** OCF at a 3-year high against a
   net loss is explained in part by the working-capital release
   (Rs 459,820,754) and by D&A (Rs 650,871,600) — but the ~Rs 81M
   bridge gap means the reconciliation is incomplete. Verdict:
   **Watch**, not "explained".
3. **Funding shape.** All borrowings (Rs 2,344,466,783) are current
   with nil non-current, against cash of Rs 36,531,377. That is a
   refinancing/rollover question for the next filing, not a
   solvency verdict — solvency on fuller balance-sheet data is
   UNKNOWN in this example.
4. **Tax-rate note (immaterial, logged anyway).** NOPAT at the 25%
   statutory rate is Rs 305.52M vs Rs 307.96M at the 24.4%
   effective rate — a Rs 2.44M difference. Logged, not argued over.

## 5. Market context (Nepal Market Researcher + Valuation Analyst, sanity checks only)

**Thin trading is a finding, not background.** The 11,888 close
used for market-value weights was set by **2 trades / 50 shares**.
The 120-day average fallback is 11,696.53 vs 11,758.02 across
sources (they disagree slightly — both stated). Peer closes for
13–15 Oct 2026 carry the same warning: BNL stale since 9 Oct 2026
(4+ sessions untraded), UNL thin at 5 trades, BNT itself thin at
2 trades / 20 shares on the peer-table session. Any argument that
treats a single thin close as "the market's verdict" fails this
note's own standard.

**Market-value weights (frozen, recomputed).** Equity at the 11,888
close × 1,210,000 shares = Rs 14,384,480,000 (≈Rs 14,384.48M);
debt Rs 2,344.47M; weights **86/14**, as frozen. Enterprise value
on those legs: 14,384.48 + 2,344.47 − 36.53 cash = **≈Rs 16,692M**.

**Multiples — sanity checks only, no valuation conclusion.**
EV/Sales = 16,692 / 7,527.3 ≈ **2.2x**; EV/EBITDA = 16,692 /
1,058.23 ≈ **15.8x** — both on depressed LTM earnings (revenue
−14.2%, EBIT −43.5%). Per the Valuation Analyst's rule, multiples
belong on **normalised**, not depressed, earnings, so these LTM
multiples are reported as a warning against using them, not as a
value. Damodaran US Beverage (Soft), Jan 2026: EV/Sales 4.16x,
P/S 3.57x — a US cross-check, not a Nepal price. EM/global
EV/EBITDA was **unverified** on the web in the sprint and stays
UNKNOWN here.

**WACC anchors (quoted, not built into a value).** Rf ~5.0%
(PDMO FY 2081/82, 22 auctions; 8–11yr long end 5.00–5.49%, last
three long prints 5.00%; sensitivity band 5.00–5.49%). Beta: EM
beverage-soft unlevered **0.50** anchor, vintage unverified; US
0.56 unlevered cross-check (Jan 2026, 27 firms). **Do not regress
BNT's own beta (thin trades).** ERP/CRP: Damodaran Jan 2026
(CRP 4.66%, total ERP 8.89%; July 2026 refresh: mature ERP
4.23→4.20%). Tax 25%. Terminal-growth anchors (World Bank Nepal
Development Update, Oct 2026: FY26 real GDP 3.9%, inflation 3.1%
→ implied nominal GDP ~7.1%): base g ~7%, top ~8%, 9% prove-it
ceiling. No DCF is computed from these anchors in this example.

**Normalisation evidence (unaudited — labelled every time).**
BNT unaudited FY 2082/83 quarterlies: Q1 273.85M → Q2 135.49M →
Q3 277.05M → Q4 **659.28M**. LTM EPS = 659.28M / 1,210,000 = 545
(544.86 unrounded); at the 11,900 close, LTM P/E ≈ 21.83x (ledger
figure on rounded EPS). This is evidence the FY 2081/82
depression may be over — it is **not** audited confirmation, and
the audited FY 2081/82 year remains the anchor.

**Thesis in one paragraph (Investment Researcher).** BNT's
FY 2081/82 audited year looks like a depressed, tax-distorted year
for a bottler whose cash generation stayed strong: revenue and
EBIT fell sharply, yet OCF hit a 3-year high on a working-capital
release, and unaudited FY 2082/83 quarterlies point to recovery —
but every price leg behind that story is thin, all debt is
current, the tax provision's fate is unknown, and an ~Rs 81M
reconciliation gap is still open. The research question is
therefore whether the recovery is audited and fundable, not
whether one thin close looks cheap.

## 6. Nepal frictions the downside must carry (Risk Stance Analyst input)

User-supplied Nepal market frictions set, 2026-10-28. Any
downside that ignores these is incomplete.

| Friction | Frozen schedule |
|---|---|
| Broker commission | 0.36 / 0.33 / 0.31 / 0.27 / 0.24% by slab, minimum Rs 10 |
| SEBON fee | 0.015% |
| DP charge | Rs 25 per scrip |
| Capital gains tax | 5% if held ≤365 days; 3.75% if held >365 days |
| Circuit limit | ±15% |
| Settlement | T+2 (broker 58 offers T+1) |

## 7. Structured debate (Debate Analyst) — every argument answered or marked

### Bull case (best case, with numbers)

- **B1 — The loss is tax arithmetic, not operating collapse.**
  +149,116,571 headline add-back (§3); OCF at a 3-year high
  (1,497,212,819) and OCF − capex ≈ Rs 1,299.7M show a business
  generating cash while reporting a loss.
- **B2 — The depression is already lifting on unaudited evidence.**
  FY 2082/83 quarterlies rise to Q4 659.28M; LTM EPS 545 and
  LTM P/E ≈21.83x at 11,900 describe a recovering, not a
  collapsing, earnings base — labelled unaudited throughout.
- **B3 — The LTM multiples flatter the bear case.**
  EV/EBITDA 15.8x and EV/Sales 2.2x sit on depressed earnings;
  on normalised earnings the same enterprise value implies
  lower multiples — so LTM multiples must not be read as
  "expensive" without normalisation.

### Bear case (worst case, with numbers)

- **R1 — The top line and operating profit actually fell.**
  Revenue −14.2%, EBIT −43.5%, EBIT margin 8.22% → 5.41%.
  A recovery story must explain a demand/cost reversal, and
  unaudited quarterlies are not that explanation yet.
- **R2 — The price legs are too thin to trust.**
  The 11,888 close rests on 2 trades / 50 shares; peer closes
  are stale (BNL since 9 Oct) or thin (UNL 5 trades). Market
  weights, EV, and multiples built on those closes inherit
  that fragility — including the Bull's own P/E leg.
- **R3 — Funding and the open items are unresolved.**
  All Rs 2,344,466,783 of borrowings is current against
  Rs 36,531,377 cash; the ~Rs 81M bridge gap is unexplained;
  the Rs 763M provision's fate is UNKNOWN. Any one of these
  could reframe the year when the 40th annual report lands.

### Debate — each side answers the other's strongest point

- **Bull answers R2 (Bear's strongest):** conceded in part.
  Thin closes are real, which is why this note reports the
  120-day average fallback (11,696.53 / 11,758.02, sources
  disagreeing) alongside the close, and why no conclusion in
  this note depends on a single close. **Partial answer:**
  fragility is disclosed and bounded, but not cured — the
  close remains thin, and that limit travels with the veto.
- **Bear answers B1 (Bull's strongest):** the add-back is
  arithmetic, not proof. +149,116,571 follows *if* the
  763,054,705 item is one-off; until the 40th annual report
  shows its fate, the Bull cannot claim the repeatable base
  is proven — only that the arithmetic points that way.
  **Answer stands:** B1 survives as arithmetic, not as proof.
- **Bull answers R3:** the WC release (Rs 459,820,754) and
  OCF − capex (≈Rs 1,299.7M) show near-term cash cover in
  the frozen year, but the Bull concedes the rollover
  question itself is unanswered until the next filing.
- **Bear answers B2/B3:** unaudited quarterlies cannot carry
  a normalised-earnings claim, and normalised multiples
  cannot be computed until normalised earnings are audited
  — so B3 is a warning against LTM multiples, not a value.
  **Answer stands:** B2/B3 survive only in their labelled,
  limited form.

**Unanswered debate arguments: none.** Every argument above
was answered by the other side or explicitly conceded in part.
What remains is not unanswered argument but **open questions**
(§9) — facts awaiting a filing, not points awaiting a reply.
That distinction is what lets the veto be "Publish with
limits" rather than "Hold" under the runbook's gate rule.

**The losing side's best argument survives.** The Bear's R2
(thin price legs) is the strongest single argument in the
debate: it qualifies every market-based number in this note,
and it is retained here and in the veto limits rather than
argued away.

## 8. Risk scenarios (Risk Stance Analyst) — each with an observable trigger

Scenarios are analysis, not advice. None sizes a position.

| Stance | Break path | Trigger (observable) | What it does NOT prove |
|---|---|---|---|
| **Risky** (optimistic assumptions wrong) | The unaudited recovery reverses: FY 2082/83 audited revenue/EBIT land near the depressed FY 2081/82 base, while all-current borrowings must be rolled in the same window; thin closes gap toward the ±15% circuit band on low volume, so friction costs (§6) dominate any exit. | The 40th annual report filing, or a quarterly filing, printing audited revenue/EBIT at or below the FY 2081/82 base. | It does not prove the business is unviable — only that the recovery thesis fails on audited numbers. |
| **Safe** (even cautious assumptions break) | Even granting the cash story, the price legs stay thin: closes continue to print on a handful of trades, BNL-style staleness spreads, and the ~Rs 81M gap is never reconciled — so no market-based multiple in this note can be tightened, whatever the audited outcome. | Two consecutive NEPSE sessions in which BNT prints on ≤5 trades, or the 40th annual report leaves the bridge gap unreconciled. | It does not prove the price is wrong — only that it is unmeasurable from these legs. |
| **Neutral** (middle path, own failure modes) | Audited recovery confirms direction but not magnitude: earnings normalise part-way, the 763M provision resolves favourably but slowly, and multiples on normalised earnings land between the depressed-LTM 15.8x and the US 4.16x EV/Sales cross-check — leaving the "cheap vs fairly valued" question still open. | The 40th annual report resolving the provision with a stated figure, plus one audited quarter at a normalised margin. | It does not prove a value — this example builds no DCF and no valuation conclusion. |

## 9. Risk Veto verdict (Debate Analyst + Reality Checker)

### ✅ PUBLISH WITH LIMITS

**Why not full Publish:** the ~Rs 81M bridge gap is unresolved,
the Rs 763M provision's fate is UNKNOWN, every price leg is thin,
and the recovery leg is unaudited. A full Publish would overstate
what the frozen inputs prove.

**Why not Hold:** no claim in this note fails its source; every
debate argument was answered or conceded in part (§7); every risk
scenario carries an observable trigger (§8); and every limit is
stated on the same page as the claim it limits. The runbook's
Hold triggers (failed claim, triggerless scenario, unanswered
argument) are all absent.

**Stated limits that travel with publication:**
1. As-of 2026-10-16 only — current price UNKNOWN; do not reuse
   October 2026 closes as current.
2. Audited FY 2081/82 is the anchor; FY 2082/83 quarterlies are
   unaudited normalisation evidence only.
3. Market weights, EV (≈Rs 16,692M), and multiples inherit thin
   closes (11,888 on 2 trades / 50 shares).
4. No DCF, no target, no valuation conclusion — the multiples
   here are sanity warnings, not a value.
5. No news/sentiment claim is made (no dated count sourced).
6. Full-statement tie-out beyond §2, BNT's own beta, audited
   FY 2082/83 results, and the 40th annual report outcome are
   all UNKNOWN.

**Falsifier (what would change this note).** Any one of: the
40th annual report restating FY 2081/82 audited figures; the
763M provision resolving adversely; audited FY 2082/83 earnings
landing at or below the FY 2081/82 base; or a filing showing
borrowings no longer rolling. On any of these, this note is
superseded, not defended.

## 10. Accuracy audit (Accuracy Auditor)

This debate touched **no forecast with a logged outcome**, so
there is nothing to score: **n = 0 scored predictions, 0 pending
counted as wins.** No accuracy figure is claimed. The WACC
anchors, terminal-growth anchors, and US multiples in §5 are
quoted inputs with their own caveats, not predictions, and are
not entered in any prediction ledger. If a future run forecasts
from this note, that forecast must be logged **before** its
outcome, with horizon stated, or the Accuracy Auditor blocks
publication.

## 11. Open questions (carried, not hidden)

1. What happened to the Rs 763M prior-period tax provision?
   (Awaiting the 40th annual report.)
2. What explains the ~Rs 81M OCF-minus-capex vs EBIT-bridge gap?
   (Cash taxes / interest classification — unresolved.)
3. What is BNT's normalised, audited earnings base for any
   future multiples work? (Awaiting audited FY 2082/83.)
4. Do borrowings roll, and on what terms? (Awaiting next filing.)
5. What does a dated news/sentiment count show? (Not sourced
   for this run.)
6. Current BNT price, current peer closes, and any post-October
   2026 filing — all UNKNOWN in this frozen example.

## Sources

- BNT 39th annual report, FY 2081/82 (year ended 16 July 2025),
  as consolidated in the sprint verified-inputs ledger,
  prepared 2026-10-16. All §2 figures and §3 recomputations.
- BNT unaudited FY 2082/83 quarterlies (Q1 273.85M, Q2 135.49M,
  Q3 277.05M, Q4 659.28M) via the same ledger — unaudited.
- NEPSE session prints, 13–15 Oct 2026, via the same ledger
  (BNT, BNL, UNL, HDL, SHIVM, NLO peer table).
- Damodaran, Jan 2026: US Beverage (Soft) EV/Sales 4.16x,
  P/S 3.57x; country-premium page (CRP 4.66%, total ERP 8.89%);
  July 2026 refresh (mature ERP 4.23→4.20%); US unlevered beta
  0.56 (27 firms). EM beta 0.50 anchor, vintage unverified.
- Public Debt Management Office (PDMO), FY 2081/82: 22 auctions,
  8–11yr long end 5.00–5.49%.
- World Bank Nepal Development Update, Oct 2026: FY26 real GDP
  3.9%, inflation 3.1% → implied nominal GDP ~7.1%.
- Nepal trading frictions: user-supplied set, 2026-10-28
  (broker slabs, SEBON 0.015%, DP Rs 25/scrip, CGT 5% / 3.75%,
  circuit ±15%, T+2 with broker-58 T+1).
- Pack method: `agents/ledger-controller.md`,
  `agents/debate-analyst.md`, `agents/risk-stance-analyst.md`,
  `runbooks/structured-debate.md` in this repo.

*Retired figures deliberately excluded: BNT stake "~92%"
(superseded by 90.78%) and Day 6 P/E close 11,751 (superseded by
11,888). The BNL-stake / SOTP analysis from the sprint ledger is
out of scope for this note and is not repeated here.*
