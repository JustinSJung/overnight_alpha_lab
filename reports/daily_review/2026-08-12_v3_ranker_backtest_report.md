# V3 Ranker Backtest Report - 2026-08-12

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **83.83%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **16902**
- Overall success rate: **41.97%**
- Current selected group success rate: **54.14%**
- Simulated v3 Top 10 success rate: **48.51%**
- Simulated v3 Top 20 success rate: **50.57%**
- Simulated v3 Top 50 success rate: **46.48%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **51.27%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 101 | 49 | 52 | 48.51% | 0.54% | 0.11% | 51.69% |
| Top 20 | 176 | 89 | 87 | 50.57% | 0.88% | -0.28% | 51.27% |
| Top 50 | 355 | 165 | 190 | 46.48% | 0.90% | -0.17% | 51.10% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.