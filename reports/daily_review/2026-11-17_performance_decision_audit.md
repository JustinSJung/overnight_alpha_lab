# Performance Decision Audit - 2026-11-17

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **50.1%** (24262 evaluated)
- Benchmark-adjusted success rate: **50.81%** (17626 evaluated)
- Selected raw success rate: **43.97%**
- Non-selected raw success rate: **50.41%**
- Selected benchmark-adjusted success rate: **52.55%**
- Non-selected benchmark-adjusted success rate: **50.75%**
- Benchmark coverage: **72.65%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.89% (270 eval); 100-199: 54.33% (670 eval); 200+: 49.99% (23322 eval)

## Return Horizons

- Close T+1 success rate: **39.57%**
- Close T+3 success rate: **37.49%**
- Close T+5 success rate: **35.61%**
- Excess T+1 success rate: **51.34%**
- Excess T+3 success rate: **53.36%**
- Excess T+5 success rate: **53.74%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
