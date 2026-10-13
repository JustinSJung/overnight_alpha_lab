# Performance Decision Audit - 2026-10-13

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **48.85%** (10637 evaluated)
- Benchmark-adjusted success rate: **49.98%** (8517 evaluated)
- Selected raw success rate: **44.47%**
- Non-selected raw success rate: **49.21%**
- Selected benchmark-adjusted success rate: **47.93%**
- Non-selected benchmark-adjusted success rate: **50.14%**
- Benchmark coverage: **80.07%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 47.78% (270 eval); 100-199: 53.91% (653 eval); 200+: 48.54% (9714 eval)

## Return Horizons

- Close T+1 success rate: **39.12%**
- Close T+3 success rate: **41.28%**
- Close T+5 success rate: **42.65%**
- Excess T+1 success rate: **50.97%**
- Excess T+3 success rate: **47.52%**
- Excess T+5 success rate: **45.26%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
