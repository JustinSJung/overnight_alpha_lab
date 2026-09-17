# V2 Performance Monitor - 2026-09-17

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **6220**
- V2 success count: **2865**
- V2 failure count: **3355**
- V2 raw success rate: **46.06%**
- V2 benchmark-adjusted evaluated cases: **6220**
- V2 benchmark-adjusted success rate: **50.10%**
- V2 benchmark coverage rate: **100.00%**
- V2 average close_t1_return: **0.27%**
- V2 average excess_t1_return: **0.07%**
- Selected-pick evaluated cases: **596**
- Selected-pick success rate: **44.30%**
- Non-selected evaluated cases: **5624**
- Non-selected success rate: **46.25%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 340 | 155 | 185 | 45.59% |
| Top 20 | 596 | 264 | 332 | 44.30% |
| Top 50 | 876 | 387 | 489 | 44.18% |
| Top 100 | 1204 | 507 | 697 | 42.11% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 907 | 393 | 514 | 43.33% | -0.09% | -0.57% | -0.87% | 907 | 45.09% |
| avoid | 5313 | 2472 | 2841 | 46.53% | 0.33% | 1.17% | 2.02% | 5313 | 50.95% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.