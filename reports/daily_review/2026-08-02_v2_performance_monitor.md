# V2 Performance Monitor - 2026-08-02

This report monitors `v2_conservative_ranker` only. It is diagnostic and does not change scoring or place trades.

## Summary

- V2 evaluated cases: **3980**
- V2 success count: **1861**
- V2 failure count: **2119**
- V2 raw success rate: **46.76%**
- V2 benchmark-adjusted evaluated cases: **1666**
- V2 benchmark-adjusted success rate: **51.74%**
- V2 benchmark coverage rate: **41.86%**
- V2 average close_t1_return: **-0.12%**
- V2 average excess_t1_return: **-0.43%**
- Selected-pick evaluated cases: **240**
- Selected-pick success rate: **48.75%**
- Non-selected evaluated cases: **3740**
- Non-selected success rate: **46.63%**
- V2 diagnosis: **Weak / 약함**
- Benchmark diagnosis: **Neutral / 중립**

## Rank Buckets

| bucket | evaluated_count | success_count | failure_count | success_rate |
|---|---|---|---|---|
| Top 10 | 58 | 25 | 33 | 43.10% |
| Top 20 | 103 | 50 | 53 | 48.54% |
| Top 50 | 184 | 87 | 97 | 47.28% |
| Top 100 | 240 | 117 | 123 | 48.75% |

## Interpretation

- Improving means selected picks beat non-selected candidates by more than 3 percentage points.
- Weak means selected and non-selected performance are within +/-3 percentage points.
- Inverted means selected picks trail non-selected candidates by more than 3 percentage points.
- Benchmark coverage below 30% should be treated as incomplete market-relative evidence.