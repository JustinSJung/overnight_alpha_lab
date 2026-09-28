# Evaluation Integrity Audit - 2026-09-28

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **366543**
- Unique evaluation keys: **17869**
- Duplicate rows by candidate key: **348674**
- Duplicate rate: **95.12%**
- Exact same-day duplicate rows: **114267**
- Same stock_code + signal_date repeated keys: **17080**
- Same candidate re-evaluated across multiple files: **17081**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 276730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 025980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 064400 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 276730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 025980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 064400 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 276730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 025980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 064400 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 276730 |  |  | 2026-07-20 |  | ab2530577956c747 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 025980 |  |  | 2026-07-20 |  | 331c322c17fab620 | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 415 | 205 | 210 | 49.4 | -0.014 | 0.0089 | 0.0031 |
| v2_conservative_ranker | 7661 | 3519 | 4142 | 45.93 | 0.0029 | 0.0087 | 0.0133 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1089 | 483 | 606 | 44.35 | 0.0001 | -0.0047 | -0.0079 |
| avoid | 6572 | 3036 | 3536 | 46.2 | 0.0033 | 0.0109 | 0.0168 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 379 | 178 | 201 | 46.97 | 0.0018 | -0.001 | 0.0026 |
| Top 20 | 673 | 307 | 366 | 45.62 | 0.0003 | -0.0043 | -0.0022 |
| Top 50 | 1031 | 460 | 571 | 44.62 | 0.0001 | -0.005 | -0.0075 |
| Top 100 | 1403 | 602 | 801 | 42.91 | 0.0031 | 0.0021 | -0.0006 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 767 | 347 | 420 | 45.24 | 19.72 | 0.0011 | 0.0142 | 0.028 |
| D2 | 766 | 351 | 415 | 45.82 | 26.3 | 0.0072 | 0.0203 | 0.034 |
| D3 | 766 | 344 | 422 | 44.91 | 29.59 | 0.0064 | 0.0161 | 0.0221 |
| D4 | 766 | 361 | 405 | 47.13 | 31.92 | 0.0016 | 0.0074 | 0.008 |
| D5 | 766 | 354 | 412 | 46.21 | 33.84 | 0.0023 | 0.0048 | 0.0052 |
| D6 | 766 | 362 | 404 | 47.26 | 35.6 | -0.0003 | 0.0105 | 0.0136 |
| D7 | 766 | 360 | 406 | 47.0 | 37.24 | 0.0043 | 0.0088 | 0.014 |
| D8 | 766 | 364 | 402 | 47.52 | 38.69 | 0.0039 | 0.0084 | 0.0133 |
| D9 | 766 | 330 | 436 | 43.08 | 49.26 | 0.0008 | -0.0005 | -0.0005 |
| D10 | 766 | 346 | 420 | 45.17 | 66.68 | 0.0012 | -0.0047 | -0.0082 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 45.0614 | 44.6505 | -0.4109 |
| volume_confirmation_score | -1.2047 | -1.0805 | 0.1242 |
| liquidity_score | 2.162 | 2.0145 | -0.1475 |
| overextension_penalty | 1.6989 | 1.3314 | -0.3675 |
| reversal_risk_penalty | 1.2301 | 1.0361 | -0.194 |
| news_risk_penalty | 0.1768 | 0.1939 | 0.0171 |
| attention_noise_penalty | 0.35 | 0.346 | -0.0039 |
| market_regime_penalty | 0.1029 | 0.0821 | -0.0208 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **7006**
- Benchmark-adjusted coverage: **39.21%**
- Benchmark-adjusted success rate: **51.36%**
- Benchmark rows available: **80**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260928.csv`
- Latest market index date: **2026-09-28**
- Latest price signal date: **2026-09-28**
- Latest candidate signal date: **2026-09-28**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **7**
- Eligible groups: **11**
- Groups close to activation: **1**
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