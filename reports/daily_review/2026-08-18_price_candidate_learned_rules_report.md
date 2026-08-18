# Price Candidate Learned Rules Report - 2026-08-18

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260818.csv`
- Baseline evaluated count: **2613**
- Baseline success rate: **41.41%**
- Total rule rows: **44**
- Boost rules: **17**
- Penalize rules: **9**
- Watch rules: **3**
- Suspicious rules: **4**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 342 | 180 | 162 | 52.63 | 41.41 | 11.22 | high | boost | True | boost_on_semantically_risky_bucket | 19 |
| score_version | legacy_or_unknown | 363 | 184 | 179 | 50.69 | 41.41 | 9.28 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 363 | 184 | 179 | 50.69 | 41.41 | 9.28 | high | boost | False |  | 7 |
| overextension_penalty | missing | 363 | 184 | 179 | 50.69 | 41.41 | 9.28 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 363 | 184 | 179 | 50.69 | 41.41 | 9.28 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 363 | 184 | 179 | 50.69 | 41.41 | 9.28 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 363 | 184 | 179 | 50.69 | 41.41 | 9.28 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 363 | 184 | 179 | 50.69 | 41.41 | 9.28 | high | boost | False |  | 7 |
| liquidity_score | missing | 363 | 184 | 179 | 50.69 | 41.41 | 9.28 | high | boost | False |  | 7 |
| liquidity_score | confirmed | 729 | 330 | 399 | 45.27 | 41.41 | 3.86 | high | boost | False |  | 19 |
| news_risk_penalty | medium | 76 | 37 | 39 | 48.68 | 41.41 | 7.27 | low | boost | False |  | 19 |
| candidate_rank | missing | 289 | 153 | 136 | 52.94 | 41.41 | 11.53 | medium | boost | False |  | 6 |
| overextension_penalty | high | 299 | 153 | 146 | 51.17 | 41.41 | 9.76 | medium | boost | True | boost_on_semantically_risky_bucket | 19 |
| candidate_rank | top_10 | 184 | 87 | 97 | 47.28 | 41.41 | 5.87 | medium | boost | False |  | 20 |
| selected_pick | selected | 287 | 135 | 152 | 47.04 | 41.41 | 5.63 | medium | boost | False |  | 20 |
| candidate_rank | rank_11_20 | 103 | 48 | 55 | 46.6 | 41.41 | 5.19 | medium | boost | False |  | 11 |
| volume_confirmation_score | high | 180 | 82 | 98 | 45.56 | 41.41 | 4.15 | medium | boost | False |  | 18 |
| final_price_signal_score_v2 | score_20_30 | 610 | 232 | 378 | 38.03 | 41.41 | -3.38 | high | penalize | False |  | 19 |
| overextension_penalty | none | 1768 | 671 | 1097 | 37.95 | 41.41 | -3.46 | high | penalize | False |  | 19 |
| reversal_risk_penalty | none | 1178 | 433 | 745 | 36.76 | 41.41 | -4.65 | high | penalize | False |  | 19 |
| candidate_rank | rank_51_100 | 406 | 147 | 259 | 36.21 | 41.41 | -5.2 | high | penalize | False |  | 14 |
| volume_confirmation_score | none | 567 | 199 | 368 | 35.1 | 41.41 | -6.31 | high | penalize | False |  | 19 |
| reversal_risk_penalty | low | 315 | 107 | 208 | 33.97 | 41.41 | -7.44 | high | penalize | False |  | 19 |
| overextension_penalty | medium | 81 | 31 | 50 | 38.27 | 41.41 | -3.14 | low | penalize | False |  | 16 |
| candidate_rank | rank_21_50 | 227 | 83 | 144 | 36.56 | 41.41 | -4.85 | medium | penalize | False |  | 10 |
| liquidity_score | none | 127 | 5 | 122 | 3.94 | 41.41 | -37.47 | medium | penalize | False |  | 19 |
| reversal_risk_penalty | medium | 415 | 178 | 237 | 42.89 | 41.41 | 1.48 | high | neutral | False |  | 19 |
| volume_confirmation_score | moderate | 355 | 146 | 209 | 41.13 | 41.41 | -0.28 | high | neutral | False |  | 19 |
| volume_confirmation_score | negative | 1148 | 471 | 677 | 41.03 | 41.41 | -0.38 | high | neutral | False |  | 19 |
| final_price_signal_score_v2 | score_30_40 | 964 | 394 | 570 | 40.87 | 41.41 | -0.54 | high | neutral | False |  | 19 |
| selected_pick | broad_pool | 2326 | 947 | 1379 | 40.71 | 41.41 | -0.7 | high | neutral | False |  | 26 |
| final_price_signal_score_v2 | score_50_plus | 503 | 204 | 299 | 40.56 | 41.41 | -0.85 | high | neutral | False |  | 19 |
| liquidity_score | basic | 1394 | 563 | 831 | 40.39 | 41.41 | -1.02 | high | neutral | False |  | 19 |
| candidate_rank | rank_101_plus | 1404 | 564 | 840 | 40.17 | 41.41 | -1.24 | high | neutral | False |  | 19 |
| score_version | v2_conservative_ranker | 2250 | 898 | 1352 | 39.91 | 41.41 | -1.5 | high | neutral | False |  | 19 |
| attention_noise_penalty | none | 2171 | 864 | 1307 | 39.8 | 41.41 | -1.61 | high | neutral | False |  | 19 |
| news_risk_penalty | none | 2075 | 816 | 1259 | 39.33 | 41.41 | -2.08 | high | neutral | False |  | 19 |
| attention_noise_penalty | high | 70 | 31 | 39 | 44.29 | 41.41 | 2.88 | low | neutral | False |  | 15 |
| news_risk_penalty | high | 77 | 32 | 45 | 41.56 | 41.41 | 0.15 | low | neutral | False |  | 9 |
| overextension_penalty | low | 102 | 43 | 59 | 42.16 | 41.41 | 0.75 | medium | neutral | False |  | 17 |
| final_price_signal_score_v2 | score_lt_20 | 173 | 68 | 105 | 39.31 | 41.41 | -2.1 | medium | neutral | False |  | 19 |
| news_risk_penalty | low | 22 | 13 | 9 | 59.09 | 41.41 | 17.68 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| attention_noise_penalty | low | 6 | 3 | 3 | 50.0 | 41.41 | 8.59 | insufficient | watch | False |  | 4 |
| attention_noise_penalty | medium | 3 | 0 | 3 | 0.0 | 41.41 | -41.41 | insufficient | watch | True | large_lift_with_under_100_cases | 3 |