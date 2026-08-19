# V3 Ranker Backtest Report - 2026-08-19

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **88.21%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **27525**
- Overall success rate: **41.29%**
- Current selected group success rate: **52.10%**
- Simulated v3 Top 10 success rate: **48.44%**
- Simulated v3 Top 20 success rate: **43.36%**
- Simulated v3 Top 50 success rate: **43.66%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **40.98%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 128 | 62 | 66 | 48.44% | 0.49% | -0.35% | 44.83% |
| Top 20 | 256 | 111 | 145 | 43.36% | 0.34% | -0.61% | 40.98% |
| Top 50 | 552 | 241 | 311 | 43.66% | 0.36% | -0.70% | 45.74% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.