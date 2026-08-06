# V2 Performance Monitor - 2026-08-06

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **8875**
- V2 success count: **3832**
- V2 failure count: **5043**
- V2 raw success rate: **43.18%**
- V2 benchmark-adjusted evaluated cases: **6561**
- V2 benchmark-adjusted success rate: **51.84%**
- V2 benchmark coverage rate: **73.93%**
- V2 average close_t1_return: **0.45%**
- V2 average excess_t1_return: **-0.34%**
- Selected-pick evaluated cases: **572**
- Selected-pick success rate: **51.40%**
- Non-selected evaluated cases: **8303**
- Non-selected success rate: **42.61%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 92 | 45 | 47 | 48.91% |
| Top 20 | 186 | 100 | 86 | 53.76% |
| Top 50 | 381 | 198 | 183 | 51.97% |
| Top 100 | 525 | 267 | 258 | 50.86% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.