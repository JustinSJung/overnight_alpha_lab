# V2 Performance Monitor - 2026-08-10

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **13345**
- V2 success count: **5651**
- V2 failure count: **7694**
- V2 raw success rate: **42.35%**
- V2 benchmark-adjusted evaluated cases: **11031**
- V2 benchmark-adjusted success rate: **52.28%**
- V2 benchmark coverage rate: **82.66%**
- V2 average close_t1_return: **0.63%**
- V2 average excess_t1_return: **-0.29%**
- Selected-pick evaluated cases: **992**
- Selected-pick success rate: **53.33%**
- Non-selected evaluated cases: **12353**
- Non-selected success rate: **41.46%**
- V2 diagnosis: **Improving / 개선 가능성**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 113 | 55 | 58 | 48.67% |
| Top 20 | 229 | 119 | 110 | 51.97% |
| Top 50 | 539 | 296 | 243 | 54.92% |
| Top 100 | 871 | 474 | 397 | 54.42% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.