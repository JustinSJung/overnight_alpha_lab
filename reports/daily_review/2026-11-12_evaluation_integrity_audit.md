# Evaluation Integrity Audit - 2026-11-12

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1297620**
- Unique evaluation keys: **44883**
- Duplicate rows by candidate key: **1252737**
- Duplicate rate: **96.54%**
- Exact same-day duplicate rows: **516074**
- Same stock_code + signal_date repeated keys: **43727**
- Same candidate re-evaluated across multiple files: **43728**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 419540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 008930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 007980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 419540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 008930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 007980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 008930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 419540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 007980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 419540 |  |  | 2026-07-20 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 008930 |  |  | 2026-07-20 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 007980 |  |  | 2026-07-20 |  | 6bdf1cf3aa42e769 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 406 | 199 | 207 | 49.01 | -0.0136 | 0.01 | 0.0056 |
| v2_conservative_ranker | 22028 | 10763 | 11265 | 48.86 | -0.0009 | -0.0066 | -0.0136 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2233 | 962 | 1271 | 43.08 | -0.0016 | -0.0106 | -0.0195 |
| avoid | 19795 | 9801 | 9994 | 49.51 | -0.0008 | -0.0062 | -0.013 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 624 | 273 | 351 | 43.75 | 0.0003 | -0.006 | -0.0048 |
| Top 20 | 1121 | 496 | 625 | 44.25 | -0.0004 | -0.0071 | -0.0066 |
| Top 50 | 1854 | 808 | 1046 | 43.58 | -0.0009 | -0.0074 | -0.0108 |
| Top 100 | 2433 | 1036 | 1397 | 42.58 | 0.0008 | -0.0045 | -0.0109 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 2203 | 1028 | 1175 | 46.66 | 21.46 | 0.0015 | -0.0014 | -0.0044 |
| D2 | 2203 | 1079 | 1124 | 48.98 | 26.64 | -0.0018 | -0.007 | -0.0176 |
| D3 | 2203 | 1052 | 1151 | 47.75 | 28.9 | -0.0006 | -0.0052 | -0.0155 |
| D4 | 2202 | 1062 | 1140 | 48.23 | 30.93 | -0.0002 | -0.0071 | -0.0139 |
| D5 | 2203 | 1106 | 1097 | 50.2 | 32.83 | -0.0005 | -0.0059 | -0.0146 |
| D6 | 2203 | 1121 | 1082 | 50.89 | 34.64 | -0.0024 | -0.009 | -0.0124 |
| D7 | 2202 | 1117 | 1085 | 50.73 | 36.33 | -0.0015 | -0.0059 | -0.0116 |
| D8 | 2203 | 1127 | 1076 | 51.16 | 37.96 | -0.0005 | -0.0044 | -0.01 |
| D9 | 2203 | 1123 | 1080 | 50.98 | 40.41 | -0.0008 | -0.0092 | -0.0163 |
| D10 | 2203 | 948 | 1255 | 43.03 | 65.71 | -0.0017 | -0.0108 | -0.0196 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.3742 | 41.6466 | 0.2724 |
| volume_confirmation_score | -1.2614 | -1.0636 | 0.1978 |
| liquidity_score | 2.1482 | 2.0711 | -0.0771 |
| overextension_penalty | 0.9353 | 0.7984 | -0.1369 |
| reversal_risk_penalty | 0.7065 | 0.6822 | -0.0243 |
| news_risk_penalty | 0.0976 | 0.1223 | 0.0247 |
| attention_noise_penalty | 0.2214 | 0.2391 | 0.0177 |
| market_regime_penalty | 0.0476 | 0.0455 | -0.0021 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **17093**
- Benchmark-adjusted coverage: **38.08%**
- Benchmark-adjusted success rate: **51.56%**
- Benchmark rows available: **80**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261112.csv`
- Latest market index date: **2026-11-12**
- Latest price signal date: **2026-11-11**
- Latest candidate signal date: **2026-11-11**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **9**
- Eligible groups: **12**
- Groups close to activation: **6**
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