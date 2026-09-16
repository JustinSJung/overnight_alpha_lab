# Performance Decision Audit - 2026-09-16

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **47.06%** (6175 evaluated)
- Benchmark-adjusted success rate: **49.36%** (5845 evaluated)
- Selected raw success rate: **44.41%**
- Non-selected raw success rate: **47.33%**
- Selected benchmark-adjusted success rate: **49.3%**
- Non-selected benchmark-adjusted success rate: **49.36%**
- Benchmark coverage: **94.66%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.31% (267 eval); 100-199: 53.22% (652 eval); 200+: 46.23% (5256 eval)

## Return Horizons

- Close T+1 success rate: **39.82%**
- Close T+3 success rate: **41.71%**
- Close T+5 success rate: **42.94%**
- Excess T+1 success rate: **50.15%**
- Excess T+3 success rate: **51.42%**
- Excess T+5 success rate: **48.61%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
