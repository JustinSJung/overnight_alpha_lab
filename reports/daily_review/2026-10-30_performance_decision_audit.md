# Performance Decision Audit - 2026-10-30

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **49.18%** (16963 evaluated)
- Benchmark-adjusted success rate: **52.25%** (13631 evaluated)
- Selected raw success rate: **44.25%**
- Non-selected raw success rate: **49.48%**
- Selected benchmark-adjusted success rate: **50.58%**
- Non-selected benchmark-adjusted success rate: **52.33%**
- Benchmark coverage: **80.36%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.13% (268 eval); 100-199: 53.8% (658 eval); 200+: 49.01% (16037 eval)

## Return Horizons

- Close T+1 success rate: **39.61%**
- Close T+3 success rate: **37.73%**
- Close T+5 success rate: **36.02%**
- Excess T+1 success rate: **49.38%**
- Excess T+3 success rate: **49.93%**
- Excess T+5 success rate: **51.92%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
