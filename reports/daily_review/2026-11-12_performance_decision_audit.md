# Performance Decision Audit - 2026-11-12

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **48.86%** (22434 evaluated)
- Benchmark-adjusted success rate: **51.56%** (17093 evaluated)
- Selected raw success rate: **44.07%**
- Non-selected raw success rate: **49.12%**
- Selected benchmark-adjusted success rate: **48.75%**
- Non-selected benchmark-adjusted success rate: **51.66%**
- Benchmark coverage: **76.19%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 47.96% (269 eval); 100-199: 53.61% (664 eval); 200+: 48.73% (21501 eval)

## Return Horizons

- Close T+1 success rate: **40.45%**
- Close T+3 success rate: **36.79%**
- Close T+5 success rate: **34.19%**
- Excess T+1 success rate: **49.15%**
- Excess T+3 success rate: **52.2%**
- Excess T+5 success rate: **53.18%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
