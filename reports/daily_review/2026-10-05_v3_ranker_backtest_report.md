# V3 Ranker Backtest Report - 2026-10-05

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **96.32%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **8529**
- Overall success rate: **46.59%**
- Current selected group success rate: **45.21%**
- Simulated v3 Top 10 success rate: **45.73%**
- Simulated v3 Top 20 success rate: **48.29%**
- Simulated v3 Top 50 success rate: **44.62%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **45.14%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 199 | 91 | 108 | 45.73% | 0.01% | -0.59% | 40.62% |
| Top 20 | 321 | 155 | 166 | 48.29% | 0.29% | -0.22% | 45.14% |
| Top 50 | 623 | 278 | 345 | 44.62% | 0.37% | -0.26% | 42.08% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.