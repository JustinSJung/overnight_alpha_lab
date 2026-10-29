# V2 Performance Monitor - 2026-10-06

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **9090**
- V2 success count: **4236**
- V2 failure count: **4854**
- V2 raw success rate: **46.60%**
- V2 benchmark-adjusted evaluated cases: **7727**
- V2 benchmark-adjusted success rate: **52.31%**
- V2 benchmark coverage rate: **85.01%**
- V2 average close_t1_return: **0.25%**
- V2 average excess_t1_return: **-0.17%**
- Selected-pick evaluated cases: **752**
- Selected-pick success rate: **45.88%**
- Non-selected evaluated cases: **8338**
- Non-selected success rate: **46.67%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 417 | 194 | 223 | 46.52% |
| Top 20 | 751 | 344 | 407 | 45.81% |
| Top 50 | 1207 | 556 | 651 | 46.06% |
| Top 100 | 1627 | 721 | 906 | 44.31% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1346 | 621 | 725 | 46.14% | 0.16% | -0.00% | -0.15% | 1213 | 42.62% |
| avoid | 7744 | 3615 | 4129 | 46.68% | 0.27% | 0.99% | 1.42% | 6514 | 54.11% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.