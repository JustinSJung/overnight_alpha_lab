# Price Candidate Learned Rules Report - 2026-08-03

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260803.csv`
- Baseline evaluated count: **1441**
- Baseline success rate: **45.18%**
- Total rule rows: **43**
- Boost rules: **14**
- Penalize rules: **9**
- Watch rules: **9**
- Suspicious rules: **7**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| score_version | legacy_or_unknown | 368 | 192 | 176 | 52.17 | 45.18 | 6.99 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 368 | 192 | 176 | 52.17 | 45.18 | 6.99 | high | boost | False |  | 7 |
| overextension_penalty | missing | 368 | 192 | 176 | 52.17 | 45.18 | 6.99 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 368 | 192 | 176 | 52.17 | 45.18 | 6.99 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 368 | 192 | 176 | 52.17 | 45.18 | 6.99 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 368 | 192 | 176 | 52.17 | 45.18 | 6.99 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 368 | 192 | 176 | 52.17 | 45.18 | 6.99 | high | boost | False |  | 7 |
| liquidity_score | missing | 368 | 192 | 176 | 52.17 | 45.18 | 6.99 | high | boost | False |  | 7 |
| volume_confirmation_score | high | 76 | 46 | 30 | 60.53 | 45.18 | 15.35 | low | boost | True | large_lift_with_under_100_cases | 8 |
| candidate_rank | top_10 | 66 | 34 | 32 | 51.52 | 45.18 | 6.34 | low | boost | False |  | 10 |
| final_price_signal_score_v2 | score_50_plus | 66 | 33 | 33 | 50.0 | 45.18 | 4.82 | low | boost | False |  | 9 |
| selected_pick | selected | 71 | 35 | 36 | 49.3 | 45.18 | 4.12 | low | boost | False |  | 10 |
| candidate_rank | missing | 294 | 161 | 133 | 54.76 | 45.18 | 9.58 | medium | boost | False |  | 6 |
| reversal_risk_penalty | high | 149 | 80 | 69 | 53.69 | 45.18 | 8.51 | medium | boost | True | boost_on_semantically_risky_bucket | 9 |
| news_risk_penalty | none | 1021 | 430 | 591 | 42.12 | 45.18 | -3.06 | high | penalize | False |  | 9 |
| final_price_signal_score_v2 | score_20_30 | 404 | 167 | 237 | 41.34 | 45.18 | -3.84 | high | penalize | False |  | 9 |
| reversal_risk_penalty | none | 558 | 217 | 341 | 38.89 | 45.18 | -6.29 | high | penalize | False |  | 9 |
| candidate_rank | rank_51_100 | 367 | 138 | 229 | 37.6 | 45.18 | -7.58 | high | penalize | False |  | 9 |
| liquidity_score | none | 53 | 3 | 50 | 5.66 | 45.18 | -39.52 | low | penalize | True | large_lift_with_under_100_cases | 9 |
| final_price_signal_score_v2 | score_lt_20 | 125 | 51 | 74 | 40.8 | 45.18 | -4.38 | medium | penalize | False |  | 9 |
| reversal_risk_penalty | low | 163 | 66 | 97 | 40.49 | 45.18 | -4.69 | medium | penalize | False |  | 9 |
| volume_confirmation_score | moderate | 169 | 65 | 104 | 38.46 | 45.18 | -6.72 | medium | penalize | False |  | 9 |
| volume_confirmation_score | none | 254 | 92 | 162 | 36.22 | 45.18 | -8.96 | medium | penalize | False |  | 9 |
| liquidity_score | confirmed | 330 | 156 | 174 | 47.27 | 45.18 | 2.09 | high | neutral | False |  | 9 |
| selected_pick | broad_pool | 1370 | 616 | 754 | 44.96 | 45.18 | -0.22 | high | neutral | False |  | 16 |
| volume_confirmation_score | negative | 574 | 256 | 318 | 44.6 | 45.18 | -0.58 | high | neutral | False |  | 9 |
| candidate_rank | rank_101_plus | 675 | 298 | 377 | 44.15 | 45.18 | -1.03 | high | neutral | False |  | 9 |
| final_price_signal_score_v2 | score_30_40 | 478 | 208 | 270 | 43.51 | 45.18 | -1.67 | high | neutral | False |  | 9 |
| liquidity_score | basic | 690 | 300 | 390 | 43.48 | 45.18 | -1.7 | high | neutral | False |  | 9 |
| attention_noise_penalty | none | 1023 | 440 | 583 | 43.01 | 45.18 | -2.17 | high | neutral | False |  | 9 |
| score_version | v2_conservative_ranker | 1073 | 459 | 614 | 42.78 | 45.18 | -2.4 | high | neutral | False |  | 9 |
| overextension_penalty | none | 903 | 384 | 519 | 42.52 | 45.18 | -2.66 | high | neutral | False |  | 9 |
| reversal_risk_penalty | medium | 203 | 96 | 107 | 47.29 | 45.18 | 2.11 | medium | neutral | False |  | 9 |
| overextension_penalty | high | 107 | 49 | 58 | 45.79 | 45.18 | 0.61 | medium | neutral | False |  | 9 |
| news_risk_penalty | high | 2 | 2 | 0 | 100.0 | 45.18 | 54.82 | insufficient | watch | True | large_lift_with_under_100_cases; only_one_or_two_signal_dates | 2 |
| news_risk_penalty | low | 16 | 11 | 5 | 68.75 | 45.18 | 23.57 | insufficient | watch | True | large_lift_with_under_100_cases | 7 |
| candidate_rank | rank_21_50 | 34 | 19 | 15 | 55.88 | 45.18 | 10.7 | insufficient | watch | True | large_lift_with_under_100_cases; only_one_or_two_signal_dates | 2 |
| attention_noise_penalty | low | 4 | 2 | 2 | 50.0 | 45.18 | 4.82 | insufficient | watch | False |  | 3 |
| news_risk_penalty | medium | 34 | 16 | 18 | 47.06 | 45.18 | 1.88 | insufficient | watch | False |  | 9 |
| overextension_penalty | low | 40 | 17 | 23 | 42.5 | 45.18 | -2.68 | insufficient | watch | False |  | 7 |
| overextension_penalty | medium | 23 | 9 | 14 | 39.13 | 45.18 | -6.05 | insufficient | watch | False |  | 6 |
| attention_noise_penalty | high | 46 | 17 | 29 | 36.96 | 45.18 | -8.22 | insufficient | watch | False |  | 8 |
| candidate_rank | rank_11_20 | 5 | 1 | 4 | 20.0 | 45.18 | -25.18 | insufficient | watch | True | large_lift_with_under_100_cases; only_one_or_two_signal_dates | 2 |