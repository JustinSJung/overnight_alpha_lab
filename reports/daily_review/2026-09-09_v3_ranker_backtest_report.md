# V3 Ranker Backtest Report - 2026-09-09

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **93.03%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **4361**
- Overall success rate: **43.66%**
- Current selected group success rate: **45.80%**
- Simulated v3 Top 10 success rate: **44.83%**
- Simulated v3 Top 20 success rate: **46.72%**
- Simulated v3 Top 50 success rate: **43.61%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **48.47%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 145 | 65 | 80 | 44.83% | 0.30% | 0.20% | 45.52% |
| Top 20 | 229 | 107 | 122 | 46.72% | 0.49% | 0.42% | 48.47% |
| Top 50 | 454 | 198 | 256 | 43.61% | 0.49% | 0.13% | 44.71% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.