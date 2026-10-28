# ARCHITECTURE.md — Hybrid: separate repos, monorepo discipline

**Decision (approved by the owner, 28 Oct 2026, "ok do it"): HYBRID.**
Keep the separate public repos. Do NOT migrate to a monorepo, move repos,
merge repos, rewrite history, or change any repo's visibility. Impose
monorepo discipline instead: one system map, one generated status source
of truth, one shared CI template, and roster-consistency checks.

**Canonical location of this document:** `ops/ARCHITECTURE.md` in the
local programme workspace. It is published to GitHub with the Phase 2
deployment manifest (see `ops/DEPLOYMENT-MANIFEST.md`); until then, the
local copy is canonical and the live repos still carry their old
INTEGRATION.md files, which this document supersedes (see below).

> Research only, not investment advice. Nothing here is a recommendation
> to buy, sell, or invest in any security. Every number below carries
> its evidence and date, or is labelled TO VERIFY.

## Why hybrid, and not the other two options

### Why not a monorepo
- **Visibility was the programme's stated goal.** Separate public repos
  are findable, pinnable, and searchable on GitHub as "NEPSE scanner" or
  "finance agents"; a monorepo hides the Nepal scanner inside a larger
  tree (it was already invisible from its own parent README — a monorepo
  would make that worse unless the hub were excellent).
- **No outside project needs folding in.** The programme's eight repos
  already cover every layer in the diagram below; a monorepo would add
  migration cost without adding a layer the programme lacks.
- **Different audiences, different stability.** The agent pack (Markdown,
  copy a prompt) and the toolkit (Python, semver) change at different
  speeds and are consumed differently; forcing one versioning scheme on
  both creates friction the split avoids.
- **Zero migration cost today, rising cost tomorrow.** All programme
  repos were created 28 Oct 2026 with 0 stars / 0 forks, so keeping them
  costs nothing in redirects or shims — and every existing URL, pin, and
  profile link keeps working.

### Why not untouched separate repos
- **Drift was the programme's #1 problem (Phase 1, evidence-based).**
  Seven INTEGRATION.md files carried divergent numbers (7 vs 10 agents;
  8/8 vs 37/37 vs 47 tests); agents.json listed 3 of 4 runbooks; four
  profile rows read "Live (deploying)"; the toolkit README said a live
  v0.5.0 was "NOT DEPLOYED YET". Untouched separation has no mechanism
  that stops this recurring.
- The hybrid fixes the actual problem — drift — with generated status,
  a shared CI template, and roster checks, without paying migration cost.

## Layer diagram and repo ownership

```
User question (company / market / business idea)
        │
        ▼
AGENTS / RUNBOOKS  (think, in order) ......... finance-research-agents
        │  (Markdown agents + runbooks; executable checks via
        │   ops/check_roster.py, not by the prompts themselves)
        ▼
ENGINES  (calculate, with falsifiers) ........ investment-analyst-toolkit
        │  (ratios, DuPont, DCF, multiples, portfolio, performance,
        │   forecast, options, Monte Carlo, backtest, autonomous)
        │  + financial-research-analyst-agent (standalone pipeline:
        │   technicals, Piotroski, valuation by company type, VaR,
        │   debate + Risk Veto, hash-chained audit log)
        │  + nepali-capital-market-research/scanner (NEPSE engine:
        │   EMA/SMA crossovers, RSI, MACD, Bollinger, ATR, Stochastic,
        │   ADX, volume checks, signal-vs-noise labels)
        ▼
DATA  (adapters, validated, fallback chain) .. toolkit/free_data.py
        │  (Yahoo → Stooq; CoinGecko; ECB; World Bank; keyed providers
        │   env-only. NEPSE: user-supplied CSV only — no documented free
        │   public NEPSE OHLCV API verified as of 28 Oct 2026; the
        │   licensed feed is paid and not started.)
        ▼
REPORTS / SITE  (static, generated, dated) ... profile repo (hub front
        │  door) + domain repos (see SYSTEM-MAP.md)
        ▼
DOMAIN REPOS (apply, with sources) .......... nepal-market-research
        (NEPSE company case studies, inputs only) ·
        nepali-capital-market-research (whole-market structure) ·
        nepali-business-opportunities (8-sector scorecard, alphabetical,
        ranked only on evidence ≥ 3) · equity-research-playbook
        (templates — see pointer candidate below)
```

Ownership rule: each layer has exactly one owning repo (above). A repo
may *use* another layer, but it does not duplicate it — duplication is
how the Phase 1 drift happened.

## The generated-status rule (non-negotiable)

- **Counts and statuses are generated from evidence, never hand-typed.**
  The generator is `ops/generate_status.py`: it reads an evidence JSON
  (test run date + result, CI run, live listing) and prints a table.
  A repo with no evidence entry is listed UNKNOWN, never guessed.
- **READMEs must not carry a second, hand-typed copy of the same number.**
  Where a README states a test count, that count must match the latest
  evidence file, and the next evidence refresh must update it — or the
  count is removed and replaced with a pointer to CI.
- Historical version sections may keep their as-at counts, but only
  labelled as historical (as-at their version), never as the current
  count. Phase 2 applied this to the toolkit README (v0.3: 23, v0.4: 33,
  current: 47/47).

## CHANGELOG and versioning policy

- **Code repos (toolkit, analyst-agent, scanner):** semantic versioning
  in the code's own version file where one exists (toolkit: pyproject
  `0.5.0`); each release gets dated notes stating what changed, what
  was tested (exact counts), and what remains TO VERIFY. No release is
  claimed before its CI run passes.
- **Research repos (agent pack, playbook, Nepal repos, profile):**
  dated notes, not semver — a change is recorded with its date, what
  changed, and its evidence (e.g. "roster check passed 28 Oct 2026").
  The agent pack's `agents.json` version `0.1.0` is the roster's own
  version string; it is NOT the same numbering as the README's v0.4/v0.5
  improvement batches, which describe batches of work, not a pack
  release. That distinction is recorded here so it is not "fixed" into
  a false consistency later.
- **Breaking changes:** a moved/renamed file keeps a pointer note in
  its old location for at least one release cycle; no silent renames.

## Superseded files (deprecation, not deletion)

The seven INTEGRATION.md files (one per repo, including the profile's)
are **superseded by SYSTEM-MAP.md** as of Phase 2. They are NOT deleted
in this phase: deletion is a separately-approved step, and live links
may still point at them. Each INTEGRATION.md's divergent numbers were
the drift this phase fixes; SYSTEM-MAP.md replaces them with one map
whose numbers come from the evidence file. When the parent deploys Phase
2, a one-line supersession note should be added to each INTEGRATION.md
(or they should be deleted in a single, separately-approved cleanup) —
that step is in the deployment manifest as a follow-up, not done here.

## Pointer candidate (not actioned in this phase)

`equity-research-playbook`'s four templates are byte-identical to the
agent pack's `templates/` (diff-verified in Phase 1). The playbook is a
candidate to become a **pointer/satellite** (its README pointing at the
pack's templates, with any playbook-only content kept) rather than a
second copy. This is a content decision for a later step: it is recorded
here, not executed here, because deleting or gutting a live repo's
content needs its own approval and a redirect plan for its links.

## What this phase deliberately does NOT do

- No monorepo migration, no repo moves/merges/renames, no history
  rewriting, no visibility changes, no deletions.
- No work on `shirjankhadka.github.io` — separate Nepse Decode project, out of scope, untouched.
- No access to the private Nepse Decode project/repo, in any form.
- No Cloudflare, domain, or email actions (blockers, see `ops/BLOCKERS.md`).
- No scheduled autonomous run with public output (Phase 3/4 work; the
  toolkit's autonomous runner exists as code + a cron example only).
- No live NEPSE feed (no documented free public API verified; the
  licensed feed is paid and not started — owner's funding decision only).
- No de-duplication of the playbook templates (see pointer candidate).
