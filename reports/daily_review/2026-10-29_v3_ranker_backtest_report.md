# V3 Ranker Backtest Report - 2026-10-29

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **97.86%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **16564**
- Overall success rate: **49.08%**
- Current selected group success rate: **44.09%**
- Simulated v3 Top 10 success rate: **43.77%**
- Simulated v3 Top 20 success rate: **46.34%**
- Simulated v3 Top 50 success rate: **43.71%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **54.37%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 281 | 123 | 158 | 43.77% | -0.12% | 0.06% | 50.30% |
| Top 20 | 451 | 209 | 242 | 46.34% | 0.19% | 0.49% | 54.37% |
| Top 50 | 842 | 368 | 474 | 43.71% | 0.21% | 0.64% | 55.58% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.