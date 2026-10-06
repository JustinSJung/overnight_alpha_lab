# Performance Decision Audit - 2026-10-06

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.72%** (9505 evaluated)
- Benchmark-adjusted success rate: **52.31%** (7727 evaluated)
- Selected raw success rate: **45.84%**
- Non-selected raw success rate: **46.8%**
- Selected benchmark-adjusted success rate: **42.04%**
- Non-selected benchmark-adjusted success rate: **53.22%**
- Benchmark coverage: **81.29%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.36% (275 eval); 100-199: 54.14% (713 eval); 200+: 46.05% (8517 eval)

## Return Horizons

- Close T+1 success rate: **42.19%**
- Close T+3 success rate: **43.91%**
- Close T+5 success rate: **42.95%**
- Excess T+1 success rate: **45.03%**
- Excess T+3 success rate: **42.63%**
- Excess T+5 success rate: **41.31%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
