# V3 Ranker Backtest Report - 2026-10-09

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **96.74%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **9399**
- Overall success rate: **46.70%**
- Current selected group success rate: **45.37%**
- Simulated v3 Top 10 success rate: **43.60%**
- Simulated v3 Top 20 success rate: **46.44%**
- Simulated v3 Top 50 success rate: **43.36%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **45.13%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 211 | 92 | 119 | 43.60% | -0.11% | -0.48% | 41.52% |
| Top 20 | 351 | 163 | 188 | 46.44% | 0.22% | -0.22% | 45.13% |
| Top 50 | 685 | 297 | 388 | 43.36% | 0.31% | -0.12% | 44.09% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.