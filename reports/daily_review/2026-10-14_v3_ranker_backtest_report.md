# V3 Ranker Backtest Report - 2026-10-14

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **97.07%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **10752**
- Overall success rate: **48.02%**
- Current selected group success rate: **44.96%**
- Simulated v3 Top 10 success rate: **45.11%**
- Simulated v3 Top 20 success rate: **47.15%**
- Simulated v3 Top 50 success rate: **43.22%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **55.38%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 235 | 106 | 129 | 45.11% | 0.01% | 0.17% | 51.30% |
| Top 20 | 386 | 182 | 204 | 47.15% | 0.25% | 0.40% | 55.38% |
| Top 50 | 738 | 319 | 419 | 43.22% | 0.25% | 0.48% | 52.37% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.