# V3 Ranker Backtest Report - 2026-08-31

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **90.15%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **2997**
- Overall success rate: **41.71%**
- Current selected group success rate: **46.22%**
- Simulated v3 Top 10 success rate: **43.10%**
- Simulated v3 Top 20 success rate: **45.79%**
- Simulated v3 Top 50 success rate: **42.38%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **49.47%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 116 | 50 | 66 | 43.10% | 0.29% | 0.40% | 48.28% |
| Top 20 | 190 | 87 | 103 | 45.79% | 0.49% | 0.53% | 49.47% |
| Top 50 | 387 | 164 | 223 | 42.38% | 0.56% | 0.22% | 46.25% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.