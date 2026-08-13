# Evaluation Integrity Audit - 2026-08-13

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **54102**
- Unique evaluation keys: **5040**
- Duplicate rows by candidate key: **49062**
- Duplicate rate: **90.68%**
- Exact same-day duplicate rows: **9000**
- Same stock_code + signal_date repeated keys: **4185**
- Same candidate re-evaluated across multiple files: **4539**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 322780 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 3537343dda2bb2ff | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 141080 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 86c5d271d855238c | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 043260 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | e4617eadc375de9f | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 000720 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 8803cd8e00cafaa3 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 322780 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 3537343dda2bb2ff | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 141080 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 86c5d271d855238c | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 043260 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | e4617eadc375de9f | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 000720 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 8803cd8e00cafaa3 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 322780 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 3537343dda2bb2ff | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 141080 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 86c5d271d855238c | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 043260 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | e4617eadc375de9f | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 000720 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 8803cd8e00cafaa3 | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 375 | 192 | 183 | 51.2 | -0.0114 | -0.0041 | -0.0256 |
| v2_conservative_ranker | 1946 | 785 | 1161 | 40.34 | 0.0102 | 0.0267 | 0.0479 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 356 | 172 | 184 | 48.31 | 0.0045 | 0.0085 | 0.0191 |
| avoid | 1590 | 613 | 977 | 38.55 | 0.0115 | 0.0297 | 0.051 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 137 | 75 | 62 | 54.74 | 0.0063 | 0.0094 | 0.0192 |
| Top 20 | 209 | 109 | 100 | 52.15 | 0.006 | 0.0108 | 0.0179 |
| Top 50 | 351 | 173 | 178 | 49.29 | 0.0049 | 0.0081 | 0.0136 |
| Top 100 | 604 | 277 | 327 | 45.86 | 0.0076 | 0.0181 | 0.0144 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 195 | 79 | 116 | 40.51 | 17.5 | 0.007 | 0.0455 | 0.0788 |
| D2 | 195 | 76 | 119 | 38.97 | 23.13 | 0.0092 | 0.0236 | 0.0339 |
| D3 | 194 | 71 | 123 | 36.6 | 26.5 | 0.0181 | 0.0408 | 0.0656 |
| D4 | 195 | 73 | 122 | 37.44 | 29.33 | 0.0178 | 0.0322 | 0.057 |
| D5 | 194 | 68 | 126 | 35.05 | 31.66 | 0.0101 | 0.041 | 0.0491 |
| D6 | 195 | 80 | 115 | 41.03 | 34.19 | 0.0075 | 0.0115 | 0.0292 |
| D7 | 194 | 79 | 115 | 40.72 | 36.43 | 0.0099 | 0.0162 | 0.0374 |
| D8 | 195 | 76 | 119 | 38.97 | 38.52 | 0.012 | 0.0255 | 0.0524 |
| D9 | 194 | 91 | 103 | 46.91 | 58.19 | 0.0056 | 0.0125 | 0.0406 |
| D10 | 195 | 92 | 103 | 47.18 | 69.19 | 0.0048 | 0.0089 | 0.0089 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 48.1271 | 44.1578 | -3.9693 |
| volume_confirmation_score | -0.3634 | -0.5156 | -0.1521 |
| liquidity_score | 2.349 | 2.1025 | -0.2465 |
| overextension_penalty | 2.6322 | 1.4839 | -1.1483 |
| reversal_risk_penalty | 2.162 | 1.5568 | -0.6052 |
| news_risk_penalty | 0.3363 | 0.1886 | -0.1477 |
| attention_noise_penalty | 0.2096 | 0.1891 | -0.0205 |
| market_regime_penalty | 0.0688 | 0.0534 | -0.0154 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **2321**
- Benchmark-adjusted coverage: **46.05%**
- Benchmark-adjusted success rate: **51.36%**
- Benchmark rows available: **86**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260813.csv`
- Latest market index date: **2026-08-13**
- Latest price signal date: **2026-08-13**
- Latest candidate signal date: **2026-08-13**
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