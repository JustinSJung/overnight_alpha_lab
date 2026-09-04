# Evaluation Integrity Audit - 2026-09-04

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **164691**
- Unique evaluation keys: **9556**
- Duplicate rows by candidate key: **155135**
- Duplicate rate: **94.2%**
- Exact same-day duplicate rows: **32174**
- Same stock_code + signal_date repeated keys: **9028**
- Same candidate re-evaluated across multiple files: **9029**
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
| v1/unknown | 387 | 190 | 197 | 49.1 | -0.0133 | 0.0123 | 0.005 |
| v2_conservative_ranker | 3781 | 1615 | 2166 | 42.71 | 0.0044 | 0.0166 | 0.0291 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 682 | 289 | 393 | 42.38 | -0.0009 | -0.0051 | -0.0095 |
| avoid | 3099 | 1326 | 1773 | 42.79 | 0.0056 | 0.0219 | 0.0387 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 262 | 124 | 138 | 47.33 | 0.0021 | 0.0039 | 0.0082 |
| Top 20 | 447 | 205 | 242 | 45.86 | 0.0009 | -0.0011 | 0.002 |
| Top 50 | 655 | 285 | 370 | 43.51 | -0.0004 | -0.0052 | -0.009 |
| Top 100 | 968 | 394 | 574 | 40.7 | 0.0033 | 0.0028 | -0.0006 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 379 | 157 | 222 | 41.42 | 18.81 | 0.0072 | 0.0337 | 0.0571 |
| D2 | 378 | 149 | 229 | 39.42 | 25.04 | 0.0108 | 0.0431 | 0.074 |
| D3 | 378 | 158 | 220 | 41.8 | 28.49 | 0.0103 | 0.0215 | 0.039 |
| D4 | 378 | 158 | 220 | 41.8 | 31.05 | 0.004 | 0.0235 | 0.0329 |
| D5 | 378 | 166 | 212 | 43.92 | 33.28 | 0.0019 | 0.0101 | 0.0118 |
| D6 | 378 | 174 | 204 | 46.03 | 35.17 | 0.001 | 0.025 | 0.0461 |
| D7 | 378 | 164 | 214 | 43.39 | 37.04 | 0.0064 | 0.0128 | 0.019 |
| D8 | 378 | 172 | 206 | 45.5 | 38.85 | 0.0038 | 0.009 | 0.0296 |
| D9 | 378 | 157 | 221 | 41.53 | 57.53 | -0.0018 | -0.0092 | -0.009 |
| D10 | 378 | 160 | 218 | 42.33 | 68.61 | 0.0006 | -0.0014 | -0.0084 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 47.4901 | 45.679 | -1.8111 |
| volume_confirmation_score | -0.7515 | -0.6755 | 0.0761 |
| liquidity_score | 2.2687 | 2.0697 | -0.199 |
| overextension_penalty | 2.3293 | 1.5327 | -0.7967 |
| reversal_risk_penalty | 1.7971 | 1.2807 | -0.5164 |
| news_risk_penalty | 0.2842 | 0.2673 | -0.0169 |
| attention_noise_penalty | 0.3438 | 0.335 | -0.0087 |
| market_regime_penalty | 0.0941 | 0.0739 | -0.0202 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **3909**
- Benchmark-adjusted coverage: **40.91%**
- Benchmark-adjusted success rate: **50.5%**
- Benchmark rows available: **86**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260904.csv`
- Latest market index date: **2026-09-04**
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
- Ranking status: **Ranking improving**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.