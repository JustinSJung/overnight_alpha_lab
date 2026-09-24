# V2 Performance Monitor - 2026-09-24

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **7131**
- V2 success count: **3307**
- V2 failure count: **3824**
- V2 raw success rate: **46.37%**
- V2 benchmark-adjusted evaluated cases: **6817**
- V2 benchmark-adjusted success rate: **51.62%**
- V2 benchmark coverage rate: **95.60%**
- V2 average close_t1_return: **0.23%**
- V2 average excess_t1_return: **-0.06%**
- Selected-pick evaluated cases: **648**
- Selected-pick success rate: **45.52%**
- Non-selected evaluated cases: **6483**
- Non-selected success rate: **46.46%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 364 | 169 | 195 | 46.43% |
| Top 20 | 648 | 295 | 353 | 45.52% |
| Top 50 | 985 | 442 | 543 | 44.87% |
| Top 100 | 1317 | 560 | 757 | 42.52% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.

## Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits the same v2 population above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return | benchmark_evaluated_cases | benchmark_success_rate |
|---|---|---|---|---|---|---|---|---|---|
| buy | 1017 | 448 | 569 | 44.05% | 0.03% | -0.41% | -0.78% | 997 | 45.14% |
| avoid | 6114 | 2859 | 3255 | 46.76% | 0.27% | 1.05% | 1.58% | 5820 | 52.73% |

Buy-type candidates expect a positive move (BUY_CANDIDATE/WATCHLIST); avoid-type candidates expect a negative move (AVOID). Small buy-type sample sizes should be read conservatively.