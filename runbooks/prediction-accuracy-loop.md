# Prediction Accuracy Loop — runbook

Data (fresh, fallback chain, freshness gate) → Predictive auto-selection
(walk-forward MAE) → Record prediction to ledger (before outcome known)
→ Autonomous update writes report + archive entry → Next run scores
pending predictions against the actual close → Accuracy Auditor reviews
failures, demotes failing models, updates weights → Next selection uses
the new weights.

One loop, every run, no exceptions. A prediction that is never scored
is not a track record; a failure that is never logged is not learning.

## Phase 10 steps (multi-horizon, intervals, drift)

After auto-selection, and before any prediction is recorded as a track
record, the loop now also runs, on the same walk-forward split:

1. **Multi-horizon check** — evaluate at h=1, h=3, h=5 (or the horizons
   the question actually needs). A model that wins at h=1 and collapses
   at h=5 is reported that way; horizon is part of every claim.
2. **Intervals, not points** — every recorded prediction carries a
   prediction interval from walk-forward residuals inside the training
   window, with its method (empirical vs normal-approx) and n stated.
   An interval is a statement about past residuals, never a guarantee.
3. **Drift flag** — split walk-forward errors into first/second half;
   if recent MAE >= 1.5x early MAE (each half n >= 3), flag drift in
   words in the accuracy report. A flagged model is NOT silently
   swapped out — the flag stays until a new evaluation clears it.
