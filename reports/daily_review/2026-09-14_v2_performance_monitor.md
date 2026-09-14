# V2 Performance Monitor - 2026-09-14

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **5132**
- V2 success count: **2359**
- V2 failure count: **2773**
- V2 raw success rate: **45.97%**
- V2 benchmark-adjusted evaluated cases: **5132**
- V2 benchmark-adjusted success rate: **48.62%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.27%**
- V2 average excess_t1_return: **0.14%**
- Selected-pick evaluated cases: **533**
- Selected-pick success rate: **44.84%**
- Non-selected evaluated cases: **4599**
- Non-selected success rate: **46.10%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 309 | 144 | 165 | 46.60% |
| Top 20 | 533 | 239 | 294 | 44.84% |
| Top 50 | 785 | 340 | 445 | 43.31% |
| Top 100 | 1114 | 460 | 654 | 41.29% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 818 | 347 | 471 | 42.42% | -0.13% | -0.41% | -0.76% | 818 | 47.07% |
| avoid | 4314 | 2012 | 2302 | 46.64% | 0.34% | 1.53% | 2.80% | 4314 | 48.91% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.