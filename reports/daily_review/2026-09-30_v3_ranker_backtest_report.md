# V3 Ranker Backtest Report - 2026-09-30

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **96.16%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **8076**
- Overall success rate: **46.48%**
- Current selected group success rate: **44.96%**
- Simulated v3 Top 10 success rate: **45.31%**
- Simulated v3 Top 20 success rate: **46.71%**
- Simulated v3 Top 50 success rate: **44.20%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **46.56%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 192 | 87 | 105 | 45.31% | 0.01% | -0.35% | 40.85% |
| Top 20 | 304 | 142 | 162 | 46.71% | 0.32% | 0.06% | 46.56% |
| Top 50 | 595 | 263 | 332 | 44.20% | 0.35% | 0.01% | 43.58% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.