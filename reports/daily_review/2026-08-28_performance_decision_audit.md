# Performance Decision Audit - 2026-08-28

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **42.25%** (49647 evaluated)
- Benchmark-adjusted success rate: **51.89%** (45359 evaluated)
- Selected raw success rate: **49.45%**
- Non-selected raw success rate: **41.45%**
- Selected benchmark-adjusted success rate: **51.64%**
- Non-selected benchmark-adjusted success rate: **51.92%**
- Benchmark coverage: **91.36%**
- Diagnosis: **market_relative_signal_only**
- Public metric recommendation: **selected_group_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

200+: 42.25% (49647 eval)

## Return Horizons

- Close T+1 success rate: **44.59%**
- Close T+3 success rate: **47.74%**
- Close T+5 success rate: **48.55%**
- Excess T+1 success rate: **46.88%**
- Excess T+3 success rate: **48.63%**
- Excess T+5 success rate: **47.18%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
