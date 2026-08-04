# V2 Performance Monitor - 2026-08-04

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **6243**
- V2 success count: **2793**
- V2 failure count: **3450**
- V2 raw success rate: **44.74%**
- V2 benchmark-adjusted evaluated cases: **3929**
- V2 benchmark-adjusted success rate: **51.62%**
- V2 benchmark coverage rate: **62.93%**
- V2 average close_t1_return: **0.21%**
- V2 average excess_t1_return: **-0.40%**
- Selected-pick evaluated cases: **377**
- Selected-pick success rate: **49.87%**
- Non-selected evaluated cases: **5866**
- Non-selected success rate: **44.41%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 75 | 34 | 41 | 45.33% |
| Top 20 | 143 | 76 | 67 | 53.15% |
| Top 50 | 259 | 131 | 128 | 50.58% |
| Top 100 | 375 | 186 | 189 | 49.60% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.