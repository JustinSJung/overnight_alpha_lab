# V3 Ranker Backtest Report - 2026-09-14

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **94.09%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **5132**
- Overall success rate: **45.97%**
- Current selected group success rate: **44.84%**
- Simulated v3 Top 10 success rate: **46.58%**
- Simulated v3 Top 20 success rate: **48.41%**
- Simulated v3 Top 50 success rate: **43.44%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **52.38%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 161 | 75 | 86 | 46.58% | 0.26% | 0.34% | 49.07% |
| Top 20 | 252 | 122 | 130 | 48.41% | 0.53% | 0.67% | 52.38% |
| Top 50 | 488 | 212 | 276 | 43.44% | 0.44% | 0.22% | 47.75% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.