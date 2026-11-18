# Evaluation Integrity Audit - 2026-11-18

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **1486752**
- Unique evaluation keys: **49583**
- Duplicate rows by candidate key: **1437169**
- Duplicate rate: **96.67%**
- Exact same-day duplicate rows: **605435**
- Same stock_code + signal_date repeated keys: **48397**
- Same candidate re-evaluated across multiple files: **48398**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 020560 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 020560 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 020560 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 003490 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 013520 |  |  | 2026-07-20 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 003490 |  |  | 2026-07-20 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 020560 |  |  | 2026-07-20 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260720.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 328 | 160 | 168 | 48.78 | -0.0096 | 0.0016 | -0.0166 |
| v2_conservative_ranker | 24412 | 12261 | 12151 | 50.23 | -0.0019 | -0.0065 | -0.0107 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 2558 | 1069 | 1489 | 41.79 | -0.0028 | -0.011 | -0.0183 |
| avoid | 21854 | 11192 | 10662 | 51.21 | -0.0018 | -0.006 | -0.0099 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 668 | 284 | 384 | 42.51 | -0.0005 | -0.0058 | -0.0053 |
| Top 20 | 1200 | 523 | 677 | 43.58 | -0.0009 | -0.0074 | -0.0068 |
| Top 50 | 2057 | 886 | 1171 | 43.07 | -0.0019 | -0.0077 | -0.0106 |
| Top 100 | 2759 | 1144 | 1615 | 41.46 | -0.0007 | -0.0059 | -0.0111 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 2442 | 1187 | 1255 | 48.61 | 21.23 | -0.0005 | -0.0023 | 0.0005 |
| D2 | 2441 | 1233 | 1208 | 50.51 | 26.55 | -0.0027 | -0.0055 | -0.011 |
| D3 | 2441 | 1216 | 1225 | 49.82 | 28.85 | -0.001 | -0.0046 | -0.0113 |
| D4 | 2441 | 1214 | 1227 | 49.73 | 30.91 | -0.0013 | -0.006 | -0.0106 |
| D5 | 2441 | 1273 | 1168 | 52.15 | 32.84 | -0.0021 | -0.007 | -0.0126 |
| D6 | 2441 | 1289 | 1152 | 52.81 | 34.62 | -0.0029 | -0.0084 | -0.0107 |
| D7 | 2441 | 1285 | 1156 | 52.64 | 36.33 | -0.0032 | -0.0061 | -0.0094 |
| D8 | 2441 | 1282 | 1159 | 52.52 | 37.98 | -0.0014 | -0.0058 | -0.0094 |
| D9 | 2441 | 1259 | 1182 | 51.58 | 41.06 | -0.0016 | -0.008 | -0.0145 |
| D10 | 2442 | 1023 | 1419 | 41.89 | 66.04 | -0.0029 | -0.0111 | -0.0185 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.2362 | 41.8775 | 0.6413 |
| volume_confirmation_score | -1.2036 | -0.9992 | 0.2044 |
| liquidity_score | 2.1617 | 2.0857 | -0.076 |
| overextension_penalty | 0.9441 | 0.8173 | -0.1268 |
| reversal_risk_penalty | 0.7323 | 0.6829 | -0.0495 |
| news_risk_penalty | 0.097 | 0.1244 | 0.0274 |
| attention_noise_penalty | 0.2211 | 0.2445 | 0.0233 |
| market_regime_penalty | 0.0498 | 0.0461 | -0.0037 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **18078**
- Benchmark-adjusted coverage: **36.46%**
- Benchmark-adjusted success rate: **50.71%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261118.csv`
- Latest market index date: **2026-11-18**
- Latest price signal date: **2026-11-17**
- Latest candidate signal date: **2026-11-17**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **8**
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