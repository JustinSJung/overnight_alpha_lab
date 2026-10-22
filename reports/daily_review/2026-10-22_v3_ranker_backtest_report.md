# V3 Ranker Backtest Report - 2026-10-22

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **97.58%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **14155**
- Overall success rate: **48.17%**
- Current selected group success rate: **43.83%**
- Simulated v3 Top 10 success rate: **44.15%**
- Simulated v3 Top 20 success rate: **46.77%**
- Simulated v3 Top 50 success rate: **43.08%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **56.00%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 265 | 117 | 148 | 44.15% | 0.04% | 0.42% | 53.57% |
| Top 20 | 434 | 203 | 231 | 46.77% | 0.31% | 0.71% | 56.00% |
| Top 50 | 824 | 355 | 469 | 43.08% | 0.22% | 0.67% | 55.01% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.