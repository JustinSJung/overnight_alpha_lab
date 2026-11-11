# Performance Decision Audit - 2026-11-11

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **49.95%** (21624 evaluated)
- Benchmark-adjusted success rate: **50.7%** (16283 evaluated)
- Selected raw success rate: **44.37%**
- Non-selected raw success rate: **50.25%**
- Selected benchmark-adjusted success rate: **50.35%**
- Non-selected benchmark-adjusted success rate: **50.71%**
- Benchmark coverage: **75.3%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.3% (265 eval); 100-199: 54.28% (654 eval); 200+: 49.83% (20705 eval)

## Return Horizons

- Close T+1 success rate: **39.75%**
- Close T+3 success rate: **35.85%**
- Close T+5 success rate: **34.12%**
- Excess T+1 success rate: **50.29%**
- Excess T+3 success rate: **53.46%**
- Excess T+5 success rate: **52.61%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
