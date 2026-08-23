# Evaluation Integrity Audit - 2026-08-23

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **88660**
- Unique evaluation keys: **6777**
- Duplicate rows by candidate key: **81883**
- Duplicate rate: **92.36%**
- Exact same-day duplicate rows: **11538**
- Same stock_code + signal_date repeated keys: **5614**
- Same candidate re-evaluated across multiple files: **6249**
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
| v1/unknown | 380 | 195 | 185 | 51.32 | -0.0114 | -0.0048 | -0.0265 |
| v2_conservative_ranker | 2628 | 1101 | 1527 | 41.89 | 0.0047 | 0.0159 | 0.0357 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 565 | 230 | 335 | 40.71 | -0.0032 | -0.0079 | -0.0087 |
| avoid | 2063 | 871 | 1192 | 42.22 | 0.0069 | 0.0228 | 0.0464 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 187 | 91 | 96 | 48.66 | 0.0042 | -0.0017 | 0.004 |
| Top 20 | 307 | 142 | 165 | 46.25 | 0.0008 | -0.0048 | 0.0005 |
| Top 50 | 502 | 224 | 278 | 44.62 | -0.0001 | -0.0055 | -0.0085 |
| Top 100 | 805 | 335 | 470 | 41.61 | 0.0018 | 0.0039 | -0.0008 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 263 | 109 | 154 | 41.44 | 17.88 | 0.0094 | 0.0371 | 0.063 |
| D2 | 263 | 105 | 158 | 39.92 | 24.03 | 0.0081 | 0.0301 | 0.0532 |
| D3 | 263 | 93 | 170 | 35.36 | 27.63 | 0.0218 | 0.0323 | 0.0586 |
| D4 | 262 | 105 | 157 | 40.08 | 30.41 | 0.0024 | 0.035 | 0.0438 |
| D5 | 263 | 120 | 143 | 45.63 | 32.9 | -0.0003 | -0.0038 | 0.0115 |
| D6 | 263 | 121 | 142 | 46.01 | 35.25 | 0.0005 | 0.0183 | 0.0418 |
| D7 | 262 | 117 | 145 | 44.66 | 37.33 | 0.007 | 0.0125 | 0.0416 |
| D8 | 263 | 114 | 149 | 43.35 | 42.32 | 0.0042 | 0.0115 | 0.0421 |
| D9 | 263 | 106 | 157 | 40.3 | 62.66 | -0.007 | -0.0081 | -0.0065 |
| D10 | 263 | 111 | 152 | 42.21 | 69.68 | 0.001 | -0.0067 | -0.0102 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 48.4179 | 46.3146 | -2.1033 |
| volume_confirmation_score | -0.4031 | -0.3784 | 0.0246 |
| liquidity_score | 2.3442 | 2.1139 | -0.2303 |
| overextension_penalty | 2.6142 | 1.4963 | -1.1179 |
| reversal_risk_penalty | 2.1568 | 1.4897 | -0.6671 |
| news_risk_penalty | 0.3224 | 0.2796 | -0.0428 |
| attention_noise_penalty | 0.2272 | 0.1891 | -0.038 |
| market_regime_penalty | 0.0672 | 0.0537 | -0.0135 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **3008**
- Benchmark-adjusted coverage: **44.39%**
- Benchmark-adjusted success rate: **51.43%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260823.csv`
- Latest market index date: **2026-08-21**
- Latest price signal date: **2026-08-21**
- Latest candidate signal date: **2026-08-21**
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