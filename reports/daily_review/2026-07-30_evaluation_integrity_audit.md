# Evaluation Integrity Audit - 2026-07-30

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **15405**
- Unique evaluation keys: **2175**
- Duplicate rows by candidate key: **13230**
- Duplicate rate: **85.88%**
- Exact same-day duplicate rows: **4347**
- Same stock_code + signal_date repeated keys: **1837**
- Same candidate re-evaluated across multiple files: **1941**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 025980 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 19abd2d60fbabea4 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 378800 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 2120f3cba4e93f0a | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 025980 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 19abd2d60fbabea4 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 378800 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 2120f3cba4e93f0a | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 010960 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 025980 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 19abd2d60fbabea4 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 378800 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 2120f3cba4e93f0a | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 4532 | 2340 | 2192 | 51.63 | -0.0125 | -0.0128 | -0.0379 |
| v2_conservative_ranker | 3064 | 1457 | 1607 | 47.55 | -0.0028 | -0.0385 | -0.0784 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 70 | 33 | 37 | 47.14 | -0.002 | -0.0522 | -0.0433 |
| Top 20 | 140 | 80 | 60 | 57.14 | -0.004 | -0.0157 | -0.0453 |
| Top 50 | 350 | 180 | 170 | 51.43 | 0.0089 | -0.0038 | -0.0412 |
| Top 100 | 700 | 373 | 327 | 53.29 | -0.0032 | -0.0266 | -0.0461 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 307 | 174 | 133 | 56.68 | 17.09 | -0.0258 | -0.0727 | -0.0933 |
| D2 | 306 | 160 | 146 | 52.29 | 21.91 | -0.0103 | -0.0549 | -0.1088 |
| D3 | 306 | 119 | 187 | 38.89 | 24.63 | -0.0019 | -0.0176 | -0.0728 |
| D4 | 307 | 143 | 164 | 46.58 | 27.35 | -0.0011 | -0.0432 | -0.123 |
| D5 | 306 | 151 | 155 | 49.35 | 29.55 | 0.0003 | -0.0395 | -0.1164 |
| D6 | 306 | 145 | 161 | 47.39 | 31.77 | 0.0021 | -0.0381 | -0.018 |
| D7 | 307 | 108 | 199 | 35.18 | 33.93 | 0.0073 | 0.0117 | -0.051 |
| D8 | 306 | 145 | 161 | 47.39 | 35.83 | -0.0032 | -0.0553 | -0.0543 |
| D9 | 306 | 168 | 138 | 54.9 | 37.84 | -0.015 | -0.0658 | -0.1032 |
| D10 | 307 | 144 | 163 | 46.91 | 56.36 | 0.0196 | -0.0088 | -0.0098 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.8964 | 40.6776 | -1.2188 |
| volume_confirmation_score | -0.898 | -0.9442 | -0.0462 |
| liquidity_score | 2.2526 | 1.9994 | -0.2532 |
| overextension_penalty | 1.853 | 0.9592 | -0.8939 |
| reversal_risk_penalty | 2.241 | 1.6656 | -0.5754 |
| news_risk_penalty | 0.1359 | 0.0915 | -0.0444 |
| attention_noise_penalty | 0.1956 | 0.216 | 0.0204 |
| market_regime_penalty | 0.0741 | 0.0672 | -0.0069 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **1116**
- Benchmark-adjusted coverage: **7.24%**
- Benchmark-adjusted success rate: **48.66%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260730.csv`
- Latest market index date: **2026-07-30**
- Latest price signal date: **2026-07-30**
- Latest candidate signal date: **2026-07-30**
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