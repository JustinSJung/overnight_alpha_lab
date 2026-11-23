# Performance Decision Audit - 2026-11-23

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **50.59%** (26212 evaluated)
- Benchmark-adjusted success rate: **51.5%** (19125 evaluated)
- Selected raw success rate: **43.26%**
- Non-selected raw success rate: **50.94%**
- Selected benchmark-adjusted success rate: **51.91%**
- Non-selected benchmark-adjusted success rate: **51.49%**
- Benchmark coverage: **72.96%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 50.75% (201 eval); 100-199: 63.25% (351 eval); 200+: 50.41% (25660 eval)

## Return Horizons

- Close T+1 success rate: **39.4%**
- Close T+3 success rate: **36.63%**
- Close T+5 success rate: **34.59%**
- Excess T+1 success rate: **50.59%**
- Excess T+3 success rate: **53.06%**
- Excess T+5 success rate: **55.69%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
