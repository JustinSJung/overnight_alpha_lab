# Evaluation Integrity Audit - 2026-08-02

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **17741**
- Unique evaluation keys: **2403**
- Duplicate rows by candidate key: **15338**
- Duplicate rate: **86.46%**
- Exact same-day duplicate rows: **4770**
- Same stock_code + signal_date repeated keys: **2053**
- Same candidate re-evaluated across multiple files: **2158**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 368970 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | cd91621fccff8931 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 065770 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | 63709cb8ab5628d0 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 038530 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | a21abe17269c1a0d | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 006730 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 013520 | 2026-07-07 | 2026-07-07 | 2026-07-10 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 368970 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | cd91621fccff8931 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 065770 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | 63709cb8ab5628d0 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 038530 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | a21abe17269c1a0d | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 006730 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 013520 | 2026-07-07 | 2026-07-07 | 2026-07-12 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 368970 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | cd91621fccff8931 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 065770 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | 63709cb8ab5628d0 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 038530 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | a21abe17269c1a0d | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 006730 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 013520 | 2026-07-07 | 2026-07-07 | 2026-07-13 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260713.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 4902 | 2534 | 2368 | 51.69 | -0.0126 | -0.0126 | -0.0373 |
| v2_conservative_ranker | 3980 | 1861 | 2119 | 46.76 | -0.0012 | -0.0425 | -0.0789 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 80 | 38 | 42 | 47.5 | 0.003 | -0.0577 | -0.0789 |
| Top 20 | 160 | 77 | 83 | 48.12 | -0.0015 | -0.0221 | -0.0447 |
| Top 50 | 400 | 169 | 231 | 42.25 | 0.0096 | 0.0039 | -0.0318 |
| Top 100 | 800 | 373 | 427 | 46.62 | 0.0084 | -0.0185 | -0.0466 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 398 | 219 | 179 | 55.03 | 17.06 | -0.0191 | -0.0767 | -0.0921 |
| D2 | 398 | 201 | 197 | 50.5 | 21.84 | -0.0073 | -0.0543 | -0.1093 |
| D3 | 398 | 148 | 250 | 37.19 | 24.63 | 0.0019 | -0.0216 | -0.0535 |
| D4 | 398 | 179 | 219 | 44.97 | 27.26 | 0.0017 | -0.0496 | -0.1139 |
| D5 | 398 | 188 | 210 | 47.24 | 29.5 | 0.004 | -0.0439 | -0.1186 |
| D6 | 398 | 195 | 203 | 48.99 | 31.68 | -0.0018 | -0.0396 | -0.0484 |
| D7 | 398 | 141 | 257 | 35.43 | 33.9 | 0.0102 | -0.0023 | -0.0559 |
| D8 | 398 | 186 | 212 | 46.73 | 35.81 | -0.003 | -0.0598 | -0.0696 |
| D9 | 398 | 215 | 183 | 54.02 | 37.85 | -0.0133 | -0.0658 | -0.0935 |
| D10 | 398 | 189 | 209 | 47.49 | 56.11 | 0.0152 | -0.0134 | -0.0173 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.7663 | 40.2329 | -1.5334 |
| volume_confirmation_score | -0.8066 | -0.8533 | -0.0467 |
| liquidity_score | 2.2649 | 2.026 | -0.239 |
| overextension_penalty | 1.8071 | 0.8863 | -0.9208 |
| reversal_risk_penalty | 2.222 | 1.6314 | -0.5906 |
| news_risk_penalty | 0.1322 | 0.0873 | -0.0449 |
| attention_noise_penalty | 0.1955 | 0.2298 | 0.0343 |
| market_regime_penalty | 0.0709 | 0.068 | -0.003 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **2402**
- Benchmark-adjusted coverage: **13.54%**
- Benchmark-adjusted success rate: **51.29%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260802.csv`
- Latest market index date: **2026-07-31**
- Latest price signal date: **2026-07-31**
- Latest candidate signal date: **2026-07-31**
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
- Ranking status: **Ranking weak**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.