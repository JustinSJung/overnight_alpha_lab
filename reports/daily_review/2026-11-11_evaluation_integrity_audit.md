# Evaluation Integrity Audit - 2026-11-11

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1253266**
- Unique evaluation keys: **43728**
- Duplicate rows by candidate key: **1209538**
- Duplicate rate: **96.51%**
- Exact same-day duplicate rows: **495346**
- Same stock_code + signal_date repeated keys: **42583**
- Same candidate re-evaluated across multiple files: **42584**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 216080 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 253450 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 216080 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 253450 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 253450 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 216080 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 216080 |  |  | 2026-07-20 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 253450 |  |  | 2026-07-20 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 004990 |  |  | 2026-07-20 |  | 65698458accec52f | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 397 | 196 | 201 | 49.37 | -0.0152 | 0.005 | 0.0007 |
| v2_conservative_ranker | 21227 | 10605 | 10622 | 49.96 | -0.002 | -0.0096 | -0.0143 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2149 | 920 | 1229 | 42.81 | -0.002 | -0.0115 | -0.0203 |
| avoid | 19078 | 9685 | 9393 | 50.77 | -0.002 | -0.0094 | -0.0136 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 603 | 266 | 337 | 44.11 | -0.0 | -0.0065 | -0.0073 |
| Top 20 | 1084 | 483 | 601 | 44.56 | -0.0008 | -0.0074 | -0.0085 |
| Top 50 | 1790 | 782 | 1008 | 43.69 | -0.0014 | -0.0082 | -0.012 |
| Top 100 | 2347 | 999 | 1348 | 42.56 | 0.0003 | -0.0054 | -0.0111 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 2123 | 1038 | 1085 | 48.89 | 21.62 | -0.002 | -0.0069 | -0.0046 |
| D2 | 2123 | 1099 | 1024 | 51.77 | 26.77 | -0.005 | -0.0161 | -0.0215 |
| D3 | 2122 | 1048 | 1074 | 49.39 | 29.03 | -0.001 | -0.0074 | -0.0139 |
| D4 | 2123 | 1051 | 1072 | 49.51 | 31.07 | -0.0016 | -0.0106 | -0.014 |
| D5 | 2123 | 1077 | 1046 | 50.73 | 32.96 | -0.0017 | -0.0087 | -0.0176 |
| D6 | 2122 | 1096 | 1026 | 51.65 | 34.73 | -0.0029 | -0.0101 | -0.0116 |
| D7 | 2123 | 1096 | 1027 | 51.63 | 36.4 | -0.002 | -0.0078 | -0.0114 |
| D8 | 2122 | 1103 | 1019 | 51.98 | 37.98 | -0.0004 | -0.0064 | -0.0105 |
| D9 | 2123 | 1089 | 1034 | 51.3 | 40.43 | -0.0009 | -0.0101 | -0.0169 |
| D10 | 2123 | 908 | 1215 | 42.77 | 65.63 | -0.002 | -0.0117 | -0.0207 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.3127 | 41.8795 | 0.5668 |
| volume_confirmation_score | -1.2816 | -1.0873 | 0.1943 |
| liquidity_score | 2.1448 | 2.0622 | -0.0826 |
| overextension_penalty | 0.913 | 0.7809 | -0.1321 |
| reversal_risk_penalty | 0.6999 | 0.674 | -0.026 |
| news_risk_penalty | 0.1012 | 0.1249 | 0.0238 |
| attention_noise_penalty | 0.2241 | 0.2397 | 0.0155 |
| market_regime_penalty | 0.0475 | 0.0458 | -0.0018 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **16283**
- Benchmark-adjusted coverage: **37.24%**
- Benchmark-adjusted success rate: **50.7%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261111.csv`
- Latest market index date: **2026-11-11**
- Latest price signal date: **2026-11-10**
- Latest candidate signal date: **2026-11-10**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **9**
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