# Evaluation Integrity Audit - 2026-10-27

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **869971**
- Unique evaluation keys: **33994**
- Duplicate rows by candidate key: **835977**
- Duplicate rate: **96.09%**
- Exact same-day duplicate rows: **322989**
- Same stock_code + signal_date repeated keys: **32962**
- Same candidate re-evaluated across multiple files: **32963**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 038530 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 216080 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 038530 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 216080 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 038530 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 216080 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 038530 |  |  | 2026-07-20 |  | a21abe17269c1a0d | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 216080 |  |  | 2026-07-20 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 405 | 201 | 204 | 49.63 | -0.0136 | 0.0104 | 0.0046 |
| v2_conservative_ranker | 15903 | 7861 | 8042 | 49.43 | -0.0011 | -0.0044 | -0.0048 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1831 | 770 | 1061 | 42.05 | -0.0024 | -0.0121 | -0.0209 |
| avoid | 14072 | 7091 | 6981 | 50.39 | -0.0009 | -0.0033 | -0.0024 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 531 | 226 | 305 | 42.56 | -0.0001 | -0.0058 | -0.0025 |
| Top 20 | 947 | 418 | 529 | 44.14 | -0.0006 | -0.0063 | -0.0052 |
| Top 50 | 1503 | 650 | 853 | 43.25 | -0.0014 | -0.0077 | -0.0106 |
| Top 100 | 2022 | 847 | 1175 | 41.89 | 0.0004 | -0.0053 | -0.0113 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1591 | 716 | 875 | 45.0 | 21.45 | 0.0013 | 0.0058 | 0.0217 |
| D2 | 1590 | 764 | 826 | 48.05 | 26.97 | 0.0006 | -0.0058 | -0.0076 |
| D3 | 1590 | 745 | 845 | 46.86 | 29.37 | 0.0019 | 0.0011 | -0.0005 |
| D4 | 1590 | 790 | 800 | 49.69 | 31.5 | -0.001 | -0.002 | -0.0025 |
| D5 | 1591 | 805 | 786 | 50.6 | 33.42 | -0.0016 | -0.0061 | -0.0104 |
| D6 | 1590 | 844 | 746 | 53.08 | 35.19 | -0.0049 | -0.0068 | -0.0041 |
| D7 | 1590 | 844 | 746 | 53.08 | 36.81 | -0.0006 | -0.0043 | -0.0049 |
| D8 | 1590 | 852 | 738 | 53.58 | 38.29 | -0.0025 | -0.0046 | -0.0052 |
| D9 | 1590 | 825 | 765 | 51.89 | 43.23 | -0.0015 | -0.0076 | -0.0109 |
| D10 | 1591 | 676 | 915 | 42.49 | 66.11 | -0.0026 | -0.0122 | -0.0209 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 42.6486 | 43.0864 | 0.4378 |
| volume_confirmation_score | -1.4396 | -1.264 | 0.1756 |
| liquidity_score | 2.1132 | 1.9994 | -0.1138 |
| overextension_penalty | 1.1757 | 1.0626 | -0.1131 |
| reversal_risk_penalty | 0.8007 | 0.7787 | -0.022 |
| news_risk_penalty | 0.1114 | 0.1339 | 0.0225 |
| attention_noise_penalty | 0.2441 | 0.2569 | 0.0128 |
| market_regime_penalty | 0.0522 | 0.0497 | -0.0024 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **13092**
- Benchmark-adjusted coverage: **38.51%**
- Benchmark-adjusted success rate: **50.73%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261027.csv`
- Latest market index date: **2026-10-27**
- Latest price signal date: **2026-10-27**
- Latest candidate signal date: **2026-10-27**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **8**
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