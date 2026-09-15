# V3 Ranker Backtest Report - 2026-09-15

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **94.39%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **5533**
- Overall success rate: **45.04%**
- Current selected group success rate: **43.01%**
- Simulated v3 Top 10 success rate: **45.73%**
- Simulated v3 Top 20 success rate: **47.06%**
- Simulated v3 Top 50 success rate: **42.66%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **51.76%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 164 | 75 | 89 | 45.73% | 0.21% | 0.27% | 48.17% |
| Top 20 | 255 | 120 | 135 | 47.06% | 0.46% | 0.63% | 51.76% |
| Top 50 | 497 | 212 | 285 | 42.66% | 0.31% | 0.12% | 46.68% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.