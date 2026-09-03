# Performance Decision Audit - 2026-09-03

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **44.75%** (4000 evaluated)
- Benchmark-adjusted success rate: **50.23%** (3741 evaluated)
- Selected raw success rate: **45.21%**
- Non-selected raw success rate: **44.69%**
- Selected benchmark-adjusted success rate: **48.86%**
- Non-selected benchmark-adjusted success rate: **50.41%**
- Benchmark coverage: **93.53%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.54% (274 eval); 100-199: 54.49% (690 eval); 200+: 42.19% (3036 eval)

## Return Horizons

- Close T+1 success rate: **41.22%**
- Close T+3 success rate: **45.06%**
- Close T+5 success rate: **46.89%**
- Excess T+1 success rate: **48.3%**
- Excess T+3 success rate: **50.06%**
- Excess T+5 success rate: **47.21%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
