# Evaluation Integrity Audit - 2026-08-24

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **95477**
- Unique evaluation keys: **7092**
- Duplicate rows by candidate key: **88385**
- Duplicate rate: **92.57%**
- Exact same-day duplicate rows: **11961**
- Same stock_code + signal_date repeated keys: **5915**
- Same candidate re-evaluated across multiple files: **6552**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 419540 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 378800 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 2120f3cba4e93f0a | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 322780 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 3537343dda2bb2ff | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 229000 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 50cb3d910d8c51ef | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 066430 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 354e37246d8a38a5 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 419540 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 378800 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 2120f3cba4e93f0a | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 322780 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 3537343dda2bb2ff | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 229000 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 50cb3d910d8c51ef | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 066430 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 354e37246d8a38a5 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 419540 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | fc9e96db954ab6fd | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 378800 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 2120f3cba4e93f0a | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 322780 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 3537343dda2bb2ff | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 229000 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 50cb3d910d8c51ef | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 066430 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 354e37246d8a38a5 | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 358 | 180 | 178 | 50.28 | -0.0095 | -0.0002 | -0.0213 |
| v2_conservative_ranker | 2787 | 1168 | 1619 | 41.91 | 0.0046 | 0.0151 | 0.0292 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 586 | 240 | 346 | 40.96 | -0.0025 | -0.0075 | -0.0172 |
| avoid | 2201 | 928 | 1273 | 42.16 | 0.0065 | 0.0215 | 0.0428 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 197 | 96 | 101 | 48.73 | 0.0054 | 0.0033 | -0.0009 |
| Top 20 | 327 | 152 | 175 | 46.48 | 0.0019 | -0.0041 | -0.0056 |
| Top 50 | 522 | 233 | 289 | 44.64 | 0.0005 | -0.0051 | -0.0126 |
| Top 100 | 816 | 339 | 477 | 41.54 | 0.0022 | 0.004 | -0.0059 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 279 | 117 | 162 | 41.94 | 17.9 | 0.007 | 0.0377 | 0.0642 |
| D2 | 279 | 113 | 166 | 40.5 | 24.09 | 0.0081 | 0.0301 | 0.0539 |
| D3 | 278 | 104 | 174 | 37.41 | 27.67 | 0.0197 | 0.0302 | 0.0532 |
| D4 | 279 | 115 | 164 | 41.22 | 30.46 | 0.002 | 0.0336 | 0.0428 |
| D5 | 279 | 120 | 159 | 43.01 | 32.92 | 0.002 | -0.0043 | 0.002 |
| D6 | 278 | 128 | 150 | 46.04 | 35.15 | 0.0002 | 0.0142 | 0.0371 |
| D7 | 279 | 118 | 161 | 42.29 | 37.2 | 0.0078 | 0.0116 | 0.0347 |
| D8 | 278 | 123 | 155 | 44.24 | 41.25 | 0.0037 | 0.014 | 0.0407 |
| D9 | 279 | 111 | 168 | 39.78 | 62.48 | -0.0067 | -0.0135 | -0.0195 |
| D10 | 279 | 119 | 160 | 42.65 | 69.61 | 0.0021 | -0.0017 | -0.0162 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 48.1456 | 46.1907 | -1.955 |
| volume_confirmation_score | -0.4264 | -0.3766 | 0.0498 |
| liquidity_score | 2.3399 | 2.1143 | -0.2256 |
| overextension_penalty | 2.5286 | 1.482 | -1.0467 |
| reversal_risk_penalty | 2.1287 | 1.4727 | -0.656 |
| news_risk_penalty | 0.3193 | 0.2841 | -0.0352 |
| attention_noise_penalty | 0.2374 | 0.1979 | -0.0395 |
| market_regime_penalty | 0.0685 | 0.0568 | -0.0117 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **3145**
- Benchmark-adjusted coverage: **44.35%**
- Benchmark-adjusted success rate: **50.94%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260824.csv`
- Latest market index date: **2026-08-24**
- Latest price signal date: **2026-08-24**
- Latest candidate signal date: **2026-08-24**
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