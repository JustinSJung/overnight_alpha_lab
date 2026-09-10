# Evaluation Integrity Audit - 2026-09-10

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **204474**
- Unique evaluation keys: **11380**
- Duplicate rows by candidate key: **193094**
- Duplicate rate: **94.43%**
- Exact same-day duplicate rows: **48045**
- Same stock_code + signal_date repeated keys: **10765**
- Same candidate re-evaluated across multiple files: **10766**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 000720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 000720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 187870 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 321370 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 000720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 000720 |  |  | 2026-07-20 |  | 03e8ccf2ee7fbf0d | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 321370 |  |  | 2026-07-20 |  | df654892030874da | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 394 | 194 | 200 | 49.24 | -0.0137 | 0.0103 | 0.0039 |
| v2_conservative_ranker | 4618 | 2087 | 2531 | 45.19 | 0.0033 | 0.0149 | 0.0244 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 763 | 324 | 439 | 42.46 | -0.0011 | -0.0048 | -0.008 |
| avoid | 3855 | 1763 | 2092 | 45.73 | 0.0042 | 0.0191 | 0.0315 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 285 | 132 | 153 | 46.32 | 0.0017 | 0.0036 | 0.008 |
| Top 20 | 494 | 220 | 274 | 44.53 | -0.0 | -0.0017 | 0.0029 |
| Top 50 | 729 | 316 | 413 | 43.35 | -0.0007 | -0.0052 | -0.0072 |
| Top 100 | 1054 | 434 | 620 | 41.18 | 0.0027 | 0.0027 | 0.0008 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 462 | 200 | 262 | 43.29 | 19.07 | 0.006 | 0.0356 | 0.0571 |
| D2 | 462 | 195 | 267 | 42.21 | 25.46 | 0.0099 | 0.0329 | 0.0578 |
| D3 | 462 | 203 | 259 | 43.94 | 28.98 | 0.0087 | 0.023 | 0.0371 |
| D4 | 461 | 209 | 252 | 45.34 | 31.46 | -0.0003 | 0.0163 | 0.0225 |
| D5 | 462 | 227 | 235 | 49.13 | 33.52 | 0.0019 | 0.0144 | 0.0152 |
| D6 | 462 | 206 | 256 | 44.59 | 35.39 | 0.0008 | 0.0137 | 0.0152 |
| D7 | 461 | 219 | 242 | 47.51 | 37.13 | 0.0058 | 0.013 | 0.0207 |
| D8 | 462 | 231 | 231 | 50.0 | 38.79 | 0.0023 | 0.009 | 0.0257 |
| D9 | 462 | 202 | 260 | 43.72 | 54.24 | -0.0019 | -0.0062 | -0.0019 |
| D10 | 462 | 195 | 267 | 42.21 | 67.9 | -0.0002 | -0.0034 | -0.0096 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 46.3559 | 45.5937 | -0.7622 |
| volume_confirmation_score | -0.9291 | -0.8005 | 0.1286 |
| liquidity_score | 2.2214 | 2.0462 | -0.1751 |
| overextension_penalty | 2.018 | 1.4874 | -0.5305 |
| reversal_risk_penalty | 1.5494 | 1.2374 | -0.3121 |
| news_risk_penalty | 0.2516 | 0.2643 | 0.0128 |
| attention_noise_penalty | 0.3393 | 0.3503 | 0.0109 |
| market_regime_penalty | 0.0997 | 0.0735 | -0.0262 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **4753**
- Benchmark-adjusted coverage: **41.77%**
- Benchmark-adjusted success rate: **50.54%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260910.csv`
- Latest market index date: **2026-09-10**
- Latest price signal date: **2026-09-10**
- Latest candidate signal date: **2026-09-10**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **11**
- Eligible groups: **11**
- Groups close to activation: **1**
- Criteria: DART/error-note event_type groups, minimum 5 evaluated rows, neutral 45%-55% success gives zero adjustment.
- Finding: Some learned event rules are active.

## Dashboard Status Flags

- Duplicate status: **Possible duplicates**
- Benchmark status: **Partial**
- Ranking status: **Ranking weak**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.