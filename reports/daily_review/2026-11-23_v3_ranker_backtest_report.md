# V3 Ranker Backtest Report - 2026-11-23

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.59%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **25953**
- Overall success rate: **50.59%**
- Current selected group success rate: **43.26%**
- Simulated v3 Top 10 success rate: **43.83%**
- Simulated v3 Top 20 success rate: **44.77%**
- Simulated v3 Top 50 success rate: **42.98%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **53.22%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 381 | 167 | 214 | 43.83% | -0.17% | 0.58% | 56.19% |
| Top 20 | 621 | 278 | 343 | 44.77% | -0.07% | 0.52% | 53.22% |
| Top 50 | 1154 | 496 | 658 | 42.98% | -0.05% | 0.57% | 55.19% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.