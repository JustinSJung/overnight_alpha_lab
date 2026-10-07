# V3 Ranker Backtest Report - 2026-10-07

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **96.61%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **9118**
- Overall success rate: **46.36%**
- Current selected group success rate: **45.80%**
- Simulated v3 Top 10 success rate: **44.39%**
- Simulated v3 Top 20 success rate: **46.78%**
- Simulated v3 Top 50 success rate: **43.84%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **42.91%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 205 | 91 | 114 | 44.39% | 0.05% | -0.52% | 38.41% |
| Top 20 | 342 | 160 | 182 | 46.78% | 0.38% | -0.25% | 42.91% |
| Top 50 | 657 | 288 | 369 | 43.84% | 0.50% | -0.14% | 42.66% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.