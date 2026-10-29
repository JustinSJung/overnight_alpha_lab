# V2 Performance Monitor - 2026-10-02

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **8483**
- V2 success count: **3966**
- V2 failure count: **4517**
- V2 raw success rate: **46.75%**
- V2 benchmark-adjusted evaluated cases: **7592**
- V2 benchmark-adjusted success rate: **52.77%**
- V2 benchmark coverage rate: **89.50%**
- V2 average close_t1_return: **0.22%**
- V2 average excess_t1_return: **-0.13%**
- Selected-pick evaluated cases: **726**
- Selected-pick success rate: **45.87%**
- Non-selected evaluated cases: **7757**
- Non-selected success rate: **46.84%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 405 | 190 | 215 | 46.91% |
| Top 20 | 726 | 333 | 393 | 45.87% |
| Top 50 | 1147 | 527 | 620 | 45.95% |
| Top 100 | 1511 | 666 | 845 | 44.08% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1222 | 555 | 667 | 45.42% | 0.12% | -0.09% | -0.36% | 1162 | 43.72% |
| avoid | 7261 | 3411 | 3850 | 46.98% | 0.24% | 0.87% | 1.35% | 6430 | 54.40% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.