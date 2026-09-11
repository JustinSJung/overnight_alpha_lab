# Performance Decision Audit - 2026-09-11

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **45.43%** (5307 evaluated)
- Benchmark-adjusted success rate: **49.96%** (5048 evaluated)
- Selected raw success rate: **45.58%**
- Non-selected raw success rate: **45.41%**
- Selected benchmark-adjusted success rate: **48.27%**
- Non-selected benchmark-adjusted success rate: **50.15%**
- Benchmark coverage: **95.12%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 49.06% (267 eval); 100-199: 55.91% (660 eval); 200+: 43.63% (4380 eval)

## Return Horizons

- Close T+1 success rate: **40.93%**
- Close T+3 success rate: **44.63%**
- Close T+5 success rate: **45.64%**
- Excess T+1 success rate: **49.35%**
- Excess T+3 success rate: **46.07%**
- Excess T+5 success rate: **43.63%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
