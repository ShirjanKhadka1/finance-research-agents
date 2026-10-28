# status/

Programme health, generated and human-readable — Phase 8.

- `STATUS.md` — the human-readable status page: per-repo health, data
  freshness, ledger accuracy, and known blockers, every value labelled
  by how it was produced. First snapshot dated 28 Oct 2026 (local +
  live-fetch evidence); replaced by the daily health job's findings as
  they arrive.
- `HEALTH.md` — the latest generated daily health report (written by
  `.github/workflows/health.yml`, daily 02:00 UTC). Absent until the
  health job's first run — its absence is itself the honest state.
- `failures/` — dated notes for any FAIL or UNKNOWN day (phase, error,
  repo, retry status, fix attempted). Empty means no failure day has
  been recorded, not that none could occur.
- `WEEKLY-SUMMARY-TEMPLATE.md` — the weekly summary shape: what
  changed, health for the week, and what genuinely needs the owner's
  decision. Weekly copies live under `status/weekly/` once written.

Failure visibility without email (blocked) and without a Cloudflare
cron backup (blocked): this directory + the public workflow run log.
No email alert is claimed anywhere.

Research only. Not investment advice.
