# V3 Ranker Backtest Report - 2026-09-11

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **93.76%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **4912**
- Overall success rate: **45.05%**
- Current selected group success rate: **45.63%**
- Simulated v3 Top 10 success rate: **46.10%**
- Simulated v3 Top 20 success rate: **47.74%**
- Simulated v3 Top 50 success rate: **43.46%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **50.21%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 154 | 71 | 83 | 46.10% | 0.22% | 0.18% | 46.75% |
| Top 20 | 243 | 116 | 127 | 47.74% | 0.49% | 0.51% | 50.21% |
| Top 50 | 474 | 206 | 268 | 43.46% | 0.47% | 0.19% | 45.99% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.