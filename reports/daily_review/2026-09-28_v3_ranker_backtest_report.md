# V3 Ranker Backtest Report - 2026-09-28

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **95.80%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **7661**
- Overall success rate: **45.93%**
- Current selected group success rate: **45.62%**
- Simulated v3 Top 10 success rate: **45.50%**
- Simulated v3 Top 20 success rate: **47.16%**
- Simulated v3 Top 50 success rate: **44.44%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **47.19%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 189 | 86 | 103 | 45.50% | 0.02% | -0.49% | 42.26% |
| Top 20 | 299 | 141 | 158 | 47.16% | 0.34% | -0.10% | 47.19% |
| Top 50 | 585 | 260 | 325 | 44.44% | 0.39% | -0.29% | 45.11% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.