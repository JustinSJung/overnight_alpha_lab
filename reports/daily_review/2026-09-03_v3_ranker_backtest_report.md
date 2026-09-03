# V3 Ranker Backtest Report - 2026-09-03

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **91.69%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **3595**
- Overall success rate: **44.23%**
- Current selected group success rate: **45.27%**
- Simulated v3 Top 10 success rate: **42.96%**
- Simulated v3 Top 20 success rate: **45.33%**
- Simulated v3 Top 50 success rate: **42.65%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **48.13%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 135 | 58 | 77 | 42.96% | 0.30% | 0.26% | 45.93% |
| Top 20 | 214 | 97 | 117 | 45.33% | 0.48% | 0.41% | 48.13% |
| Top 50 | 422 | 180 | 242 | 42.65% | 0.53% | 0.10% | 45.02% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.