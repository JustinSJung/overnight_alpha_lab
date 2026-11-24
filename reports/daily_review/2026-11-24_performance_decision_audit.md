# Performance Decision Audit - 2026-11-24

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **51.24%** (26720 evaluated)
- Benchmark-adjusted success rate: **51.73%** (19751 evaluated)
- Selected raw success rate: **43.07%**
- Non-selected raw success rate: **51.64%**
- Selected benchmark-adjusted success rate: **52.54%**
- Non-selected benchmark-adjusted success rate: **51.7%**
- Benchmark coverage: **73.92%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 50.75% (201 eval); 100-199: 61.54% (338 eval); 200+: 51.11% (26181 eval)

## Return Horizons

- Close T+1 success rate: **38.75%**
- Close T+3 success rate: **36.13%**
- Close T+5 success rate: **34.19%**
- Excess T+1 success rate: **50.59%**
- Excess T+3 success rate: **53.27%**
- Excess T+5 success rate: **55.59%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
