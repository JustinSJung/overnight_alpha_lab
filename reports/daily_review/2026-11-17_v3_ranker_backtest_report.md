# V3 Ranker Backtest Report - 2026-11-17

This report simulates `v3_stability_ranker` on already-evaluated historical candidates.
It is diagnostic only and does not alter historical decisions, selected picks, or trading behavior.

## Summary

- Experimental score version: **v3_stability_ranker**
- Historical component coverage: **98.45%**
- Data status: **sufficient historical component coverage**
- Overall evaluated cases: **23934**
- Overall success rate: **50.11%**
- Current selected group success rate: **43.98%**
- Simulated v3 Top 10 success rate: **45.43%**
- Simulated v3 Top 20 success rate: **46.08%**
- Simulated v3 Top 50 success rate: **43.47%**
- Simulated v3 Top 20 benchmark-adjusted success rate: **53.50%**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_excess_t1_return | benchmark_adjusted_success_rate |
|---|---:|---:|---:|---:|---:|---:|---:|
| Top 10 | 361 | 164 | 197 | 45.43% | -0.05% | 0.60% | 56.15% |
| Top 20 | 586 | 270 | 316 | 46.08% | 0.12% | 0.57% | 53.50% |
| Top 50 | 1095 | 476 | 619 | 43.47% | 0.10% | 0.63% | 55.59% |

## Notes

- V3 favors moderate confirmed momentum, stable liquidity, and lower reversal/noise risk.
- V3 is not public production scoring yet.
- No order placement or trading action is performed by this project.