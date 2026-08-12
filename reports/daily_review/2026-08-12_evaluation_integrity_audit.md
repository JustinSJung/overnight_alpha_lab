# Evaluation Integrity Audit - 2026-08-12

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **49337**
- Unique evaluation keys: **4764**
- Duplicate rows by candidate key: **44573**
- Duplicate rate: **90.34%**
- Exact same-day duplicate rows: **8577**
- Same stock_code + signal_date repeated keys: **3917**
- Same candidate re-evaluated across multiple files: **4270**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 141080 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 86c5d271d855238c | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 043260 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | e4617eadc375de9f | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 000720 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 8803cd8e00cafaa3 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 141080 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 86c5d271d855238c | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 043260 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | e4617eadc375de9f | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 000720 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 8803cd8e00cafaa3 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 141080 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 86c5d271d855238c | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 043260 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | e4617eadc375de9f | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 000720 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 8803cd8e00cafaa3 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 375 | 192 | 183 | 51.2 | -0.0118 | -0.0047 | -0.0268 |
| v2_conservative_ranker | 1834 | 740 | 1094 | 40.35 | 0.0105 | 0.0274 | 0.0472 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 303 | 151 | 152 | 49.83 | 0.0049 | 0.0148 | 0.0224 |
| avoid | 1531 | 589 | 942 | 38.47 | 0.0116 | 0.029 | 0.0494 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 127 | 72 | 55 | 56.69 | 0.0069 | 0.0109 | 0.0203 |
| Top 20 | 189 | 102 | 87 | 53.97 | 0.0067 | 0.0131 | 0.0212 |
| Top 50 | 301 | 153 | 148 | 50.83 | 0.0053 | 0.0136 | 0.0153 |
| Top 100 | 551 | 256 | 295 | 46.46 | 0.0081 | 0.022 | 0.0151 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 184 | 72 | 112 | 39.13 | 17.43 | 0.0093 | 0.0504 | 0.0824 |
| D2 | 183 | 74 | 109 | 40.44 | 22.9 | 0.008 | 0.0179 | 0.0369 |
| D3 | 183 | 65 | 118 | 35.52 | 26.22 | 0.0175 | 0.0402 | 0.0609 |
| D4 | 184 | 66 | 118 | 35.87 | 29.02 | 0.0226 | 0.0363 | 0.056 |
| D5 | 183 | 68 | 115 | 37.16 | 31.32 | 0.0029 | 0.0381 | 0.0409 |
| D6 | 183 | 73 | 110 | 39.89 | 33.82 | 0.0116 | 0.0169 | 0.0309 |
| D7 | 184 | 76 | 108 | 41.3 | 36.09 | 0.0061 | 0.008 | 0.0294 |
| D8 | 183 | 69 | 114 | 37.7 | 38.16 | 0.0161 | 0.0219 | 0.0478 |
| D9 | 183 | 87 | 96 | 47.54 | 53.93 | 0.005 | 0.0204 | 0.0479 |
| D10 | 184 | 90 | 94 | 48.91 | 68.76 | 0.0058 | 0.0167 | 0.0151 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 47.6645 | 43.4759 | -4.1886 |
| volume_confirmation_score | -0.3516 | -0.5408 | -0.1892 |
| liquidity_score | 2.3473 | 2.1005 | -0.2467 |
| overextension_penalty | 2.6706 | 1.4811 | -1.1896 |
| reversal_risk_penalty | 2.1745 | 1.5879 | -0.5866 |
| news_risk_penalty | 0.3203 | 0.1782 | -0.142 |
| attention_noise_penalty | 0.215 | 0.1889 | -0.0261 |
| market_regime_penalty | 0.0703 | 0.0494 | -0.0209 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **2209**
- Benchmark-adjusted coverage: **46.37%**
- Benchmark-adjusted success rate: **51.47%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260812.csv`
- Latest market index date: **2026-08-12**
- Latest price signal date: **2026-08-12**
- Latest candidate signal date: **2026-08-12**
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