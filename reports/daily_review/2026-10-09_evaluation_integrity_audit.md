# Evaluation Integrity Audit - 2026-10-09

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **530524**
- Unique evaluation keys: **22996**
- Duplicate rows by candidate key: **507528**
- Duplicate rate: **95.67%**
- Exact same-day duplicate rows: **180964**
- Same stock_code + signal_date repeated keys: **22995**
- Same candidate re-evaluated across multiple files: **22996**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 253450 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 253450 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 253450 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 013520 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 006730 |  |  | 2026-07-20 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 013520 |  |  | 2026-07-20 |  | bf35eff02e0d2746 | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 253450 |  |  | 2026-07-20 |  | f4cc8221599d8c01 | data/predictions/price_candidate_evaluation_20260720.csv | failure |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 407 | 203 | 204 | 49.88 | -0.0138 | 0.0095 | 0.0044 |
| v2_conservative_ranker | 9399 | 4389 | 5010 | 46.7 | 0.0019 | 0.0079 | 0.0119 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1537 | 669 | 868 | 43.53 | -0.0004 | 0.0004 | 0.0014 |
| avoid | 7862 | 3720 | 4142 | 47.32 | 0.0024 | 0.0093 | 0.0136 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 412 | 188 | 224 | 45.63 | 0.0017 | 0.0001 | 0.0064 |
| Top 20 | 755 | 343 | 412 | 45.43 | 0.0005 | -0.0011 | 0.0024 |
| Top 50 | 1260 | 563 | 697 | 44.68 | 0.0003 | -0.0005 | 0.0004 |
| Top 100 | 1748 | 749 | 999 | 42.85 | 0.0018 | 0.0045 | 0.005 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 940 | 426 | 514 | 45.32 | 20.32 | -0.0001 | 0.0119 | 0.0244 |
| D2 | 940 | 439 | 501 | 46.7 | 27.1 | 0.0063 | 0.0165 | 0.0249 |
| D3 | 940 | 418 | 522 | 44.47 | 30.3 | 0.0039 | 0.0113 | 0.0136 |
| D4 | 940 | 452 | 488 | 48.09 | 32.55 | 0.002 | 0.0067 | 0.0029 |
| D5 | 940 | 473 | 467 | 50.32 | 34.45 | -0.0007 | 0.0056 | 0.0102 |
| D6 | 939 | 439 | 500 | 46.75 | 36.15 | 0.0012 | 0.0099 | 0.0118 |
| D7 | 940 | 444 | 496 | 47.23 | 37.68 | 0.0026 | 0.0064 | 0.0122 |
| D8 | 940 | 475 | 465 | 50.53 | 39.06 | 0.0029 | 0.0086 | 0.0106 |
| D9 | 940 | 415 | 525 | 44.15 | 54.11 | 0.0008 | 0.001 | 0.006 |
| D10 | 940 | 408 | 532 | 43.4 | 67.95 | 0.0002 | 0.0001 | -0.0016 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 45.3215 | 45.3577 | 0.0362 |
| volume_confirmation_score | -1.2352 | -1.0937 | 0.1415 |
| liquidity_score | 2.1556 | 2.0265 | -0.1291 |
| overextension_penalty | 1.5756 | 1.3489 | -0.2267 |
| reversal_risk_penalty | 1.0813 | 0.9387 | -0.1426 |
| news_risk_penalty | 0.1643 | 0.1776 | 0.0134 |
| attention_noise_penalty | 0.2818 | 0.2972 | 0.0154 |
| market_regime_penalty | 0.0934 | 0.0754 | -0.018 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **8072**
- Benchmark-adjusted coverage: **35.1%**
- Benchmark-adjusted success rate: **51.3%**
- Benchmark rows available: **80**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261009.csv`
- Latest market index date: **2026-10-08**
- Latest price signal date: **2026-10-08**
- Latest candidate signal date: **2026-10-08**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **7**
- Eligible groups: **11**
- Groups close to activation: **2**
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