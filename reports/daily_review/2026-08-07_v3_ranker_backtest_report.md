# V3 Ranker Backtest Report - 2026-08-07

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **78.11%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **10307**
- Overall success rate: **42.82%**
- Current selected group success rate: **51.64%**
- Simulated v3 Top 10 success rate: **40.62%**
- Simulated v3 Top 20 success rate: **43.59%**
- Simulated v3 Top 50 success rate: **42.11%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **57.95%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 64 | 26 | 38 | 40.62% | 0.61% | 0.68% | 61.54% |
| Top 20 | 117 | 51 | 66 | 43.59% | 0.75% | 0.45% | 57.95% |
| Top 50 | 228 | 96 | 132 | 42.11% | 0.49% | 1.03% | 64.67% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.