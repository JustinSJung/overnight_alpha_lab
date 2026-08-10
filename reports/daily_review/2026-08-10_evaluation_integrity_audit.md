# Evaluation Integrity Audit - 2026-08-10

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **40628**
- Unique evaluation keys: **4232**
- Duplicate rows by candidate key: **36396**
- Duplicate rate: **89.58%**
- Exact same-day duplicate rows: **7731**
- Same stock_code + signal_date repeated keys: **3408**
- Same candidate re-evaluated across multiple files: **3759**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 003070 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 216080 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 003070 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 216080 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 008930 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 5ce72a163b913877 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 003070 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | f1d2502f0ec6bc0d | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 216080 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 8e1453eb4b5434af | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 253450 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 011930 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | b2835b8ef265332f | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 7492 | 3869 | 3623 | 51.64 | -0.0125 | -0.0102 | -0.0335 |
| v2_conservative_ranker | 13345 | 5651 | 7694 | 42.35 | 0.0063 | 0.0024 | 0.0011 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 140 | 72 | 68 | 51.43 | 0.0091 | -0.0168 | -0.0254 |
| Top 20 | 280 | 154 | 126 | 55.0 | 0.0107 | -0.0087 | -0.0286 |
| Top 50 | 700 | 388 | 312 | 55.43 | 0.0086 | 0.0095 | 0.0023 |
| Top 100 | 1400 | 656 | 744 | 46.86 | 0.0114 | 0.0198 | 0.0157 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking improving**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1335 | 568 | 767 | 42.55 | 16.8 | 0.0037 | 0.0202 | 0.0329 |
| D2 | 1334 | 593 | 741 | 44.45 | 21.72 | 0.0017 | -0.0092 | -0.0213 |
| D3 | 1335 | 508 | 827 | 38.05 | 24.79 | 0.0087 | 0.018 | 0.0226 |
| D4 | 1334 | 519 | 815 | 38.91 | 27.39 | 0.0155 | 0.0111 | 0.0003 |
| D5 | 1335 | 582 | 753 | 43.6 | 29.65 | 0.008 | 0.0095 | -0.0109 |
| D6 | 1334 | 469 | 865 | 35.16 | 31.85 | 0.0123 | 0.0044 | -0.0032 |
| D7 | 1334 | 556 | 778 | 41.68 | 34.19 | 0.0031 | 0.0029 | -0.0069 |
| D8 | 1335 | 574 | 761 | 43.0 | 36.24 | -0.0002 | -0.0277 | -0.0165 |
| D9 | 1334 | 617 | 717 | 46.25 | 38.34 | 0.0063 | -0.0044 | 0.0119 |
| D10 | 1335 | 665 | 670 | 49.81 | 60.52 | 0.0041 | -0.0024 | 0.0048 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 43.023 | 39.995 | -3.0279 |
| volume_confirmation_score | -0.5222 | -0.658 | -0.1358 |
| liquidity_score | 2.312 | 2.0818 | -0.2302 |
| overextension_penalty | 2.0601 | 1.0453 | -1.0148 |
| reversal_risk_penalty | 2.1907 | 1.5658 | -0.6249 |
| news_risk_penalty | 0.1609 | 0.0863 | -0.0746 |
| attention_noise_penalty | 0.2206 | 0.2227 | 0.0021 |
| market_regime_penalty | 0.0711 | 0.0554 | -0.0158 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **14357**
- Benchmark-adjusted coverage: **35.34%**
- Benchmark-adjusted success rate: **51.73%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260810.csv`
- Latest market index date: **2026-08-10**
- Latest price signal date: **2026-08-10**
- Latest candidate signal date: **2026-08-10**
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