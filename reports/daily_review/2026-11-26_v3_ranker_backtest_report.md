# V3 Ranker Backtest Report - 2026-11-26

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.68%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **28277**
- Overall success rate: **50.85%**
- Current selected group success rate: **43.83%**
- Simulated v3 Top 10 success rate: **43.45%**
- Simulated v3 Top 20 success rate: **44.59%**
- Simulated v3 Top 50 success rate: **43.18%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **53.37%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 412 | 179 | 233 | 43.45% | -0.14% | 0.62% | 57.08% |
| Top 20 | 675 | 301 | 374 | 44.59% | -0.01% | 0.52% | 53.37% |
| Top 50 | 1253 | 541 | 712 | 43.18% | -0.03% | 0.51% | 54.83% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.