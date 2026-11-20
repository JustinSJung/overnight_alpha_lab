# V3 Ranker Backtest Report - 2026-11-20

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.56%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **25499**
- Overall success rate: **49.64%**
- Current selected group success rate: **44.16%**
- Simulated v3 Top 10 success rate: **44.59%**
- Simulated v3 Top 20 success rate: **44.62%**
- Simulated v3 Top 50 success rate: **43.23%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **52.17%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 388 | 173 | 215 | 44.59% | -0.07% | 0.42% | 54.79% |
| Top 20 | 632 | 282 | 350 | 44.62% | 0.06% | 0.41% | 52.17% |
| Top 50 | 1182 | 511 | 671 | 43.23% | 0.10% | 0.49% | 54.16% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.