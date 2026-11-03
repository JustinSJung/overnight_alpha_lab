# Performance Decision Audit - 2026-11-03

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **48.23%** (17672 evaluated)
- Benchmark-adjusted success rate: **52.63%** (13604 evaluated)
- Selected raw success rate: **44.39%**
- Non-selected raw success rate: **48.46%**
- Selected benchmark-adjusted success rate: **49.73%**
- Non-selected benchmark-adjusted success rate: **52.75%**
- Benchmark coverage: **76.98%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.69% (267 eval); 100-199: 54.42% (667 eval); 200+: 47.98% (16738 eval)

## Return Horizons

- Close T+1 success rate: **40.1%**
- Close T+3 success rate: **37.06%**
- Close T+5 success rate: **35.59%**
- Excess T+1 success rate: **48.84%**
- Excess T+3 success rate: **49.94%**
- Excess T+5 success rate: **51.15%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
