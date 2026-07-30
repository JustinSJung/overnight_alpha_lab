# Evaluation Integrity Audit - 2026-07-30

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **15392**
- Unique evaluation keys: **2162**
- Duplicate rows by candidate key: **13230**
- Duplicate rate: **85.95%**
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
| v2_conservative_ranker | 3064 | 1424 | 1640 | 46.48 | -0.0016 | -0.0376 | -0.0752 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 70 | 31 | 39 | 44.29 | 0.0005 | -0.0504 | -0.0382 |
| Top 20 | 140 | 76 | 64 | 54.29 | -0.0015 | -0.0147 | -0.0419 |
| Top 50 | 350 | 171 | 179 | 48.86 | 0.0124 | -0.0016 | -0.0371 |
| Top 100 | 700 | 347 | 353 | 49.57 | 0.0007 | -0.0233 | -0.043 |

Ranking status: **Ranking improving**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 307 | 173 | 134 | 56.35 | 17.09 | -0.0248 | -0.0723 | -0.0952 |
| D2 | 306 | 158 | 148 | 51.63 | 21.91 | -0.0096 | -0.0549 | -0.1054 |
| D3 | 306 | 113 | 193 | 36.93 | 24.63 | -0.0006 | -0.0169 | -0.0693 |
| D4 | 307 | 142 | 165 | 46.25 | 27.35 | -0.0003 | -0.0417 | -0.1202 |
| D5 | 306 | 144 | 162 | 47.06 | 29.55 | 0.0025 | -0.0393 | -0.1134 |
| D6 | 306 | 141 | 165 | 46.08 | 31.77 | 0.003 | -0.038 | -0.0149 |
| D7 | 307 | 102 | 205 | 33.22 | 33.93 | 0.0088 | 0.0122 | -0.0448 |
| D8 | 306 | 143 | 163 | 46.73 | 35.83 | -0.0018 | -0.0529 | -0.0507 |
| D9 | 306 | 167 | 139 | 54.58 | 37.84 | -0.0139 | -0.0649 | -0.0974 |
| D10 | 307 | 141 | 166 | 45.93 | 56.36 | 0.0202 | -0.0062 | -0.0058 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 42.1062 | 40.5199 | -1.5863 |
| volume_confirmation_score | -0.9499 | -0.8982 | 0.0516 |
| liquidity_score | 2.2451 | 2.011 | -0.2341 |
| overextension_penalty | 1.9046 | 0.9323 | -0.9723 |
| reversal_risk_penalty | 2.2693 | 1.6526 | -0.6167 |
| news_risk_penalty | 0.139 | 0.0896 | -0.0494 |
| attention_noise_penalty | 0.2133 | 0.2002 | -0.0132 |
| market_regime_penalty | 0.0772 | 0.0646 | -0.0126 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **0**
- Benchmark-adjusted coverage: **0.0%**
- Latest market index file: `data/raw/market_index_20260627.csv`
- Latest market index date: **2026-06-26**
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
- Benchmark status: **Benchmark missing**
- Ranking status: **Ranking improving**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.