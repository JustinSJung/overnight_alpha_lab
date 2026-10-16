# V3 Ranker Backtest Report - 2026-10-16

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **97.26%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **11816**
- Overall success rate: **48.10%**
- Current selected group success rate: **44.98%**
- Simulated v3 Top 10 success rate: **44.03%**
- Simulated v3 Top 20 success rate: **47.31%**
- Simulated v3 Top 50 success rate: **43.29%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **56.15%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 243 | 107 | 136 | 44.03% | -0.05% | 0.61% | 53.99% |
| Top 20 | 391 | 185 | 206 | 47.31% | 0.25% | 0.82% | 56.15% |
| Top 50 | 753 | 326 | 427 | 43.29% | 0.20% | 0.81% | 53.59% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.