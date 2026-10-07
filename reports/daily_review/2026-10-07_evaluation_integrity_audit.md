# Evaluation Integrity Audit - 2026-10-07

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **485590**
- Unique evaluation keys: **22100**
- Duplicate rows by candidate key: **463490**
- Duplicate rate: **95.45%**
- Exact same-day duplicate rows: **162872**
- Same stock_code + signal_date repeated keys: **21220**
- Same candidate re-evaluated across multiple files: **21221**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 024720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 010960 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 091590 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 024720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010960 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 091590 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 024720 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010960 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 091590 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 024720 |  |  | 2026-07-20 |  | 2208642a6721d2cc | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 010960 |  |  | 2026-07-20 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 091590 |  |  | 2026-07-20 |  | 5bc402d6287954af | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 394 | 193 | 201 | 48.98 | -0.0136 | 0.0075 | 0.0033 |
| v2_conservative_ranker | 9118 | 4227 | 4891 | 46.36 | 0.0025 | 0.0085 | 0.0122 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1415 | 640 | 775 | 45.23 | 0.0017 | 0.001 | 0.0009 |
| avoid | 7703 | 3587 | 4116 | 46.57 | 0.0027 | 0.0097 | 0.0141 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 402 | 186 | 216 | 46.27 | 0.0028 | 0.0009 | 0.0072 |
| Top 20 | 737 | 338 | 399 | 45.86 | 0.0019 | -0.0001 | 0.0031 |
| Top 50 | 1209 | 549 | 660 | 45.41 | 0.0018 | 0.0003 | -0.0001 |
| Top 100 | 1641 | 713 | 928 | 43.45 | 0.0038 | 0.0054 | 0.0047 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 912 | 409 | 503 | 44.85 | 20.41 | 0.001 | 0.0144 | 0.0263 |
| D2 | 912 | 421 | 491 | 46.16 | 26.97 | 0.0063 | 0.0148 | 0.0216 |
| D3 | 912 | 412 | 500 | 45.18 | 30.18 | 0.0039 | 0.0121 | 0.0164 |
| D4 | 911 | 435 | 476 | 47.75 | 32.42 | 0.0007 | 0.0065 | 0.004 |
| D5 | 912 | 442 | 470 | 48.46 | 34.33 | 0.0009 | 0.006 | 0.0111 |
| D6 | 912 | 420 | 492 | 46.05 | 36.04 | 0.001 | 0.0093 | 0.0109 |
| D7 | 911 | 427 | 484 | 46.87 | 37.58 | 0.0035 | 0.0084 | 0.0133 |
| D8 | 912 | 446 | 466 | 48.9 | 38.96 | 0.0036 | 0.0095 | 0.0114 |
| D9 | 912 | 406 | 506 | 44.52 | 52.26 | 0.0019 | 0.0009 | 0.0048 |
| D10 | 912 | 409 | 503 | 44.85 | 67.75 | 0.0024 | 0.0013 | -0.0008 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 45.3016 | 45.0217 | -0.2799 |
| volume_confirmation_score | -1.2227 | -1.0903 | 0.1325 |
| liquidity_score | 2.1597 | 2.0182 | -0.1415 |
| overextension_penalty | 1.6038 | 1.3552 | -0.2486 |
| reversal_risk_penalty | 1.0952 | 0.9426 | -0.1526 |
| news_risk_penalty | 0.1637 | 0.1756 | 0.0119 |
| attention_noise_penalty | 0.2984 | 0.3144 | 0.016 |
| market_regime_penalty | 0.0946 | 0.0797 | -0.0149 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **7832**
- Benchmark-adjusted coverage: **35.44%**
- Benchmark-adjusted success rate: **51.53%**
- Benchmark rows available: **78**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261007.csv`
- Latest market index date: **2026-10-07**
- Latest price signal date: **2026-10-07**
- Latest candidate signal date: **2026-10-07**
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