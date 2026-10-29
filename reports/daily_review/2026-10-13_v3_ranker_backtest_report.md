# V3 Ranker Backtest Report - 2026-10-13

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **96.97%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **10233**
- Overall success rate: **48.82%**
- Current selected group success rate: **44.44%**
- Simulated v3 Top 10 success rate: **44.44%**
- Simulated v3 Top 20 success rate: **46.61%**
- Simulated v3 Top 50 success rate: **42.88%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **51.78%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 234 | 104 | 130 | 44.44% | -0.19% | -0.04% | 48.05% |
| Top 20 | 384 | 179 | 205 | 46.61% | 0.11% | 0.18% | 51.78% |
| Top 50 | 744 | 319 | 425 | 42.88% | 0.13% | 0.35% | 51.57% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.