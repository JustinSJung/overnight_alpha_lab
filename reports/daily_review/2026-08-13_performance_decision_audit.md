# Performance Decision Audit - 2026-08-13

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **43.34%** (22335 evaluated)
- Benchmark-adjusted success rate: **52.88%** (18047 evaluated)
- Selected raw success rate: **53.18%**
- Non-selected raw success rate: **42.53%**
- Selected benchmark-adjusted success rate: **61.99%**
- Non-selected benchmark-adjusted success rate: **52.04%**
- Benchmark coverage: **80.8%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 43.34% (22335 eval)

## Return Horizons

- Close T+1 success rate: **44.44%**
- Close T+3 success rate: **46.61%**
- Close T+5 success rate: **45.34%**
- Excess T+1 success rate: **49.76%**
- Excess T+3 success rate: **53.57%**
- Excess T+5 success rate: **53.52%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
