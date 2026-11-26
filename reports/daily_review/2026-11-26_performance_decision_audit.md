# Performance Decision Audit - 2026-11-26

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **50.85%** (28536 evaluated)
- Benchmark-adjusted success rate: **51.64%** (21470 evaluated)
- Selected raw success rate: **43.83%**
- Non-selected raw success rate: **51.18%**
- Selected benchmark-adjusted success rate: **52.24%**
- Non-selected benchmark-adjusted success rate: **51.62%**
- Benchmark coverage: **75.24%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 50.75% (201 eval); 100-199: 60.65% (277 eval); 200+: 50.76% (28058 eval)

## Return Horizons

- Close T+1 success rate: **39.4%**
- Close T+3 success rate: **35.63%**
- Close T+5 success rate: **33.81%**
- Excess T+1 success rate: **50.38%**
- Excess T+3 success rate: **52.99%**
- Excess T+5 success rate: **54.53%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
