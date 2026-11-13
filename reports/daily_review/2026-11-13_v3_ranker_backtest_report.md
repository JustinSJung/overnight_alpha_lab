# V3 Ranker Backtest Report - 2026-11-13

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.37%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **22533**
- Overall success rate: **49.44%**
- Current selected group success rate: **44.27%**
- Simulated v3 Top 10 success rate: **45.71%**
- Simulated v3 Top 20 success rate: **47.00%**
- Simulated v3 Top 50 success rate: **44.01%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **49.21%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 350 | 160 | 190 | 45.71% | 0.06% | 0.18% | 50.26% |
| Top 20 | 566 | 266 | 300 | 47.00% | 0.21% | 0.28% | 49.21% |
| Top 50 | 1068 | 470 | 598 | 44.01% | 0.17% | 0.42% | 52.55% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.