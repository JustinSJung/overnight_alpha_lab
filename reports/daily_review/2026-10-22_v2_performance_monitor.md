# V2 Performance Monitor - 2026-10-22

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **14155**
- V2 success count: **6818**
- V2 failure count: **7337**
- V2 raw success rate: **48.17%**
- V2 benchmark-adjusted evaluated cases: **11825**
- V2 benchmark-adjusted success rate: **47.97%**
- V2 benchmark coverage rate: **83.54%**
- V2 average close_t1_return: **-0.03%**
- V2 average excess_t1_return: **0.45%**
- Selected-pick evaluated cases: **924**
- Selected-pick success rate: **43.83%**
- Non-selected evaluated cases: **13231**
- Non-selected success rate: **48.47%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Weak market-relative signal / 시장 대비 약한 신호**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 507 | 219 | 288 | 43.20% |
| Top 20 | 920 | 405 | 515 | 44.02% |
| Top 50 | 1484 | 645 | 839 | 43.46% |
| Top 100 | 2008 | 843 | 1165 | 41.98% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1815 | 767 | 1048 | 42.26% | -0.19% | -1.13% | -2.08% | 1344 | 53.50% |
| avoid | 12340 | 6051 | 6289 | 49.04% | -0.01% | 0.13% | 0.53% | 10481 | 47.26% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.