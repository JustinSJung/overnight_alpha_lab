# V3 Ranker Backtest Report - 2026-08-28

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **91.38%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **44897**
- Overall success rate: **41.28%**
- Current selected group success rate: **49.74%**
- Simulated v3 Top 10 success rate: **44.05%**
- Simulated v3 Top 20 success rate: **47.26%**
- Simulated v3 Top 50 success rate: **43.99%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **40.82%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 168 | 74 | 94 | 44.05% | 0.12% | -0.57% | 41.03% |
| Top 20 | 328 | 155 | 173 | 47.26% | 0.25% | -0.64% | 40.82% |
| Top 50 | 757 | 333 | 424 | 43.99% | 0.17% | -0.87% | 41.02% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.