# Performance Decision Audit - 2026-10-29

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **49.08%** (16974 evaluated)
- Benchmark-adjusted success rate: **52.13%** (13680 evaluated)
- Selected raw success rate: **44.07%**
- Non-selected raw success rate: **49.38%**
- Selected benchmark-adjusted success rate: **50.17%**
- Non-selected benchmark-adjusted success rate: **52.23%**
- Benchmark coverage: **80.59%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 47.79% (272 eval); 100-199: 53.34% (658 eval); 200+: 48.93% (16044 eval)

## Return Horizons

- Close T+1 success rate: **39.41%**
- Close T+3 success rate: **37.19%**
- Close T+5 success rate: **35.71%**
- Excess T+1 success rate: **49.46%**
- Excess T+3 success rate: **49.86%**
- Excess T+5 success rate: **51.96%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
