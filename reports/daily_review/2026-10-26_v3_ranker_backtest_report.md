# V3 Ranker Backtest Report - 2026-10-26

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **97.72%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **15178**
- Overall success rate: **50.15%**
- Current selected group success rate: **43.41%**
- Simulated v3 Top 10 success rate: **43.32%**
- Simulated v3 Top 20 success rate: **46.12%**
- Simulated v3 Top 50 success rate: **43.27%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **57.45%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 277 | 120 | 157 | 43.32% | -0.08% | 0.32% | 55.03% |
| Top 20 | 451 | 208 | 243 | 46.12% | 0.22% | 0.65% | 57.45% |
| Top 50 | 855 | 370 | 485 | 43.27% | 0.19% | 0.68% | 56.91% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.