# Evaluation Integrity Audit - 2026-11-10

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1210067**
- Unique evaluation keys: **42584**
- Duplicate rows by candidate key: **1167483**
- Duplicate rate: **96.48%**
- Exact same-day duplicate rows: **475491**
- Same stock_code + signal_date repeated keys: **41452**
- Same candidate re-evaluated across multiple files: **41453**
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
| v1/unknown | 402 | 197 | 205 | 49.0 | -0.0138 | 0.01 | 0.0043 |
| v2_conservative_ranker | 20437 | 10405 | 10032 | 50.91 | -0.0031 | -0.0095 | -0.0137 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2089 | 881 | 1208 | 42.17 | -0.0022 | -0.0114 | -0.0203 |
| avoid | 18348 | 9524 | 8824 | 51.91 | -0.0032 | -0.0093 | -0.0129 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 599 | 264 | 335 | 44.07 | 0.001 | -0.0049 | -0.0049 |
| Top 20 | 1068 | 471 | 597 | 44.1 | -0.0002 | -0.0058 | -0.0065 |
| Top 50 | 1743 | 751 | 992 | 43.09 | -0.0015 | -0.0074 | -0.0112 |
| Top 100 | 2284 | 955 | 1329 | 41.81 | 0.0002 | -0.0053 | -0.0116 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 2044 | 1026 | 1018 | 50.2 | 21.7 | -0.0036 | -0.0079 | -0.0035 |
| D2 | 2044 | 1085 | 959 | 53.08 | 26.8 | -0.0065 | -0.0162 | -0.0204 |
| D3 | 2043 | 1041 | 1002 | 50.95 | 29.08 | -0.0028 | -0.0066 | -0.012 |
| D4 | 2044 | 1055 | 989 | 51.61 | 31.15 | -0.0034 | -0.0104 | -0.0155 |
| D5 | 2044 | 1056 | 988 | 51.66 | 33.05 | -0.0032 | -0.0089 | -0.017 |
| D6 | 2043 | 1082 | 961 | 52.96 | 34.83 | -0.0042 | -0.0102 | -0.0111 |
| D7 | 2044 | 1075 | 969 | 52.59 | 36.48 | -0.0024 | -0.0076 | -0.0118 |
| D8 | 2043 | 1067 | 976 | 52.23 | 38.05 | -0.0014 | -0.0069 | -0.0091 |
| D9 | 2044 | 1055 | 989 | 51.61 | 40.66 | -0.001 | -0.0093 | -0.016 |
| D10 | 2044 | 863 | 1181 | 42.22 | 65.68 | -0.0024 | -0.0115 | -0.0204 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.3341 | 42.3347 | 1.0006 |
| volume_confirmation_score | -1.2973 | -1.1578 | 0.1395 |
| liquidity_score | 2.1403 | 2.0362 | -0.1041 |
| overextension_penalty | 0.9368 | 0.8692 | -0.0676 |
| reversal_risk_penalty | 0.7092 | 0.6975 | -0.0117 |
| news_risk_penalty | 0.1008 | 0.1272 | 0.0264 |
| attention_noise_penalty | 0.2213 | 0.2444 | 0.0231 |
| market_regime_penalty | 0.0461 | 0.0459 | -0.0003 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **15832**
- Benchmark-adjusted coverage: **37.18%**
- Benchmark-adjusted success rate: **49.68%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261110.csv`
- Latest market index date: **2026-11-10**
- Latest price signal date: **2026-11-09**
- Latest candidate signal date: **2026-11-09**
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