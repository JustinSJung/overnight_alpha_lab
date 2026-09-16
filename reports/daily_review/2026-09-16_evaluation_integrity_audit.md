# Evaluation Integrity Audit - 2026-09-16

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **254519**
- Unique evaluation keys: **14078**
- Duplicate rows by candidate key: **240441**
- Duplicate rate: **94.47%**
- Exact same-day duplicate rows: **67925**
- Same stock_code + signal_date repeated keys: **13371**
- Same candidate re-evaluated across multiple files: **13372**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 004380 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 019570 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004380 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 019570 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 004380 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010140 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 019570 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  | 2026-07-20 |  | 6ddc663d233d1452 | data/predictions/price_candidate_evaluation_20260720.csv | pending |
| 004380 |  |  | 2026-07-20 |  | 0c7b363eacd84407 | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 019570 |  |  | 2026-07-20 |  | dbf433a2a1645983 | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 396 | 195 | 201 | 49.24 | -0.0125 | 0.0124 | 0.0086 |
| v2_conservative_ranker | 5779 | 2711 | 3068 | 46.91 | 0.002 | 0.009 | 0.0165 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 856 | 362 | 494 | 42.29 | -0.0019 | -0.0062 | -0.0085 |
| avoid | 4923 | 2349 | 2574 | 47.71 | 0.0027 | 0.0118 | 0.0213 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 323 | 149 | 174 | 46.13 | 0.0009 | 0.0003 | 0.0037 |
| Top 20 | 567 | 252 | 315 | 44.44 | -0.0007 | -0.0033 | 0.0006 |
| Top 50 | 825 | 355 | 470 | 43.03 | -0.0018 | -0.0066 | -0.008 |
| Top 100 | 1155 | 475 | 680 | 41.13 | 0.0018 | 0.0016 | -0.0003 |

Ranking status: **Ranking weak**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 578 | 244 | 334 | 42.21 | 19.81 | 0.0043 | 0.0233 | 0.046 |
| D2 | 578 | 260 | 318 | 44.98 | 26.06 | 0.0075 | 0.0274 | 0.0418 |
| D3 | 578 | 261 | 317 | 45.16 | 29.26 | 0.0066 | 0.0148 | 0.0267 |
| D4 | 578 | 289 | 289 | 50.0 | 31.6 | -0.0026 | 0.0056 | 0.0048 |
| D5 | 578 | 290 | 288 | 50.17 | 33.57 | 0.0022 | 0.0059 | 0.0095 |
| D6 | 577 | 285 | 292 | 49.39 | 35.33 | -0.0011 | 0.0046 | 0.0129 |
| D7 | 578 | 289 | 289 | 50.0 | 36.99 | 0.003 | 0.0097 | 0.0148 |
| D8 | 578 | 280 | 298 | 48.44 | 38.58 | 0.0035 | 0.0074 | 0.019 |
| D9 | 578 | 267 | 311 | 46.19 | 50.25 | -0.0024 | -0.0029 | 0.0003 |
| D10 | 578 | 246 | 332 | 42.56 | 66.98 | -0.0009 | -0.0058 | -0.0102 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 45.1913 | 45.036 | -0.1553 |
| volume_confirmation_score | -1.1693 | -0.9737 | 0.1956 |
| liquidity_score | 2.1697 | 2.0068 | -0.1628 |
| overextension_penalty | 1.7669 | 1.3749 | -0.3921 |
| reversal_risk_penalty | 1.2866 | 1.1015 | -0.185 |
| news_risk_penalty | 0.1981 | 0.2379 | 0.0399 |
| attention_noise_penalty | 0.33 | 0.3778 | 0.0478 |
| market_regime_penalty | 0.1018 | 0.0847 | -0.0171 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **5845**
- Benchmark-adjusted coverage: **41.52%**
- Benchmark-adjusted success rate: **49.36%**
- Benchmark rows available: **84**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20260916.csv`
- Latest market index date: **2026-09-16**
- Latest price signal date: **2026-09-16**
- Latest candidate signal date: **2026-09-16**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **9**
- Eligible groups: **11**
- Groups close to activation: **0**
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