# V3 Ranker Backtest Report - 2026-08-29

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **89.58%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **2985**
- Overall success rate: **41.37%**
- Current selected group success rate: **47.06%**
- Simulated v3 Top 10 success rate: **44.74%**
- Simulated v3 Top 20 success rate: **46.49%**
- Simulated v3 Top 50 success rate: **43.01%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **45.95%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 114 | 51 | 63 | 44.74% | 0.35% | 0.17% | 44.74% |
| Top 20 | 185 | 86 | 99 | 46.49% | 0.54% | 0.39% | 45.95% |
| Top 50 | 379 | 163 | 216 | 43.01% | 0.62% | 0.06% | 43.54% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.