# V2 Performance Monitor - 2026-11-27

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **28806**
- V2 success count: **14568**
- V2 failure count: **14238**
- V2 raw success rate: **50.57%**
- V2 benchmark-adjusted evaluated cases: **22170**
- V2 benchmark-adjusted success rate: **51.81%**
- V2 benchmark coverage rate: **76.96%**
- V2 average close_t1_return: **-0.21%**
- V2 average excess_t1_return: **0.11%**
- Selected-pick evaluated cases: **1282**
- Selected-pick success rate: **43.99%**
- Non-selected evaluated cases: **27524**
- Non-selected success rate: **50.88%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 682 | 294 | 388 | 43.11% |
| Top 20 | 1278 | 564 | 714 | 44.13% |
| Top 50 | 2311 | 1009 | 1302 | 43.66% |
| Top 100 | 2916 | 1218 | 1698 | 41.77% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 2894 | 1224 | 1670 | 42.29% | -0.27% | -1.08% | -2.17% | 1913 | 53.53% |
| avoid | 25912 | 13344 | 12568 | 51.50% | -0.21% | -0.79% | -1.53% | 20257 | 51.65% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.