# Performance Decision Audit - 2026-11-27

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **50.57%** (29065 evaluated)
- Benchmark-adjusted success rate: **51.81%** (22170 evaluated)
- Selected raw success rate: **43.99%**
- Non-selected raw success rate: **50.88%**
- Selected benchmark-adjusted success rate: **52.69%**
- Non-selected benchmark-adjusted success rate: **51.78%**
- Benchmark coverage: **76.28%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 50.75% (201 eval); 100-199: 48.07% (181 eval); 200+: 50.59% (28683 eval)

## Return Horizons

- Close T+1 success rate: **39.77%**
- Close T+3 success rate: **36.2%**
- Close T+5 success rate: **33.41%**
- Excess T+1 success rate: **50.03%**
- Excess T+3 success rate: **52.98%**
- Excess T+5 success rate: **54.92%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
