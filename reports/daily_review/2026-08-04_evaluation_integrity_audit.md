# Evaluation Integrity Audit - 2026-08-04

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **23286**
- Unique evaluation keys: **3069**
- Duplicate rows by candidate key: **20217**
- Duplicate rate: **86.82%**
- Exact same-day duplicate rows: **5616**
- Same stock_code + signal_date repeated keys: **2497**
- Same candidate re-evaluated across multiple files: **2604**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 006730 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 288980 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 020560 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 006730 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 288980 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 020560 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 006730 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 288980 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 333a787914ba462d | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 020560 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | fd0308f1ee2cdc9e | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260713.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 5638 | 2916 | 2722 | 51.72 | -0.0127 | -0.0121 | -0.0363 |
| v2_conservative_ranker | 6258 | 2799 | 3459 | 44.73 | 0.0022 | -0.0287 | -0.0676 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 100 | 46 | 54 | 46.0 | 0.006 | -0.0445 | -0.0723 |
| Top 20 | 200 | 110 | 90 | 55.0 | 0.0083 | -0.0119 | -0.0436 |
| Top 50 | 500 | 228 | 272 | 45.6 | 0.0085 | 0.0035 | -0.0235 |
| Top 100 | 1000 | 435 | 565 | 43.5 | 0.0113 | 0.0016 | -0.0294 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 626 | 300 | 326 | 47.92 | 16.81 | -0.0056 | -0.0395 | -0.0765 |
| D2 | 626 | 313 | 313 | 50.0 | 21.61 | -0.0059 | -0.0402 | -0.0957 |
| D3 | 626 | 236 | 390 | 37.7 | 24.53 | 0.0061 | -0.02 | -0.0401 |
| D4 | 625 | 256 | 369 | 40.96 | 27.06 | 0.0082 | -0.0285 | -0.0898 |
| D5 | 626 | 266 | 360 | 42.49 | 29.36 | 0.0127 | -0.022 | -0.1005 |
| D6 | 626 | 297 | 329 | 47.44 | 31.45 | -0.0009 | -0.0268 | -0.0731 |
| D7 | 625 | 210 | 415 | 33.6 | 33.79 | 0.0094 | -0.0112 | -0.0451 |
| D8 | 626 | 298 | 328 | 47.6 | 35.74 | -0.0031 | -0.0377 | -0.0701 |
| D9 | 626 | 319 | 307 | 50.96 | 37.85 | -0.0098 | -0.0502 | -0.0742 |
| D10 | 626 | 304 | 322 | 48.56 | 56.0 | 0.0107 | -0.0111 | -0.0115 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.7142 | 39.5899 | -2.1243 |
| volume_confirmation_score | -0.6761 | -0.7417 | -0.0657 |
| liquidity_score | 2.2847 | 2.0607 | -0.224 |
| overextension_penalty | 1.7952 | 0.9073 | -0.8878 |
| reversal_risk_penalty | 2.1861 | 1.5754 | -0.6107 |
| news_risk_penalty | 0.1336 | 0.0789 | -0.0547 |
| attention_noise_penalty | 0.1947 | 0.2307 | 0.0361 |
| market_regime_penalty | 0.0715 | 0.0648 | -0.0067 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **5416**
- Benchmark-adjusted coverage: **23.26%**
- Benchmark-adjusted success rate: **51.2%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260804.csv`
- Latest market index date: **2026-08-04**
- Latest price signal date: **2026-08-04**
- Latest candidate signal date: **2026-08-04**
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