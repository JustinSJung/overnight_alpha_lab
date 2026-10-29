# V3 Ranker Backtest Report - 2026-10-27

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **97.79%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **15903**
- Overall success rate: **49.43%**
- Current selected group success rate: **43.95%**
- Simulated v3 Top 10 success rate: **43.77%**
- Simulated v3 Top 20 success rate: **45.92%**
- Simulated v3 Top 50 success rate: **43.65%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **54.78%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 281 | 123 | 158 | 43.77% | -0.19% | 0.07% | 50.89% |
| Top 20 | 453 | 208 | 245 | 45.92% | 0.11% | 0.44% | 54.78% |
| Top 50 | 843 | 368 | 475 | 43.65% | 0.15% | 0.59% | 55.90% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.