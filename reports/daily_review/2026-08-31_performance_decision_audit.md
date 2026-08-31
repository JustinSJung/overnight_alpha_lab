# Performance Decision Audit - 2026-08-31

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **42.66%** (3385 evaluated)
- Benchmark-adjusted success rate: **50.29%** (3126 evaluated)
- Selected raw success rate: **46.13%**
- Non-selected raw success rate: **42.23%**
- Selected benchmark-adjusted success rate: **50.13%**
- Non-selected benchmark-adjusted success rate: **50.31%**
- Benchmark coverage: **92.35%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.87% (266 eval); 100-199: 54.59% (632 eval); 200+: 38.96% (2487 eval)

## Return Horizons

- Close T+1 success rate: **42.15%**
- Close T+3 success rate: **47.21%**
- Close T+5 success rate: **47.55%**
- Excess T+1 success rate: **49.54%**
- Excess T+3 success rate: **46.31%**
- Excess T+5 success rate: **46.85%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
