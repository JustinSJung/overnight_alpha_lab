# Evaluation Integrity Audit - 2026-09-03

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **155664**
- Unique evaluation keys: **9029**
- Duplicate rows by candidate key: **146635**
- Duplicate rate: **94.2%**
- Exact same-day duplicate rows: **28599**
- Same stock_code + signal_date repeated keys: **8520**
- Same candidate re-evaluated across multiple files: **8521**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 000720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 236810 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 066430 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 000720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 236810 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 066430 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 236810 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 000720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 066430 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 000720 |  |  | 2026-07-20 |  | 03e8ccf2ee7fbf0d | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 236810 |  |  | 2026-07-20 |  | 9902a24996692a3c | data/predictions/price_candidate_evaluation_20260720.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 405 | 200 | 205 | 49.38 | -0.0138 | 0.0095 | 0.0028 |
| v2_conservative_ranker | 3595 | 1590 | 2005 | 44.23 | 0.0038 | 0.0173 | 0.0288 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 668 | 280 | 388 | 41.92 | -0.0008 | -0.0053 | -0.0097 |
| avoid | 2927 | 1310 | 1617 | 44.76 | 0.0048 | 0.0227 | 0.0374 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 255 | 119 | 136 | 46.67 | 0.0021 | 0.0038 | 0.0078 |
| Top 20 | 433 | 196 | 237 | 45.27 | 0.001 | -0.0017 | 0.0019 |
| Top 50 | 642 | 277 | 365 | 43.15 | -0.0004 | -0.0055 | -0.0094 |
| Top 100 | 967 | 394 | 573 | 40.74 | 0.0034 | 0.0031 | -0.0004 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 360 | 156 | 204 | 43.33 | 18.43 | 0.0065 | 0.0359 | 0.0607 |
| D2 | 359 | 151 | 208 | 42.06 | 24.64 | 0.0084 | 0.0453 | 0.0754 |
| D3 | 360 | 163 | 197 | 45.28 | 28.24 | 0.0101 | 0.0269 | 0.0388 |
| D4 | 359 | 155 | 204 | 43.18 | 30.92 | 0.0018 | 0.0224 | 0.03 |
| D5 | 360 | 171 | 189 | 47.5 | 33.2 | 0.0018 | 0.0103 | 0.0115 |
| D6 | 359 | 172 | 187 | 47.91 | 35.13 | 0.0004 | 0.0163 | 0.0286 |
| D7 | 359 | 152 | 207 | 42.34 | 37.07 | 0.0072 | 0.0134 | 0.0201 |
| D8 | 360 | 169 | 191 | 46.94 | 38.92 | 0.003 | 0.0129 | 0.0316 |
| D9 | 359 | 148 | 211 | 41.23 | 58.83 | -0.002 | -0.0113 | -0.0111 |
| D10 | 360 | 153 | 207 | 42.5 | 68.83 | 0.0007 | -0.0006 | -0.007 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 47.3736 | 46.077 | -1.2966 |
| volume_confirmation_score | -0.7273 | -0.5869 | 0.1404 |
| liquidity_score | 2.2755 | 2.0863 | -0.1892 |
| overextension_penalty | 2.3657 | 1.555 | -0.8107 |
| reversal_risk_penalty | 1.8699 | 1.3693 | -0.5006 |
| news_risk_penalty | 0.2811 | 0.2788 | -0.0023 |
| attention_noise_penalty | 0.3286 | 0.3184 | -0.0101 |
| market_regime_penalty | 0.0981 | 0.0748 | -0.0233 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **3741**
- Benchmark-adjusted coverage: **41.43%**
- Benchmark-adjusted success rate: **50.23%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260903.csv`
- Latest market index date: **2026-09-03**
- Latest price signal date: **2026-09-03**
- Latest candidate signal date: **2026-09-03**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **11**
- Eligible groups: **11**
- Groups close to activation: **1**
- Criteria: DART/error-note event_type groups, minimum 5 evaluated rows, neutral 45%-55% success gives zero adjustment.
- Finding: Some learned event rules are active.

## Dashboard Status Flags

- Duplicate status: **Possible duplicates**
- Benchmark status: **Partial**
- Ranking status: **Ranking weak**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.