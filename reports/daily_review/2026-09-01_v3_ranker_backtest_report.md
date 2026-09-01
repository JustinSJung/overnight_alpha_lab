# V3 Ranker Backtest Report - 2026-09-01

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **90.68%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **3136**
- Overall success rate: **42.32%**
- Current selected group success rate: **45.92%**
- Simulated v3 Top 10 success rate: **44.72%**
- Simulated v3 Top 20 success rate: **46.70%**
- Simulated v3 Top 50 success rate: **42.60%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **47.21%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 123 | 55 | 68 | 44.72% | 0.32% | 0.32% | 46.34% |
| Top 20 | 197 | 92 | 105 | 46.70% | 0.48% | 0.47% | 47.21% |
| Top 50 | 392 | 167 | 225 | 42.60% | 0.54% | 0.07% | 43.88% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.