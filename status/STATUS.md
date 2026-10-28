# Programme status

> Research only. Not investment advice. This page is replaced section by
> section by the daily health job (`.github/workflows/health.yml`, daily
> 02:00 UTC) once that job runs. Until then, the snapshot below is the
> honest state — every value labelled with how it was produced. Nothing
> here is a recommendation, and no number is invented.

## How to read this page

- **[local test run, date]** — pytest / roster check run on a local
  machine on that date. Proves the code, not the live CI run.
- **[live fetch, date]** — fetched from public GitHub on that date.
- **[TO VERIFY]** — not observed yet. Never read as green.
- **UNKNOWN** — a check could not be completed. Never read as green.
- **STALE** — data older than the freshness limit, or labelled
  STALE_OR_FAILED. Never read as fresh.

## First snapshot — 28 Oct 2026 (~15:16 UTC / 21:01 NPT)

Produced by a local run of `ops/health_check.py --live` on 28 Oct 2026.
This is a snapshot, not a live health result: the daily health job had
not run yet when it was written.

| Repo | Health | Evidence |
|---|---|---|
| finance-research-agents | Roster PASS [local test run, 28 Oct 2026]; workflow UNKNOWN [live fetch, 28 Oct 2026 — no completed run yet, health workflow not yet live] | Roster check: 16 agents, 8 runbooks, PASS. Internal links: 24 checked, none missing. |
| investment-analyst-toolkit | Tests 124/124 [local test run, 28 Oct 2026]; latest completed workflow: Tests → success [live fetch, 28 Oct 2026] | Local suite v0.7.0 (118 + 6 Phase 7 property tests). The live CI run predates Phase 7 deployment, so it does NOT prove 124/124 on GitHub — that proof waits for the post-deployment CI run. |
| financial-research-analyst-agent | Tests 46/46 [local test run, 28 Oct 2026]; latest completed workflow: Tests → success [live fetch, 28 Oct 2026] | Same caveat as the toolkit: the live run predates Phase 7 deployment. |
| nepali-capital-market-research | Scanner 57/57 [local test run, 28 Oct 2026]; latest completed workflow: Tests → success [live fetch, 28 Oct 2026] | Scanner is CSV-only, no live NEPSE feed. Same post-deployment caveat. |
| nepal-market-research | Inputs only [local, 28 Oct 2026] | No code tests (Markdown). `data/` honestly empty. |
| nepali-business-opportunities | Framework only [local, 28 Oct 2026] | No code tests. Sectors alphabetical, not ranked. |
| equity-research-playbook | Templates only [local, 28 Oct 2026] | No code tests. |
| ShirjanKhadka1 (profile) | Hub README [local, 28 Oct 2026] | Projects table current at Phase 5 counts in the local copy; live update rides with the deploy queue. |

## Data freshness — UNKNOWN [live fetch, 28 Oct 2026]

No summary exists in the toolkit's `reports/daily/` on main yet: the
Phase 3 scheduled workflow (daily 01:00 UTC) has not been observed
running. The schedule is a plan, not a proven fact, until its first run
is seen with public output. Freshness stays UNKNOWN until then.

## Prediction ledger — UNKNOWN [live fetch, 28 Oct 2026]

No run summary is publicly published yet, so ledger drift cannot be
checked from public output (the ledger is only checkable locally).
Publishing a ledger summary in `reports/daily/` on every run is an open
owner decision (see the weekly template).

## Security config — FAIL on main, for a known reason [live fetch, 28 Oct 2026]

CodeQL workflow + Dependabot config files are absent from the three
code repos on main — because Phase 7, which adds them, is queued and
not yet deployed. This is the queue state, not a defect in the code:
after Phase 7 deploys, this check should flip to PASS on config
presence, with actual enablement in GitHub settings still TO VERIFY in
each repo's Security tab (the API needs auth for alerts).

## Known blockers (standing)

- Email alerts: blocked (Gmail connector not connected). Failure
  visibility is the health report + workflow run log + dated notes
  under `status/failures/`.
- Cloudflare cron backup: blocked (Cloudflare access unverified).
- Private repos: cannot be listed without a token, and that would NOT
  authorise opening the private Nepse Decode project, which stays out
  of scope regardless.
- Nepal friction re-checks before reliance on a real trade: circuit
  limits (+15%/−15%, user-supplied 28 Oct 2026) against a current
  NEPSE/SEBON notice; broker-58 T+1 example against that broker.
- Live NEPSE data: no documented free public NEPSE OHLCV API exists;
  the scanner stays CSV-only.

## Where the live report lives

Once the daily health job runs, `status/HEALTH.md` in this repo holds
the latest generated report, and `status/failures/` holds dated notes
for any FAIL or UNKNOWN day. This STATUS.md page is the human-readable
summary; HEALTH.md is the machine-checked record.

Research only. Not investment advice. No trade is made by this system.
