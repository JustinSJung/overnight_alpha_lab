# Performance Decision Audit - 2026-09-25

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.36%** (7735 evaluated)
- Benchmark-adjusted success rate: **51.56%** (6982 evaluated)
- Selected raw success rate: **44.96%**
- Non-selected raw success rate: **46.49%**
- Selected benchmark-adjusted success rate: **46.48%**
- Non-selected benchmark-adjusted success rate: **52.07%**
- Benchmark coverage: **90.27%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.36% (275 eval); 100-199: 54.14% (713 eval); 200+: 45.46% (6747 eval)

## Return Horizons

- Close T+1 success rate: **41.05%**
- Close T+3 success rate: **42.38%**
- Close T+5 success rate: **42.16%**
- Excess T+1 success rate: **46.72%**
- Excess T+3 success rate: **44.31%**
- Excess T+5 success rate: **43.85%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
