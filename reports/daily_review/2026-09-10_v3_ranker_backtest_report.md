# V3 Ranker Backtest Report - 2026-09-10

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **93.41%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **4618**
- Overall success rate: **45.19%**
- Current selected group success rate: **44.53%**
- Simulated v3 Top 10 success rate: **43.84%**
- Simulated v3 Top 20 success rate: **46.32%**
- Simulated v3 Top 50 success rate: **42.64%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **48.92%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 146 | 64 | 82 | 43.84% | 0.20% | 0.27% | 45.89% |
| Top 20 | 231 | 107 | 124 | 46.32% | 0.45% | 0.50% | 48.92% |
| Top 50 | 462 | 197 | 265 | 42.64% | 0.45% | 0.11% | 45.67% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.