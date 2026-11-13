# Evaluation Integrity Audit - 2026-11-13

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1343138**
- Unique evaluation keys: **46047**
- Duplicate rows by candidate key: **1297091**
- Duplicate rate: **96.57%**
- Exact same-day duplicate rows: **537362**
- Same stock_code + signal_date repeated keys: **44882**
- Same candidate re-evaluated across multiple files: **44883**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 038530 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 008930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 038530 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 008930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 008930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 038530 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 038530 |  |  | 2026-07-20 |  | a21abe17269c1a0d | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 008930 |  |  | 2026-07-20 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 393 | 193 | 200 | 49.11 | -0.015 | 0.0057 | 0.006 |
| v2_conservative_ranker | 22533 | 11140 | 11393 | 49.44 | -0.001 | -0.0047 | -0.013 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2302 | 999 | 1303 | 43.4 | -0.0017 | -0.0095 | -0.0189 |
| avoid | 20231 | 10141 | 10090 | 50.13 | -0.0009 | -0.0042 | -0.0123 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 637 | 279 | 358 | 43.8 | 0.0006 | -0.0056 | -0.0047 |
| Top 20 | 1141 | 506 | 635 | 44.35 | 0.0 | -0.0058 | -0.0053 |
| Top 50 | 1906 | 837 | 1069 | 43.91 | -0.001 | -0.0064 | -0.0098 |
| Top 100 | 2483 | 1063 | 1420 | 42.81 | 0.0007 | -0.0034 | -0.01 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 2254 | 1067 | 1187 | 47.34 | 21.57 | 0.0014 | 0.0036 | -0.0001 |
| D2 | 2253 | 1125 | 1128 | 49.93 | 26.6 | -0.0018 | -0.0046 | -0.0176 |
| D3 | 2253 | 1104 | 1149 | 49.0 | 28.84 | -0.0009 | -0.0033 | -0.016 |
| D4 | 2253 | 1095 | 1158 | 48.6 | 30.87 | -0.0002 | -0.0038 | -0.0127 |
| D5 | 2254 | 1146 | 1108 | 50.84 | 32.78 | -0.0015 | -0.0047 | -0.0141 |
| D6 | 2253 | 1163 | 1090 | 51.62 | 34.59 | -0.0025 | -0.007 | -0.0118 |
| D7 | 2253 | 1159 | 1094 | 51.44 | 36.3 | -0.0019 | -0.0052 | -0.0129 |
| D8 | 2253 | 1150 | 1103 | 51.04 | 37.93 | -0.0003 | -0.0039 | -0.0092 |
| D9 | 2253 | 1153 | 1100 | 51.18 | 40.53 | -0.0003 | -0.0078 | -0.0158 |
| D10 | 2254 | 978 | 1276 | 43.39 | 65.79 | -0.0018 | -0.0097 | -0.019 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.2253 | 41.6252 | 0.3999 |
| volume_confirmation_score | -1.2448 | -1.051 | 0.1938 |
| liquidity_score | 2.1513 | 2.0806 | -0.0707 |
| overextension_penalty | 0.898 | 0.7921 | -0.1059 |
| reversal_risk_penalty | 0.6761 | 0.6616 | -0.0146 |
| news_risk_penalty | 0.0993 | 0.1242 | 0.0249 |
| attention_noise_penalty | 0.2257 | 0.2424 | 0.0167 |
| market_regime_penalty | 0.049 | 0.0474 | -0.0016 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **17739**
- Benchmark-adjusted coverage: **38.52%**
- Benchmark-adjusted success rate: **51.71%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261113.csv`
- Latest market index date: **2026-11-13**
- Latest price signal date: **2026-11-12**
- Latest candidate signal date: **2026-11-12**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **7**
- Eligible groups: **12**
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