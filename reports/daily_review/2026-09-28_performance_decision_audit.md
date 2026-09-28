# Performance Decision Audit - 2026-09-28

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **46.11%** (8076 evaluated)
- Benchmark-adjusted success rate: **51.36%** (7006 evaluated)
- Selected raw success rate: **45.58%**
- Non-selected raw success rate: **46.16%**
- Selected benchmark-adjusted success rate: **45.32%**
- Non-selected benchmark-adjusted success rate: **51.95%**
- Benchmark coverage: **86.75%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.36% (275 eval); 100-199: 54.14% (713 eval); 200+: 45.22% (7088 eval)

## Return Horizons

- Close T+1 success rate: **41.96%**
- Close T+3 success rate: **42.75%**
- Close T+5 success rate: **42.23%**
- Excess T+1 success rate: **47.05%**
- Excess T+3 success rate: **45.18%**
- Excess T+5 success rate: **42.51%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
