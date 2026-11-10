# Performance Decision Audit - 2026-11-10

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **50.88%** (20839 evaluated)
- Benchmark-adjusted success rate: **49.68%** (15832 evaluated)
- Selected raw success rate: **43.92%**
- Non-selected raw success rate: **51.25%**
- Selected benchmark-adjusted success rate: **52.66%**
- Non-selected benchmark-adjusted success rate: **49.57%**
- Benchmark coverage: **75.97%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.13% (268 eval); 100-199: 54.13% (641 eval); 200+: 50.81% (19930 eval)

## Return Horizons

- Close T+1 success rate: **38.72%**
- Close T+3 success rate: **35.62%**
- Close T+5 success rate: **34.23%**
- Excess T+1 success rate: **52.01%**
- Excess T+3 success rate: **52.8%**
- Excess T+5 success rate: **51.3%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
