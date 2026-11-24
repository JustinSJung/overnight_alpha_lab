# V3 Ranker Backtest Report - 2026-11-24

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.62%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **26461**
- Overall success rate: **51.25%**
- Current selected group success rate: **43.07%**
- Simulated v3 Top 10 success rate: **42.89%**
- Simulated v3 Top 20 success rate: **43.55%**
- Simulated v3 Top 50 success rate: **42.10%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **53.46%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 394 | 169 | 225 | 42.89% | -0.21% | 0.64% | 56.89% |
| Top 20 | 643 | 280 | 363 | 43.55% | -0.11% | 0.56% | 53.46% |
| Top 50 | 1202 | 506 | 696 | 42.10% | -0.09% | 0.58% | 55.40% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.