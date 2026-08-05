# V2 Performance Monitor - 2026-08-05

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **7521**
- V2 success count: **3292**
- V2 failure count: **4229**
- V2 raw success rate: **43.77%**
- V2 benchmark-adjusted evaluated cases: **5207**
- V2 benchmark-adjusted success rate: **51.76%**
- V2 benchmark coverage rate: **69.23%**
- V2 average close_t1_return: **0.36%**
- V2 average excess_t1_return: **-0.38%**
- Selected-pick evaluated cases: **463**
- Selected-pick success rate: **50.76%**
- Non-selected evaluated cases: **7058**
- Non-selected success rate: **43.31%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 84 | 42 | 42 | 50.00% |
| Top 20 | 165 | 88 | 77 | 53.33% |
| Top 50 | 310 | 159 | 151 | 51.29% |
| Top 100 | 440 | 217 | 223 | 49.32% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.