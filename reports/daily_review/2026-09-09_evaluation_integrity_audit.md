# Evaluation Integrity Audit - 2026-09-09

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **193623**
- Unique evaluation keys: **10766**
- Duplicate rows by candidate key: **182857**
- Duplicate rate: **94.44%**
- Exact same-day duplicate rows: **43722**
- Same stock_code + signal_date repeated keys: **10165**
- Same candidate re-evaluated across multiple files: **10166**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 002780 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 025980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 002780 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 025980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 002780 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 025980 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 047040 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 002780 |  |  | 2026-07-20 |  | 1f9e79d6223e57c6 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 025980 |  |  | 2026-07-20 |  | 331c322c17fab620 | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 391 | 193 | 198 | 49.36 | -0.0131 | 0.0115 | 0.0059 |
| v2_conservative_ranker | 4361 | 1904 | 2457 | 43.66 | 0.0046 | 0.0167 | 0.0243 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 736 | 320 | 416 | 43.48 | -0.0006 | -0.0049 | -0.0089 |
| avoid | 3625 | 1584 | 2041 | 43.7 | 0.0056 | 0.0214 | 0.0321 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 279 | 134 | 145 | 48.03 | 0.0026 | 0.0041 | 0.0074 |
| Top 20 | 476 | 218 | 258 | 45.8 | 0.0007 | -0.0009 | 0.0021 |
| Top 50 | 702 | 313 | 389 | 44.59 | -0.0002 | -0.005 | -0.0082 |
| Top 100 | 1035 | 429 | 606 | 41.45 | 0.0038 | 0.0038 | 0.0009 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 437 | 182 | 255 | 41.65 | 19.23 | 0.0073 | 0.0357 | 0.0566 |
| D2 | 436 | 177 | 259 | 40.6 | 25.49 | 0.0104 | 0.0375 | 0.0612 |
| D3 | 436 | 180 | 256 | 41.28 | 28.92 | 0.012 | 0.0268 | 0.0361 |
| D4 | 436 | 194 | 242 | 44.5 | 31.36 | 0.0009 | 0.0202 | 0.0236 |
| D5 | 436 | 192 | 244 | 44.04 | 33.44 | 0.0048 | 0.0174 | 0.0189 |
| D6 | 436 | 196 | 240 | 44.95 | 35.35 | 0.0012 | 0.0114 | 0.015 |
| D7 | 436 | 203 | 233 | 46.56 | 37.09 | 0.0067 | 0.0134 | 0.0201 |
| D8 | 436 | 199 | 237 | 45.64 | 38.82 | 0.0044 | 0.0122 | 0.0262 |
| D9 | 436 | 197 | 239 | 45.18 | 55.09 | -0.0017 | -0.0065 | -0.0049 |
| D10 | 436 | 184 | 252 | 42.2 | 68.16 | -0.0001 | -0.0036 | -0.0101 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 46.8855 | 45.4108 | -1.4746 |
| volume_confirmation_score | -0.8367 | -0.756 | 0.0808 |
| liquidity_score | 2.2495 | 2.057 | -0.1925 |
| overextension_penalty | 2.1133 | 1.5074 | -0.6059 |
| reversal_risk_penalty | 1.6102 | 1.2185 | -0.3917 |
| news_risk_penalty | 0.281 | 0.2527 | -0.0282 |
| attention_noise_penalty | 0.3429 | 0.3548 | 0.0119 |
| market_regime_penalty | 0.1008 | 0.0757 | -0.0251 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **4493**
- Benchmark-adjusted coverage: **41.73%**
- Benchmark-adjusted success rate: **51.61%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260909.csv`
- Latest market index date: **2026-09-09**
- Latest price signal date: **2026-09-09**
- Latest candidate signal date: **2026-09-09**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **10**
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