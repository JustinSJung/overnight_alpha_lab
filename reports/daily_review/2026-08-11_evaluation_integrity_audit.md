# Evaluation Integrity Audit - 2026-08-11

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **29480**
- Unique evaluation keys: **3491**
- Duplicate rows by candidate key: **25989**
- Duplicate rate: **88.16%**
- Exact same-day duplicate rows: **6462**
- Same stock_code + signal_date repeated keys: **2933**
- Same candidate re-evaluated across multiple files: **3042**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 008930 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 445bd57d12ab54d2 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 012160 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 2169107ccec3965e | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 036630 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 75dbf5263508de49 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 006730 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 0db69c5859b49a3e | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 065770 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | bba767a7e7a60e01 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 008930 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 445bd57d12ab54d2 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 012160 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 2169107ccec3965e | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 036630 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 75dbf5263508de49 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 006730 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 0db69c5859b49a3e | data/predictions/price_candidate_evaluation_20260712.csv | pending |
| 065770 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | bba767a7e7a60e01 | data/predictions/price_candidate_evaluation_20260712.csv | pending |
| 008930 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 445bd57d12ab54d2 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 012160 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 2169107ccec3965e | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 036630 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 75dbf5263508de49 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 006730 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 0db69c5859b49a3e | data/predictions/price_candidate_evaluation_20260713.csv | pending |
| 065770 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | bba767a7e7a60e01 | data/predictions/price_candidate_evaluation_20260713.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 6374 | 3296 | 3078 | 51.71 | -0.0128 | -0.0117 | -0.0356 |
| v2_conservative_ranker | 8875 | 3838 | 5037 | 43.25 | 0.0045 | -0.011 | -0.0328 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 575 | 295 | 280 | 51.3 | 0.0025 | -0.0171 | -0.0193 |
| avoid | 8300 | 3543 | 4757 | 42.69 | 0.0046 | -0.0107 | -0.0337 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 120 | 64 | 56 | 53.33 | 0.0088 | -0.0301 | -0.0611 |
| Top 20 | 240 | 138 | 102 | 57.5 | 0.0098 | -0.0097 | -0.0431 |
| Top 50 | 600 | 300 | 300 | 50.0 | 0.0071 | 0.0066 | -0.0091 |
| Top 100 | 1173 | 524 | 649 | 44.67 | 0.0089 | 0.0104 | -0.0091 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 888 | 403 | 485 | 45.38 | 16.74 | -0.0003 | -0.0025 | -0.0216 |
| D2 | 887 | 418 | 469 | 47.13 | 21.57 | -0.0033 | -0.0246 | -0.0627 |
| D3 | 888 | 328 | 560 | 36.94 | 24.58 | 0.0091 | 0.0032 | -0.0092 |
| D4 | 887 | 358 | 529 | 40.36 | 27.11 | 0.0117 | -0.0024 | -0.0409 |
| D5 | 888 | 369 | 519 | 41.55 | 29.41 | 0.0127 | -0.0078 | -0.0565 |
| D6 | 887 | 377 | 510 | 42.5 | 31.51 | 0.0033 | -0.003 | -0.0333 |
| D7 | 887 | 329 | 558 | 37.09 | 33.89 | 0.0089 | 0.0004 | -0.0266 |
| D8 | 888 | 409 | 479 | 46.06 | 35.9 | -0.0053 | -0.0426 | -0.0431 |
| D9 | 887 | 414 | 473 | 46.67 | 38.0 | 0.0003 | -0.0239 | -0.0253 |
| D10 | 888 | 433 | 455 | 48.76 | 57.07 | 0.0075 | -0.0066 | -0.0049 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 42.0922 | 39.5178 | -2.5743 |
| volume_confirmation_score | -0.5971 | -0.696 | -0.0988 |
| liquidity_score | 2.2981 | 2.0737 | -0.2244 |
| overextension_penalty | 1.887 | 0.9254 | -0.9616 |
| reversal_risk_penalty | 2.1883 | 1.5562 | -0.6321 |
| news_risk_penalty | 0.1376 | 0.0758 | -0.0617 |
| attention_noise_penalty | 0.2096 | 0.2283 | 0.0187 |
| market_regime_penalty | 0.0703 | 0.0584 | -0.012 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **8769**
- Benchmark-adjusted coverage: **29.75%**
- Benchmark-adjusted success rate: **51.43%**
- Benchmark rows available: **86**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260806.csv`
- Latest market index date: **2026-08-06**
- Latest price signal date: **2026-08-06**
- Latest candidate signal date: **2026-08-06**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **0**
- Eligible groups: **0**
- Groups close to activation: **0**
- Criteria: DART/error-note event_type groups, minimum 5 evaluated rows, neutral 45%-55% success gives zero adjustment.
- Finding: Learned rules are inactive because the updater learns from DART error_notes event_type groups, not price-candidate v2 outcomes, and current eligible groups are in the neutral adjustment band.

## Dashboard Status Flags

- Duplicate status: **Possible duplicates**
- Benchmark status: **Partial**
- Ranking status: **Ranking improving**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.