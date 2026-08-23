# V3 Ranker Backtest Report - 2026-08-23

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **89.45%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **32638**
- Overall success rate: **41.27%**
- Current selected group success rate: **51.08%**
- Simulated v3 Top 10 success rate: **47.79%**
- Simulated v3 Top 20 success rate: **43.62%**
- Simulated v3 Top 50 success rate: **41.64%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **40.37%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 136 | 65 | 71 | 47.79% | 0.41% | -0.52% | 42.74% |
| Top 20 | 282 | 123 | 159 | 43.62% | 0.02% | -0.86% | 40.37% |
| Top 50 | 622 | 259 | 363 | 41.64% | 0.06% | -1.00% | 41.64% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.