# V3 Ranker Backtest Report - 2026-08-10

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **81.31%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **13345**
- Overall success rate: **42.35%**
- Current selected group success rate: **53.33%**
- Simulated v3 Top 10 success rate: **44.44%**
- Simulated v3 Top 20 success rate: **48.18%**
- Simulated v3 Top 50 success rate: **46.27%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **55.75%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 81 | 36 | 45 | 44.44% | 0.65% | 0.57% | 57.97% |
| Top 20 | 137 | 66 | 71 | 48.18% | 0.84% | 0.01% | 55.75% |
| Top 50 | 268 | 124 | 144 | 46.27% | 0.99% | 0.23% | 56.19% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.