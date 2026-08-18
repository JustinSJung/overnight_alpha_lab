# Performance Decision Audit - 2026-08-18

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **42.73%** (29040 evaluated)
- Benchmark-adjusted success rate: **52.54%** (24752 evaluated)
- Selected raw success rate: **52.2%**
- Non-selected raw success rate: **41.85%**
- Selected benchmark-adjusted success rate: **57.37%**
- Non-selected benchmark-adjusted success rate: **52.04%**
- Benchmark coverage: **85.23%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 42.73% (29040 eval)

## Return Horizons

- Close T+1 success rate: **45.14%**
- Close T+3 success rate: **48.61%**
- Close T+5 success rate: **48.82%**
- Excess T+1 success rate: **48.28%**
- Excess T+3 success rate: **51.46%**
- Excess T+5 success rate: **51.13%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
