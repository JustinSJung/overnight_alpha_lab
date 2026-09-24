# V3 Ranker Backtest Report - 2026-09-24

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **95.61%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **7131**
- Overall success rate: **46.37%**
- Current selected group success rate: **45.52%**
- Simulated v3 Top 10 success rate: **44.57%**
- Simulated v3 Top 20 success rate: **47.57%**
- Simulated v3 Top 50 success rate: **44.70%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **49.44%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 184 | 82 | 102 | 44.57% | 0.17% | 0.00% | 44.77% |
| Top 20 | 288 | 137 | 151 | 47.57% | 0.47% | 0.33% | 49.44% |
| Top 50 | 557 | 249 | 308 | 44.70% | 0.43% | 0.04% | 45.83% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.