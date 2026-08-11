# V3 Ranker Backtest Report - 2026-08-11

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **82.63%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **15067**
- Overall success rate: **42.20%**
- Current selected group success rate: **53.92%**
- Simulated v3 Top 10 success rate: **49.45%**
- Simulated v3 Top 20 success rate: **50.64%**
- Simulated v3 Top 50 success rate: **48.36%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **54.07%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 91 | 45 | 46 | 49.45% | 0.69% | 0.29% | 55.70% |
| Top 20 | 156 | 79 | 77 | 50.64% | 0.91% | -0.18% | 54.07% |
| Top 50 | 304 | 147 | 157 | 48.36% | 1.08% | 0.16% | 55.64% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.