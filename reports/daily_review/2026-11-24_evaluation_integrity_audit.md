# Evaluation Integrity Audit - 2026-11-24

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1694995**
- Unique evaluation keys: **54410**
- Duplicate rows by candidate key: **1640585**
- Duplicate rate: **96.79%**
- Exact same-day duplicate rows: **702510**
- Same stock_code + signal_date repeated keys: **53190**
- Same candidate re-evaluated across multiple files: **53191**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 189330 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 189330 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 189330 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 189330 |  |  | 2026-07-20 |  | 36aaea07ab7c2d86 | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 003490 |  |  | 2026-07-20 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 259 | 131 | 128 | 50.58 | -0.0136 | -0.0151 | -0.0326 |
| v2_conservative_ranker | 26461 | 13561 | 12900 | 51.25 | -0.0032 | -0.0083 | -0.0132 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2738 | 1127 | 1611 | 41.16 | -0.0036 | -0.0114 | -0.0201 |
| avoid | 23723 | 12434 | 11289 | 52.41 | -0.0032 | -0.0079 | -0.0124 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 664 | 279 | 385 | 42.02 | -0.0012 | -0.0059 | -0.0049 |
| Top 20 | 1229 | 531 | 698 | 43.21 | -0.0014 | -0.0069 | -0.0069 |
| Top 50 | 2171 | 918 | 1253 | 42.28 | -0.0025 | -0.008 | -0.0118 |
| Top 100 | 2782 | 1140 | 1642 | 40.98 | -0.0023 | -0.0054 | -0.0095 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 2647 | 1329 | 1318 | 50.21 | 21.41 | -0.0023 | -0.0022 | -0.0002 |
| D2 | 2646 | 1397 | 1249 | 52.8 | 26.55 | -0.0057 | -0.0099 | -0.0156 |
| D3 | 2646 | 1358 | 1288 | 51.32 | 28.83 | -0.0029 | -0.0068 | -0.0118 |
| D4 | 2646 | 1367 | 1279 | 51.66 | 30.84 | -0.0031 | -0.0071 | -0.0118 |
| D5 | 2646 | 1397 | 1249 | 52.8 | 32.73 | -0.0032 | -0.0096 | -0.0155 |
| D6 | 2646 | 1414 | 1232 | 53.44 | 34.53 | -0.0034 | -0.0094 | -0.0131 |
| D7 | 2646 | 1434 | 1212 | 54.2 | 36.26 | -0.0042 | -0.0093 | -0.0149 |
| D8 | 2646 | 1385 | 1261 | 52.34 | 37.92 | -0.0012 | -0.006 | -0.0108 |
| D9 | 2646 | 1386 | 1260 | 52.38 | 40.69 | -0.0028 | -0.0107 | -0.0176 |
| D10 | 2646 | 1094 | 1552 | 41.35 | 66.03 | -0.0036 | -0.0113 | -0.0202 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 40.7739 | 41.8182 | 1.0443 |
| volume_confirmation_score | -1.1521 | -0.9473 | 0.2047 |
| liquidity_score | 2.1712 | 2.1006 | -0.0706 |
| overextension_penalty | 0.8596 | 0.7999 | -0.0598 |
| reversal_risk_penalty | 0.6921 | 0.6684 | -0.0237 |
| news_risk_penalty | 0.0911 | 0.1193 | 0.0282 |
| attention_noise_penalty | 0.2095 | 0.2411 | 0.0316 |
| market_regime_penalty | 0.0485 | 0.045 | -0.0036 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **19751**
- Benchmark-adjusted coverage: **36.3%**
- Benchmark-adjusted success rate: **51.73%**
- Benchmark rows available: **80**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261124.csv`
- Latest market index date: **2026-11-24**
- Latest price signal date: **2026-11-23**
- Latest candidate signal date: **2026-11-23**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **8**
- Eligible groups: **12**
- Groups close to activation: **5**
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