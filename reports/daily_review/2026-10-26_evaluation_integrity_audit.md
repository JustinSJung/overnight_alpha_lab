# Evaluation Integrity Audit - 2026-10-26

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **836506**
- Unique evaluation keys: **32963**
- Duplicate rows by candidate key: **803543**
- Duplicate rate: **96.06%**
- Exact same-day duplicate rows: **308265**
- Same stock_code + signal_date repeated keys: **32000**
- Same candidate re-evaluated across multiple files: **32001**
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
| v1/unknown | 399 | 195 | 204 | 48.87 | -0.0131 | 0.0003 | -0.0098 |
| v2_conservative_ranker | 15178 | 7612 | 7566 | 50.15 | -0.0015 | -0.0035 | -0.0034 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1856 | 778 | 1078 | 41.92 | -0.0021 | -0.0116 | -0.0198 |
| avoid | 13322 | 6834 | 6488 | 51.3 | -0.0014 | -0.0023 | -0.0008 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 531 | 226 | 305 | 42.56 | 0.0 | -0.0053 | -0.0018 |
| Top 20 | 959 | 418 | 541 | 43.59 | -0.0001 | -0.0056 | -0.0038 |
| Top 50 | 1525 | 655 | 870 | 42.95 | -0.0009 | -0.0068 | -0.0092 |
| Top 100 | 2054 | 853 | 1201 | 41.53 | 0.0007 | -0.0044 | -0.0097 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1518 | 717 | 801 | 47.23 | 21.57 | -0.0009 | 0.0059 | 0.0232 |
| D2 | 1518 | 761 | 757 | 50.13 | 27.15 | -0.0003 | -0.0045 | -0.0053 |
| D3 | 1518 | 743 | 775 | 48.95 | 29.62 | 0.0004 | -0.0003 | -0.0018 |
| D4 | 1517 | 780 | 737 | 51.42 | 31.75 | -0.0017 | -0.0015 | -0.003 |
| D5 | 1518 | 787 | 731 | 51.84 | 33.65 | -0.0022 | -0.004 | -0.0071 |
| D6 | 1518 | 798 | 720 | 52.57 | 35.38 | -0.0044 | -0.0043 | -0.0006 |
| D7 | 1517 | 804 | 713 | 53.0 | 36.99 | -0.0006 | -0.0032 | -0.0027 |
| D8 | 1518 | 809 | 709 | 53.29 | 38.43 | -0.0019 | -0.0038 | -0.0041 |
| D9 | 1518 | 763 | 755 | 50.26 | 44.84 | -0.0016 | -0.0083 | -0.011 |
| D10 | 1518 | 650 | 868 | 42.82 | 66.45 | -0.0017 | -0.0104 | -0.019 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 42.7889 | 43.6061 | 0.8172 |
| volume_confirmation_score | -1.4264 | -1.2173 | 0.2091 |
| liquidity_score | 2.116 | 2.0011 | -0.1149 |
| overextension_penalty | 1.1785 | 1.0849 | -0.0936 |
| reversal_risk_penalty | 0.798 | 0.7873 | -0.0107 |
| news_risk_penalty | 0.1122 | 0.1479 | 0.0357 |
| attention_noise_penalty | 0.2458 | 0.2597 | 0.0139 |
| market_regime_penalty | 0.0547 | 0.0521 | -0.0026 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **12492**
- Benchmark-adjusted coverage: **37.9%**
- Benchmark-adjusted success rate: **48.05%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261026.csv`
- Latest market index date: **2026-10-26**
- Latest price signal date: **2026-10-26**
- Latest candidate signal date: **2026-10-26**
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