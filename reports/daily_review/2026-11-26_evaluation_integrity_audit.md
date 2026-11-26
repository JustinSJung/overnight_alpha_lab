# Evaluation Integrity Audit - 2026-11-26

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1806445**
- Unique evaluation keys: **56871**
- Duplicate rows by candidate key: **1749574**
- Duplicate rate: **96.85%**
- Exact same-day duplicate rows: **755005**
- Same stock_code + signal_date repeated keys: **55636**
- Same candidate re-evaluated across multiple files: **55637**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 288980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 020560 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 288980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 020560 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 020560 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 288980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003490 |  |  | 2026-07-20 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 288980 |  |  | 2026-07-20 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 020560 |  |  | 2026-07-20 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260720.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 259 | 131 | 128 | 50.58 | -0.0136 | -0.0151 | -0.0326 |
| v2_conservative_ranker | 28277 | 14380 | 13897 | 50.85 | -0.0025 | -0.0087 | -0.014 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2864 | 1204 | 1660 | 42.04 | -0.0028 | -0.011 | -0.0205 |
| avoid | 25413 | 13176 | 12237 | 51.85 | -0.0025 | -0.0085 | -0.0132 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 688 | 292 | 396 | 42.44 | -0.0003 | -0.0066 | -0.0064 |
| Top 20 | 1276 | 561 | 715 | 43.97 | -0.0005 | -0.0065 | -0.0082 |
| Top 50 | 2288 | 992 | 1296 | 43.36 | -0.0016 | -0.0077 | -0.0122 |
| Top 100 | 2905 | 1219 | 1686 | 41.96 | -0.0018 | -0.006 | -0.0112 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 2828 | 1416 | 1412 | 50.07 | 21.31 | -0.0016 | -0.0031 | -0.0011 |
| D2 | 2828 | 1457 | 1371 | 51.52 | 26.45 | -0.0038 | -0.0112 | -0.0173 |
| D3 | 2827 | 1450 | 1377 | 51.29 | 28.68 | -0.0025 | -0.0084 | -0.0136 |
| D4 | 2828 | 1430 | 1398 | 50.57 | 30.67 | -0.0026 | -0.0073 | -0.0117 |
| D5 | 2828 | 1455 | 1373 | 51.45 | 32.55 | -0.0019 | -0.0106 | -0.0155 |
| D6 | 2827 | 1514 | 1313 | 53.56 | 34.36 | -0.0027 | -0.0094 | -0.014 |
| D7 | 2828 | 1503 | 1325 | 53.15 | 36.11 | -0.0039 | -0.0089 | -0.015 |
| D8 | 2827 | 1476 | 1351 | 52.21 | 37.81 | -0.0011 | -0.0073 | -0.0125 |
| D9 | 2828 | 1491 | 1337 | 52.72 | 40.17 | -0.0021 | -0.01 | -0.0175 |
| D10 | 2828 | 1188 | 1640 | 42.01 | 65.9 | -0.0029 | -0.0111 | -0.0206 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 40.5818 | 41.4658 | 0.884 |
| volume_confirmation_score | -1.1081 | -0.9339 | 0.1742 |
| liquidity_score | 2.181 | 2.1076 | -0.0734 |
| overextension_penalty | 0.8194 | 0.7628 | -0.0566 |
| reversal_risk_penalty | 0.6777 | 0.6611 | -0.0166 |
| news_risk_penalty | 0.0894 | 0.1161 | 0.0267 |
| attention_noise_penalty | 0.2091 | 0.2312 | 0.0221 |
| market_regime_penalty | 0.046 | 0.0426 | -0.0034 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **21470**
- Benchmark-adjusted coverage: **37.75%**
- Benchmark-adjusted success rate: **51.64%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261126.csv`
- Latest market index date: **2026-11-26**
- Latest price signal date: **2026-11-25**
- Latest candidate signal date: **2026-11-25**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **8**
- Eligible groups: **12**
- Groups close to activation: **4**
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