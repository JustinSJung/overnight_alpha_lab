# Price Candidate Learned Rules Report - 2026-09-03

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260903.csv`
- Baseline evaluated count: **4000**
- Baseline success rate: **44.75%**
- Total rule rows: **45**
- Boost rules: **12**
- Penalize rules: **6**
- Watch rules: **4**
- Suspicious rules: **4**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 437 | 239 | 198 | 54.69 | 44.75 | 9.94 | high | boost | True | boost_on_semantically_risky_bucket | 30 |
| overextension_penalty | high | 448 | 233 | 215 | 52.01 | 44.75 | 7.26 | high | boost | True | boost_on_semantically_risky_bucket | 30 |
| candidate_rank | missing | 332 | 169 | 163 | 50.9 | 44.75 | 6.15 | high | boost | False |  | 6 |
| score_version | legacy_or_unknown | 405 | 200 | 205 | 49.38 | 44.75 | 4.63 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 405 | 200 | 205 | 49.38 | 44.75 | 4.63 | high | boost | False |  | 7 |
| overextension_penalty | missing | 405 | 200 | 205 | 49.38 | 44.75 | 4.63 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 405 | 200 | 205 | 49.38 | 44.75 | 4.63 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 405 | 200 | 205 | 49.38 | 44.75 | 4.63 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 405 | 200 | 205 | 49.38 | 44.75 | 4.63 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 405 | 200 | 205 | 49.38 | 44.75 | 4.63 | high | boost | False |  | 7 |
| liquidity_score | missing | 405 | 200 | 205 | 49.38 | 44.75 | 4.63 | high | boost | False |  | 7 |
| reversal_risk_penalty | medium | 648 | 312 | 336 | 48.15 | 44.75 | 3.4 | high | boost | False |  | 30 |
| reversal_risk_penalty | none | 1936 | 804 | 1132 | 41.53 | 44.75 | -3.22 | high | penalize | False |  | 30 |
| reversal_risk_penalty | low | 574 | 235 | 339 | 40.94 | 44.75 | -3.81 | high | penalize | False |  | 30 |
| volume_confirmation_score | none | 789 | 298 | 491 | 37.77 | 44.75 | -6.98 | high | penalize | False |  | 30 |
| candidate_rank | rank_51_100 | 366 | 133 | 233 | 36.34 | 44.75 | -8.41 | high | penalize | False |  | 16 |
| candidate_rank | rank_21_50 | 228 | 92 | 136 | 40.35 | 44.75 | -4.4 | medium | penalize | False |  | 18 |
| liquidity_score | none | 180 | 8 | 172 | 4.44 | 44.75 | -40.31 | medium | penalize | False |  | 30 |
| volume_confirmation_score | negative | 2113 | 992 | 1121 | 46.95 | 44.75 | 2.2 | high | neutral | False |  | 30 |
| liquidity_score | confirmed | 971 | 454 | 517 | 46.76 | 44.75 | 2.01 | high | neutral | False |  | 30 |
| liquidity_score | basic | 2444 | 1128 | 1316 | 46.15 | 44.75 | 1.4 | high | neutral | False |  | 30 |
| final_price_signal_score_v2 | score_30_40 | 1789 | 817 | 972 | 45.67 | 44.75 | 0.92 | high | neutral | False |  | 30 |
| candidate_rank | rank_101_plus | 2636 | 1198 | 1438 | 45.45 | 44.75 | 0.7 | high | neutral | False |  | 30 |
| selected_pick | selected | 438 | 198 | 240 | 45.21 | 44.75 | 0.46 | high | neutral | False |  | 31 |
| selected_pick | broad_pool | 3562 | 1592 | 1970 | 44.69 | 44.75 | -0.06 | high | neutral | False |  | 37 |
| score_version | v2_conservative_ranker | 3595 | 1590 | 2005 | 44.23 | 44.75 | -0.52 | high | neutral | False |  | 30 |
| news_risk_penalty | none | 3358 | 1482 | 1876 | 44.13 | 44.75 | -0.62 | high | neutral | False |  | 30 |
| attention_noise_penalty | none | 3386 | 1493 | 1893 | 44.09 | 44.75 | -0.66 | high | neutral | False |  | 30 |
| final_price_signal_score_v2 | score_20_30 | 886 | 385 | 501 | 43.45 | 44.75 | -1.3 | high | neutral | False |  | 30 |
| overextension_penalty | none | 2901 | 1252 | 1649 | 43.16 | 44.75 | -1.59 | high | neutral | False |  | 30 |
| final_price_signal_score_v2 | score_50_plus | 669 | 281 | 388 | 42.0 | 44.75 | -2.75 | high | neutral | False |  | 30 |
| volume_confirmation_score | moderate | 471 | 197 | 274 | 41.83 | 44.75 | -2.92 | high | neutral | False |  | 30 |
| news_risk_penalty | medium | 89 | 42 | 47 | 47.19 | 44.75 | 2.44 | low | neutral | False |  | 27 |
| candidate_rank | top_10 | 260 | 121 | 139 | 46.54 | 44.75 | 1.79 | medium | neutral | False |  | 31 |
| volume_confirmation_score | high | 222 | 103 | 119 | 46.4 | 44.75 | 1.65 | medium | neutral | False |  | 29 |
| attention_noise_penalty | high | 195 | 88 | 107 | 45.13 | 44.75 | 0.38 | medium | neutral | False |  | 22 |
| overextension_penalty | medium | 108 | 47 | 61 | 43.52 | 44.75 | -1.23 | medium | neutral | False |  | 27 |
| candidate_rank | rank_11_20 | 178 | 77 | 101 | 43.26 | 44.75 | -1.49 | medium | neutral | False |  | 23 |
| news_risk_penalty | high | 128 | 55 | 73 | 42.97 | 44.75 | -1.78 | medium | neutral | False |  | 19 |
| final_price_signal_score_v2 | score_lt_20 | 231 | 98 | 133 | 42.42 | 44.75 | -2.33 | medium | neutral | False |  | 30 |
| overextension_penalty | low | 138 | 58 | 80 | 42.03 | 44.75 | -2.72 | medium | neutral | False |  | 28 |
| attention_noise_penalty | low | 8 | 6 | 2 | 75.0 | 44.75 | 30.25 | insufficient | watch | True | large_lift_with_under_100_cases | 7 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 44.75 | 10.25 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| attention_noise_penalty | medium | 6 | 3 | 3 | 50.0 | 44.75 | 5.25 | insufficient | watch | False |  | 5 |
| final_price_signal_score_v2 | score_40_50 | 20 | 9 | 11 | 45.0 | 44.75 | 0.25 | insufficient | watch | False |  | 4 |