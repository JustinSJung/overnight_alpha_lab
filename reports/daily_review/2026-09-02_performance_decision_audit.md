# Performance Decision Audit - 2026-09-02

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **43.2%** (3669 evaluated)
- Benchmark-adjusted success rate: **49.47%** (3410 evaluated)
- Selected raw success rate: **44.04%**
- Non-selected raw success rate: **43.09%**
- Selected benchmark-adjusted success rate: **47.45%**
- Non-selected benchmark-adjusted success rate: **49.75%**
- Benchmark coverage: **92.94%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.85% (262 eval); 100-199: 52.74% (603 eval); 200+: 40.62% (2804 eval)

## Return Horizons

- Close T+1 success rate: **41.69%**
- Close T+3 success rate: **46.06%**
- Close T+5 success rate: **47.54%**
- Excess T+1 success rate: **48.58%**
- Excess T+3 success rate: **48.69%**
- Excess T+5 success rate: **45.53%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
