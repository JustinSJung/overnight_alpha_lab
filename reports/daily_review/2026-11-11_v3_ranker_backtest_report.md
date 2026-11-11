# V3 Ranker Backtest Report - 2026-11-11

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.28%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **21227**
- Overall success rate: **49.96%**
- Current selected group success rate: **44.39%**
- Simulated v3 Top 10 success rate: **45.26%**
- Simulated v3 Top 20 success rate: **46.43%**
- Simulated v3 Top 50 success rate: **43.64%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **50.70%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 327 | 148 | 179 | 45.26% | -0.02% | 0.36% | 51.19% |
| Top 20 | 532 | 247 | 285 | 46.43% | 0.20% | 0.52% | 50.70% |
| Top 50 | 999 | 436 | 563 | 43.64% | 0.11% | 0.72% | 54.73% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.