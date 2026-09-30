# V2 Performance Monitor - 2026-09-30

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **8076**
- V2 success count: **3754**
- V2 failure count: **4322**
- V2 raw success rate: **46.48%**
- V2 benchmark-adjusted evaluated cases: **7200**
- V2 benchmark-adjusted success rate: **51.58%**
- V2 benchmark coverage rate: **89.15%**
- V2 average close_t1_return: **0.20%**
- V2 average excess_t1_return: **0.01%**
- Selected-pick evaluated cases: **685**
- Selected-pick success rate: **44.96%**
- Non-selected evaluated cases: **7391**
- Non-selected success rate: **46.62%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 380 | 177 | 203 | 46.58% |
| Top 20 | 685 | 308 | 377 | 44.96% |
| Top 50 | 1069 | 474 | 595 | 44.34% |
| Top 100 | 1426 | 607 | 819 | 42.57% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1137 | 500 | 637 | 43.98% | 0.01% | -0.36% | -0.69% | 1080 | 44.81% |
| avoid | 6939 | 3254 | 3685 | 46.89% | 0.23% | 0.89% | 1.42% | 6120 | 52.78% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.