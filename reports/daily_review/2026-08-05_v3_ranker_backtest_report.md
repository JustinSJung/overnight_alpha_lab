# V3 Ranker Backtest Report - 2026-08-05

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **71.45%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **6258**
- Overall success rate: **44.73%**
- Current selected group success rate: **50.00%**
- Simulated v3 Top 10 success rate: **46.94%**
- Simulated v3 Top 20 success rate: **40.23%**
- Simulated v3 Top 50 success rate: **37.04%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **57.69%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 49 | 23 | 26 | 46.94% | 0.83% | 0.05% | 62.16% |
| Top 20 | 87 | 35 | 52 | 40.23% | 0.77% | -0.09% | 57.69% |
| Top 50 | 135 | 50 | 85 | 37.04% | 0.23% | 1.60% | 70.00% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.