# SYSTEM-MAP.md — one map for the whole programme (Phase 2, hybrid)

**This file supersedes the seven INTEGRATION.md files** (one per repo,
including the profile's). Those files are not deleted in this phase;
they are superseded, and their divergent numbers (7 vs 10 agents,
8/8 vs 37/37 vs 47 tests, "Live (deploying)", "NOT DEPLOYED YET") are
the drift this map fixes. Numbers in this map come from evidence dated
28 Oct 2026 (Phase 1 audit + Phase 2 re-runs); where no evidence exists
the cell says so — it is never guessed. Regenerate counts with
`ops/generate_status.py` from a fresh evidence file; do not hand-edit
this table's numbers and call the result generated.

> Research only, not investment advice. Nothing here is a recommendation
> to buy, sell, or invest in any security.

## The system in one diagram

```
Question ──► Agents (think) ──► Engines (calculate) ──► Data (validated)
   │              │                     │                     │
   │              ▼                     ▼                     ▼
   │        finance-research-     investment-analyst-     toolkit/free_data
   │        agents (10 agents,    toolkit (47/47) +      (Yahoo, CoinGecko,
   │        4 runbooks)           analyst-agent (4/4)    ECB, World Bank;
   │                              + NEPSE scanner        NEPSE = CSV only)
   │                              (40/40)
   ▼
Reports / site ──► profile repo (hub)
Domain repos ──► nepal-market-research · nepali-capital-market-research
                 · nepali-business-opportunities · equity-research-playbook
```

## Repo-by-repo map

| Repo | Purpose | Layer | Live status (28 Oct 2026) | Tests / checks (evidence) | Links |
|---|---|---|---|---|---|
| `finance-research-agents` | Free, local Markdown agent pack: research agents + runbooks + templates | Agents / runbooks | Live, public, main | Roster check: agents.json vs disk vs README — run in Phase 2 verification (see below). No code tests (Markdown). CI: none yet — roster check is the Phase 2 addition (template in ops/). | https://github.com/ShirjanKhadka1/finance-research-agents |
| `investment-analyst-toolkit` | Tested Python toolkit: ratios, DuPont, DCF, multiples, portfolio, performance, forecast, options, Monte Carlo, backtest, autonomous, free-data layer | Engines + Data | Live, public, main, v0.5.0 + free-data layer | 47/47 passed (fresh venv, 28 Oct 2026; also CI run #4 succeeded 28 Oct 2026). CI: GitHub Actions, pytest 3.10/3.11/3.12. | https://github.com/ShirjanKhadka1/investment-analyst-toolkit |
| `financial-research-analyst-agent` | Standalone stdlib-only pipeline: technicals, Piotroski, valuation by company type, VaR, debate + Risk Veto, hash-chained audit log | Engines | Live, public, main | 4/4 passed (fresh venv, 28 Oct 2026; CI run #1 succeeded 28 Oct 2026). Thin coverage for 11 modules — Phase 1 finding, not fixed in Phase 2. | https://github.com/ShirjanKhadka1/financial-research-analyst-agent |
| `nepali-capital-market-research` | Whole Nepal capital market: agent, guides, templates, NEPSE scanner, reference-site teardown | Domain (Nepal) + Engines (scanner) | Live, public, main | Scanner 40/40 passed (fresh venv, 28 Oct 2026). CI: workflow added in Phase 2 (`.github/workflows/test.yml`, same Python matrix) — runs publicly after deployment. Parent README now mentions `scanner/` and `research/`. | https://github.com/ShirjanKhadka1/nepali-capital-market-research |
| `nepal-market-research` | Sourced NEPSE company case studies, starting with Bottlers Nepal (Terai) | Domain (Nepal) | Live, public, main | No code tests (Markdown). Case study status: **inputs only** — no DCF, no target price. `data/` folder: empty, now honestly labelled (see `data/README.md`). | https://github.com/ShirjanKhadka1/nepal-market-research |
| `nepali-business-opportunities` | 8-sector Nepal business-opportunity scoring framework | Domain (Nepal) | Live, public, main | No code tests (Markdown). Sectors alphabetical, NOT a ranking; rank only on evidence quality ≥ 3. No scored evidence exists yet. | https://github.com/ShirjanKhadka1/nepali-business-opportunities |
| `equity-research-playbook` | Research templates: initiation, earnings, forensic, valuation-sanity | Templates | Live, public, main | No code tests (Markdown). **Pointer candidate:** its 4 templates are byte-identical to the agent pack's `templates/` (Phase 1, diff-verified) — duplication recorded, not yet resolved. | https://github.com/ShirjanKhadka1/equity-research-playbook |
| `ShirjanKhadka1` (profile) | Profile README: hub front door for the programme | Reports / site (hub) | Live, public, main | No code tests. Projects table fixed in Phase 2: toolkit 47/47, analyst-agent + scanner rows added, no "Live (deploying)" cells. No LICENSE file — Phase 1 finding, not fixed in Phase 2. | https://github.com/ShirjanKhadka1 |
shirjankhadka.github.io — separate Nepse Decode project, out of scope, untouched.

## Cross-repo rules (hybrid discipline)

1. **One source of truth for counts:** `ops/generate_status.py` +
   an evidence JSON. READMEs point at CI or at the generated table;
   they do not carry a second hand-typed copy of the same number.
2. **One CI template:** `ops/ci-template.yml` (pytest, Python
   3.10/3.11/3.12). Live in toolkit + analyst-agent; added for the
   scanner in Phase 2; roster check for the agent pack.
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
