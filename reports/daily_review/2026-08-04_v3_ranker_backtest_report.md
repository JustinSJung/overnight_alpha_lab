# V3 Ranker Backtest Report - 2026-08-04

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **71.43%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **6243**
- Overall success rate: **44.74%**
- Current selected group success rate: **49.87%**
- Simulated v3 Top 10 success rate: **45.65%**
- Simulated v3 Top 20 success rate: **39.29%**
- Simulated v3 Top 50 success rate: **36.36%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **59.18%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 46 | 21 | 25 | 45.65% | 0.78% | 0.40% | 64.71% |
| Top 20 | 84 | 33 | 51 | 39.29% | 0.74% | 0.15% | 59.18% |
| Top 50 | 132 | 48 | 84 | 36.36% | 0.20% | 1.79% | 71.26% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.