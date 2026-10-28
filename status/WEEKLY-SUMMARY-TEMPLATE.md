# Weekly summary — template

> Copy this file to `status/weekly/YYYY-MM-DD.md` each week and fill it
> in from the daily health reports (`status/HEALTH.md`), the workflow
> run logs, and the deploy queue. Nothing in a weekly summary is
> invented: a claim without its evidence label (local run / live fetch /
> TO VERIFY) does not go in. Research only. Not investment advice.

## Week of: <!-- YYYY-MM-DD --> (Monday–Sunday, NPT)

## What changed this week

<!-- One line per change, each with repo + evidence: e.g.
- investment-analyst-toolkit v0.7.0: engine validation + Nepal
  frictions, 124/124 [local test run, date]; CI run [live fetch, link].
- finance-research-agents: health workflow added, first run [observed /
  TO VERIFY].
- Nothing changed: say so. An empty week is a result, not a gap to fill.
-->

## Health this week

<!-- From status/HEALTH.md: days PASS / FAIL / INCOMPLETE, with the
reason for every non-PASS day. If a day is missing, say which day and
why (no run, failed run, unobserved) — never silently skip it. -->

- Days fully PASS: <!-- n / 7 -->
- Days FAIL: <!-- list dates + reasons -->
- Days INCOMPLETE (UNKNOWN present): <!-- list dates + reasons -->
- Data freshness at week end: <!-- latest reports/daily run stamp +
  age, or UNKNOWN with reason -->
- Prediction ledger at week end: <!-- latest published accuracy, with
  n, or UNKNOWN with reason -->

## What needs the owner's decision

These are the real open decisions as of Phase 8 (28 Oct 2026). Close
one only when the owner decides it; do not close one by assuming it.

1. **Digest schedule approval** — the Phase 5 digest templates
   (international + Nepal) are design only. Publishing them on a
   schedule needs the owner's approval and an observed first run.
2. **Release publishing** — release-notes drafts exist (Phase 6) for
   the toolkit and the other code repos. No release is claimed until
   it is created on GitHub.
3. **Repo metadata application** — descriptions / website / topics
   were prepared in Phase 6, not applied. Applying them is a GitHub
   UI step by the owner (or a delegated task with that step named).
4. **Docs-site publication** — the docs site outline and starter
   content exist (Phase 6). Publishing it to GitHub Pages is a
   separate step; no live docs site is claimed until it is seen.
5. **Nepal friction re-checks** — before reliance on a real trade:
   circuit limits (+15%/−15%, user-supplied 28 Oct 2026) against a
   current NEPSE/SEBON notice; broker-58 T+1 example against that
   broker; CGT Gazette citation re-checked if rates change.
6. **Scheduled workflow first run observation** — the Phase 3 toolkit
   workflow (daily 01:00 UTC) and the Phase 8 health workflow (daily
   02:00 UTC) are plans until their first runs are observed with
   public output. The first dry-run, then real dispatch, still needs
   observing.
7. **Ledger summary publication** — publishing a per-run accuracy
   summary in `reports/daily/` so ledger drift becomes publicly
   checkable (today it is local-only).
8. **Security enablement verification** — CodeQL / Dependabot /
   secret scanning / push protection actually enabled in each code
   repo's GitHub settings (config files alone do not prove it).

## Resolved (do not reopen without new evidence)

- Profile repo licence: MIT added in Phase 6 (all 8 programme repos
  MIT on local copies; live once Phase 6 deploys).
- Nepse Decode / shirjankhadka.github.io: out of scope, untouched —
  not a decision to revisit; any change there needs a new, explicit
  owner instruction.
- Email alerts / Cloudflare cron backup: blocked on unverified
  access; worked around with public reports, not faked.

## Failures and fixes this week

<!-- For each failure: phase, error, repo, retry status, fix attempted
(or "none — reporting only"). A failure with no fix attempted is
listed as such, not hidden. -->

## Next week's plan

<!-- Only items the owner has approved or the mandate queue already
contains. Do not invent new scope here. -->

Research only. Not investment advice. No trade is made by this system.
