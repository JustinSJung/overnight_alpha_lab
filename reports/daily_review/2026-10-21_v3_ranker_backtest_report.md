# V3 Ranker Backtest Report - 2026-10-21

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **97.51%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **13766**
- Overall success rate: **47.95%**
- Current selected group success rate: **45.03%**
- Simulated v3 Top 10 success rate: **44.06%**
- Simulated v3 Top 20 success rate: **47.33%**
- Simulated v3 Top 50 success rate: **44.29%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **55.15%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 261 | 115 | 146 | 44.06% | -0.07% | 0.40% | 52.12% |
| Top 20 | 431 | 204 | 227 | 47.33% | 0.26% | 0.72% | 55.15% |
| Top 50 | 815 | 361 | 454 | 44.29% | 0.25% | 0.67% | 54.13% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.