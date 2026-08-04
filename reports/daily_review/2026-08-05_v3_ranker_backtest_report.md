# V3 Ranker Backtest Report - 2026-08-05

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **68.06%**
- Data status: **partial historical component coverage**
- Overall evaluated cases: **5053**
- Overall success rate: **45.91%**
- Current selected group success rate: **49.02%**
- Simulated v3 Top 10 success rate: **43.59%**
- Simulated v3 Top 20 success rate: **40.54%**
- Simulated v3 Top 50 success rate: **35.14%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **60.53%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 39 | 17 | 22 | 43.59% | 0.72% | -0.29% | 57.69% |
| Top 20 | 74 | 30 | 44 | 40.54% | 0.93% | 0.14% | 60.53% |
| Top 50 | 111 | 39 | 72 | 35.14% | 0.14% | 1.48% | 66.67% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.