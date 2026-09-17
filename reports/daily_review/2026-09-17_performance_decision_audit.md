# Performance Decision Audit - 2026-09-17

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.3%** (6620 evaluated)
- Benchmark-adjusted success rate: **50.37%** (6285 evaluated)
- Selected raw success rate: **44.26%**
- Non-selected raw success rate: **46.5%**
- Selected benchmark-adjusted success rate: **47.09%**
- Non-selected benchmark-adjusted success rate: **50.72%**
- Benchmark coverage: **94.94%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.12% (266 eval); 100-199: 54.01% (661 eval); 200+: 45.32% (5693 eval)

## Return Horizons

- Close T+1 success rate: **40.82%**
- Close T+3 success rate: **42.2%**
- Close T+5 success rate: **42.64%**
- Excess T+1 success rate: **48.04%**
- Excess T+3 success rate: **49.21%**
- Excess T+5 success rate: **49.7%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
