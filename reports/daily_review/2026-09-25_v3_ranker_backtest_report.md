# V3 Ranker Backtest Report - 2026-09-25

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **95.61%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **7320**
- Overall success rate: **46.19%**
- Current selected group success rate: **45.00%**
- Simulated v3 Top 10 success rate: **45.21%**
- Simulated v3 Top 20 success rate: **47.12%**
- Simulated v3 Top 50 success rate: **44.15%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **48.91%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 188 | 85 | 103 | 45.21% | 0.03% | -0.15% | 44.89% |
| Top 20 | 295 | 139 | 156 | 47.12% | 0.35% | 0.19% | 48.91% |
| Top 50 | 573 | 253 | 320 | 44.15% | 0.37% | -0.06% | 45.47% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.