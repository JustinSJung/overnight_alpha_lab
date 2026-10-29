# Performance Decision Audit - 2026-10-23

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **49.61%** (15009 evaluated)
- Benchmark-adjusted success rate: **47.33%** (12247 evaluated)
- Selected raw success rate: **43.95%**
- Non-selected raw success rate: **49.99%**
- Selected benchmark-adjusted success rate: **51.91%**
- Non-selected benchmark-adjusted success rate: **47.08%**
- Benchmark coverage: **81.6%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.7% (269 eval); 100-199: 53.52% (667 eval); 200+: 49.44% (14073 eval)

## Return Horizons

- Close T+1 success rate: **38.82%**
- Close T+3 success rate: **38.49%**
- Close T+5 success rate: **38.36%**
- Excess T+1 success rate: **53.87%**
- Excess T+3 success rate: **54.74%**
- Excess T+5 success rate: **56.17%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
