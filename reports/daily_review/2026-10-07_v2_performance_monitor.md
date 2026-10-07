# V2 Performance Monitor - 2026-10-07

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **9118**
- V2 success count: **4227**
- V2 failure count: **4891**
- V2 raw success rate: **46.36%**
- V2 benchmark-adjusted evaluated cases: **7832**
- V2 benchmark-adjusted success rate: **51.53%**
- V2 benchmark coverage rate: **85.90%**
- V2 average close_t1_return: **0.25%**
- V2 average excess_t1_return: **-0.06%**
- Selected-pick evaluated cases: **738**
- Selected-pick success rate: **45.80%**
- Non-selected evaluated cases: **8380**
- Non-selected success rate: **46.41%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 402 | 186 | 216 | 46.27% |
| Top 20 | 737 | 338 | 399 | 45.86% |
| Top 50 | 1209 | 549 | 660 | 45.41% |
| Top 100 | 1641 | 713 | 928 | 43.45% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1415 | 640 | 775 | 45.23% | 0.17% | 0.10% | 0.09% | 1282 | 44.46% |
| avoid | 7703 | 3587 | 4116 | 46.57% | 0.27% | 0.97% | 1.41% | 6550 | 52.92% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.