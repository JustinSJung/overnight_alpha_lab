# Performance Decision Audit - 2026-09-30

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.63%** (8475 evaluated)
- Benchmark-adjusted success rate: **51.58%** (7200 evaluated)
- Selected raw success rate: **44.93%**
- Non-selected raw success rate: **46.78%**
- Selected benchmark-adjusted success rate: **44.82%**
- Non-selected benchmark-adjusted success rate: **52.23%**
- Benchmark coverage: **84.96%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 47.94% (267 eval); 100-199: 52.49% (642 eval); 200+: 46.09% (7566 eval)

## Return Horizons

- Close T+1 success rate: **41.31%**
- Close T+3 success rate: **42.35%**
- Close T+5 success rate: **41.75%**
- Excess T+1 success rate: **46.34%**
- Excess T+3 success rate: **45.79%**
- Excess T+5 success rate: **42.41%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
