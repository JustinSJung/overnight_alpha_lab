# V3 Ranker Backtest Report - 2026-10-20

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **97.43%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **12914**
- Overall success rate: **48.30%**
- Current selected group success rate: **44.47%**
- Simulated v3 Top 10 success rate: **44.18%**
- Simulated v3 Top 20 success rate: **47.56%**
- Simulated v3 Top 50 success rate: **43.48%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **56.55%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 249 | 110 | 139 | 44.18% | -0.00% | 0.54% | 53.09% |
| Top 20 | 410 | 195 | 215 | 47.56% | 0.33% | 0.83% | 56.55% |
| Top 50 | 775 | 337 | 438 | 43.48% | 0.31% | 0.75% | 54.56% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.