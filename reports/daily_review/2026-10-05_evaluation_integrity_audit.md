# Evaluation Integrity Audit - 2026-10-05

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **443327**
- Unique evaluation keys: **20358**
- Duplicate rows by candidate key: **422969**
- Duplicate rate: **95.41%**
- Exact same-day duplicate rows: **145449**
- Same stock_code + signal_date repeated keys: **20357**
- Same candidate re-evaluated across multiple files: **20358**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 189330 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 419540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 189330 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 419540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 189330 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 419540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 013520 |  |  | 2026-07-20 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 189330 |  |  | 2026-07-20 |  | 36aaea07ab7c2d86 | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 419540 |  |  | 2026-07-20 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 408 | 201 | 207 | 49.26 | -0.0139 | 0.0084 | 0.0021 |
| v2_conservative_ranker | 8529 | 3974 | 4555 | 46.59 | 0.0021 | 0.0075 | 0.0111 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1213 | 546 | 667 | 45.01 | 0.0009 | -0.0012 | -0.0039 |
| avoid | 7316 | 3428 | 3888 | 46.86 | 0.0023 | 0.0089 | 0.0136 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 401 | 187 | 214 | 46.63 | 0.0018 | 0.0013 | 0.0048 |
| Top 20 | 721 | 326 | 395 | 45.21 | 0.0006 | -0.0018 | -0.0003 |
| Top 50 | 1142 | 519 | 623 | 45.45 | 0.001 | -0.002 | -0.0045 |
| Top 100 | 1513 | 659 | 854 | 43.56 | 0.0033 | 0.0036 | 0.001 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 853 | 387 | 466 | 45.37 | 20.03 | -0.0013 | 0.0109 | 0.0265 |
| D2 | 853 | 390 | 463 | 45.72 | 26.61 | 0.0072 | 0.016 | 0.0271 |
| D3 | 853 | 370 | 483 | 43.38 | 29.87 | 0.0054 | 0.0139 | 0.0163 |
| D4 | 853 | 416 | 437 | 48.77 | 32.13 | 0.0003 | 0.0066 | 0.0054 |
| D5 | 853 | 420 | 433 | 49.24 | 34.02 | 0.0007 | 0.0063 | 0.0075 |
| D6 | 852 | 399 | 453 | 46.83 | 35.73 | -0.0009 | 0.0058 | 0.0075 |
| D7 | 853 | 402 | 451 | 47.13 | 37.3 | 0.0037 | 0.0084 | 0.0106 |
| D8 | 853 | 415 | 438 | 48.65 | 38.69 | 0.0033 | 0.0074 | 0.0103 |
| D9 | 853 | 385 | 468 | 45.13 | 49.2 | 0.001 | 0.0002 | 0.0025 |
| D10 | 853 | 390 | 463 | 45.72 | 66.62 | 0.0018 | -0.001 | -0.0039 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 44.8717 | 44.4877 | -0.384 |
| volume_confirmation_score | -1.271 | -1.1344 | 0.1366 |
| liquidity_score | 2.1497 | 2.0134 | -0.1363 |
| overextension_penalty | 1.5803 | 1.288 | -0.2923 |
| reversal_risk_penalty | 1.1428 | 0.9639 | -0.1789 |
| news_risk_penalty | 0.1663 | 0.1855 | 0.0192 |
| attention_noise_penalty | 0.3091 | 0.3236 | 0.0145 |
| market_regime_penalty | 0.1017 | 0.0821 | -0.0196 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **7303**
- Benchmark-adjusted coverage: **35.87%**
- Benchmark-adjusted success rate: **52.66%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261005.csv`
- Latest market index date: **2026-10-02**
- Latest price signal date: **2026-10-02**
- Latest candidate signal date: **2026-10-02**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **7**
- Eligible groups: **11**
- Groups close to activation: **2**
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