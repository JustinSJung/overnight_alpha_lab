# Evaluation Integrity Audit - 2026-09-17

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **268788**
- Unique evaluation keys: **14798**
- Duplicate rows by candidate key: **253990**
- Duplicate rate: **94.49%**
- Exact same-day duplicate rows: **73643**
- Same stock_code + signal_date repeated keys: **14077**
- Same candidate re-evaluated across multiple files: **14078**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 065770 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 065770 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 065770 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 065770 |  |  | 2026-07-20 |  | 63709cb8ab5628d0 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 006730 |  |  | 2026-07-20 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 013520 |  |  | 2026-07-20 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260720.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 400 | 200 | 200 | 50.0 | -0.0142 | 0.0111 | 0.0051 |
| v2_conservative_ranker | 6220 | 2865 | 3355 | 46.06 | 0.0027 | 0.0091 | 0.0155 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 907 | 393 | 514 | 43.33 | -0.0009 | -0.0057 | -0.0087 |
| avoid | 5313 | 2472 | 2841 | 46.53 | 0.0033 | 0.0117 | 0.0202 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 340 | 155 | 185 | 45.59 | 0.0009 | -0.0001 | 0.003 |
| Top 20 | 596 | 264 | 332 | 44.3 | -0.0006 | -0.0037 | -0.0004 |
| Top 50 | 876 | 387 | 489 | 44.18 | -0.0006 | -0.006 | -0.0082 |
| Top 100 | 1204 | 507 | 697 | 42.11 | 0.0027 | 0.0017 | 0.0002 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 622 | 273 | 349 | 43.89 | 19.7 | 0.0047 | 0.0239 | 0.0452 |
| D2 | 622 | 281 | 341 | 45.18 | 26.06 | 0.0072 | 0.0249 | 0.0421 |
| D3 | 622 | 276 | 346 | 44.37 | 29.3 | 0.0066 | 0.0137 | 0.0269 |
| D4 | 622 | 297 | 325 | 47.75 | 31.65 | -0.0002 | 0.0068 | 0.0014 |
| D5 | 622 | 294 | 328 | 47.27 | 33.61 | 0.0029 | 0.0069 | 0.0073 |
| D6 | 622 | 296 | 326 | 47.59 | 35.38 | -0.0009 | 0.0045 | 0.0108 |
| D7 | 622 | 301 | 321 | 48.39 | 37.03 | 0.0046 | 0.0105 | 0.0181 |
| D8 | 622 | 290 | 332 | 46.62 | 38.57 | 0.0029 | 0.0062 | 0.0136 |
| D9 | 622 | 287 | 335 | 46.14 | 49.73 | -0.0006 | -0.0028 | -0.0008 |
| D10 | 622 | 270 | 352 | 43.41 | 66.95 | -0.0001 | -0.0046 | -0.0092 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 45.2131 | 44.8377 | -0.3754 |
| volume_confirmation_score | -1.1601 | -1.0239 | 0.1362 |
| liquidity_score | 2.1721 | 2.0167 | -0.1554 |
| overextension_penalty | 1.7711 | 1.3627 | -0.4084 |
| reversal_risk_penalty | 1.3005 | 1.0792 | -0.2213 |
| news_risk_penalty | 0.1951 | 0.2221 | 0.0269 |
| attention_noise_penalty | 0.3455 | 0.3664 | 0.0209 |
| market_regime_penalty | 0.0963 | 0.09 | -0.0063 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **6285**
- Benchmark-adjusted coverage: **42.47%**
- Benchmark-adjusted success rate: **50.37%**
- Benchmark rows available: **86**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260917.csv`
- Latest market index date: **2026-09-17**
- Latest price signal date: **2026-09-17**
- Latest candidate signal date: **2026-09-17**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **8**
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