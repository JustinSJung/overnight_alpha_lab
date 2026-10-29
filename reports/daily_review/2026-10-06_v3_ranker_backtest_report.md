# V3 Ranker Backtest Report - 2026-10-06

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **96.47%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **9090**
- Overall success rate: **46.60%**
- Current selected group success rate: **45.88%**
- Simulated v3 Top 10 success rate: **44.98%**
- Simulated v3 Top 20 success rate: **48.25%**
- Simulated v3 Top 50 success rate: **45.20%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **41.29%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 209 | 94 | 115 | 44.98% | -0.04% | -0.73% | 37.58% |
| Top 20 | 342 | 165 | 177 | 48.25% | 0.37% | -0.40% | 41.29% |
| Top 50 | 666 | 301 | 365 | 45.20% | 0.39% | -0.37% | 40.71% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.