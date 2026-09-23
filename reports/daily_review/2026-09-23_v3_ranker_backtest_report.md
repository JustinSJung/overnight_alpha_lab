# V3 Ranker Backtest Report - 2026-09-23

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **95.61%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **7060**
- Overall success rate: **46.60%**
- Current selected group success rate: **44.98%**
- Simulated v3 Top 10 success rate: **45.65%**
- Simulated v3 Top 20 success rate: **47.75%**
- Simulated v3 Top 50 success rate: **44.85%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **49.45%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 184 | 84 | 100 | 45.65% | 0.10% | -0.04% | 45.35% |
| Top 20 | 289 | 138 | 151 | 47.75% | 0.39% | 0.26% | 49.45% |
| Top 50 | 553 | 248 | 305 | 44.85% | 0.32% | -0.07% | 46.61% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.