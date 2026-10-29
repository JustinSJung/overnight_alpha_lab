# Evaluation Integrity Audit - 2026-10-29

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **904481**
- Unique evaluation keys: **35039**
- Duplicate rows by candidate key: **869442**
- Duplicate rate: **96.13%**
- Exact same-day duplicate rows: **338313**
- Same stock_code + signal_date repeated keys: **33993**
- Same candidate re-evaluated across multiple files: **33994**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 065770 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 253450 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 065770 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 253450 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 253450 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 065770 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004990 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 065770 |  |  | 2026-07-20 |  | 63709cb8ab5628d0 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 253450 |  |  | 2026-07-20 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 004990 |  |  | 2026-07-20 |  | 65698458accec52f | data/predictions/price_candidate_evaluation_20260720.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 410 | 201 | 209 | 49.02 | -0.013 | 0.0109 | 0.006 |
| v2_conservative_ranker | 16564 | 8130 | 8434 | 49.08 | -0.001 | -0.0042 | -0.0071 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1849 | 781 | 1068 | 42.24 | -0.0019 | -0.0116 | -0.021 |
| avoid | 14715 | 7349 | 7366 | 49.94 | -0.0009 | -0.0033 | -0.0051 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 544 | 238 | 306 | 43.75 | 0.0008 | -0.0053 | -0.0053 |
| Top 20 | 960 | 425 | 535 | 44.27 | -0.0 | -0.0062 | -0.0071 |
| Top 50 | 1521 | 662 | 859 | 43.52 | -0.0006 | -0.0068 | -0.0111 |
| Top 100 | 2043 | 853 | 1190 | 41.75 | 0.0009 | -0.0046 | -0.0117 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1657 | 761 | 896 | 45.93 | 21.48 | -0.0001 | 0.0045 | 0.0161 |
| D2 | 1656 | 792 | 864 | 47.83 | 27.01 | -0.0001 | -0.0048 | -0.0093 |
| D3 | 1656 | 775 | 881 | 46.8 | 29.39 | 0.0015 | 0.0014 | -0.0028 |
| D4 | 1657 | 810 | 847 | 48.88 | 31.49 | -0.0002 | -0.0018 | -0.005 |
| D5 | 1656 | 813 | 843 | 49.09 | 33.4 | -0.001 | -0.0049 | -0.0128 |
| D6 | 1656 | 864 | 792 | 52.17 | 35.14 | -0.0041 | -0.0065 | -0.0058 |
| D7 | 1657 | 873 | 784 | 52.69 | 36.74 | -0.0012 | -0.0051 | -0.0078 |
| D8 | 1656 | 877 | 779 | 52.96 | 38.23 | -0.002 | -0.0051 | -0.007 |
| D9 | 1656 | 857 | 799 | 51.75 | 42.47 | -0.0014 | -0.0079 | -0.0127 |
| D10 | 1657 | 708 | 949 | 42.73 | 65.98 | -0.0019 | -0.0117 | -0.0211 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 42.502 | 42.7931 | 0.2911 |
| volume_confirmation_score | -1.4645 | -1.2936 | 0.1709 |
| liquidity_score | 2.1085 | 1.9962 | -0.1123 |
| overextension_penalty | 1.1253 | 0.9723 | -0.153 |
| reversal_risk_penalty | 0.784 | 0.7321 | -0.0518 |
| news_risk_penalty | 0.1071 | 0.1343 | 0.0272 |
| attention_noise_penalty | 0.2427 | 0.2554 | 0.0127 |
| market_regime_penalty | 0.0517 | 0.047 | -0.0047 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **13680**
- Benchmark-adjusted coverage: **39.04%**
- Benchmark-adjusted success rate: **52.13%**
- Benchmark rows available: **80**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261029.csv`
- Latest market index date: **2026-10-29**
- Latest price signal date: **2026-10-29**
- Latest candidate signal date: **2026-10-29**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **9**
- Eligible groups: **12**
- Groups close to activation: **4**
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