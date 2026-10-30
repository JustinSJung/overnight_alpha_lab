# Evaluation Integrity Audit - 2026-10-30

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **939007**
- Unique evaluation keys: **35055**
- Duplicate rows by candidate key: **903952**
- Duplicate rate: **96.27%**
- Exact same-day duplicate rows: **354453**
- Same stock_code + signal_date repeated keys: **35038**
- Same candidate re-evaluated across multiple files: **35039**
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
| v1/unknown | 403 | 198 | 205 | 49.13 | -0.0136 | -0.0015 | -0.0109 |
| v2_conservative_ranker | 16560 | 8145 | 8415 | 49.18 | -0.0009 | -0.0038 | -0.0068 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1835 | 772 | 1063 | 42.07 | -0.0023 | -0.0118 | -0.0217 |
| avoid | 14725 | 7373 | 7352 | 50.07 | -0.0008 | -0.0028 | -0.0046 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 545 | 236 | 309 | 43.3 | 0.0 | -0.0054 | -0.0059 |
| Top 20 | 956 | 424 | 532 | 44.35 | -0.0003 | -0.0057 | -0.0068 |
| Top 50 | 1509 | 653 | 856 | 43.27 | -0.001 | -0.007 | -0.0115 |
| Top 100 | 2015 | 837 | 1178 | 41.54 | 0.001 | -0.0045 | -0.0115 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1656 | 759 | 897 | 45.83 | 21.42 | 0.0007 | 0.0058 | 0.0163 |
| D2 | 1656 | 798 | 858 | 48.19 | 26.97 | -0.0006 | -0.0041 | -0.0103 |
| D3 | 1656 | 773 | 883 | 46.68 | 29.36 | 0.0023 | 0.0029 | -0.0016 |
| D4 | 1656 | 810 | 846 | 48.91 | 31.46 | -0.0001 | -0.0014 | -0.0046 |
| D5 | 1656 | 831 | 825 | 50.18 | 33.37 | -0.0014 | -0.0046 | -0.0118 |
| D6 | 1656 | 865 | 791 | 52.23 | 35.12 | -0.004 | -0.0066 | -0.0055 |
| D7 | 1656 | 868 | 788 | 52.42 | 36.71 | -0.0011 | -0.005 | -0.0084 |
| D8 | 1656 | 879 | 777 | 53.08 | 38.22 | -0.0018 | -0.005 | -0.0057 |
| D9 | 1656 | 857 | 799 | 51.75 | 42.3 | -0.0011 | -0.0078 | -0.0119 |
| D10 | 1656 | 705 | 951 | 42.57 | 65.98 | -0.0024 | -0.0117 | -0.0215 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 42.4861 | 42.7555 | 0.2695 |
| volume_confirmation_score | -1.4613 | -1.295 | 0.1663 |
| liquidity_score | 2.1088 | 2.0072 | -0.1015 |
| overextension_penalty | 1.1423 | 0.9696 | -0.1726 |
| reversal_risk_penalty | 0.7909 | 0.7377 | -0.0532 |
| news_risk_penalty | 0.1072 | 0.1296 | 0.0225 |
| attention_noise_penalty | 0.2483 | 0.2506 | 0.0023 |
| market_regime_penalty | 0.053 | 0.048 | -0.005 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **13631**
- Benchmark-adjusted coverage: **38.88%**
- Benchmark-adjusted success rate: **52.25%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261030.csv`
- Latest market index date: **2026-10-30**
- Latest price signal date: **2026-10-29**
- Latest candidate signal date: **2026-10-29**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **10**
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