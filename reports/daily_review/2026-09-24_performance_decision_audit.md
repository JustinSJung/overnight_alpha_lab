# Performance Decision Audit - 2026-09-24

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.53%** (7531 evaluated)
- Benchmark-adjusted success rate: **51.62%** (6817 evaluated)
- Selected raw success rate: **45.48%**
- Non-selected raw success rate: **46.63%**
- Selected benchmark-adjusted success rate: **47.05%**
- Non-selected benchmark-adjusted success rate: **52.08%**
- Benchmark coverage: **90.52%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.13% (268 eval); 100-199: 53.48% (660 eval); 200+: 45.77% (6603 eval)

## Return Horizons

- Close T+1 success rate: **41.08%**
- Close T+3 success rate: **42.33%**
- Close T+5 success rate: **42.01%**
- Excess T+1 success rate: **46.78%**
- Excess T+3 success rate: **44.36%**
- Excess T+5 success rate: **43.97%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
