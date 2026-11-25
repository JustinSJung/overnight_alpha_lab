# V3 Ranker Backtest Report - 2026-11-25

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.65%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **27593**
- Overall success rate: **50.37%**
- Current selected group success rate: **43.06%**
- Simulated v3 Top 10 success rate: **43.32%**
- Simulated v3 Top 20 success rate: **44.13%**
- Simulated v3 Top 50 success rate: **42.87%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **52.30%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 404 | 175 | 229 | 43.32% | -0.20% | 0.45% | 55.56% |
| Top 20 | 664 | 293 | 371 | 44.13% | -0.08% | 0.36% | 52.30% |
| Top 50 | 1234 | 529 | 705 | 42.87% | -0.07% | 0.37% | 53.93% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.