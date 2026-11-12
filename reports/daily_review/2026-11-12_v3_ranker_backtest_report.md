# V3 Ranker Backtest Report - 2026-11-12

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.33%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **22028**
- Overall success rate: **48.86%**
- Current selected group success rate: **44.09%**
- Simulated v3 Top 10 success rate: **45.83%**
- Simulated v3 Top 20 success rate: **47.08%**
- Simulated v3 Top 50 success rate: **44.13%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **49.83%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 336 | 154 | 182 | 45.83% | 0.01% | 0.23% | 51.12% |
| Top 20 | 548 | 258 | 290 | 47.08% | 0.22% | 0.30% | 49.83% |
| Top 50 | 1031 | 455 | 576 | 44.13% | 0.18% | 0.48% | 52.86% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.