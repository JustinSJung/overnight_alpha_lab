# Performance Decision Audit - 2026-08-27

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **42.3%** (46223 evaluated)
- Benchmark-adjusted success rate: **52.02%** (41935 evaluated)
- Selected raw success rate: **49.67%**
- Non-selected raw success rate: **41.48%**
- Selected benchmark-adjusted success rate: **52.08%**
- Non-selected benchmark-adjusted success rate: **52.01%**
- Benchmark coverage: **90.72%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 42.3% (46223 eval)

## Return Horizons

- Close T+1 success rate: **44.62%**
- Close T+3 success rate: **47.82%**
- Close T+5 success rate: **48.76%**
- Excess T+1 success rate: **46.88%**
- Excess T+3 success rate: **48.88%**
- Excess T+5 success rate: **47.52%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
