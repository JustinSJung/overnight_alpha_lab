# V3 Ranker Backtest Report - 2026-08-06

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **76.17%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **8875**
- Overall success rate: **43.25%**
- Current selected group success rate: **51.57%**
- Simulated v3 Top 10 success rate: **39.66%**
- Simulated v3 Top 20 success rate: **39.81%**
- Simulated v3 Top 50 success rate: **40.41%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **53.25%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 58 | 23 | 35 | 39.66% | 0.65% | 0.46% | 60.87% |
| Top 20 | 108 | 43 | 65 | 39.81% | 0.39% | -0.21% | 53.25% |
| Top 50 | 193 | 78 | 115 | 40.41% | 0.17% | 1.06% | 64.86% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.