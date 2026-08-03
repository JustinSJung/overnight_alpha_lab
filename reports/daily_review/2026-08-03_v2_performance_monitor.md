# V2 Performance Monitor - 2026-08-03

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **5053**
- V2 success count: **2320**
- V2 failure count: **2733**
- V2 raw success rate: **45.91%**
- V2 benchmark-adjusted evaluated cases: **2739**
- V2 benchmark-adjusted success rate: **51.70%**
- V2 benchmark coverage rate: **54.21%**
- V2 average close_t1_return: **0.03%**
- V2 average excess_t1_return: **-0.45%**
- Selected-pick evaluated cases: **306**
- Selected-pick success rate: **49.02%**
- Non-selected evaluated cases: **4747**
- Non-selected success rate: **45.71%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 67 | 29 | 38 | 43.28% |
| Top 20 | 127 | 67 | 60 | 52.76% |
| Top 50 | 219 | 109 | 110 | 49.77% |
| Top 100 | 306 | 150 | 156 | 49.02% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.