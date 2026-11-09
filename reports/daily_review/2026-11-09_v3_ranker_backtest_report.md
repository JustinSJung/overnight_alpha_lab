# V3 Ranker Backtest Report - 2026-11-09

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.19%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **19799**
- Overall success rate: **50.95%**
- Current selected group success rate: **44.81%**
- Simulated v3 Top 10 success rate: **45.48%**
- Simulated v3 Top 20 success rate: **47.01%**
- Simulated v3 Top 50 success rate: **43.78%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **57.97%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 310 | 141 | 169 | 45.48% | 0.04% | 0.69% | 58.18% |
| Top 20 | 502 | 236 | 266 | 47.01% | 0.31% | 1.00% | 57.97% |
| Top 50 | 948 | 415 | 533 | 43.78% | 0.23% | 1.10% | 59.80% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.