# V3 Ranker Backtest Report - 2026-08-24

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **89.99%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **35425**
- Overall success rate: **41.32%**
- Current selected group success rate: **50.65%**
- Simulated v3 Top 10 success rate: **47.14%**
- Simulated v3 Top 20 success rate: **45.00%**
- Simulated v3 Top 50 success rate: **41.53%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **40.97%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 140 | 66 | 74 | 47.14% | 0.56% | -0.30% | 42.97% |
| Top 20 | 300 | 135 | 165 | 45.00% | 0.03% | -0.83% | 40.97% |
| Top 50 | 655 | 272 | 383 | 41.53% | -0.09% | -1.11% | 40.00% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.