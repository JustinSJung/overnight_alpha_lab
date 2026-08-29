# Performance Decision Audit - 2026-08-29

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **42.2%** (3301 evaluated)
- Benchmark-adjusted success rate: **50.2%** (3042 evaluated)
- Selected raw success rate: **47.21%**
- Non-selected raw success rate: **41.59%**
- Selected benchmark-adjusted success rate: **47.77%**
- Non-selected benchmark-adjusted success rate: **50.52%**
- Benchmark coverage: **92.15%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.87% (266 eval); 100-199: 54.59% (632 eval); 200+: 38.2% (2403 eval)

## Return Horizons

- Close T+1 success rate: **43.68%**
- Close T+3 success rate: **47.48%**
- Close T+5 success rate: **47.53%**
- Excess T+1 success rate: **47.28%**
- Excess T+3 success rate: **46.33%**
- Excess T+5 success rate: **45.24%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
