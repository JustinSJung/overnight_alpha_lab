# V3 Ranker Backtest Report - 2026-11-10

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.24%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **20437**
- Overall success rate: **50.91%**
- Current selected group success rate: **43.94%**
- Simulated v3 Top 10 success rate: **44.20%**
- Simulated v3 Top 20 success rate: **45.37%**
- Simulated v3 Top 50 success rate: **42.80%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **56.27%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 319 | 141 | 178 | 44.20% | -0.05% | 0.61% | 56.63% |
| Top 20 | 518 | 235 | 283 | 45.37% | 0.20% | 0.92% | 56.27% |
| Top 50 | 979 | 419 | 560 | 42.80% | 0.17% | 1.03% | 58.33% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.