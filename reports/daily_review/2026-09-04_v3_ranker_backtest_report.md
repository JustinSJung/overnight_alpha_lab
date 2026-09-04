# V3 Ranker Backtest Report - 2026-09-04

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **92.15%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **3781**
- Overall success rate: **42.71%**
- Current selected group success rate: **45.86%**
- Simulated v3 Top 10 success rate: **44.53%**
- Simulated v3 Top 20 success rate: **46.08%**
- Simulated v3 Top 50 success rate: **42.39%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **48.85%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 137 | 61 | 76 | 44.53% | 0.29% | 0.27% | 47.45% |
| Top 20 | 217 | 100 | 117 | 46.08% | 0.47% | 0.45% | 48.85% |
| Top 50 | 427 | 181 | 246 | 42.39% | 0.52% | 0.15% | 44.96% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.