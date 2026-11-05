# Evaluation Integrity Audit - 2026-11-05

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1087284**
- Unique evaluation keys: **39224**
- Duplicate rows by candidate key: **1048060**
- Duplicate rate: **96.39%**
- Exact same-day duplicate rows: **419890**
- Same stock_code + signal_date repeated keys: **38122**
- Same candidate re-evaluated across multiple files: **38123**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 068240 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 068240 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 068240 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 011930 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 068240 |  |  | 2026-07-20 |  | eb4fc4f1f3913c40 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 011930 |  |  | 2026-07-20 |  | 65a793d7f669e415 | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 406 | 201 | 205 | 49.51 | -0.0136 | -0.0017 | -0.0124 |
| v2_conservative_ranker | 18668 | 9109 | 9559 | 48.79 | -0.0009 | -0.0048 | -0.0096 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1939 | 820 | 1119 | 42.29 | -0.0019 | -0.0116 | -0.0206 |
| avoid | 16729 | 8289 | 8440 | 49.55 | -0.0008 | -0.004 | -0.0082 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 567 | 248 | 319 | 43.74 | 0.0011 | -0.0062 | -0.0056 |
| Top 20 | 1013 | 446 | 567 | 44.03 | 0.0001 | -0.0064 | -0.0066 |
| Top 50 | 1613 | 700 | 913 | 43.4 | -0.0008 | -0.0071 | -0.0108 |
| Top 100 | 2151 | 897 | 1254 | 41.7 | 0.0008 | -0.0048 | -0.0112 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1867 | 879 | 988 | 47.08 | 21.51 | -0.0008 | 0.0017 | 0.0055 |
| D2 | 1867 | 907 | 960 | 48.58 | 26.96 | -0.0011 | -0.006 | -0.0139 |
| D3 | 1867 | 872 | 995 | 46.71 | 29.31 | 0.0018 | 0.0004 | -0.0062 |
| D4 | 1866 | 897 | 969 | 48.07 | 31.41 | -0.0004 | -0.0024 | -0.0078 |
| D5 | 1867 | 935 | 932 | 50.08 | 33.29 | -0.002 | -0.006 | -0.0146 |
| D6 | 1867 | 959 | 908 | 51.37 | 35.04 | -0.0024 | -0.0064 | -0.0075 |
| D7 | 1866 | 970 | 896 | 51.98 | 36.68 | -0.001 | -0.0056 | -0.0103 |
| D8 | 1867 | 953 | 914 | 51.04 | 38.19 | -0.001 | -0.0052 | -0.0079 |
| D9 | 1867 | 945 | 922 | 50.62 | 41.13 | 0.0 | -0.0061 | -0.0115 |
| D10 | 1867 | 792 | 1075 | 42.42 | 65.63 | -0.0021 | -0.0118 | -0.0208 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 42.1084 | 42.4142 | 0.3058 |
| volume_confirmation_score | -1.3954 | -1.2356 | 0.1599 |
| liquidity_score | 2.1198 | 2.0155 | -0.1043 |
| overextension_penalty | 1.0713 | 0.8887 | -0.1826 |
| reversal_risk_penalty | 0.7773 | 0.7113 | -0.066 |
| news_risk_penalty | 0.1059 | 0.1276 | 0.0217 |
| attention_noise_penalty | 0.2438 | 0.2455 | 0.0017 |
| market_regime_penalty | 0.0503 | 0.0456 | -0.0047 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **14866**
- Benchmark-adjusted coverage: **37.9%**
- Benchmark-adjusted success rate: **51.86%**
- Benchmark rows available: **80**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261105.csv`
- Latest market index date: **2026-11-05**
- Latest price signal date: **2026-11-04**
- Latest candidate signal date: **2026-11-04**
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