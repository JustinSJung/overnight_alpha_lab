# Evaluation Integrity Audit - 2026-10-08

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **508057**
- Unique evaluation keys: **22996**
- Duplicate rows by candidate key: **485061**
- Duplicate rate: **95.47%**
- Exact same-day duplicate rows: **171828**
- Same stock_code + signal_date repeated keys: **22099**
- Same candidate re-evaluated across multiple files: **22100**
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
| v1/unknown | 401 | 197 | 204 | 49.13 | -0.0135 | -0.0012 | -0.0111 |
| v2_conservative_ranker | 9525 | 4444 | 5081 | 46.66 | 0.002 | 0.0077 | 0.0115 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1565 | 691 | 874 | 44.15 | -0.0001 | -0.0003 | -0.0001 |
| avoid | 7960 | 3753 | 4207 | 47.15 | 0.0024 | 0.0091 | 0.0135 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 425 | 192 | 233 | 45.18 | 0.0004 | -0.0031 | -0.0002 |
| Top 20 | 774 | 347 | 427 | 44.83 | -0.0002 | -0.0024 | -0.0002 |
| Top 50 | 1284 | 575 | 709 | 44.78 | 0.0002 | -0.0011 | -0.001 |
| Top 100 | 1795 | 768 | 1027 | 42.79 | 0.0024 | 0.0045 | 0.0047 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 953 | 428 | 525 | 44.91 | 20.54 | 0.0014 | 0.0124 | 0.025 |
| D2 | 952 | 443 | 509 | 46.53 | 27.17 | 0.0056 | 0.0152 | 0.021 |
| D3 | 953 | 429 | 524 | 45.02 | 30.33 | 0.0036 | 0.0119 | 0.0135 |
| D4 | 952 | 450 | 502 | 47.27 | 32.55 | 0.0021 | 0.0083 | 0.0046 |
| D5 | 953 | 467 | 486 | 49.0 | 34.45 | -0.0005 | 0.0038 | 0.0098 |
| D6 | 952 | 453 | 499 | 47.58 | 36.17 | 0.0009 | 0.009 | 0.0114 |
| D7 | 952 | 449 | 503 | 47.16 | 37.71 | 0.0029 | 0.0066 | 0.0124 |
| D8 | 953 | 482 | 471 | 50.58 | 39.08 | 0.0025 | 0.0075 | 0.0115 |
| D9 | 952 | 425 | 527 | 44.64 | 54.27 | 0.0015 | 0.001 | 0.007 |
| D10 | 953 | 418 | 535 | 43.86 | 68.02 | 0.0004 | -0.0004 | -0.0046 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 45.3203 | 45.3368 | 0.0165 |
| volume_confirmation_score | -1.2331 | -1.0796 | 0.1535 |
| liquidity_score | 2.1573 | 2.0228 | -0.1345 |
| overextension_penalty | 1.5195 | 1.3137 | -0.2057 |
| reversal_risk_penalty | 1.0471 | 0.9257 | -0.1214 |
| news_risk_penalty | 0.1658 | 0.1803 | 0.0144 |
| attention_noise_penalty | 0.2841 | 0.2968 | 0.0126 |
| market_regime_penalty | 0.0941 | 0.0775 | -0.0165 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **8182**
- Benchmark-adjusted coverage: **35.58%**
- Benchmark-adjusted success rate: **51.26%**
- Benchmark rows available: **80**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261008.csv`
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