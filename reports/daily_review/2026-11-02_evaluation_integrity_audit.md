# Evaluation Integrity Audit - 2026-11-02

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **974495**
- Unique evaluation keys: **36017**
- Duplicate rows by candidate key: **938478**
- Duplicate rate: **96.3%**
- Exact same-day duplicate rows: **369731**
- Same stock_code + signal_date repeated keys: **35054**
- Same candidate re-evaluated across multiple files: **35055**
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
| v1/unknown | 383 | 189 | 194 | 49.35 | -0.0135 | 0.0073 | 0.0055 |
| v2_conservative_ranker | 15936 | 7787 | 8149 | 48.86 | -0.001 | -0.0056 | -0.0095 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1744 | 729 | 1015 | 41.8 | -0.0026 | -0.0126 | -0.0221 |
| avoid | 14192 | 7058 | 7134 | 49.73 | -0.0009 | -0.0047 | -0.0077 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 505 | 222 | 283 | 43.96 | 0.0005 | -0.0067 | -0.0067 |
| Top 20 | 901 | 396 | 505 | 43.95 | -0.0004 | -0.0065 | -0.0073 |
| Top 50 | 1425 | 612 | 813 | 42.95 | -0.0014 | -0.008 | -0.012 |
| Top 100 | 1904 | 786 | 1118 | 41.28 | 0.0003 | -0.0053 | -0.012 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1594 | 727 | 867 | 45.61 | 21.65 | 0.0001 | 0.0037 | 0.0124 |
| D2 | 1594 | 755 | 839 | 47.37 | 27.05 | 0.0001 | -0.0074 | -0.0146 |
| D3 | 1593 | 749 | 844 | 47.02 | 29.38 | 0.0016 | -0.0007 | -0.0058 |
| D4 | 1594 | 772 | 822 | 48.43 | 31.49 | -0.0004 | -0.0039 | -0.0081 |
| D5 | 1593 | 788 | 805 | 49.47 | 33.4 | -0.0009 | -0.0065 | -0.0138 |
| D6 | 1594 | 822 | 772 | 51.57 | 35.13 | -0.0038 | -0.0073 | -0.0091 |
| D7 | 1593 | 842 | 751 | 52.86 | 36.73 | -0.0014 | -0.0057 | -0.0091 |
| D8 | 1594 | 838 | 756 | 52.57 | 38.22 | -0.0019 | -0.0064 | -0.0088 |
| D9 | 1593 | 820 | 773 | 51.48 | 42.02 | -0.0012 | -0.0089 | -0.014 |
| D10 | 1594 | 674 | 920 | 42.28 | 65.8 | -0.0025 | -0.0124 | -0.0219 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 42.458 | 42.7529 | 0.2949 |
| volume_confirmation_score | -1.4748 | -1.3001 | 0.1747 |
| liquidity_score | 2.1067 | 1.9947 | -0.112 |
| overextension_penalty | 1.1642 | 0.9957 | -0.1685 |
| reversal_risk_penalty | 0.7776 | 0.7209 | -0.0567 |
| news_risk_penalty | 0.1052 | 0.1317 | 0.0265 |
| attention_noise_penalty | 0.238 | 0.2507 | 0.0127 |
| market_regime_penalty | 0.0501 | 0.0464 | -0.0037 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **12857**
- Benchmark-adjusted coverage: **35.7%**
- Benchmark-adjusted success rate: **52.14%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261102.csv`
- Latest market index date: **2026-11-02**
- Latest price signal date: **2026-10-30**
- Latest candidate signal date: **2026-10-30**
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