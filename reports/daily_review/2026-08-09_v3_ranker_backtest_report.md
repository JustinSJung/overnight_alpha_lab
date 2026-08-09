# V3 Ranker Backtest Report - 2026-08-09

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **79.81%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **11739**
- Overall success rate: **42.56%**
- Current selected group success rate: **52.17%**
- Simulated v3 Top 10 success rate: **42.25%**
- Simulated v3 Top 20 success rate: **45.16%**
- Simulated v3 Top 50 success rate: **43.32%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **59.79%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 71 | 30 | 41 | 42.25% | 0.57% | 0.86% | 62.71% |
| Top 20 | 124 | 56 | 68 | 45.16% | 0.90% | 0.62% | 59.79% |
| Top 50 | 247 | 107 | 140 | 43.32% | 0.64% | 0.62% | 60.59% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.