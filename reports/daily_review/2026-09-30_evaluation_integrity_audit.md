# Evaluation Integrity Audit - 2026-09-30

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **403669**
- Unique evaluation keys: **19509**
- Duplicate rows by candidate key: **384160**
- Duplicate rate: **95.17%**
- Exact same-day duplicate rows: **129186**
- Same stock_code + signal_date repeated keys: **18674**
- Same candidate re-evaluated across multiple files: **18675**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 101970 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 068240 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 049950 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 101970 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 068240 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 049950 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 101970 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 068240 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 049950 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 101970 |  |  | 2026-07-20 |  | dd1b5a251ebc1581 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 068240 |  |  | 2026-07-20 |  | eb4fc4f1f3913c40 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 399 | 198 | 201 | 49.62 | -0.0137 | 0.0103 | 0.0064 |
| v2_conservative_ranker | 8076 | 3754 | 4322 | 46.48 | 0.002 | 0.0072 | 0.0112 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1137 | 500 | 637 | 43.98 | 0.0001 | -0.0036 | -0.0069 |
| avoid | 6939 | 3254 | 3685 | 46.89 | 0.0023 | 0.0089 | 0.0142 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 380 | 177 | 203 | 46.58 | 0.0015 | -0.0018 | 0.0021 |
| Top 20 | 685 | 308 | 377 | 44.96 | 0.0 | -0.0038 | -0.0018 |
| Top 50 | 1069 | 474 | 595 | 44.34 | 0.0001 | -0.004 | -0.0064 |
| Top 100 | 1426 | 607 | 819 | 42.57 | 0.0029 | 0.0026 | 0.0006 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 808 | 370 | 438 | 45.79 | 20.17 | -0.001 | 0.0161 | 0.0303 |
| D2 | 808 | 376 | 432 | 46.53 | 26.68 | 0.0069 | 0.0142 | 0.0259 |
| D3 | 807 | 355 | 452 | 43.99 | 29.9 | 0.0051 | 0.0133 | 0.0169 |
| D4 | 808 | 392 | 416 | 48.51 | 32.17 | 0.0003 | 0.0061 | 0.0014 |
| D5 | 807 | 389 | 418 | 48.2 | 34.06 | 0.0009 | 0.0061 | 0.0113 |
| D6 | 808 | 381 | 427 | 47.15 | 35.75 | -0.0011 | 0.0056 | 0.0087 |
| D7 | 807 | 388 | 419 | 48.08 | 37.32 | 0.0031 | 0.0061 | 0.0114 |
| D8 | 808 | 385 | 423 | 47.65 | 38.7 | 0.0037 | 0.0072 | 0.0113 |
| D9 | 807 | 357 | 450 | 44.24 | 48.91 | 0.0011 | -0.0002 | -0.0015 |
| D10 | 808 | 361 | 447 | 44.68 | 66.46 | 0.0008 | -0.0035 | -0.0068 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 44.8529 | 44.6813 | -0.1716 |
| volume_confirmation_score | -1.2741 | -1.1321 | 0.1421 |
| liquidity_score | 2.1489 | 2.0099 | -0.139 |
| overextension_penalty | 1.6313 | 1.3382 | -0.2931 |
| reversal_risk_penalty | 1.1597 | 0.9898 | -0.1699 |
| news_risk_penalty | 0.1636 | 0.1883 | 0.0248 |
| attention_noise_penalty | 0.3272 | 0.3156 | -0.0116 |
| market_regime_penalty | 0.1023 | 0.0838 | -0.0185 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **7200**
- Benchmark-adjusted coverage: **36.91%**
- Benchmark-adjusted success rate: **51.58%**
- Benchmark rows available: **80**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260930.csv`
- Latest market index date: **2026-09-30**
- Latest price signal date: **2026-09-30**
- Latest candidate signal date: **2026-09-30**
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
- Ranking status: **Ranking weak**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.