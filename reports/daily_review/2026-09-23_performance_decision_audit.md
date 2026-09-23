# Performance Decision Audit - 2026-09-23

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.75%** (7456 evaluated)
- Benchmark-adjusted success rate: **51.15%** (6749 evaluated)
- Selected raw success rate: **44.94%**
- Non-selected raw success rate: **46.93%**
- Selected benchmark-adjusted success rate: **46.89%**
- Non-selected benchmark-adjusted success rate: **51.58%**
- Benchmark coverage: **90.52%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.69% (267 eval); 100-199: 53.21% (654 eval); 200+: 46.03% (6535 eval)

## Return Horizons

- Close T+1 success rate: **40.85%**
- Close T+3 success rate: **42.29%**
- Close T+5 success rate: **41.93%**
- Excess T+1 success rate: **47.3%**
- Excess T+3 success rate: **44.42%**
- Excess T+5 success rate: **44.18%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
