# V3 Ranker Backtest Report - 2026-10-19

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **97.35%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **12657**
- Overall success rate: **48.17%**
- Current selected group success rate: **44.19%**
- Simulated v3 Top 10 success rate: **43.36%**
- Simulated v3 Top 20 success rate: **45.58%**
- Simulated v3 Top 50 success rate: **42.45%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **57.09%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 256 | 111 | 145 | 43.36% | -0.04% | 0.73% | 55.62% |
| Top 20 | 419 | 191 | 228 | 45.58% | 0.23% | 0.92% | 57.09% |
| Top 50 | 801 | 340 | 461 | 42.45% | 0.20% | 0.81% | 55.06% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.