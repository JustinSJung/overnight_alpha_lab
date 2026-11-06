# Evaluation Integrity Audit - 2026-11-06

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1127088**
- Unique evaluation keys: **40333**
- Duplicate rows by candidate key: **1086755**
- Duplicate rate: **96.42%**
- Exact same-day duplicate rows: **437875**
- Same stock_code + signal_date repeated keys: **39223**
- Same candidate re-evaluated across multiple files: **39224**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 065770 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 276730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 115480 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 065770 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 276730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 115480 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 065770 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 276730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 115480 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 065770 |  |  | 2026-07-20 |  | 63709cb8ab5628d0 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 276730 |  |  | 2026-07-20 |  | ab2530577956c747 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 115480 |  |  | 2026-07-20 |  | 99324e77405de44c | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 404 | 199 | 205 | 49.26 | -0.0134 | 0.0116 | 0.0078 |
| v2_conservative_ranker | 18961 | 9451 | 9510 | 49.84 | -0.0021 | -0.0061 | -0.0094 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1951 | 836 | 1115 | 42.85 | -0.002 | -0.0117 | -0.0202 |
| avoid | 17010 | 8615 | 8395 | 50.65 | -0.0021 | -0.0055 | -0.008 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 568 | 254 | 314 | 44.72 | 0.0013 | -0.0055 | -0.0055 |
| Top 20 | 1022 | 460 | 562 | 45.01 | 0.0002 | -0.0064 | -0.0065 |
| Top 50 | 1628 | 715 | 913 | 43.92 | -0.0008 | -0.0069 | -0.0102 |
| Top 100 | 2141 | 903 | 1238 | 42.18 | 0.0007 | -0.0051 | -0.0116 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1897 | 936 | 961 | 49.34 | 21.74 | -0.0035 | -0.001 | 0.0081 |
| D2 | 1896 | 964 | 932 | 50.84 | 26.98 | -0.0043 | -0.0092 | -0.0148 |
| D3 | 1896 | 913 | 983 | 48.15 | 29.27 | -0.0001 | -0.0019 | -0.0053 |
| D4 | 1896 | 943 | 953 | 49.74 | 31.35 | -0.0015 | -0.0043 | -0.0069 |
| D5 | 1896 | 962 | 934 | 50.74 | 33.24 | -0.0027 | -0.0061 | -0.0137 |
| D6 | 1896 | 984 | 912 | 51.9 | 34.98 | -0.0034 | -0.0076 | -0.0081 |
| D7 | 1896 | 984 | 912 | 51.9 | 36.61 | -0.001 | -0.0063 | -0.0112 |
| D8 | 1896 | 978 | 918 | 51.58 | 38.14 | -0.0011 | -0.0051 | -0.0067 |
| D9 | 1896 | 974 | 922 | 51.37 | 40.91 | -0.0012 | -0.0078 | -0.0132 |
| D10 | 1896 | 813 | 1083 | 42.88 | 65.59 | -0.0021 | -0.0117 | -0.0202 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.7909 | 42.2845 | 0.4936 |
| volume_confirmation_score | -1.3828 | -1.2339 | 0.1489 |
| liquidity_score | 2.1204 | 2.0199 | -0.1005 |
| overextension_penalty | 0.9893 | 0.8237 | -0.1655 |
| reversal_risk_penalty | 0.7201 | 0.666 | -0.054 |
| news_risk_penalty | 0.1046 | 0.1245 | 0.0199 |
| attention_noise_penalty | 0.2261 | 0.2504 | 0.0243 |
| market_regime_penalty | 0.0453 | 0.0452 | -0.0001 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **15430**
- Benchmark-adjusted coverage: **38.26%**
- Benchmark-adjusted success rate: **50.9%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261106.csv`
- Latest market index date: **2026-11-06**
- Latest price signal date: **2026-11-05**
- Latest candidate signal date: **2026-11-05**
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