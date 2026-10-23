# Evaluation Integrity Audit - 2026-10-23

This report audits duplicate inflation, score-version drift, benchmark coverage, and learned-rule activation. It is not investment advice.

## Duplicate and Leakage Audit

- Total evaluation rows: **804072**
- Unique evaluation keys: **32001**
- Duplicate rows by candidate key: **772071**
- Duplicate rate: **96.02%**
- Exact same-day duplicate rows: **294073**
- Same stock_code + signal_date repeated keys: **31051**
- Same candidate re-evaluated across multiple files: **31052**
- Cumulative evaluated cases may be inflated: **True**

Recommended safe deduplication key: `candidate_id` when available; otherwise `stock_code + signal_date + prediction_date + score_version`.

### Duplicate Examples

| stock_code | signal_date | prediction_date | evaluation_date | score_version | candidate_id | source_file | prediction_result |
|---|---|---|---|---|---|---|---|
| 010960 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 189330 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260707.csv |  |
| 010960 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 189330 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 189330 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 006730 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010960 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 069460 |  |  |  |  |  | data/predictions/price_candidate_evaluation_20260709.csv |  |
| 010960 |  |  | 2026-07-20 |  | 0911149d5a6a91d7 | data/predictions/price_candidate_evaluation_20260720.csv | success |
| 006730 |  |  | 2026-07-20 |  | dde001888090afdc | data/predictions/price_candidate_evaluation_20260720.csv | failure |
| 189330 |  |  | 2026-07-20 |  | 36aaea07ab7c2d86 | data/predictions/price_candidate_evaluation_20260720.csv | success |

## v1 vs v2 Performance

| score_version | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| v1/unknown | 404 | 200 | 204 | 49.5 | -0.0143 | 0.0088 | 0.001 |
| v2_conservative_ranker | 14605 | 7246 | 7359 | 49.61 | -0.0013 | -0.0021 | -0.0009 |

## v2 Directional Breakdown (Buy vs Avoid)

Diagnostic only. Splits v2 performance above by expects_positive() direction; does not change scoring or candidate selection.

| direction | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| buy | 1838 | 776 | 1062 | 42.22 | -0.0019 | -0.0107 | -0.0197 |
| avoid | 12767 | 6470 | 6297 | 50.68 | -0.0012 | -0.0008 | 0.0022 |

## v2 Rank Bucket Performance

| bucket | evaluated_count | success_count | failure_count | success_rate | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|
| Top 10 | 520 | 225 | 295 | 43.27 | 0.001 | -0.0039 | -0.0012 |
| Top 20 | 942 | 416 | 526 | 44.16 | 0.0001 | -0.0042 | -0.0034 |
| Top 50 | 1507 | 654 | 853 | 43.4 | -0.0006 | -0.0058 | -0.0091 |
| Top 100 | 2026 | 847 | 1179 | 41.81 | 0.0008 | -0.0047 | -0.0111 |

Ranking status: **Ranking inverted**
Score decile diagnosis: **Ranking flat/random**

## v2 Score Deciles

| decile | evaluated_count | success_count | failure_count | success_rate | avg_final_price_signal_score_v2 | avg_close_t1_return | avg_close_t3_return | avg_close_t5_return |
|---|---|---|---|---|---|---|---|---|
| D1 | 1461 | 668 | 793 | 45.72 | 21.52 | 0.0001 | 0.0098 | 0.0274 |
| D2 | 1460 | 708 | 752 | 48.49 | 27.2 | 0.0004 | -0.0026 | -0.0014 |
| D3 | 1461 | 696 | 765 | 47.64 | 29.73 | 0.0006 | 0.0024 | 0.0046 |
| D4 | 1460 | 740 | 720 | 50.68 | 31.86 | -0.001 | -0.0005 | -0.0007 |
| D5 | 1461 | 757 | 704 | 51.81 | 33.75 | -0.0028 | -0.0028 | -0.0045 |
| D6 | 1460 | 754 | 706 | 51.64 | 35.48 | -0.0038 | -0.0038 | -0.0004 |
| D7 | 1460 | 779 | 681 | 53.36 | 37.09 | -0.0002 | -0.0013 | 0.0013 |
| D8 | 1461 | 788 | 673 | 53.94 | 38.51 | -0.003 | -0.0044 | -0.0047 |
| D9 | 1460 | 725 | 735 | 49.66 | 45.67 | -0.0018 | -0.0085 | -0.0097 |
| D10 | 1461 | 631 | 830 | 43.19 | 66.62 | -0.0013 | -0.0092 | -0.0189 |

## v2 Component Failure Associations

| component | success_avg | failure_avg | failure_minus_success |
|---|---|---|---|
| base_momentum_score | 43.1104 | 43.6824 | 0.572 |
| volume_confirmation_score | -1.4019 | -1.2098 | 0.1921 |
| liquidity_score | 2.1202 | 2.0063 | -0.114 |
| overextension_penalty | 1.1979 | 1.1017 | -0.0962 |
| reversal_risk_penalty | 0.8153 | 0.7939 | -0.0213 |
| news_risk_penalty | 0.1168 | 0.1503 | 0.0335 |
| attention_noise_penalty | 0.2492 | 0.2599 | 0.0107 |
| market_regime_penalty | 0.0571 | 0.0544 | -0.0028 |

## Benchmark-Adjusted Evaluation Audit

- Benchmark-adjusted evaluated cases: **12247**
- Benchmark-adjusted coverage: **38.27%**
- Benchmark-adjusted success rate: **47.33%**
- Benchmark rows available: **82**
- Benchmark status: **Partial**
- Latest market index file: `data/raw/market_index_20261023.csv`
- Latest market index date: **2026-10-23**
- Latest price signal date: **2026-10-23**
- Latest candidate signal date: **2026-10-23**
- Finding: Benchmark-adjusted evaluation is partially available.

## Learning Loop Audit

- Active learned rules: **9**
- Eligible groups: **12**
- Groups close to activation: **4**
- Criteria: DART/error-note event_type groups, minimum 5 evaluated rows, neutral 45%-55% success gives zero adjustment.
- Finding: Some learned event rules are active.

## Dashboard Status Flags

- Duplicate status: **Possible duplicates**
- Benchmark status: **Partial**
- Ranking status: **Ranking inverted**

## Next Diagnostic Recommendations

- Deduplicate cumulative dashboard learning metrics by the recommended candidate-level key before interpreting reliability.
- Refresh or extend market index data past the latest candidate dates before expecting benchmark-adjusted coverage.
- Add price-signal component groups as a separate learning loop rather than relying on DART event_type learned rules.
- Do not change v2 score weights until duplicate inflation and benchmark coverage are handled.