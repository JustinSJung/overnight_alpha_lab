# V3 Ranker Backtest Report - 2026-08-11

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **82.64%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **15068**
- Overall success rate: **42.16%**
- Current selected group success rate: **54.00%**
- Simulated v3 Top 10 success rate: **49.45%**
- Simulated v3 Top 20 success rate: **51.28%**
- Simulated v3 Top 50 success rate: **48.68%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **54.07%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 91 | 45 | 46 | 49.45% | 0.72% | 0.32% | 55.70% |
| Top 20 | 156 | 80 | 76 | 51.28% | 0.93% | -0.16% | 54.07% |
| Top 50 | 304 | 148 | 156 | 48.68% | 1.09% | 0.15% | 55.26% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.