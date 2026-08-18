# Evaluation Integrity Audit - 2026-08-18

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **70063**
- Unique evaluation keys: **5878**
- Duplicate rows by candidate key: **64185**
- Duplicate rate: **91.61%**
- Exact same-day duplicate rows: **10269**
- Same stock_code + signal_date repeated keys: **4735**
- Same candidate re-evaluated across multiple files: **5367**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 065770 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 63709cb8ab5628d0 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 002780 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 1f9e79d6223e57c6 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 007980 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 6bdf1cf3aa42e769 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 000720 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 03e8ccf2ee7fbf0d | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 321370 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | df654892030874da | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 065770 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 63709cb8ab5628d0 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 002780 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 1f9e79d6223e57c6 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 007980 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 6bdf1cf3aa42e769 | data/predictions/price_candidate_evaluation_20260712.csv | pending |
| 000720 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 03e8ccf2ee7fbf0d | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 321370 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | df654892030874da | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 065770 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 63709cb8ab5628d0 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 002780 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 1f9e79d6223e57c6 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 007980 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 6bdf1cf3aa42e769 | data/predictions/price_candidate_evaluation_20260713.csv | pending |
| 000720 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 03e8ccf2ee7fbf0d | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 321370 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | df654892030874da | data/predictions/price_candidate_evaluation_20260713.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 363 | 184 | 179 | 50.69 | -0.0103 | -0.002 | -0.0243 |
| v2_conservative_ranker | 2250 | 898 | 1352 | 39.91 | 0.007 | 0.024 | 0.0467 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 503 | 204 | 299 | 40.56 | -0.0031 | 0.0011 | 0.0098 |
| avoid | 1747 | 694 | 1053 | 39.73 | 0.0099 | 0.0292 | 0.0527 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 157 | 77 | 80 | 49.04 | 0.0021 | 0.0046 | 0.0142 |
| Top 20 | 249 | 117 | 132 | 46.99 | 0.0015 | 0.0046 | 0.0134 |
| Top 50 | 440 | 198 | 242 | 45.0 | 0.0005 | 0.0014 | 0.0071 |
| Top 100 | 743 | 309 | 434 | 41.59 | 0.0023 | 0.0119 | 0.0108 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 225 | 91 | 134 | 40.44 | 17.75 | 0.0122 | 0.0364 | 0.0719 |
| D2 | 225 | 84 | 141 | 37.33 | 23.65 | 0.0106 | 0.0278 | 0.0495 |
| D3 | 225 | 83 | 142 | 36.89 | 27.15 | 0.0217 | 0.0408 | 0.0671 |
| D4 | 225 | 87 | 138 | 38.67 | 30.01 | 0.0066 | 0.0319 | 0.0409 |
| D5 | 225 | 95 | 130 | 42.22 | 32.5 | 0.0028 | 0.0284 | 0.04 |
| D6 | 225 | 89 | 136 | 39.56 | 35.04 | 0.0044 | 0.018 | 0.0402 |
| D7 | 225 | 91 | 134 | 40.44 | 37.33 | 0.0117 | 0.0226 | 0.0484 |
| D8 | 225 | 90 | 135 | 40.0 | 44.2 | 0.0055 | 0.0183 | 0.0578 |
| D9 | 225 | 95 | 130 | 42.22 | 62.94 | -0.0031 | 0.0042 | 0.0168 |
| D10 | 225 | 93 | 132 | 41.33 | 69.93 | -0.002 | 0.0008 | 0.0018 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 48.8136 | 46.2015 | -2.6121 |
| volume_confirmation_score | -0.3396 | -0.3899 | -0.0503 |
| liquidity_score | 2.3563 | 2.1146 | -0.2417 |
| overextension_penalty | 2.8111 | 1.5147 | -1.2964 |
| reversal_risk_penalty | 2.2007 | 1.5083 | -0.6924 |
| news_risk_penalty | 0.3341 | 0.2714 | -0.0626 |
| attention_noise_penalty | 0.2019 | 0.1693 | -0.0326 |
| market_regime_penalty | 0.0646 | 0.0503 | -0.0143 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **2613**
- Benchmark-adjusted coverage: **44.45%**
- Benchmark-adjusted success rate: **50.17%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260818.csv`
- Latest market index date: **2026-08-18**
- Latest price signal date: **2026-08-18**
- Latest candidate signal date: **2026-08-18**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **0**
- Eligible groups: **0**
- Groups close to activation: **0**
- Criteria: DART/error-note event_type groups, minimum 5 evaluated rows, neutral 45%-55% success gives zero adjustment.
- Finding: Learned rules are inactive because the updater learns from DART error_notes event_type groups, not price-candidate v2 outcomes, and current eligible groups are in the neutral adjustment band.

## Dashboard Status Flags

- Duplicate status: **Possible duplicates**
- Benchmark status: **Partial**
- Ranking status: **Ranking improving**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.