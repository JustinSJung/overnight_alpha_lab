# V3 Ranker Backtest Report - 2026-11-16

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.41%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **23486**
- Overall success rate: **49.47%**
- Current selected group success rate: **43.67%**
- Simulated v3 Top 10 success rate: **45.51%**
- Simulated v3 Top 20 success rate: **46.53%**
- Simulated v3 Top 50 success rate: **43.88%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **50.80%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 356 | 162 | 194 | 45.51% | 0.06% | 0.26% | 51.87% |
| Top 20 | 576 | 268 | 308 | 46.53% | 0.22% | 0.37% | 50.80% |
| Top 50 | 1087 | 477 | 610 | 43.88% | 0.18% | 0.51% | 53.86% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.