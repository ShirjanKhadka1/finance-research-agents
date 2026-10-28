# Runbook: Portfolio & Forecast

**Team, in order:** Data → Portfolio → Performance → Forecast → Reality Checker
**Agent:** portfolio-forecast-analyst.md (this runbook is its workflow)

1. **Data:** toolkit/data.py — Yahoo (no key), World Bank (no key), or
   CSV (your own / NEPSE annual-report data, fiscal year labelled).
   Record source, period, currency, gaps. Offline? Use demo data, labelled DEMO.
2. **Portfolio:** toolkit/portfolio.py — shrunk covariance (alpha 0.1),
   L2 0.01, equal / inverse-vol / min-variance / max-Sharpe weights.
   Clean to long-only if requested. Frontier for targets asked for.
3. **Performance:** toolkit/performance.py — Sharpe, Sortino, max
   drawdown, CVaR 5%, Calmar, train vs test separately.
4. **Forecast:** toolkit/forecast.py — walk-forward, one step at a time,
   naive vs moving-average vs trend. MAE, RMSE, interval coverage,
   beats-naive. Winner = beats naive out of sample.
5. **Reality Checker:** number audit, lookahead audit, benchmark audit,
   advice audit. Pass / fix / send back.

Done when: weights sum to 1, benchmarks are beaten or honestly not
beaten, intervals are shown, and the Reality Checker verdict is Pass.
