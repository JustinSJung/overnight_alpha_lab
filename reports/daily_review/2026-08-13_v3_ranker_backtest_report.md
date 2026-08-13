# V3 Ranker Backtest Report - 2026-08-13

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **84.90%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **18848**
- Overall success rate: **41.80%**
- Current selected group success rate: **54.01%**
- Simulated v3 Top 10 success rate: **45.95%**
- Simulated v3 Top 20 success rate: **50.25%**
- Simulated v3 Top 50 success rate: **46.80%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **48.35%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 111 | 51 | 60 | 45.95% | 0.58% | -0.07% | 46.46% |
| Top 20 | 197 | 99 | 98 | 50.25% | 0.89% | -0.28% | 48.35% |
| Top 50 | 406 | 190 | 216 | 46.80% | 0.81% | -0.35% | 47.57% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.