# Performance Decision Audit - 2026-10-16

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **48.14%** (12207 evaluated)
- Benchmark-adjusted success rate: **48.09%** (10082 evaluated)
- Selected raw success rate: **44.95%**
- Non-selected raw success rate: **48.37%**
- Selected benchmark-adjusted success rate: **49.67%**
- Non-selected benchmark-adjusted success rate: **47.98%**
- Benchmark coverage: **82.59%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 47.15% (263 eval); 100-199: 54.34% (633 eval); 200+: 47.81% (11311 eval)

## Return Horizons

- Close T+1 success rate: **40.07%**
- Close T+3 success rate: **38.88%**
- Close T+5 success rate: **39.41%**
- Excess T+1 success rate: **52.31%**
- Excess T+3 success rate: **53.0%**
- Excess T+5 success rate: **51.21%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
