# Performance Decision Audit - 2026-10-05

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.72%** (8937 evaluated)
- Benchmark-adjusted success rate: **52.66%** (7303 evaluated)
- Selected raw success rate: **45.18%**
- Non-selected raw success rate: **46.85%**
- Selected benchmark-adjusted success rate: **42.63%**
- Non-selected benchmark-adjusted success rate: **53.59%**
- Benchmark coverage: **81.72%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.53% (272 eval); 100-199: 53.88% (683 eval); 200+: 46.04% (7982 eval)

## Return Horizons

- Close T+1 success rate: **42.05%**
- Close T+3 success rate: **43.33%**
- Close T+5 success rate: **42.8%**
- Excess T+1 success rate: **44.68%**
- Excess T+3 success rate: **43.14%**
- Excess T+5 success rate: **41.88%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
