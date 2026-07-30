# Evaluation Integrity Audit - 2026-07-30

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **15416**
- Unique evaluation keys: **2186**
- Duplicate rows by candidate key: **13230**
- Duplicate rate: **85.82%**
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
| v1/unknown | 4534 | 2342 | 2192 | 51.65 | -0.0126 | -0.0128 | -0.0379 |
| v2_conservative_ranker | 3064 | 1452 | 1612 | 47.39 | -0.0026 | -0.0382 | -0.0777 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 70 | 32 | 38 | 45.71 | -0.0014 | -0.0516 | -0.0431 |
| Top 20 | 140 | 80 | 60 | 57.14 | -0.0039 | -0.016 | -0.0439 |
| Top 50 | 350 | 179 | 171 | 51.14 | 0.0099 | -0.0021 | -0.0416 |
| Top 100 | 700 | 371 | 329 | 53.0 | -0.0026 | -0.0255 | -0.0463 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 307 | 173 | 134 | 56.35 | 17.09 | -0.0253 | -0.0727 | -0.0892 |
| D2 | 306 | 159 | 147 | 51.96 | 21.91 | -0.0101 | -0.0538 | -0.109 |
| D3 | 306 | 118 | 188 | 38.56 | 24.63 | -0.0018 | -0.0175 | -0.073 |
| D4 | 307 | 142 | 165 | 46.25 | 27.35 | -0.001 | -0.0433 | -0.124 |
| D5 | 306 | 152 | 154 | 49.67 | 29.55 | 0.0001 | -0.0393 | -0.1165 |
| D6 | 306 | 144 | 162 | 47.06 | 31.77 | 0.0022 | -0.0381 | -0.0176 |
| D7 | 307 | 108 | 199 | 35.18 | 33.93 | 0.0074 | 0.0116 | -0.0462 |
| D8 | 306 | 145 | 161 | 47.39 | 35.83 | -0.0031 | -0.055 | -0.0552 |
| D9 | 306 | 168 | 138 | 54.9 | 37.84 | -0.014 | -0.0655 | -0.1025 |
| D10 | 307 | 143 | 164 | 46.58 | 56.36 | 0.0196 | -0.0075 | -0.0108 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.9252 | 40.6553 | -1.2699 |
| volume_confirmation_score | -0.9016 | -0.9408 | -0.0393 |
| liquidity_score | 2.2514 | 2.0012 | -0.2501 |
| overextension_penalty | 1.8594 | 0.9562 | -0.9032 |
| reversal_risk_penalty | 2.2405 | 1.6678 | -0.5728 |
| news_risk_penalty | 0.1364 | 0.0912 | -0.0452 |
| attention_noise_penalty | 0.1963 | 0.2153 | 0.019 |
| market_regime_penalty | 0.073 | 0.0682 | -0.0048 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **1118**
- Benchmark-adjusted coverage: **7.25%**
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