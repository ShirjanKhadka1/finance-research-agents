# Prediction Accuracy Loop — runbook

Data (fresh, fallback chain, freshness gate) → Predictive auto-selection
(walk-forward MAE) → Record prediction to ledger (before outcome known)
→ Autonomous update writes report + archive entry → Next run scores
pending predictions against the actual close → Accuracy Auditor reviews
failures, demotes failing models, updates weights → Next selection uses
the new weights.

One loop, every run, no exceptions. A prediction that is never scored
is not a track record; a failure that is never logged is not learning.
