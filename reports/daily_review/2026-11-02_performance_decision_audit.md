# Performance Decision Audit - 2026-11-02

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **48.88%** (16319 evaluated)
- Benchmark-adjusted success rate: **52.14%** (12857 evaluated)
- Selected raw success rate: **43.74%**
- Non-selected raw success rate: **49.18%**
- Selected benchmark-adjusted success rate: **49.34%**
- Non-selected benchmark-adjusted success rate: **52.26%**
- Benchmark coverage: **78.79%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.65% (259 eval); 100-199: 52.72% (588 eval); 200+: 48.73% (15472 eval)

## Return Horizons

- Close T+1 success rate: **39.25%**
- Close T+3 success rate: **36.72%**
- Close T+5 success rate: **34.96%**
- Excess T+1 success rate: **49.07%**
- Excess T+3 success rate: **49.46%**
- Excess T+5 success rate: **52.03%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
