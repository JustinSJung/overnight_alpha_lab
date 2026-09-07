# V3 Ranker Backtest Report - 2026-09-07

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **92.18%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **3775**
- Overall success rate: **42.62%**
- Current selected group success rate: **45.43%**
- Simulated v3 Top 10 success rate: **45.59%**
- Simulated v3 Top 20 success rate: **46.51%**
- Simulated v3 Top 50 success rate: **42.45%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **49.30%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 136 | 62 | 74 | 45.59% | 0.25% | 0.21% | 47.79% |
| Top 20 | 215 | 100 | 115 | 46.51% | 0.44% | 0.39% | 49.30% |
| Top 50 | 424 | 180 | 244 | 42.45% | 0.47% | 0.08% | 44.58% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.