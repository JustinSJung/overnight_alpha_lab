# Evaluation Integrity Audit - 2026-11-16

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1389829**
- Unique evaluation keys: **47220**
- Duplicate rows by candidate key: **1342609**
- Duplicate rate: **96.6%**
- Exact same-day duplicate rows: **559345**
- Same stock_code + signal_date repeated keys: **46046**
- Same candidate re-evaluated across multiple files: **46047**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 008930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 216080 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 253450 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 008930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 216080 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 253450 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 008930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 253450 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 216080 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 008930 |  |  | 2026-07-20 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 216080 |  |  | 2026-07-20 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 253450 |  |  | 2026-07-20 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260720.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 325 | 158 | 167 | 48.62 | -0.0111 | -0.003 | -0.0176 |
| v2_conservative_ranker | 23486 | 11618 | 11868 | 49.47 | -0.001 | -0.0037 | -0.0102 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2367 | 1016 | 1351 | 42.92 | -0.0019 | -0.0099 | -0.0191 |
| avoid | 21119 | 10602 | 10517 | 50.2 | -0.0009 | -0.0031 | -0.0092 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 621 | 263 | 358 | 42.35 | -0.0004 | -0.007 | -0.0071 |
| Top 20 | 1134 | 497 | 637 | 43.83 | -0.0005 | -0.0066 | -0.0071 |
| Top 50 | 1935 | 843 | 1092 | 43.57 | -0.0013 | -0.0068 | -0.0108 |
| Top 100 | 2560 | 1088 | 1472 | 42.5 | 0.0004 | -0.0038 | -0.0102 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 2349 | 1126 | 1223 | 47.94 | 21.41 | 0.0011 | 0.0071 | 0.007 |
| D2 | 2349 | 1172 | 1177 | 49.89 | 26.54 | -0.0021 | -0.0032 | -0.0116 |
| D3 | 2348 | 1166 | 1182 | 49.66 | 28.81 | -0.0003 | -0.0012 | -0.0098 |
| D4 | 2349 | 1149 | 1200 | 48.91 | 30.84 | -0.0005 | -0.0033 | -0.0097 |
| D5 | 2348 | 1181 | 1167 | 50.3 | 32.76 | -0.0009 | -0.0044 | -0.0138 |
| D6 | 2349 | 1201 | 1148 | 51.13 | 34.56 | -0.0021 | -0.0065 | -0.0099 |
| D7 | 2348 | 1217 | 1131 | 51.83 | 36.28 | -0.002 | -0.0047 | -0.0102 |
| D8 | 2349 | 1190 | 1159 | 50.66 | 37.92 | 0.0 | -0.0035 | -0.0082 |
| D9 | 2348 | 1209 | 1139 | 51.49 | 40.27 | -0.0007 | -0.0072 | -0.0145 |
| D10 | 2349 | 1007 | 1342 | 42.87 | 65.68 | -0.002 | -0.0101 | -0.0196 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.1731 | 41.6261 | 0.4529 |
| volume_confirmation_score | -1.2317 | -1.0404 | 0.1914 |
| liquidity_score | 2.1548 | 2.0869 | -0.068 |
| overextension_penalty | 0.924 | 0.8132 | -0.1108 |
| reversal_risk_penalty | 0.7004 | 0.6668 | -0.0335 |
| news_risk_penalty | 0.0978 | 0.1175 | 0.0197 |
| attention_noise_penalty | 0.221 | 0.2372 | 0.0162 |
| market_regime_penalty | 0.0475 | 0.0453 | -0.0022 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **17458**
- Benchmark-adjusted coverage: **36.97%**
- Benchmark-adjusted success rate: **51.49%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261116.csv`
- Latest market index date: **2026-11-16**
- Latest price signal date: **2026-11-13**
- Latest candidate signal date: **2026-11-13**
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