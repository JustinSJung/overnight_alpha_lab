# Evaluation Integrity Audit - 2026-11-04

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1048589**
- Unique evaluation keys: **38123**
- Duplicate rows by candidate key: **1010466**
- Duplicate rate: **96.36%**
- Exact same-day duplicate rows: **402173**
- Same stock_code + signal_date repeated keys: **37028**
- Same candidate re-evaluated across multiple files: **37029**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 091590 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 064400 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 091590 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 064400 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 091590 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 064400 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 091590 |  |  | 2026-07-20 |  | 5bc402d6287954af | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 064400 |  |  | 2026-07-20 |  | 2e327c9a00465eab | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 406 | 201 | 205 | 49.51 | -0.0141 | 0.0092 | 0.004 |
| v2_conservative_ranker | 17948 | 8842 | 9106 | 49.26 | -0.0012 | -0.0045 | -0.0089 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1896 | 799 | 1097 | 42.14 | -0.0024 | -0.0115 | -0.0201 |
| avoid | 16052 | 8043 | 8009 | 50.11 | -0.0011 | -0.0037 | -0.0075 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 562 | 246 | 316 | 43.77 | 0.0008 | -0.0052 | -0.0043 |
| Top 20 | 1004 | 446 | 558 | 44.42 | -0.0001 | -0.0059 | -0.006 |
| Top 50 | 1569 | 678 | 891 | 43.21 | -0.0012 | -0.0069 | -0.0103 |
| Top 100 | 2099 | 877 | 1222 | 41.78 | 0.0006 | -0.0043 | -0.0104 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1795 | 860 | 935 | 47.91 | 21.7 | -0.0007 | 0.0038 | 0.008 |
| D2 | 1795 | 864 | 931 | 48.13 | 27.02 | -0.0005 | -0.0055 | -0.0131 |
| D3 | 1795 | 849 | 946 | 47.3 | 29.36 | 0.0009 | 0.0006 | -0.0059 |
| D4 | 1794 | 880 | 914 | 49.05 | 31.46 | -0.0008 | -0.0026 | -0.0076 |
| D5 | 1795 | 900 | 895 | 50.14 | 33.34 | -0.0017 | -0.0054 | -0.0125 |
| D6 | 1795 | 931 | 864 | 51.87 | 35.09 | -0.0031 | -0.0065 | -0.0076 |
| D7 | 1794 | 940 | 854 | 52.4 | 36.72 | -0.0014 | -0.005 | -0.0097 |
| D8 | 1795 | 946 | 849 | 52.7 | 38.22 | -0.0021 | -0.0059 | -0.0081 |
| D9 | 1795 | 912 | 883 | 50.81 | 41.55 | -0.0001 | -0.0065 | -0.0108 |
| D10 | 1795 | 760 | 1035 | 42.34 | 65.7 | -0.0025 | -0.0119 | -0.0205 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 42.1929 | 42.5803 | 0.3874 |
| volume_confirmation_score | -1.4037 | -1.2411 | 0.1626 |
| liquidity_score | 2.1186 | 2.0192 | -0.0994 |
| overextension_penalty | 1.0995 | 0.9454 | -0.1541 |
| reversal_risk_penalty | 0.7649 | 0.705 | -0.0599 |
| news_risk_penalty | 0.1068 | 0.128 | 0.0213 |
| attention_noise_penalty | 0.237 | 0.2508 | 0.0138 |
| market_regime_penalty | 0.0491 | 0.0481 | -0.001 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **14256**
- Benchmark-adjusted coverage: **37.39%**
- Benchmark-adjusted success rate: **51.86%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261104.csv`
- Latest market index date: **2026-11-04**
- Latest price signal date: **2026-11-03**
- Latest candidate signal date: **2026-11-03**
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