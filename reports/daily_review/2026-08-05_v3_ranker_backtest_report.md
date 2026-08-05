# V3 Ranker Backtest Report - 2026-08-05

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **73.97%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **7521**
- Overall success rate: **43.77%**
- Current selected group success rate: **50.76%**
- Simulated v3 Top 10 success rate: **42.00%**
- Simulated v3 Top 20 success rate: **39.18%**
- Simulated v3 Top 50 success rate: **39.02%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **53.85%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 50 | 21 | 29 | 42.00% | 0.70% | 0.44% | 60.53% |
| Top 20 | 97 | 38 | 59 | 39.18% | 0.56% | -0.08% | 53.85% |
| Top 50 | 164 | 64 | 100 | 39.02% | 0.22% | 1.59% | 68.91% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.