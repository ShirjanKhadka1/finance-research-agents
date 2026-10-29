# SYSTEM-MAP.md — one map for the whole programme (Phase 2, hybrid; Round 3: generated numbers)

**CANONICAL MAP (Round 3). This file is the single canonical system map.**
The seven `INTEGRATION.md` files (one per repo, including the profile's)
are **SUPERSEDED** — they are kept in place with supersession banners and
their numbers are historical, not current. They are NOT deleted, so their
history is preserved. Do not edit numbers in an `INTEGRATION.md` file:
edit this map, and let the owning repo's generated `status.json` be the
source for any count.

**How numbers work here (Round 3):** every count in the table below was
verified by a local run on 29 Oct 2026 and matches the owning repo's
generated `status.json` (linked per row). Each owning repo generates its
`status.json` with `scripts/generate_status.py` (pytest runs and file
counts — never a typed constant) and enforces it with
`scripts/check_numbers.py`, which fails if any checked file disagrees
with `status.json`. Where no evidence exists the cell says so — it is
never guessed. Historical counts that remain in version-history sections
of READMEs are allowlisted by exact substring in the owning checker, so
changing one fails the check instead of passing silently.

> Research only, not investment advice. Nothing here is a recommendation
> to buy, sell, or invest in any security.

## The system in one diagram

```
Question ──► Agents (think) ──► Engines (calculate) ──► Data (validated)
   │              │                     │                     │
   │              ▼                     ▼                     ▼
   │        finance-research-     investment-analyst-     toolkit/free_data
   │        agents (18 agents,    toolkit (195/195) +    (Yahoo, CoinGecko,
   │        10 runbooks)           analyst-agent (49/49)  ECB, World Bank;
   │                              + NEPSE scanner        NEPSE = CSV only)
   │                              (70/70)
   ▼
Reports / site ──► profile repo (hub)
Domain repos ──► nepal-market-research · nepali-capital-market-research
                 · nepali-business-opportunities · equity-research-playbook
```

## Repo-by-repo map

| Repo | Purpose | Layer | Live status (29 Oct 2026) | Tests / checks (generated) | Links |
|---|---|---|---|---|---|
| `finance-research-agents` | Free, local Markdown agent pack: research agents + runbooks + templates | Agents / runbooks | Live, public, main | Roster check: agents.json vs disk vs README — PASS 18 agents, 10 runbooks (29 Oct 2026). No code tests (Markdown). Generated: [ops/status.json](https://github.com/ShirjanKhadka1/finance-research-agents/blob/main/ops/status.json) | https://github.com/ShirjanKhadka1/finance-research-agents |
| `investment-analyst-toolkit` | Tested Python toolkit: ratios, DuPont, DCF, multiples, portfolio, performance, forecast, options, Monte Carlo, backtest, autonomous, free-data layer, data layer, Nepal frictions, accuracy report | Engines + Data | Live, public, main, v0.8.0 | 195/195 passed (fresh venv, 29 Oct 2026, pytest 9.2.0); coverage 95% total, `fail_under=80`. CI: GitHub Actions, pytest 3.10/3.11/3.12; scheduled daily workflow (Phase 3) is a plan until its first run is observed. Generated: [investment-analyst-toolkit/status.json](https://github.com/ShirjanKhadka1/investment-analyst-toolkit/blob/main/status.json) | https://github.com/ShirjanKhadka1/investment-analyst-toolkit |
| `financial-research-analyst-agent` | Standalone stdlib-only pipeline: technicals, Piotroski, valuation by company type, VaR, debate + Risk Veto, hash-chained audit log | Engines | Live, public, main | 49/49 passed (fresh venv, 29 Oct 2026). Generated: [financial-research-analyst-agent/status.json](https://github.com/ShirjanKhadka1/financial-research-analyst-agent/blob/main/status.json) | https://github.com/ShirjanKhadka1/financial-research-analyst-agent |
| `nepali-capital-market-research` | Whole Nepal capital market: agent, guides, templates, NEPSE scanner, reference-site teardown | Domain (Nepal) + Engines (scanner) | Live, public, main | Scanner 70/70 passed (fresh venv, 29 Oct 2026): test_scanner 30 + test_edge_cases 10 + test_signal_labels 17 + test_backtest 13. CI: workflow added in Phase 2 (`.github/workflows/test.yml`, same Python matrix). Scanner is CSV-only, no live NEPSE feed. Generated: [nepali-capital-market-research/status.json](https://github.com/ShirjanKhadka1/nepali-capital-market-research/blob/main/status.json) | https://github.com/ShirjanKhadka1/nepali-capital-market-research |
| `nepal-market-research` | Sourced NEPSE company case studies, starting with Bottlers Nepal (Terai) | Domain (Nepal) | Live, public, main | No code tests (Markdown). Case study status: **inputs only** — no DCF, no target price. `data/` holds 1 dataset (`bnt-fy2081-82.csv`); 1 case-study folder. Generated: [nepal-market-research/status.json](https://github.com/ShirjanKhadka1/nepal-market-research/blob/main/status.json) | https://github.com/ShirjanKhadka1/nepal-market-research |
| `nepali-business-opportunities` | 8-sector Nepal business-opportunity scoring framework | Domain (Nepal) | Live, public, main | No code tests (Markdown). Sectors alphabetical, NOT a ranking; rank only on evidence quality ≥ 3. No scored evidence exists yet. Scorecard: 8 criteria, total /40. Generated: [nepali-business-opportunities/status.json](https://github.com/ShirjanKhadka1/nepali-business-opportunities/blob/main/status.json) | https://github.com/ShirjanKhadka1/nepali-business-opportunities |
| `equity-research-playbook` | Research templates: initiation, earnings, forensic, valuation-sanity, data-first, structured-debate, ledger-control, research-to-use-case | Templates | Live, public, main | 8 templates, checker tests 6/6 passed (29 Oct 2026). **Known duplication:** 4 of its templates are byte-identical to the agent pack's `templates/` (Phase 1, diff-verified) — duplication recorded, not yet resolved. Generated: [equity-research-playbook/status.json](https://github.com/ShirjanKhadka1/equity-research-playbook/blob/main/status.json) | https://github.com/ShirjanKhadka1/equity-research-playbook |
| `ShirjanKhadka1` (profile) | Profile README: hub front door for the programme | Reports / site (hub) | Live, public, main | No code tests. Programme totals generated 29 Oct 2026: 18 agents, 10 runbooks, 320 tests across the four suites (195 + 49 + 70 + 6). Generated: [ShirjanKhadka1/status.json](https://github.com/ShirjanKhadka1/ShirjanKhadka1/blob/main/status.json) | https://github.com/ShirjanKhadka1 |

shirjankhadka.github.io — separate Nepse Decode project, out of scope, untouched.

## Pointers (canonical structure, Round 3)

- **Canonical map:** this file (`finance-research-agents/ops/SYSTEM-MAP.md`).
  The local staging mirror at `~/workspace/github-repos/ops/SYSTEM-MAP.md`
  is a copy of this file, not a second source of truth.
- **Superseded, kept in place:** the seven `INTEGRATION.md` files
  (`finance-research-agents`, `investment-analyst-toolkit`,
  `nepali-capital-market-research`, `nepal-market-research`,
  `nepali-business-opportunities`, `equity-research-playbook`,
  `ShirjanKhadka1`). Each carries a Round 3 supersession banner; count
  claims in them were replaced by pointers to the owning `status.json`.
  Nothing was deleted and no history was rewritten.
- **Generated counts, per repo:** `<repo>/status.json`, produced by
  `<repo>/scripts/generate_status.py` (agents repo: `ops/generate_counts.py`
  for this repo, `ops/generate_programme_status.py` for the programme-wide
  `ops/programme-status.json` across checkouts). Profile counts are
  fetched from the owning repos' `status.json` files, never typed
  (`ShirjanKhadka1/scripts/generate_status.py`).
- **Enforcement:** `<repo>/scripts/check_numbers.py`
  (agents repo: `ops/check_numbers.py`) fails if any checked file
  disagrees with `status.json`. CI workflow content is prepared in
  `ci/check-numbers.yml` in each repo and in the Round 3 PR bodies: the
  workflow file itself must be added via the parent browser route,
  because the API token lacks workflow scope — it is NOT claimed deployed
  until a workflow run is observed.
- **Badges:** GitHub READMEs cannot render a badge from a repo
  `status.json` file (shields.io has no JSON-file endpoint for arbitrary
  repo files without a service in between), so no badge is faked here.
  The pointer is the `status.json` link in each row above and in each
  README's generated-counts line. Adding a badge later means adding a
  real badge service, not hand-drawing a number into an SVG.

## Cross-repo rules (hybrid discipline)

1. **One source of truth for counts:** each repo's generated
   `status.json` + its checker. READMEs point at `status.json` or at CI;
   they do not carry a second hand-typed copy of the same number.
2. **One CI template:** `ops/ci-template.yml` (pytest, Python
   3.10/3.11/3.12). Live in toolkit + analyst-agent; added for the
   scanner in Phase 2; roster check for the agent pack. Round 3 adds a
   numbers-check workflow per repo (browser route, see Pointers).
3. **One system map:** this file. Per-repo INTEGRATION.md files are
   superseded; do not edit their numbers — edit this map, from
   evidence, and let the INTEGRATION.md files be retired in a
   separately-approved cleanup.
4. **No duplication without a sync mechanism:** the playbook/pack
   template duplication is the standing example. Until it is resolved
   (pointer or CI sync check), it is listed here as a known
   duplication, not hidden.
5. **Nepal vs international, always labelled:** NEPSE tickers are never
   confused with other exchanges' tickers (NEPSE BNT ≠ NYSE BNT);
   exchange is stated with every ticker. NEPSE data is CSV-only until
   a documented free public API or a funded licensed feed exists.
6. **Failures published with successes:** prediction ledgers (toolkit)
   and audit reports (this programme) retain failures with reason and
   action; pending predictions never count as wins.
7. **Daily health job (Phase 8):** `finance-research-agents`
   `.github/workflows/health.yml` (daily 02:00 UTC) runs
   `ops/health_check.py --live` across all 8 repos (roster, README
   counts vs evidence, workflow runs, data freshness, ledger
   publication, internal links, security-config presence) and commits
   the report to `status/HEALTH.md` plus dated failure notes under
   `status/failures/`; the job fails on any FAIL or UNKNOWN, never
   silently green. Human-readable status: `status/STATUS.md`. No email
   alerts (blocked) and no Cloudflare cron backup (blocked); failure
   visibility is the report + the public workflow log. First run is
   TO VERIFY after deployment — no health result is claimed until it
   is observed.
8. **Round 3 numbers discipline:** a count that cannot be generated is
   left out and labelled TO VERIFY (profile CI status; analyst/capital/
   playbook versions — no version file exists in those repos). A
   generated SVG (profile numbers graphic) is never hand-edited; it is
   regenerated by its own script after the PRs merge.
