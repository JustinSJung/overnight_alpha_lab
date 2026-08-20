# V3 Ranker Backtest Report - 2026-08-20

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **88.86%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **30010**
- Overall success rate: **41.21%**
- Current selected group success rate: **51.61%**
- Simulated v3 Top 10 success rate: **48.87%**
- Simulated v3 Top 20 success rate: **43.70%**
- Simulated v3 Top 50 success rate: **42.64%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **40.31%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 133 | 65 | 68 | 48.87% | 0.26% | -0.76% | 42.98% |
| Top 20 | 270 | 118 | 152 | 43.70% | 0.17% | -0.72% | 40.31% |
| Top 50 | 591 | 252 | 339 | 42.64% | 0.25% | -0.87% | 43.60% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.