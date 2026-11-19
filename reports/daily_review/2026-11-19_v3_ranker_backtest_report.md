# V3 Ranker Backtest Report - 2026-11-19

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.52%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **25070**
- Overall success rate: **49.96%**
- Current selected group success rate: **43.15%**
- Simulated v3 Top 10 success rate: **44.39%**
- Simulated v3 Top 20 success rate: **44.41%**
- Simulated v3 Top 50 success rate: **42.37%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **53.43%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 383 | 170 | 213 | 44.39% | -0.05% | 0.50% | 55.56% |
| Top 20 | 626 | 278 | 348 | 44.41% | 0.07% | 0.48% | 53.43% |
| Top 50 | 1180 | 500 | 680 | 42.37% | 0.06% | 0.54% | 54.81% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.