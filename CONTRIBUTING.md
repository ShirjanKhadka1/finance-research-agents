# Contributing

Thank you for contributing. Keep changes small, sourced, and checkable.

## Tests

This repo has no automated test suite: it is Markdown, templates, and
research notes. Before submitting, re-read the changed file end to end
and check every number, link, and cross-reference in it.

## Proposing a Markdown change

1. Open an issue first for anything bigger than a typo, or comment on
   an existing issue asking to be picked up.
2. Fork, branch `docs/issue-<number>-<slug>` for docs or
   `fix/issue-<number>-<slug>` for a fix, and make the smallest change
   that does the job.
3. For a new template or checklist item, follow the format of the
   existing templates in the repo and keep the standard sections intact
   — if a section does not apply, write why, rather than deleting it.
4. Cite a source for every new number, with its period, on the same page.
   Unsourced numbers will not be merged, however plausible they look.

## Checking an agent change

Run the install script in dry-run mode before submitting:

```bash
./scripts/install.sh --tool claude-code --dry-run
```

If you add or rename an agent, update `agents.json` and the roster table
in `README.md` in the same change, so the roster and the files never drift.

## House rules (all contributions)

- Research and education only: never investment advice, never a buy/sell/
  hold recommendation, never guaranteed returns.
- Every number sourced with its period, or labelled UNKNOWN / TO VERIFY.
- No fake metrics, no invented features, no live NEPSE feed claim.
- No credentials anywhere. No paywalled scraping.
