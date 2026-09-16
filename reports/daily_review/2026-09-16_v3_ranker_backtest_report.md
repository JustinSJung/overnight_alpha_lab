# V3 Ranker Backtest Report - 2026-09-16

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **94.67%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **5779**
- Overall success rate: **46.91%**
- Current selected group success rate: **44.44%**
- Simulated v3 Top 10 success rate: **45.96%**
- Simulated v3 Top 20 success rate: **47.29%**
- Simulated v3 Top 50 success rate: **43.51%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **52.33%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 161 | 74 | 87 | 45.96% | 0.22% | 0.33% | 49.69% |
| Top 20 | 258 | 122 | 136 | 47.29% | 0.50% | 0.62% | 52.33% |
| Top 50 | 501 | 218 | 283 | 43.51% | 0.43% | 0.30% | 47.90% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.