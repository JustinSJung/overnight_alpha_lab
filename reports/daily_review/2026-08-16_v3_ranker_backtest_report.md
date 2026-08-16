# V3 Ranker Backtest Report - 2026-08-16

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **85.85%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **20885**
- Overall success rate: **41.64%**
- Current selected group success rate: **53.75%**
- Simulated v3 Top 10 success rate: **45.38%**
- Simulated v3 Top 20 success rate: **46.08%**
- Simulated v3 Top 50 success rate: **46.12%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **43.14%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 119 | 54 | 65 | 45.38% | 0.54% | -0.26% | 42.99% |
| Top 20 | 217 | 100 | 117 | 46.08% | 0.41% | -0.74% | 43.14% |
| Top 50 | 451 | 208 | 243 | 46.12% | 0.80% | -0.39% | 46.27% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.