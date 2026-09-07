# Evaluation Integrity Audit - 2026-09-07

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **173749**
- Unique evaluation keys: **9587**
- Duplicate rows by candidate key: **164162**
- Duplicate rate: **94.48%**
- Exact same-day duplicate rows: **35936**
- Same stock_code + signal_date repeated keys: **9555**
- Same candidate re-evaluated across multiple files: **9556**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 419540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 419540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 419540 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 347700 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 419540 |  |  | 2026-07-20 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 321370 |  |  | 2026-07-20 |  | df654892030874da | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 389 | 190 | 199 | 48.84 | -0.0128 | 0.0002 | -0.0104 |
| v2_conservative_ranker | 3775 | 1609 | 2166 | 42.62 | 0.005 | 0.0162 | 0.0281 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 683 | 288 | 395 | 42.17 | -0.0009 | -0.0054 | -0.0098 |
| avoid | 3092 | 1321 | 1771 | 42.72 | 0.0063 | 0.0214 | 0.0375 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 264 | 125 | 139 | 47.35 | 0.0022 | 0.0037 | 0.0084 |
| Top 20 | 449 | 204 | 245 | 45.43 | 0.0007 | -0.0015 | 0.0015 |
| Top 50 | 656 | 284 | 372 | 43.29 | -0.0004 | -0.0052 | -0.0088 |
| Top 100 | 967 | 393 | 574 | 40.64 | 0.0036 | 0.0042 | 0.0013 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 378 | 159 | 219 | 42.06 | 18.68 | 0.0073 | 0.0323 | 0.0572 |
| D2 | 377 | 149 | 228 | 39.52 | 24.93 | 0.0115 | 0.0454 | 0.0758 |
| D3 | 378 | 155 | 223 | 41.01 | 28.38 | 0.0124 | 0.0267 | 0.0454 |
| D4 | 377 | 155 | 222 | 41.11 | 30.99 | 0.0039 | 0.019 | 0.0282 |
| D5 | 378 | 167 | 211 | 44.18 | 33.24 | 0.0029 | 0.0105 | 0.0134 |
| D6 | 377 | 171 | 206 | 45.36 | 35.15 | 0.0019 | 0.0149 | 0.0268 |
| D7 | 377 | 170 | 207 | 45.09 | 37.03 | 0.0061 | 0.0129 | 0.0193 |
| D8 | 378 | 166 | 212 | 43.92 | 38.87 | 0.0057 | 0.0113 | 0.0321 |
| D9 | 377 | 159 | 218 | 42.18 | 57.64 | -0.0019 | -0.0083 | -0.0082 |
| D10 | 378 | 158 | 220 | 41.8 | 68.63 | 0.0004 | -0.0017 | -0.0086 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 47.5484 | 45.7349 | -1.8135 |
| volume_confirmation_score | -0.75 | -0.6956 | 0.0544 |
| liquidity_score | 2.2697 | 2.072 | -0.1977 |
| overextension_penalty | 2.4051 | 1.542 | -0.863 |
| reversal_risk_penalty | 1.8269 | 1.3002 | -0.5267 |
| news_risk_penalty | 0.2853 | 0.2678 | -0.0175 |
| attention_noise_penalty | 0.3367 | 0.3346 | -0.002 |
| market_regime_penalty | 0.1019 | 0.0748 | -0.0271 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **3905**
- Benchmark-adjusted coverage: **40.73%**
- Benchmark-adjusted success rate: **50.45%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260907.csv`
- Latest market index date: **2026-09-07**
- Latest price signal date: **2026-09-04**
- Latest candidate signal date: **2026-09-04**
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