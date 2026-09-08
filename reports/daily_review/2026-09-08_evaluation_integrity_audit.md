# Evaluation Integrity Audit - 2026-09-08

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **183386**
- Unique evaluation keys: **10166**
- Duplicate rows by candidate key: **173220**
- Duplicate rate: **94.46%**
- Exact same-day duplicate rows: **39723**
- Same stock_code + signal_date repeated keys: **9586**
- Same candidate re-evaluated across multiple files: **9587**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 064400 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 000720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 064400 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 000720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 064400 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 000720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 010140 |  |  | 2026-07-20 |  | 7a97bf307b3df2b2 | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 064400 |  |  | 2026-07-20 |  | 2e327c9a00465eab | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 394 | 195 | 199 | 49.49 | -0.0143 | 0.0081 | 0.0005 |
| v2_conservative_ranker | 4062 | 1749 | 2313 | 43.06 | 0.0048 | 0.0168 | 0.0239 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 707 | 298 | 409 | 42.15 | -0.0012 | -0.0055 | -0.0102 |
| avoid | 3355 | 1451 | 1904 | 43.25 | 0.006 | 0.0217 | 0.0322 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 268 | 127 | 141 | 47.39 | 0.002 | 0.0035 | 0.006 |
| Top 20 | 457 | 206 | 251 | 45.08 | 0.0003 | -0.0017 | 0.0007 |
| Top 50 | 672 | 290 | 382 | 43.15 | -0.0007 | -0.0057 | -0.0094 |
| Top 100 | 994 | 399 | 595 | 40.14 | 0.0034 | 0.0027 | -0.0001 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 407 | 168 | 239 | 41.28 | 18.89 | 0.0085 | 0.0341 | 0.0538 |
| D2 | 406 | 165 | 241 | 40.64 | 25.12 | 0.0101 | 0.0391 | 0.0633 |
| D3 | 406 | 166 | 240 | 40.89 | 28.66 | 0.0111 | 0.0259 | 0.0367 |
| D4 | 406 | 179 | 227 | 44.09 | 31.17 | 0.0031 | 0.0227 | 0.0225 |
| D5 | 406 | 178 | 228 | 43.84 | 33.33 | 0.003 | 0.0128 | 0.0155 |
| D6 | 406 | 181 | 225 | 44.58 | 35.26 | 0.0025 | 0.0158 | 0.0193 |
| D7 | 406 | 183 | 223 | 45.07 | 37.09 | 0.007 | 0.0146 | 0.0203 |
| D8 | 406 | 184 | 222 | 45.32 | 38.89 | 0.0045 | 0.0113 | 0.0258 |
| D9 | 406 | 176 | 230 | 43.35 | 56.31 | -0.0018 | -0.0078 | -0.0081 |
| D10 | 407 | 169 | 238 | 41.52 | 68.32 | -0.0004 | -0.0028 | -0.0102 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 47.184 | 45.5498 | -1.6342 |
| volume_confirmation_score | -0.7724 | -0.6968 | 0.0756 |
| liquidity_score | 2.2619 | 2.0683 | -0.1936 |
| overextension_penalty | 2.2571 | 1.4574 | -0.7997 |
| reversal_risk_penalty | 1.7494 | 1.2593 | -0.4901 |
| news_risk_penalty | 0.2813 | 0.2698 | -0.0115 |
| attention_noise_penalty | 0.3548 | 0.3364 | -0.0184 |
| market_regime_penalty | 0.1029 | 0.0813 | -0.0216 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **4197**
- Benchmark-adjusted coverage: **41.28%**
- Benchmark-adjusted success rate: **50.94%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260908.csv`
- Latest market index date: **2026-09-08**
- Latest price signal date: **2026-09-08**
- Latest candidate signal date: **2026-09-08**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **11**
- Eligible groups: **11**
- Groups close to activation: **2**
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