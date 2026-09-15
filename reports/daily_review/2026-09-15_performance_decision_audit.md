# Performance Decision Audit - 2026-09-15

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **45.36%** (5932 evaluated)
- Benchmark-adjusted success rate: **49.04%** (5601 evaluated)
- Selected raw success rate: **42.99%**
- Non-selected raw success rate: **45.61%**
- Selected benchmark-adjusted success rate: **47.48%**
- Non-selected benchmark-adjusted success rate: **49.22%**
- Benchmark coverage: **94.42%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 49.07% (269 eval); 100-199: 54.17% (672 eval); 200+: 43.98% (4991 eval)

## Return Horizons

- Close T+1 success rate: **40.71%**
- Close T+3 success rate: **43.11%**
- Close T+5 success rate: **44.2%**
- Excess T+1 success rate: **49.84%**
- Excess T+3 success rate: **50.03%**
- Excess T+5 success rate: **46.38%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
