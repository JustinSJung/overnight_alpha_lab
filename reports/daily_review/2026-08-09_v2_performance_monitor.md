# V2 Performance Monitor - 2026-08-09

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **11739**
- V2 success count: **4996**
- V2 failure count: **6743**
- V2 raw success rate: **42.56%**
- V2 benchmark-adjusted evaluated cases: **9425**
- V2 benchmark-adjusted success rate: **52.02%**
- V2 benchmark coverage rate: **80.29%**
- V2 average close_t1_return: **0.57%**
- V2 average excess_t1_return: **-0.28%**
- Selected-pick evaluated cases: **830**
- Selected-pick success rate: **52.17%**
- Non-selected evaluated cases: **10909**
- Non-selected success rate: **41.83%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 105 | 51 | 54 | 48.57% |
| Top 20 | 213 | 110 | 103 | 51.64% |
| Top 50 | 497 | 258 | 239 | 51.91% |
| Top 100 | 741 | 377 | 364 | 50.88% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.