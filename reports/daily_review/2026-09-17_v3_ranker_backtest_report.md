# V3 Ranker Backtest Report - 2026-09-17

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **94.93%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **6220**
- Overall success rate: **46.06%**
- Current selected group success rate: **44.30%**
- Simulated v3 Top 10 success rate: **46.47%**
- Simulated v3 Top 20 success rate: **47.57%**
- Simulated v3 Top 50 success rate: **43.62%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **49.81%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 170 | 79 | 91 | 46.47% | 0.23% | 0.28% | 47.06% |
| Top 20 | 267 | 127 | 140 | 47.57% | 0.46% | 0.50% | 49.81% |
| Top 50 | 525 | 229 | 296 | 43.62% | 0.39% | 0.13% | 46.10% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.