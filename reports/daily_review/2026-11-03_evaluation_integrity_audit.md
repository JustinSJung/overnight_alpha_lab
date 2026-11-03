# Evaluation Integrity Audit - 2026-11-03

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1010995**
- Unique evaluation keys: **37029**
- Duplicate rows by candidate key: **973966**
- Duplicate rate: **96.34%**
- Exact same-day duplicate rows: **385274**
- Same stock_code + signal_date repeated keys: **36016**
- Same candidate re-evaluated across multiple files: **36017**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 010960 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 023440 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 010960 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 023440 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010960 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 023440 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010960 |  |  | 2026-07-20 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 006730 |  |  | 2026-07-20 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 023440 |  |  | 2026-07-20 |  | b0166524146063a5 | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 401 | 196 | 205 | 48.88 | -0.0136 | 0.0078 | 0.0009 |
| v2_conservative_ranker | 17271 | 8328 | 8943 | 48.22 | -0.0004 | -0.0053 | -0.0086 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1835 | 776 | 1059 | 42.29 | -0.0021 | -0.0122 | -0.0208 |
| avoid | 15436 | 7552 | 7884 | 48.92 | -0.0002 | -0.0045 | -0.007 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 547 | 241 | 306 | 44.06 | 0.0009 | -0.0056 | -0.0041 |
| Top 20 | 971 | 433 | 538 | 44.59 | -0.0 | -0.006 | -0.0057 |
| Top 50 | 1516 | 660 | 856 | 43.54 | -0.0008 | -0.0077 | -0.0109 |
| Top 100 | 2029 | 852 | 1177 | 41.99 | 0.0007 | -0.0056 | -0.0116 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1728 | 786 | 942 | 45.49 | 21.44 | 0.0015 | 0.0031 | 0.0095 |
| D2 | 1727 | 814 | 913 | 47.13 | 26.97 | -0.0002 | -0.0071 | -0.0127 |
| D3 | 1727 | 787 | 940 | 45.57 | 29.34 | 0.0026 | -0.0003 | -0.0045 |
| D4 | 1727 | 820 | 907 | 47.48 | 31.44 | 0.0002 | -0.0038 | -0.0076 |
| D5 | 1727 | 851 | 876 | 49.28 | 33.34 | -0.0011 | -0.0069 | -0.013 |
| D6 | 1727 | 878 | 849 | 50.84 | 35.11 | -0.0025 | -0.0067 | -0.0063 |
| D7 | 1727 | 887 | 840 | 51.36 | 36.74 | -0.0007 | -0.0058 | -0.0097 |
| D8 | 1727 | 890 | 837 | 51.53 | 38.25 | -0.0017 | -0.006 | -0.0085 |
| D9 | 1727 | 880 | 847 | 50.96 | 41.74 | 0.0001 | -0.007 | -0.0113 |
| D10 | 1727 | 735 | 992 | 42.56 | 65.72 | -0.0022 | -0.0124 | -0.0211 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 42.4743 | 42.5144 | 0.04 |
| volume_confirmation_score | -1.4276 | -1.2523 | 0.1754 |
| liquidity_score | 2.1153 | 2.0104 | -0.1049 |
| overextension_penalty | 1.1547 | 0.9416 | -0.2131 |
| reversal_risk_penalty | 0.8066 | 0.7234 | -0.0832 |
| news_risk_penalty | 0.1111 | 0.1246 | 0.0135 |
| attention_noise_penalty | 0.2421 | 0.2504 | 0.0083 |
| market_regime_penalty | 0.0574 | 0.0483 | -0.0091 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **13604**
- Benchmark-adjusted coverage: **36.74%**
- Benchmark-adjusted success rate: **52.63%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261103.csv`
- Latest market index date: **2026-11-03**
- Latest price signal date: **2026-11-02**
- Latest candidate signal date: **2026-11-02**
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