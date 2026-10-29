# Programme scoring rubric — honest, checkable, evidence-only

**Scope.** The eight public repos of Shirjan Khadka's finance-research
programme (GitHub user `ShirjanKhadka1`): `finance-research-agents`,
`investment-analyst-toolkit`, `financial-research-analyst-agent`,
`nepali-capital-market-research`, `nepal-market-research`,
`nepali-business-opportunities`, `equity-research-playbook`, and the
profile repo `ShirjanKhadka1`. Never `shirjankhadka.github.io`, never
any private repo, never any unlisted repo.

**Research only.** Nothing in this rubric is investment advice or a
buy/sell/hold recommendation. Scores measure how well a repo's claims
match checkable evidence — not whether a model, signal, or dossier is
"good" as an investment.

**How to use this rubric.** For each criterion, award only what the
cited evidence proves. A prepared-but-not-applied item (a settings
payload, a release spec, a workflow file on an unmerged branch) scores
0 on that criterion: preparation is not deployment. A criterion that
was not observed scores 0 and is labelled `not-yet-verified` — never
estimated, never carried over from an earlier phase.

**Structural caps — these apply no matter how high a score is:**

- **No live NEPSE data.** There is no live NEPSE feed in any repo.
  NEPSE work is CSV-only (user-supplied CSV). No bulk re-scraping of
  any third-party data to republish a competing feed.
- **Demo / example data only.** Forecast and backtest numbers rest on
  labelled demo data or on AAPL example series (a US equity, not a
  NEPSE security). They are single-symbol, single-period results, not
  general accuracy claims.
- **BNT valuation impossible from verified inputs alone.** Bottlers
  Nepal (Terai) figures are not re-audited against the 39th annual
  report PDF (no copy on file); open items remain (the ~Rs 81M bridge
  gap, lease-in-working-capital vs debt, NOPAT 25% statutory vs 24.4%
  effective). No repo claims a completed BNT valuation.
- **Scheduled automation is NOT proven.** A scheduled daily workflow's
  output has been observed only via a manual dispatch run, never via a
  cron-scheduled run. The schedule is therefore scored as unproven.
- **Settings enablement is NOT verified.** Dependabot, secret
  scanning, and push protection are not observable with the available
  token (403); all eight repo descriptions, topics, and homepages are
  currently null/empty as verified live. See
  `ops/BLOCKERS.md` ("not yet verified — needs owner").
- **No releases exist yet.** No release has been created for any repo;
  the toolkit v0.8.0 release spec is prepared, not applied.

## Criteria (100 points total)

### A. Test / check suite reproduced green — 25 points

Tiered, because repos have different kinds of checks. Apply the tier
that fits the repo, and cite the run or count:

- **25** — a code test suite or checker reproduced green at the Round 3
  gate: toolkit 195/195, analyst-agent 49/49, scanner 70/70, playbook
  checker 6/6.
- **20** — no code suite, but live file/roster counts reproduced
  exactly (agents: 19 agent files = 18 agents + WHEN-TO-USE guide,
  10 runbooks, `agents.json` 19 entries; profile: live profile checks
  reproduced, including merged PRs #3 and #4).
- **15** — no suite to reproduce, but live file-presence checks pass
  (opportunities 4/4 Phase 11 files present; nepal-market-research
  9/9 present).
- **0** — no reproduced suite, checker, or presence check.

### B. CI / workflow run observed green at HEAD — 20 points

- **20** — a CI Tests run observed green at the live HEAD commit
  (toolkit run 40813298143; analyst-agent run 40813338085; scanner run
  40813353195). CodeQL green in the same three code repos is
  supporting evidence, not a substitute.
- **10** — no CI Tests run observed, but another workflow run observed
  green (agents health workflow run 40810597293, SUCCESS,
  `status/HEALTH.md` PASS 19/19 at 03:10 UTC).
- **0 / not-yet-verified** — no workflow run observed green for the
  repo. A workflow file existing on a branch or on main, without an
  observed green run, scores 0.

### C. Claims match evidence (R1 `verify_live` result) — 20 points

Formula, no judgement: `20 × PASS / (PASS + FAIL)`, counted from the
R1 `verify_live.py` output (44 PASS / 4 FAIL / 9 NOT_VERIFIED across
the programme). `NOT_VERIFIED` checks are excluded from the formula
but must be listed in the scores file — they are gaps, not passes.
A FAIL caused by a local-side race artefact must still be shown as a
FAIL with its explanation; it is not silently converted to a PASS.
(The four R1 FAILs are recorded as local-side race artefacts from
concurrent workers, not deployment failures — see the scores file.)

### D. Documentation completeness on live main — 15 points

- **15** — README plus core docs (LICENSE, CONTRIBUTING, SECURITY)
  present on live main AND the repo's own evidence record present
  (toolkit: post-mortem + real-data walk-forward record; agents:
  WHEN-TO-USE guide + runbooks; analyst-agent: second worked example;
  scanner: backtest table with baselines; playbook: 8 templates +
  checker section; profile: mobile heroes, 0 Nepse Decode mentions).
- **12** — record present but carrying a stated limitation that blocks
  its main claim (opportunities: dossier scores are sector-level
  indicative only; nepal-market-research: BNT inputs + skeleton only,
  figures not re-audited against the annual-report PDF).
- **0** — README or core docs missing on live main.

### E. Settings / metadata verified live — 10 points

- **10** — repo description, topics, and homepage set as verified
  live, AND Dependabot / secret scanning / push protection verified
  enabled.
- **0 / not-yet-verified** — anything less. On 2026-10-29 this is 0
  for all eight repos: descriptions/topics/homepages are null/empty
  as verified live, settings enablement is not observable via the
  token (403), and the settings payload in
  `ops/ready-for-browser/repo-settings-payload.md` is prepared, not
  applied. Prepared-not-applied scores 0.

### F. Release published — 10 points

- **10** — a release exists for the repo (versioned, published).
- **0 / not-yet-verified** — no release. On 2026-10-29 this is 0 for
  all eight repos. The toolkit v0.8.0 release spec in
  `ops/ready-for-browser/release-toolkit-v0.8.0.md` is prepared, not
  applied, and scores 0. A version string in `pyproject.toml`
  (toolkit v0.8.0) is not a release.

## Resolved count conflict (recorded, not re-derived)

An earlier health run (03:10 UTC) recorded the toolkit at 148/148.
That was the pre-Phase-11 state. The Phase 11 HEAD state is **195/195
tests, 95% coverage, `fail_under` 80**, proven by the R1 gate (195/195
local) and by CI Tests run 40813298143 SUCCESS at HEAD
(2026-10-29T03:38:43Z). **Use 195 throughout.** The 148 figure is a
historical Phase 10 count and must not be presented as current.

## What a score does NOT mean

A score of 80 does not mean "production-ready", "accurate", or
"investable". It means: the suite reproduced, CI was seen green, the
live claims mostly matched the live evidence, and the docs are present
— with releases and settings still unverified and the structural caps
above still in force. Any score quoted without its 0 / not-yet-verified
criteria and without the structural caps is a misquote.
