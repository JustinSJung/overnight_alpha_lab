# V3 Ranker Backtest Report - 2026-08-29

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **89.64%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **2913**
- Overall success rate: **41.16%**
- Current selected group success rate: **47.31%**
- Simulated v3 Top 10 success rate: **45.05%**
- Simulated v3 Top 20 success rate: **47.22%**
- Simulated v3 Top 50 success rate: **43.24%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **46.11%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 111 | 50 | 61 | 45.05% | 0.37% | 0.14% | 45.05% |
| Top 20 | 180 | 85 | 95 | 47.22% | 0.56% | 0.31% | 46.11% |
| Top 50 | 370 | 160 | 210 | 43.24% | 0.63% | 0.01% | 43.51% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.