# V2 Performance Monitor - 2026-08-04

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **6258**
- V2 success count: **2799**
- V2 failure count: **3459**
- V2 raw success rate: **44.73%**
- V2 benchmark-adjusted evaluated cases: **3944**
- V2 benchmark-adjusted success rate: **51.57%**
- V2 benchmark coverage rate: **63.02%**
- V2 average close_t1_return: **0.22%**
- V2 average excess_t1_return: **-0.40%**
- Selected-pick evaluated cases: **380**
- Selected-pick success rate: **50.00%**
- Non-selected evaluated cases: **5878**
- Non-selected success rate: **44.39%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 75 | 34 | 41 | 45.33% |
| Top 20 | 146 | 78 | 68 | 53.42% |
| Top 50 | 262 | 133 | 129 | 50.76% |
| Top 100 | 378 | 188 | 190 | 49.74% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.