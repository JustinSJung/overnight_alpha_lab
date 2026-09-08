# V3 Ranker Backtest Report - 2026-09-08

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **92.62%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **4062**
- Overall success rate: **43.06%**
- Current selected group success rate: **45.08%**
- Simulated v3 Top 10 success rate: **44.53%**
- Simulated v3 Top 20 success rate: **45.45%**
- Simulated v3 Top 50 success rate: **41.88%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **47.73%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 137 | 61 | 76 | 44.53% | 0.21% | 0.20% | 46.72% |
| Top 20 | 220 | 100 | 120 | 45.45% | 0.40% | 0.37% | 47.73% |
| Top 50 | 437 | 183 | 254 | 41.88% | 0.49% | 0.04% | 44.16% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.