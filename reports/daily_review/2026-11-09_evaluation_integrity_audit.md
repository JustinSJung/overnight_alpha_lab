# Evaluation Integrity Audit - 2026-11-09

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1168012**
- Unique evaluation keys: **41453**
- Duplicate rows by candidate key: **1126559**
- Duplicate rate: **96.45%**
- Exact same-day duplicate rows: **456248**
- Same stock_code + signal_date repeated keys: **40332**
- Same candidate re-evaluated across multiple files: **40333**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 115480 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 068240 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 115480 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 068240 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 068240 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 115480 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003490 |  |  | 2026-07-20 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 115480 |  |  | 2026-07-20 |  | 99324e77405de44c | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 068240 |  |  | 2026-07-20 |  | eb4fc4f1f3913c40 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 395 | 196 | 199 | 49.62 | -0.0136 | 0.0089 | 0.0039 |
| v2_conservative_ranker | 19799 | 10087 | 9712 | 50.95 | -0.0032 | -0.0074 | -0.0113 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2026 | 868 | 1158 | 42.84 | -0.0018 | -0.0109 | -0.0199 |
| avoid | 17773 | 9219 | 8554 | 51.87 | -0.0034 | -0.0069 | -0.0103 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 598 | 266 | 332 | 44.48 | 0.0012 | -0.005 | -0.0055 |
| Top 20 | 1065 | 479 | 586 | 44.98 | 0.0006 | -0.0054 | -0.0058 |
| Top 50 | 1702 | 745 | 957 | 43.77 | -0.0009 | -0.0066 | -0.0102 |
| Top 100 | 2215 | 939 | 1276 | 42.39 | 0.0007 | -0.0045 | -0.0107 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1980 | 999 | 981 | 50.45 | 21.58 | -0.0056 | -0.0035 | 0.0023 |
| D2 | 1980 | 1068 | 912 | 53.94 | 26.83 | -0.0069 | -0.0102 | -0.0147 |
| D3 | 1980 | 978 | 1002 | 49.39 | 29.12 | -0.0015 | -0.0023 | -0.0076 |
| D4 | 1980 | 1014 | 966 | 51.21 | 31.2 | -0.0039 | -0.0076 | -0.012 |
| D5 | 1980 | 1028 | 952 | 51.92 | 33.08 | -0.0032 | -0.0082 | -0.0158 |
| D6 | 1979 | 1041 | 938 | 52.6 | 34.85 | -0.0038 | -0.0089 | -0.0097 |
| D7 | 1980 | 1051 | 929 | 53.08 | 36.52 | -0.0025 | -0.0059 | -0.01 |
| D8 | 1980 | 1031 | 949 | 52.07 | 38.08 | -0.0013 | -0.0058 | -0.0086 |
| D9 | 1980 | 1029 | 951 | 51.97 | 40.74 | -0.0015 | -0.0098 | -0.0161 |
| D10 | 1980 | 848 | 1132 | 42.83 | 65.68 | -0.002 | -0.011 | -0.0199 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.5069 | 42.406 | 0.8991 |
| volume_confirmation_score | -1.3353 | -1.1995 | 0.1359 |
| liquidity_score | 2.1322 | 2.0272 | -0.105 |
| overextension_penalty | 0.9674 | 0.8955 | -0.0719 |
| reversal_risk_penalty | 0.7164 | 0.6956 | -0.0209 |
| news_risk_penalty | 0.1 | 0.1292 | 0.0292 |
| attention_noise_penalty | 0.2345 | 0.2483 | 0.0139 |
| market_regime_penalty | 0.0488 | 0.0465 | -0.0022 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **15374**
- Benchmark-adjusted coverage: **37.09%**
- Benchmark-adjusted success rate: **49.94%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261109.csv`
- Latest market index date: **2026-11-09**
- Latest price signal date: **2026-11-06**
- Latest candidate signal date: **2026-11-06**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **10**
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