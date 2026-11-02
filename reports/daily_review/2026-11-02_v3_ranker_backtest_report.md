# V3 Ranker Backtest Report - 2026-11-02

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **97.92%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **15936**
- Overall success rate: **48.86%**
- Current selected group success rate: **43.76%**
- Simulated v3 Top 10 success rate: **44.27%**
- Simulated v3 Top 20 success rate: **45.86%**
- Simulated v3 Top 50 success rate: **42.57%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **51.88%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 262 | 116 | 146 | 44.27% | -0.22% | -0.10% | 48.65% |
| Top 20 | 423 | 194 | 229 | 45.86% | 0.09% | 0.30% | 51.88% |
| Top 50 | 787 | 335 | 452 | 42.57% | 0.16% | 0.54% | 54.10% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.