# Evaluation Integrity Audit - 2026-08-03

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **20295**
- Unique evaluation keys: **2632**
- Duplicate rows by candidate key: **17663**
- Duplicate rate: **87.03%**
- Exact same-day duplicate rows: **5193**
- Same stock_code + signal_date repeated keys: **2269**
- Same candidate re-evaluated across multiple files: **2375**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 468530 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 92242c49f70fc615 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 019570 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 9273aabfc263ed3e | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 468530 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 92242c49f70fc615 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 019570 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 9273aabfc263ed3e | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 024720 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 047040 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 2cf5a18a2298b9f2 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 468530 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 92242c49f70fc615 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 019570 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 9273aabfc263ed3e | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 5270 | 2726 | 2544 | 51.73 | -0.0127 | -0.0123 | -0.0367 |
| v2_conservative_ranker | 5053 | 2320 | 2733 | 45.91 | 0.0003 | -0.0386 | -0.0766 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 90 | 43 | 47 | 47.78 | 0.0039 | -0.0511 | -0.0704 |
| Top 20 | 180 | 90 | 90 | 50.0 | 0.0024 | -0.0161 | -0.0483 |
| Top 50 | 450 | 207 | 243 | 46.0 | 0.0069 | -0.0004 | -0.038 |
| Top 100 | 900 | 398 | 502 | 44.22 | 0.0087 | -0.0102 | -0.042 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 506 | 262 | 244 | 51.78 | 16.91 | -0.0115 | -0.0603 | -0.0885 |
| D2 | 505 | 251 | 254 | 49.7 | 21.7 | -0.0074 | -0.0525 | -0.1071 |
| D3 | 505 | 193 | 312 | 38.22 | 24.58 | 0.0037 | -0.0251 | -0.048 |
| D4 | 505 | 214 | 291 | 42.38 | 27.14 | 0.0057 | -0.0458 | -0.1002 |
| D5 | 506 | 228 | 278 | 45.06 | 29.42 | 0.0081 | -0.0394 | -0.1165 |
| D6 | 505 | 241 | 264 | 47.72 | 31.57 | -0.0021 | -0.0353 | -0.0621 |
| D7 | 505 | 185 | 320 | 36.63 | 33.85 | 0.0095 | -0.008 | -0.0574 |
| D8 | 505 | 237 | 268 | 46.93 | 35.77 | -0.003 | -0.0493 | -0.0744 |
| D9 | 505 | 266 | 239 | 52.67 | 37.85 | -0.012 | -0.058 | -0.0899 |
| D10 | 506 | 243 | 263 | 48.02 | 56.04 | 0.0123 | -0.0137 | -0.0162 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.6977 | 39.8979 | -1.7998 |
| volume_confirmation_score | -0.7272 | -0.7753 | -0.0481 |
| liquidity_score | 2.2772 | 2.0472 | -0.23 |
| overextension_penalty | 1.7973 | 0.9127 | -0.8846 |
| reversal_risk_penalty | 2.2032 | 1.598 | -0.6051 |
| news_risk_penalty | 0.1319 | 0.0831 | -0.0488 |
| attention_noise_penalty | 0.1969 | 0.2392 | 0.0423 |
| market_regime_penalty | 0.0698 | 0.0688 | -0.001 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **3843**
- Benchmark-adjusted coverage: **18.94%**
- Benchmark-adjusted success rate: **51.29%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260803.csv`
- Latest market index date: **2026-08-03**
- Latest price signal date: **2026-08-03**
- Latest candidate signal date: **2026-08-03**
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