# Price Candidate Learned Rules Report - 2026-08-24

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260824.csv`
- Baseline evaluated count: **3145**
- Baseline success rate: **42.86%**
- Total rule rows: **44**
- Boost rules: **15**
- Penalize rules: **7**
- Watch rules: **3**
- Suspicious rules: **4**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 405 | 220 | 185 | 54.32 | 42.86 | 11.46 | high | boost | True | boost_on_semantically_risky_bucket | 23 |
| overextension_penalty | high | 346 | 178 | 168 | 51.45 | 42.86 | 8.59 | high | boost | True | boost_on_semantically_risky_bucket | 23 |
| score_version | legacy_or_unknown | 358 | 180 | 178 | 50.28 | 42.86 | 7.42 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 358 | 180 | 178 | 50.28 | 42.86 | 7.42 | high | boost | False |  | 7 |
| overextension_penalty | missing | 358 | 180 | 178 | 50.28 | 42.86 | 7.42 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 358 | 180 | 178 | 50.28 | 42.86 | 7.42 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 358 | 180 | 178 | 50.28 | 42.86 | 7.42 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 358 | 180 | 178 | 50.28 | 42.86 | 7.42 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 358 | 180 | 178 | 50.28 | 42.86 | 7.42 | high | boost | False |  | 7 |
| liquidity_score | missing | 358 | 180 | 178 | 50.28 | 42.86 | 7.42 | high | boost | False |  | 7 |
| selected_pick | selected | 365 | 170 | 195 | 46.58 | 42.86 | 3.72 | high | boost | False |  | 24 |
| liquidity_score | confirmed | 890 | 409 | 481 | 45.96 | 42.86 | 3.1 | high | boost | False |  | 23 |
| news_risk_penalty | medium | 86 | 40 | 46 | 46.51 | 42.86 | 3.65 | low | boost | False |  | 22 |
| candidate_rank | missing | 290 | 154 | 136 | 53.1 | 42.86 | 10.24 | medium | boost | False |  | 6 |
| candidate_rank | top_10 | 224 | 106 | 118 | 47.32 | 42.86 | 4.46 | medium | boost | False |  | 24 |
| final_price_signal_score_v2 | score_20_30 | 718 | 284 | 434 | 39.55 | 42.86 | -3.31 | high | penalize | False |  | 23 |
| reversal_risk_penalty | none | 1435 | 551 | 884 | 38.4 | 42.86 | -4.46 | high | penalize | False |  | 23 |
| reversal_risk_penalty | low | 429 | 161 | 268 | 37.53 | 42.86 | -5.33 | high | penalize | False |  | 23 |
| volume_confirmation_score | none | 707 | 262 | 445 | 37.06 | 42.86 | -5.8 | high | penalize | False |  | 23 |
| candidate_rank | rank_51_100 | 391 | 137 | 254 | 35.04 | 42.86 | -7.82 | high | penalize | False |  | 14 |
| candidate_rank | rank_21_50 | 230 | 83 | 147 | 36.09 | 42.86 | -6.77 | medium | penalize | False |  | 12 |
| liquidity_score | none | 154 | 6 | 148 | 3.9 | 42.86 | -38.96 | medium | penalize | False |  | 23 |
| reversal_risk_penalty | medium | 518 | 236 | 282 | 45.56 | 42.86 | 2.7 | high | neutral | False |  | 23 |
| volume_confirmation_score | negative | 1432 | 629 | 803 | 43.92 | 42.86 | 1.06 | high | neutral | False |  | 23 |
| final_price_signal_score_v2 | score_30_40 | 1281 | 558 | 723 | 43.56 | 42.86 | 0.7 | high | neutral | False |  | 23 |
| liquidity_score | basic | 1743 | 753 | 990 | 43.2 | 42.86 | 0.34 | high | neutral | False |  | 23 |
| candidate_rank | rank_101_plus | 1869 | 804 | 1065 | 43.02 | 42.86 | 0.16 | high | neutral | False |  | 23 |
| selected_pick | broad_pool | 2780 | 1178 | 1602 | 42.37 | 42.86 | -0.49 | high | neutral | False |  | 30 |
| score_version | v2_conservative_ranker | 2787 | 1168 | 1619 | 41.91 | 42.86 | -0.95 | high | neutral | False |  | 23 |
| attention_noise_penalty | none | 2676 | 1118 | 1558 | 41.78 | 42.86 | -1.08 | high | neutral | False |  | 23 |
| news_risk_penalty | none | 2579 | 1072 | 1507 | 41.57 | 42.86 | -1.29 | high | neutral | False |  | 23 |
| volume_confirmation_score | moderate | 439 | 182 | 257 | 41.46 | 42.86 | -1.4 | high | neutral | False |  | 23 |
| final_price_signal_score_v2 | score_50_plus | 586 | 240 | 346 | 40.96 | 42.86 | -1.9 | high | neutral | False |  | 23 |
| overextension_penalty | none | 2224 | 900 | 1324 | 40.47 | 42.86 | -2.39 | high | neutral | False |  | 23 |
| overextension_penalty | medium | 96 | 39 | 57 | 40.62 | 42.86 | -2.24 | low | neutral | False |  | 20 |
| attention_noise_penalty | high | 101 | 46 | 55 | 45.54 | 42.86 | 2.68 | medium | neutral | False |  | 18 |
| volume_confirmation_score | high | 209 | 95 | 114 | 45.45 | 42.86 | 2.59 | medium | neutral | False |  | 22 |
| candidate_rank | rank_11_20 | 141 | 64 | 77 | 45.39 | 42.86 | 2.53 | medium | neutral | False |  | 15 |
| news_risk_penalty | high | 100 | 43 | 57 | 43.0 | 42.86 | 0.14 | medium | neutral | False |  | 13 |
| final_price_signal_score_v2 | score_lt_20 | 202 | 86 | 116 | 42.57 | 42.86 | -0.29 | medium | neutral | False |  | 23 |
| overextension_penalty | low | 121 | 51 | 70 | 42.15 | 42.86 | -0.71 | medium | neutral | False |  | 21 |
| news_risk_penalty | low | 22 | 13 | 9 | 59.09 | 42.86 | 16.23 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| attention_noise_penalty | low | 6 | 3 | 3 | 50.0 | 42.86 | 7.14 | insufficient | watch | False |  | 4 |
| attention_noise_penalty | medium | 4 | 1 | 3 | 25.0 | 42.86 | -17.86 | insufficient | watch | True | large_lift_with_under_100_cases | 4 |