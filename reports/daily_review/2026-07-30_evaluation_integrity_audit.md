# Evaluation Integrity Audit - 2026-07-30

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **15398**
- Unique evaluation keys: **2168**
- Duplicate rows by candidate key: **13230**
- Duplicate rate: **85.92%**
- Exact same-day duplicate rows: **4347**
- Same stock_code + signal_date repeated keys: **1837**
- Same candidate re-evaluated across multiple files: **1941**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 189330 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | d13d794b4b0bb573 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 368970 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 02a02e89ea75282a | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 008930 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 445bd57d12ab54d2 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 223220 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | 8cb3e3d1fc871be8 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 065770 | 2026-07-09 | 2026-07-09 | 2026-07-10 |  | bba767a7e7a60e01 | data/predictions/price_candidate_evaluation_20260710.csv | pending |
| 189330 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | d13d794b4b0bb573 | data/predictions/price_candidate_evaluation_20260712.csv | failure |
| 368970 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 02a02e89ea75282a | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 008930 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 445bd57d12ab54d2 | data/predictions/price_candidate_evaluation_20260712.csv | success |
| 223220 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | 8cb3e3d1fc871be8 | data/predictions/price_candidate_evaluation_20260712.csv | pending |
| 065770 | 2026-07-09 | 2026-07-09 | 2026-07-12 |  | bba767a7e7a60e01 | data/predictions/price_candidate_evaluation_20260712.csv | pending |
| 189330 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | d13d794b4b0bb573 | data/predictions/price_candidate_evaluation_20260713.csv | failure |
| 368970 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 02a02e89ea75282a | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 008930 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 445bd57d12ab54d2 | data/predictions/price_candidate_evaluation_20260713.csv | success |
| 223220 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | 8cb3e3d1fc871be8 | data/predictions/price_candidate_evaluation_20260713.csv | pending |
| 065770 | 2026-07-09 | 2026-07-09 | 2026-07-13 |  | bba767a7e7a60e01 | data/predictions/price_candidate_evaluation_20260713.csv | pending |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 4532 | 2340 | 2192 | 51.63 | -0.0125 | -0.0128 | -0.0379 |
| v2_conservative_ranker | 3064 | 1445 | 1619 | 47.16 | -0.0023 | -0.0382 | -0.0774 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 70 | 33 | 37 | 47.14 | -0.0012 | -0.0501 | -0.0402 |
| Top 20 | 140 | 80 | 60 | 57.14 | -0.0034 | -0.0149 | -0.0443 |
| Top 50 | 350 | 177 | 173 | 50.57 | 0.0104 | -0.0022 | -0.0396 |
| Top 100 | 700 | 360 | 340 | 51.43 | -0.0014 | -0.025 | -0.0452 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 307 | 176 | 131 | 57.33 | 17.09 | -0.026 | -0.0728 | -0.0976 |
| D2 | 306 | 160 | 146 | 52.29 | 21.91 | -0.0101 | -0.0552 | -0.1082 |
| D3 | 306 | 117 | 189 | 38.24 | 24.63 | -0.001 | -0.0174 | -0.0734 |
| D4 | 307 | 142 | 165 | 46.25 | 27.35 | -0.0007 | -0.043 | -0.1219 |
| D5 | 306 | 147 | 159 | 48.04 | 29.55 | 0.0015 | -0.0395 | -0.1154 |
| D6 | 306 | 144 | 162 | 47.06 | 31.77 | 0.0023 | -0.0382 | -0.0154 |
| D7 | 307 | 104 | 203 | 33.88 | 33.93 | 0.0081 | 0.0116 | -0.0464 |
| D8 | 306 | 143 | 163 | 46.73 | 35.83 | -0.0023 | -0.0542 | -0.0521 |
| D9 | 306 | 168 | 138 | 54.9 | 37.84 | -0.0145 | -0.0657 | -0.101 |
| D10 | 307 | 144 | 163 | 46.91 | 56.36 | 0.0197 | -0.0073 | -0.0088 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 41.9936 | 40.5998 | -1.3937 |
| volume_confirmation_score | -0.9185 | -0.9256 | -0.0071 |
| liquidity_score | 2.2498 | 2.0037 | -0.2461 |
| overextension_penalty | 1.877 | 0.9444 | -0.9325 |
| reversal_risk_penalty | 2.2632 | 1.65 | -0.6132 |
| news_risk_penalty | 0.137 | 0.0908 | -0.0462 |
| attention_noise_penalty | 0.207 | 0.2057 | -0.0013 |
| market_regime_penalty | 0.0761 | 0.0655 | -0.0107 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **0**
- Benchmark-adjusted coverage: **0.0%**
- Benchmark-adjusted success rate: **None%**
- Benchmark rows available: **80**
- Benchmark status: **Stale**
- Latest market index file: `data/raw/market_index_20260627.csv`
- Latest market index date: **2026-06-26**
- Latest price signal date: **2026-07-30**
- Latest candidate signal date: **2026-07-30**
- Finding: Benchmark coverage is missing because latest market index data ends at 2026-06-26, before latest price signal date 2026-07-30.

## Learning Loop Audit

- Active learned rules: **0**
- Eligible groups: **0**
- Groups close to activation: **0**
- Criteria: DART/error-note event_type groups, minimum 5 evaluated rows, neutral 45%-55% success gives zero adjustment.
- Finding: Learned rules are inactive because the updater learns from DART error_notes event_type groups, not price-candidate v2 outcomes, and current eligible groups are in the neutral adjustment band.

## Dashboard Status Flags

- Duplicate status: **Possible duplicates**
- Benchmark status: **Stale**
- Ranking status: **Ranking improving**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.