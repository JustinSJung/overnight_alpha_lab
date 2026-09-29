# V3 Ranker Backtest Report - 2026-09-29

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **95.98%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **7692**
- Overall success rate: **47.11%**
- Current selected group success rate: **45.20%**
- Simulated v3 Top 10 success rate: **45.41%**
- Simulated v3 Top 20 success rate: **47.32%**
- Simulated v3 Top 50 success rate: **44.31%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **47.15%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 185 | 84 | 101 | 45.41% | 0.14% | -0.15% | 41.72% |
| Top 20 | 298 | 141 | 157 | 47.32% | 0.40% | 0.22% | 47.15% |
| Top 50 | 589 | 261 | 328 | 44.31% | 0.42% | 0.18% | 44.13% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.