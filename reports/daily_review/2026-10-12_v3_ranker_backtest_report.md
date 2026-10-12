# V3 Ranker Backtest Report - 2026-10-12

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **96.86%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **10164**
- Overall success rate: **47.21%**
- Current selected group success rate: **45.13%**
- Simulated v3 Top 10 success rate: **44.54%**
- Simulated v3 Top 20 success rate: **46.42%**
- Simulated v3 Top 50 success rate: **43.38%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **50.59%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 229 | 102 | 127 | 44.54% | -0.05% | -0.18% | 46.50% |
| Top 20 | 377 | 175 | 202 | 46.42% | 0.21% | 0.03% | 50.59% |
| Top 50 | 740 | 321 | 419 | 43.38% | 0.27% | 0.22% | 49.49% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.