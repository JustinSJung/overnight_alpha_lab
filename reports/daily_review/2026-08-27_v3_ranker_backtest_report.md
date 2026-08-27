# V3 Ranker Backtest Report - 2026-08-27

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **90.95%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **41603**
- Overall success rate: **41.28%**
- Current selected group success rate: **49.99%**
- Simulated v3 Top 10 success rate: **44.87%**
- Simulated v3 Top 20 success rate: **48.12%**
- Simulated v3 Top 50 success rate: **42.80%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **40.58%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 156 | 70 | 86 | 44.87% | 0.19% | -0.56% | 41.67% |
| Top 20 | 320 | 154 | 166 | 48.12% | 0.58% | -0.36% | 40.58% |
| Top 50 | 729 | 312 | 417 | 42.80% | 0.09% | -0.96% | 39.51% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.