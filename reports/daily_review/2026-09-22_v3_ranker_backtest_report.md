# V3 Ranker Backtest Report - 2026-09-22

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **95.40%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **6806**
- Overall success rate: **45.86%**
- Current selected group success rate: **45.00%**
- Simulated v3 Top 10 success rate: **47.22%**
- Simulated v3 Top 20 success rate: **48.41%**
- Simulated v3 Top 50 success rate: **44.81%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **50.18%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 180 | 85 | 95 | 47.22% | 0.42% | 0.30% | 46.51% |
| Top 20 | 283 | 137 | 146 | 48.41% | 0.60% | 0.40% | 50.18% |
| Top 50 | 540 | 242 | 298 | 44.81% | 0.43% | -0.04% | 45.89% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.