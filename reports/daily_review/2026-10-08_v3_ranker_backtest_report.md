# V3 Ranker Backtest Report - 2026-10-08

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **96.74%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **9525**
- Overall success rate: **46.66%**
- Current selected group success rate: **44.77%**
- Simulated v3 Top 10 success rate: **45.00%**
- Simulated v3 Top 20 success rate: **46.85%**
- Simulated v3 Top 50 success rate: **43.72%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **44.64%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 220 | 99 | 121 | 45.00% | -0.08% | -0.45% | 41.24% |
| Top 20 | 365 | 171 | 194 | 46.85% | 0.26% | -0.18% | 44.64% |
| Top 50 | 709 | 310 | 399 | 43.72% | 0.29% | -0.17% | 43.92% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.