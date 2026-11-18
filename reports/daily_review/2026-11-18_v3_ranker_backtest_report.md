# V3 Ranker Backtest Report - 2026-11-18

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.49%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **24412**
- Overall success rate: **50.23%**
- Current selected group success rate: **43.47%**
- Simulated v3 Top 10 success rate: **44.71%**
- Simulated v3 Top 20 success rate: **45.19%**
- Simulated v3 Top 50 success rate: **43.13%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **54.44%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 378 | 169 | 209 | 44.71% | -0.06% | 0.60% | 56.72% |
| Top 20 | 613 | 277 | 336 | 45.19% | 0.10% | 0.63% | 54.44% |
| Top 50 | 1157 | 499 | 658 | 43.13% | 0.06% | 0.67% | 56.58% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.