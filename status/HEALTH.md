# Daily health check — 2026-10-29 02:47 UTC

> Research only. Not investment advice. This report is generated,
> not hand-written. A value is only as good as its evidence label:
> [local run], [live fetch], or TO VERIFY. Nothing here is a
> recommendation, and no number is invented.

## Overall: FAIL

FAIL: 2 | UNKNOWN: 0 | PASS: 17

## Checks

| Check | Status | Detail |
|---|---|---|
| roster | PASS | PASS: roster consistent (agents, runbooks, README tables all match). |
| README counts: finance-research-agents | PASS | no counts in README, none in evidence (Markdown repo) |
| README counts: investment-analyst-toolkit | PASS | README carries 148/148 matching evidence |
| README counts: financial-research-analyst-agent | PASS | README carries 46/46 matching evidence |
| README counts: nepali-capital-market-research | PASS | README carries 57/57 matching evidence |
| README counts: nepal-market-research | PASS | no counts in README, none in evidence (Markdown repo) |
| README counts: nepali-business-opportunities | PASS | no counts in README, none in evidence (Markdown repo) |
| README counts: equity-research-playbook | PASS | no counts in README, none in evidence (Markdown repo) |
| README counts: ShirjanKhadka1 | PASS | no counts in README, none in evidence (Markdown repo) |
| workflow: finance-research-agents | FAIL | latest completed run: Daily health check -> failure (https://github.com/ShirjanKhadka1/finance-research-agents/actions/runs/40807982936) |
| workflow: investment-analyst-toolkit | PASS | latest completed run: CodeQL -> success (https://github.com/ShirjanKhadka1/investment-analyst-toolkit/actions/runs/40807931656) |
| workflow: financial-research-analyst-agent | PASS | latest completed run: CodeQL -> success (https://github.com/ShirjanKhadka1/financial-research-analyst-agent/actions/runs/40807938143) |
| workflow: nepali-capital-market-research | FAIL | latest completed run: Tests -> failure (https://github.com/ShirjanKhadka1/nepali-capital-market-research/actions/runs/40807944516) |
| data: freshness | PASS | latest run 20261029T023941Z is 0.1 hours old |
| data: ledger | PASS | latest summary reports/daily/summary-20261029T023941Z.json parses; 2 symbol(s) fresh, accuracy stated per symbol |
| internal links | PASS | 31 internal link(s) checked, none missing (external links not checked: excluded, see report) |
| security config: investment-analyst-toolkit | PASS | codeql.yml + dependabot.yml present; actual enablement in GitHub settings is TO VERIFY in each repo's Security tab (API needs auth) |
| security config: financial-research-analyst-agent | PASS | codeql.yml + dependabot.yml present; actual enablement in GitHub settings is TO VERIFY in each repo's Security tab (API needs auth) |
| security config: nepali-capital-market-research | PASS | codeql.yml + dependabot.yml present; actual enablement in GitHub settings is TO VERIFY in each repo's Security tab (API needs auth) |

## What this job cannot check (recorded, not hidden)

- Email alerts: blocked (Gmail connector not connected). Failure
  visibility is this report + the public workflow run log + dated
  notes under status/failures/. No email alert is claimed.
- Cloudflare cron backup: blocked (Cloudflare access unverified).
  The toolkit's scheduled workflow is the only schedule.
- Dependabot / CodeQL / secret scanning / push protection
  enablement: the GitHub API needs auth for alerts, so this job
  checks config-file presence only; enablement is TO VERIFY in
  each repo's Security tab.
- Ledger-vs-accuracy-report drift: the ledger is only checkable
  locally. From public output this job can only confirm a run
  summary is published and parses. Publishing a ledger summary
  in reports/daily/ on every run is an open owner decision.
- External links: not checked (flaky, rate-limited). Internal
  relative links in the agents repo are checked.
- Live NEPSE data: no documented free public NEPSE OHLCV API
  exists; the scanner stays CSV-only. Nothing in this report
  implies a live NEPSE feed.

## Known blockers (standing)

- Phase 3 scheduled workflow's first run: not yet observed.
  Until it is seen with public output in reports/daily/, the
  schedule is a plan, not a proven fact, and freshness stays
  UNKNOWN.
- Nepal friction re-checks before reliance on a real trade:
  circuit limits (+15%/-15%, user-supplied 28 Oct 2026) against
  a current NEPSE/SEBON notice; broker-58 T+1 example against
  that broker.
- Private repos cannot be listed without a token, and that
  would NOT authorise opening the private Nepse Decode project,
  which stays out of scope regardless.

Research only. Not investment advice. No trade is made by this
system.
