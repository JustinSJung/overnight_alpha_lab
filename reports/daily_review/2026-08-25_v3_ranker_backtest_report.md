# V3 Ranker Backtest Report - 2026-08-25

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **90.49%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **38430**
- Overall success rate: **41.30%**
- Current selected group success rate: **50.28%**
- Simulated v3 Top 10 success rate: **44.83%**
- Simulated v3 Top 20 success rate: **46.91%**
- Simulated v3 Top 50 success rate: **41.69%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **40.00%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 145 | 65 | 80 | 44.83% | 0.25% | -0.54% | 42.11% |
| Top 20 | 307 | 144 | 163 | 46.91% | 0.46% | -0.58% | 40.00% |
| Top 50 | 686 | 286 | 400 | 41.69% | -0.05% | -1.09% | 39.20% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.