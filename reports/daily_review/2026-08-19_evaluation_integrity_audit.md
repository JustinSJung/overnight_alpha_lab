# Evaluation Integrity Audit - 2026-08-19

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **75959**
- Unique evaluation keys: **6171**
- Duplicate rows by candidate key: **69788**
- Duplicate rate: **91.88%**
- Exact same-day duplicate rows: **10692**
- Same stock_code + signal_date repeated keys: **5020**
- Same candidate re-evaluated across multiple files: **5653**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 006730 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 013520 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 288980 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 020560 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 006730 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 013520 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 288980 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 020560 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 006730 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 013520 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 003490 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 3234aec8921157e1 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 288980 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 020560 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 358 | 182 | 176 | 50.84 | -0.0116 | -0.0023 | -0.025 |
| v2_conservative_ranker | 2353 | 954 | 1399 | 40.54 | 0.0063 | 0.0224 | 0.0426 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 527 | 213 | 314 | 40.42 | -0.0032 | -0.0023 | 0.0001 |
| avoid | 1826 | 741 | 1085 | 40.58 | 0.009 | 0.0284 | 0.0509 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 167 | 82 | 85 | 49.1 | 0.0033 | 0.0012 | 0.0098 |
| Top 20 | 269 | 125 | 144 | 46.47 | 0.0013 | 0.0003 | 0.0093 |
| Top 50 | 464 | 207 | 257 | 44.61 | 0.0001 | -0.002 | -0.0001 |
| Top 100 | 767 | 318 | 449 | 41.46 | 0.0021 | 0.0092 | 0.0053 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 236 | 95 | 141 | 40.25 | 17.84 | 0.0122 | 0.0373 | 0.0691 |
| D2 | 235 | 91 | 144 | 38.72 | 23.77 | 0.0096 | 0.0309 | 0.0523 |
| D3 | 235 | 83 | 152 | 35.32 | 27.31 | 0.021 | 0.0385 | 0.0641 |
| D4 | 235 | 91 | 144 | 38.72 | 30.19 | 0.007 | 0.0298 | 0.0386 |
| D5 | 236 | 103 | 133 | 43.64 | 32.73 | 0.0015 | 0.0215 | 0.032 |
| D6 | 235 | 101 | 134 | 42.98 | 35.17 | 0.002 | 0.0226 | 0.044 |
| D7 | 235 | 98 | 137 | 41.7 | 37.39 | 0.0112 | 0.0207 | 0.0459 |
| D8 | 235 | 96 | 139 | 40.85 | 44.28 | 0.0038 | 0.016 | 0.0493 |
| D9 | 235 | 96 | 139 | 40.85 | 62.92 | -0.0048 | -0.0007 | 0.0032 |
| D10 | 236 | 100 | 136 | 42.37 | 69.88 | -0.0006 | -0.0028 | -0.0028 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 48.774 | 46.3743 | -2.3996 |
| volume_confirmation_score | -0.3263 | -0.3685 | -0.0422 |
| liquidity_score | 2.3616 | 2.1194 | -0.2423 |
| overextension_penalty | 2.7674 | 1.5289 | -1.2385 |
| reversal_risk_penalty | 2.1894 | 1.5273 | -0.6621 |
| news_risk_penalty | 0.3375 | 0.2773 | -0.0602 |
| attention_noise_penalty | 0.19 | 0.1636 | -0.0264 |
| market_regime_penalty | 0.065 | 0.0543 | -0.0107 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **2711**
- Benchmark-adjusted coverage: **43.93%**
- Benchmark-adjusted success rate: **50.09%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260819.csv`
- Latest market index date: **2026-08-19**
- Latest price signal date: **2026-08-19**
- Latest candidate signal date: **2026-08-19**
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