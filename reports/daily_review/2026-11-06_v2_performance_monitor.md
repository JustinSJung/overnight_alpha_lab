# V2 Performance Monitor - 2026-11-06

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **18961**
- V2 success count: **9451**
- V2 failure count: **9510**
- V2 raw success rate: **49.84%**
- V2 benchmark-adjusted evaluated cases: **15430**
- V2 benchmark-adjusted success rate: **50.90%**
- V2 benchmark coverage rate: **81.38%**
- V2 average close_t1_return: **-0.21%**
- V2 average excess_t1_return: **0.15%**
- Selected-pick evaluated cases: **1026**
- Selected-pick success rate: **44.83%**
- Non-selected evaluated cases: **17935**
- Non-selected success rate: **50.13%**
- V2 diagnosis: **Inverted / 역방향 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 568 | 254 | 314 | 44.72% |
| Top 20 | 1022 | 460 | 562 | 45.01% |
| Top 50 | 1628 | 715 | 913 | 43.92% |
| Top 100 | 2141 | 903 | 1238 | 42.18% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1951 | 836 | 1115 | 42.85% | -0.20% | -1.17% | -2.02% | 1316 | 53.88% |
| avoid | 17010 | 8615 | 8395 | 50.65% | -0.21% | -0.55% | -0.80% | 14114 | 50.62% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.