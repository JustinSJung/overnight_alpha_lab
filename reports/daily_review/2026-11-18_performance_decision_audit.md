# Performance Decision Audit - 2026-11-18

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **50.21%** (24740 evaluated)
- Benchmark-adjusted success rate: **50.71%** (18078 evaluated)
- Selected raw success rate: **43.46%**
- Non-selected raw success rate: **50.55%**
- Selected benchmark-adjusted success rate: **52.48%**
- Non-selected benchmark-adjusted success rate: **50.65%**
- Benchmark coverage: **73.07%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.52% (270 eval); 100-199: 54.16% (661 eval); 200+: 50.12% (23809 eval)

## Return Horizons

- Close T+1 success rate: **39.21%**
- Close T+3 success rate: **37.25%**
- Close T+5 success rate: **35.66%**
- Excess T+1 success rate: **51.75%**
- Excess T+3 success rate: **54.13%**
- Excess T+5 success rate: **53.85%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
