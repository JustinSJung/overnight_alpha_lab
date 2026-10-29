# V3 Ranker Backtest Report - 2026-10-15

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **97.17%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **11255**
- Overall success rate: **49.97%**
- Current selected group success rate: **43.92%**
- Simulated v3 Top 10 success rate: **41.77%**
- Simulated v3 Top 20 success rate: **44.96%**
- Simulated v3 Top 50 success rate: **41.94%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **57.30%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 249 | 104 | 145 | 41.77% | -0.19% | 0.38% | 53.66% |
| Top 20 | 407 | 183 | 224 | 44.96% | 0.16% | 0.70% | 57.30% |
| Top 50 | 775 | 325 | 450 | 41.94% | 0.11% | 0.66% | 55.19% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.