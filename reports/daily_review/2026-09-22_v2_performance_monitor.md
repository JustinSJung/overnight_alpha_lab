# V2 Performance Monitor - 2026-09-22

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **6806**
- V2 success count: **3121**
- V2 failure count: **3685**
- V2 raw success rate: **45.86%**
- V2 benchmark-adjusted evaluated cases: **6577**
- V2 benchmark-adjusted success rate: **51.79%**
- V2 benchmark coverage rate: **96.64%**
- V2 average close_t1_return: **0.27%**
- V2 average excess_t1_return: **-0.08%**
- Selected-pick evaluated cases: **620**
- Selected-pick success rate: **45.00%**
- Non-selected evaluated cases: **6186**
- Non-selected success rate: **45.94%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 347 | 160 | 187 | 46.11% |
| Top 20 | 620 | 279 | 341 | 45.00% |
| Top 50 | 929 | 415 | 514 | 44.67% |
| Top 100 | 1256 | 533 | 723 | 42.44% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 960 | 420 | 540 | 43.75% | -0.04% | -0.54% | -1.04% | 947 | 44.88% |
| avoid | 5846 | 2701 | 3145 | 46.20% | 0.32% | 1.20% | 1.85% | 5630 | 52.95% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.