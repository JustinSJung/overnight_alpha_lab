# V3 Ranker Backtest Report - 2026-10-02

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **96.32%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **8483**
- Overall success rate: **46.75%**
- Current selected group success rate: **45.87%**
- Simulated v3 Top 10 success rate: **45.54%**
- Simulated v3 Top 20 success rate: **47.71%**
- Simulated v3 Top 50 success rate: **44.76%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **45.77%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 202 | 92 | 110 | 45.54% | 0.02% | -0.54% | 40.23% |
| Top 20 | 327 | 156 | 171 | 47.71% | 0.38% | -0.10% | 45.77% |
| Top 50 | 630 | 282 | 348 | 44.76% | 0.44% | -0.14% | 43.05% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.