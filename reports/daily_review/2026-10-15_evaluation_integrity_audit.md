# Evaluation Integrity Audit - 2026-10-15

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **629206**
- Unique evaluation keys: **26507**
- Duplicate rows by candidate key: **602699**
- Duplicate rate: **95.79%**
- Exact same-day duplicate rows: **220420**
- Same stock_code + signal_date repeated keys: **25626**
- Same candidate re-evaluated across multiple files: **25627**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 347700 |  |  | 2026-07-20 |  | 88a6b82b07d4d16e | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 187870 |  |  | 2026-07-20 |  | d7198ed24f95f4db | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 405 | 200 | 205 | 49.38 | -0.0148 | 0.0062 | 0.0024 |
| v2_conservative_ranker | 11255 | 5624 | 5631 | 49.97 | -0.0017 | 0.001 | 0.0057 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1733 | 729 | 1004 | 42.07 | -0.0024 | -0.0118 | -0.0185 |
| avoid | 9522 | 4895 | 4627 | 51.41 | -0.0016 | 0.0035 | 0.0106 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 465 | 201 | 264 | 43.23 | -0.0006 | -0.0058 | -0.0042 |
| Top 20 | 843 | 372 | 471 | 44.13 | -0.001 | -0.0055 | -0.0058 |
| Top 50 | 1401 | 607 | 794 | 43.33 | -0.0012 | -0.0068 | -0.0097 |
| Top 100 | 1923 | 800 | 1123 | 41.6 | 0.0006 | -0.0041 | -0.0087 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1126 | 535 | 591 | 47.51 | 21.24 | -0.0008 | 0.0124 | 0.0281 |
| D2 | 1125 | 592 | 533 | 52.62 | 27.45 | -0.002 | 0.0076 | 0.0213 |
| D3 | 1126 | 565 | 561 | 50.18 | 30.29 | -0.0011 | 0.0068 | 0.0119 |
| D4 | 1125 | 580 | 545 | 51.56 | 32.47 | -0.0022 | 0.0026 | 0.0042 |
| D5 | 1126 | 589 | 537 | 52.31 | 34.38 | -0.0027 | 0.0009 | 0.0073 |
| D6 | 1125 | 581 | 544 | 51.64 | 36.1 | -0.0031 | 0.0007 | 0.005 |
| D7 | 1125 | 574 | 551 | 51.02 | 37.64 | 0.0006 | 0.0004 | 0.0061 |
| D8 | 1126 | 606 | 520 | 53.82 | 39.0 | -0.0013 | 0.0025 | 0.0056 |
| D9 | 1125 | 532 | 593 | 47.29 | 52.08 | -0.0025 | -0.0104 | -0.0086 |
| D10 | 1126 | 470 | 656 | 41.74 | 67.85 | -0.0022 | -0.0117 | -0.0213 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 44.0546 | 45.2959 | 1.2414 |
| volume_confirmation_score | -1.2682 | -1.0543 | 0.2139 |
| liquidity_score | 2.1483 | 2.0435 | -0.1048 |
| overextension_penalty | 1.3276 | 1.2796 | -0.048 |
| reversal_risk_penalty | 0.9007 | 0.8611 | -0.0396 |
| news_risk_penalty | 0.1392 | 0.1804 | 0.0412 |
| attention_noise_penalty | 0.2624 | 0.2767 | 0.0143 |
| market_regime_penalty | 0.0747 | 0.0689 | -0.0058 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **9460**
- Benchmark-adjusted coverage: **35.69%**
- Benchmark-adjusted success rate: **47.28%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261015.csv`
- Latest market index date: **2026-10-15**
- Latest price signal date: **2026-10-15**
- Latest candidate signal date: **2026-10-15**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **8**
- Eligible groups: **11**
- Groups close to activation: **3**
- Criteria: DART/error-note event_type groups, minimum 5 evaluated rows, neutral 45%-55% success gives zero adjustment.
- Finding: Some learned event rules are active.

## Dashboard Status Flags

- Duplicate status: **Possible duplicates**
- Benchmark status: **Partial**
- Ranking status: **Ranking inverted**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.