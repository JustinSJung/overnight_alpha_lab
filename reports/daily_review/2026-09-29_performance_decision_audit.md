# Performance Decision Audit - 2026-09-29

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **47.23%** (8093 evaluated)
- Benchmark-adjusted success rate: **51.04%** (6953 evaluated)
- Selected raw success rate: **45.16%**
- Non-selected raw success rate: **47.42%**
- Selected benchmark-adjusted success rate: **44.92%**
- Non-selected benchmark-adjusted success rate: **51.65%**
- Benchmark coverage: **85.91%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.7% (269 eval); 100-199: 53.78% (649 eval); 200+: 46.58% (7175 eval)

## Return Horizons

- Close T+1 success rate: **40.62%**
- Close T+3 success rate: **41.92%**
- Close T+5 success rate: **42.0%**
- Excess T+1 success rate: **46.9%**
- Excess T+3 success rate: **45.73%**
- Excess T+5 success rate: **42.68%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
