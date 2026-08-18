# V3 Ranker Backtest Report - 2026-08-18

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **87.50%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **25172**
- Overall success rate: **41.36%**
- Current selected group success rate: **52.79%**
- Simulated v3 Top 10 success rate: **48.00%**
- Simulated v3 Top 20 success rate: **44.49%**
- Simulated v3 Top 50 success rate: **44.88%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **41.63%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 125 | 60 | 65 | 48.00% | 0.55% | -0.32% | 44.25% |
| Top 20 | 245 | 109 | 136 | 44.49% | 0.41% | -0.60% | 41.63% |
| Top 50 | 508 | 228 | 280 | 44.88% | 0.66% | -0.51% | 46.82% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.