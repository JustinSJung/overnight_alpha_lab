# V3 Ranker Backtest Report - 2026-11-05

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.09%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **18668**
- Overall success rate: **48.79%**
- Current selected group success rate: **43.85%**
- Simulated v3 Top 10 success rate: **45.05%**
- Simulated v3 Top 20 success rate: **46.43%**
- Simulated v3 Top 50 success rate: **43.14%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **53.96%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 293 | 132 | 161 | 45.05% | 0.03% | 0.28% | 50.93% |
| Top 20 | 476 | 221 | 255 | 46.43% | 0.28% | 0.64% | 53.96% |
| Top 50 | 897 | 387 | 510 | 43.14% | 0.22% | 0.63% | 54.81% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.