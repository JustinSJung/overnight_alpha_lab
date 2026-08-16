# Performance Decision Audit - 2026-08-16

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **43.12%** (24500 evaluated)
- Benchmark-adjusted success rate: **52.79%** (20212 evaluated)
- Selected raw success rate: **53.01%**
- Non-selected raw success rate: **42.27%**
- Selected benchmark-adjusted success rate: **60.17%**
- Non-selected benchmark-adjusted success rate: **52.08%**
- Benchmark coverage: **82.5%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 43.12% (24500 eval)

## Return Horizons

- Close T+1 success rate: **44.83%**
- Close T+3 success rate: **47.48%**
- Close T+5 success rate: **46.84%**
- Excess T+1 success rate: **49.13%**
- Excess T+3 success rate: **52.73%**
- Excess T+5 success rate: **52.56%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
