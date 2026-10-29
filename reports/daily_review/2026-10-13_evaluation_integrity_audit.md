# Evaluation Integrity Audit - 2026-10-13

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **578130**
- Unique evaluation keys: **24759**
- Duplicate rows by candidate key: **553371**
- Duplicate rate: **95.72%**
- Exact same-day duplicate rows: **200271**
- Same stock_code + signal_date repeated keys: **23904**
- Same candidate re-evaluated across multiple files: **23905**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 288980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 288980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 288980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 142760 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 288980 |  |  | 2026-07-20 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 142760 |  |  | 2026-07-20 |  | c16f76d404f3524f | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 404 | 200 | 204 | 49.5 | -0.0136 | 0.0098 | 0.0077 |
| v2_conservative_ranker | 10233 | 4996 | 5237 | 48.82 | -0.0008 | 0.0034 | 0.0086 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1685 | 708 | 977 | 42.02 | -0.0028 | -0.0113 | -0.0073 |
| avoid | 8548 | 4288 | 4260 | 50.16 | -0.0004 | 0.0063 | 0.0115 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 447 | 200 | 247 | 44.74 | -0.0003 | -0.0045 | -0.001 |
| Top 20 | 806 | 360 | 446 | 44.67 | -0.0009 | -0.0054 | -0.0026 |
| Top 50 | 1352 | 587 | 765 | 43.42 | -0.0015 | -0.0063 | -0.0048 |
| Top 100 | 1875 | 785 | 1090 | 41.87 | 0.0004 | -0.0034 | 0.0005 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1024 | 471 | 553 | 46.0 | 20.69 | 0.0005 | 0.0113 | 0.0258 |
| D2 | 1023 | 522 | 501 | 51.03 | 27.32 | 0.0007 | 0.0148 | 0.0242 |
| D3 | 1023 | 490 | 533 | 47.9 | 30.43 | 0.001 | 0.0084 | 0.0099 |
| D4 | 1023 | 515 | 508 | 50.34 | 32.66 | -0.0006 | 0.0053 | 0.0009 |
| D5 | 1024 | 533 | 491 | 52.05 | 34.57 | -0.0036 | 0.0003 | 0.0083 |
| D6 | 1023 | 518 | 505 | 50.64 | 36.26 | -0.0012 | 0.0064 | 0.0098 |
| D7 | 1023 | 503 | 520 | 49.17 | 37.79 | 0.0006 | 0.0029 | 0.0079 |
| D8 | 1023 | 537 | 486 | 52.49 | 39.16 | -0.0005 | 0.0029 | 0.009 |
| D9 | 1023 | 479 | 544 | 46.82 | 54.52 | -0.0031 | -0.0081 | 0.0 |
| D10 | 1024 | 428 | 596 | 41.8 | 68.14 | -0.0021 | -0.011 | -0.0136 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 44.8116 | 45.6367 | 0.8251 |
| volume_confirmation_score | -1.2159 | -1.0331 | 0.1827 |
| liquidity_score | 2.1593 | 2.0355 | -0.1238 |
| overextension_penalty | 1.4656 | 1.2953 | -0.1703 |
| reversal_risk_penalty | 0.9937 | 0.903 | -0.0908 |
| news_risk_penalty | 0.1533 | 0.1894 | 0.0361 |
| attention_noise_penalty | 0.2937 | 0.291 | -0.0027 |
| market_regime_penalty | 0.0893 | 0.0737 | -0.0156 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **8517**
- Benchmark-adjusted coverage: **34.4%**
- Benchmark-adjusted success rate: **49.98%**
- Benchmark rows available: **76**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261013.csv`
- Latest market index date: **2026-10-13**
- Latest price signal date: **2026-10-13**
- Latest candidate signal date: **2026-10-13**
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