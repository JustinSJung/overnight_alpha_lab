# Performance Decision Audit - 2026-10-20

This audit is diagnostic only. It does not change candidate generation, ranking weights, or selected picks.

## Summary

- Raw success rate: **48.32%** (13306 evaluated)
- Benchmark-adjusted success rate: **46.98%** (10864 evaluated)
- Selected raw success rate: **44.55%**
- Non-selected raw success rate: **48.59%**
- Selected benchmark-adjusted success rate: **50.66%**
- Non-selected benchmark-adjusted success rate: **46.76%**
- Benchmark coverage: **81.65%**
- Diagnosis: **weak_or_mixed_signal**
- Public metric recommendation: **selected_group_benchmark_adjusted_success_rate**

## Interpretation

Raw success means the next-day close return was positive. Benchmark-adjusted success means the candidate beat the relevant market benchmark. In a weak market, raw returns can look poor while benchmark-adjusted results still show useful relative strength.

## Candidate Count Buckets

50-99: 48.29% (263 eval); 100-199: 52.5% (621 eval); 200+: 48.12% (12422 eval)

## Return Horizons

- Close T+1 success rate: **39.84%**
- Close T+3 success rate: **40.12%**
- Close T+5 success rate: **38.78%**
- Excess T+1 success rate: **53.31%**
- Excess T+3 success rate: **54.66%**
- Excess T+5 success rate: **54.91%**

## Decision Guardrail

Do not introduce a new ranker or tune score weights from this audit alone. Use it to decide whether public wording should emphasize raw candidate performance, selected group quality, or market-relative performance.
