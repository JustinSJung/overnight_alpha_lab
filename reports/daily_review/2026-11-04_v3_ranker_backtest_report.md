# V3 Ranker Backtest Report - 2026-11-04

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.03%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **17948**
- Overall success rate: **49.26%**
- Current selected group success rate: **44.25%**
- Simulated v3 Top 10 success rate: **44.26%**
- Simulated v3 Top 20 success rate: **46.11%**
- Simulated v3 Top 50 success rate: **42.79%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **54.23%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 296 | 131 | 165 | 44.26% | -0.09% | 0.23% | 51.57% |
| Top 20 | 475 | 219 | 256 | 46.11% | 0.18% | 0.56% | 54.23% |
| Top 50 | 881 | 377 | 504 | 42.79% | 0.15% | 0.63% | 56.21% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.