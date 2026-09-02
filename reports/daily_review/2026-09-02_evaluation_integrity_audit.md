# Evaluation Integrity Audit - 2026-09-02

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **147164**
- Unique evaluation keys: **8521**
- Duplicate rows by candidate key: **138643**
- Duplicate rate: **94.21%**
- Exact same-day duplicate rows: **25259**
- Same stock_code + signal_date repeated keys: **8043**
- Same candidate re-evaluated across multiple files: **8044**
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
| v1/unknown | 382 | 188 | 194 | 49.21 | -0.0135 | 0.0098 | 0.0064 |
| v2_conservative_ranker | 3287 | 1397 | 1890 | 42.5 | 0.0052 | 0.0201 | 0.0306 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 641 | 262 | 379 | 40.87 | -0.0011 | -0.004 | -0.0093 |
| avoid | 2646 | 1135 | 1511 | 42.89 | 0.0067 | 0.026 | 0.0398 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 235 | 106 | 129 | 45.11 | 0.0022 | 0.0067 | 0.0094 |
| Top 20 | 406 | 179 | 227 | 44.09 | 0.0009 | 0.0001 | 0.0034 |
| Top 50 | 615 | 259 | 356 | 42.11 | -0.0006 | -0.0043 | -0.009 |
| Top 100 | 923 | 366 | 557 | 39.65 | 0.0034 | 0.0056 | 0.0034 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 329 | 132 | 197 | 40.12 | 18.72 | 0.0091 | 0.035 | 0.0574 |
| D2 | 329 | 133 | 196 | 40.43 | 24.96 | 0.0123 | 0.0508 | 0.0783 |
| D3 | 328 | 140 | 188 | 42.68 | 28.53 | 0.0124 | 0.0285 | 0.0366 |
| D4 | 329 | 141 | 188 | 42.86 | 31.13 | 0.0028 | 0.0294 | 0.0346 |
| D5 | 329 | 142 | 187 | 43.16 | 33.41 | 0.006 | 0.0199 | 0.0237 |
| D6 | 328 | 149 | 179 | 45.43 | 35.35 | -0.001 | 0.0163 | 0.0239 |
| D7 | 329 | 145 | 184 | 44.07 | 37.23 | 0.007 | 0.0134 | 0.0245 |
| D8 | 328 | 145 | 183 | 44.21 | 39.1 | 0.005 | 0.0166 | 0.0382 |
| D9 | 329 | 132 | 197 | 40.12 | 60.97 | -0.0025 | -0.0111 | -0.0148 |
| D10 | 329 | 138 | 191 | 41.95 | 69.12 | 0.0005 | 0.0004 | -0.0061 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 48.0216 | 46.3646 | -1.657 |
| volume_confirmation_score | -0.6064 | -0.5263 | 0.0802 |
| liquidity_score | 2.2985 | 2.0921 | -0.2064 |
| overextension_penalty | 2.5038 | 1.5609 | -0.9429 |
| reversal_risk_penalty | 1.9121 | 1.3844 | -0.5277 |
| news_risk_penalty | 0.3114 | 0.2942 | -0.0172 |
| attention_noise_penalty | 0.3155 | 0.2875 | -0.0279 |
| market_regime_penalty | 0.0902 | 0.072 | -0.0182 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **3410**
- Benchmark-adjusted coverage: **40.02%**
- Benchmark-adjusted success rate: **49.47%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260902.csv`
- Latest market index date: **2026-09-02**
- Latest price signal date: **2026-09-02**
- Latest candidate signal date: **2026-09-02**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **9**
- Eligible groups: **11**
- Groups close to activation: **0**
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