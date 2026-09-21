# Performance Decision Audit - 2026-09-21

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.0%** (6917 evaluated)
- Benchmark-adjusted success rate: **50.53%** (6374 evaluated)
- Selected raw success rate: **44.44%**
- Non-selected raw success rate: **46.15%**
- Selected benchmark-adjusted success rate: **47.26%**
- Non-selected benchmark-adjusted success rate: **50.88%**
- Benchmark coverage: **92.15%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.31% (267 eval); 100-199: 53.51% (656 eval); 200+: 45.08% (5994 eval)

## Return Horizons

- Close T+1 success rate: **41.07%**
- Close T+3 success rate: **42.35%**
- Close T+5 success rate: **41.75%**
- Excess T+1 success rate: **48.27%**
- Excess T+3 success rate: **46.33%**
- Excess T+5 success rate: **47.02%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
