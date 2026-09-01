# Performance Decision Audit - 2026-09-01

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **43.04%** (3520 evaluated)
- Benchmark-adjusted success rate: **49.68%** (3261 evaluated)
- Selected raw success rate: **45.84%**
- Non-selected raw success rate: **42.68%**
- Selected benchmark-adjusted success rate: **48.61%**
- Non-selected benchmark-adjusted success rate: **49.83%**
- Benchmark coverage: **92.64%**
- Diagnosis: **overall_pool_noisy_selected_group_promising**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.3% (265 eval); 100-199: 54.24% (625 eval); 200+: 39.85% (2630 eval)

## Return Horizons

- Close T+1 success rate: **42.63%**
- Close T+3 success rate: **46.91%**
- Close T+5 success rate: **47.76%**
- Excess T+1 success rate: **48.08%**
- Excess T+3 success rate: **47.48%**
- Excess T+5 success rate: **45.64%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
