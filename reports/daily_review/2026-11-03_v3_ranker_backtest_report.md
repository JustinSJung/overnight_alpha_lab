# V3 Ranker Backtest Report - 2026-11-03

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **97.97%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **17271**
- Overall success rate: **48.22%**
- Current selected group success rate: **44.41%**
- Simulated v3 Top 10 success rate: **42.96%**
- Simulated v3 Top 20 success rate: **45.21%**
- Simulated v3 Top 50 success rate: **42.16%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **51.24%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 277 | 119 | 158 | 42.96% | -0.20% | -0.10% | 47.62% |
| Top 20 | 449 | 203 | 246 | 45.21% | 0.14% | 0.36% | 51.24% |
| Top 50 | 842 | 355 | 487 | 42.16% | 0.16% | 0.52% | 54.97% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.