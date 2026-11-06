# V3 Ranker Backtest Report - 2026-11-06

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.14%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **18961**
- Overall success rate: **49.84%**
- Current selected group success rate: **44.83%**
- Simulated v3 Top 10 success rate: **45.45%**
- Simulated v3 Top 20 success rate: **46.03%**
- Simulated v3 Top 50 success rate: **43.33%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **54.71%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 297 | 135 | 162 | 45.45% | -0.04% | 0.49% | 53.57% |
| Top 20 | 478 | 220 | 258 | 46.03% | 0.17% | 0.70% | 54.71% |
| Top 50 | 900 | 390 | 510 | 43.33% | 0.16% | 0.77% | 56.57% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.