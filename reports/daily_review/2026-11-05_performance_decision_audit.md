# Performance Decision Audit - 2026-11-05

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **48.81%** (19074 evaluated)
- Benchmark-adjusted success rate: **51.86%** (14866 evaluated)
- Selected raw success rate: **43.84%**
- Non-selected raw success rate: **49.09%**
- Selected benchmark-adjusted success rate: **49.66%**
- Non-selected benchmark-adjusted success rate: **51.95%**
- Benchmark coverage: **77.94%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **overall_candidate_pool_with_market_relative_context**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.53% (272 eval); 100-199: 53.28% (685 eval); 200+: 48.64% (18117 eval)

## Return Horizons

- Close T+1 success rate: **39.93%**
- Close T+3 success rate: **37.31%**
- Close T+5 success rate: **35.37%**
- Excess T+1 success rate: **49.35%**
- Excess T+3 success rate: **50.32%**
- Excess T+5 success rate: **50.7%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
