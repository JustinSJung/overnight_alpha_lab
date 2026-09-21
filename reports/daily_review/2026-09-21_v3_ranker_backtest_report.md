# V3 Ranker Backtest Report - 2026-09-21

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **95.17%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **6523**
- Overall success rate: **45.79%**
- Current selected group success rate: **44.48%**
- Simulated v3 Top 10 success rate: **45.45%**
- Simulated v3 Top 20 success rate: **47.46%**
- Simulated v3 Top 50 success rate: **44.28%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **50.56%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 176 | 80 | 96 | 45.45% | 0.08% | 0.05% | 46.78% |
| Top 20 | 276 | 131 | 145 | 47.46% | 0.40% | 0.41% | 50.56% |
| Top 50 | 533 | 236 | 297 | 44.28% | 0.35% | 0.07% | 46.71% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.