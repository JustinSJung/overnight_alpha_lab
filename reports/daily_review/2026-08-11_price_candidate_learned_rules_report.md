# Price Candidate Learned Rules Report - 2026-08-11

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260811.csv`
- Baseline evaluated count: **1976**
- Baseline success rate: **42.76%**
- Total rule rows: **44**
- Boost rules: **20**
- Penalize rules: **11**
- Watch rules: **5**
- Suspicious rules: **8**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| score_version | legacy_or_unknown | 370 | 190 | 180 | 51.35 | 42.76 | 8.59 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 370 | 190 | 180 | 51.35 | 42.76 | 8.59 | high | boost | False |  | 7 |
| overextension_penalty | missing | 370 | 190 | 180 | 51.35 | 42.76 | 8.59 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 370 | 190 | 180 | 51.35 | 42.76 | 8.59 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 370 | 190 | 180 | 51.35 | 42.76 | 8.59 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 370 | 190 | 180 | 51.35 | 42.76 | 8.59 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 370 | 190 | 180 | 51.35 | 42.76 | 8.59 | high | boost | False |  | 7 |
| liquidity_score | missing | 370 | 190 | 180 | 51.35 | 42.76 | 8.59 | high | boost | False |  | 7 |
| liquidity_score | confirmed | 479 | 232 | 247 | 48.43 | 42.76 | 5.67 | high | boost | False |  | 14 |
| candidate_rank | rank_21_50 | 59 | 32 | 27 | 54.24 | 42.76 | 11.48 | low | boost | True | large_lift_with_under_100_cases | 5 |
| news_risk_penalty | medium | 56 | 29 | 27 | 51.79 | 42.76 | 9.03 | low | boost | False |  | 14 |
| overextension_penalty | medium | 52 | 25 | 27 | 48.08 | 42.76 | 5.32 | low | boost | False |  | 11 |
| overextension_penalty | low | 67 | 31 | 36 | 46.27 | 42.76 | 3.51 | low | boost | False |  | 12 |
| candidate_rank | top_10 | 124 | 74 | 50 | 59.68 | 42.76 | 16.92 | medium | boost | False |  | 15 |
| selected_pick | selected | 167 | 98 | 69 | 58.68 | 42.76 | 15.92 | medium | boost | False |  | 15 |
| volume_confirmation_score | high | 108 | 63 | 45 | 58.33 | 42.76 | 15.57 | medium | boost | False |  | 13 |
| final_price_signal_score_v2 | score_50_plus | 187 | 109 | 78 | 58.29 | 42.76 | 15.53 | medium | boost | False |  | 14 |
| candidate_rank | missing | 296 | 159 | 137 | 53.72 | 42.76 | 10.96 | medium | boost | False |  | 6 |
| reversal_risk_penalty | high | 242 | 126 | 116 | 52.07 | 42.76 | 9.31 | medium | boost | True | boost_on_semantically_risky_bucket | 14 |
| overextension_penalty | high | 209 | 105 | 104 | 50.24 | 42.76 | 7.48 | medium | boost | True | boost_on_semantically_risky_bucket | 14 |
| news_risk_penalty | none | 1507 | 598 | 909 | 39.68 | 42.76 | -3.08 | high | penalize | False |  | 14 |
| final_price_signal_score_v2 | score_30_40 | 736 | 290 | 446 | 39.4 | 42.76 | -3.36 | high | penalize | False |  | 14 |
| candidate_rank | rank_101_plus | 1076 | 416 | 660 | 38.66 | 42.76 | -4.1 | high | penalize | False |  | 14 |
| overextension_penalty | none | 1278 | 494 | 784 | 38.65 | 42.76 | -4.11 | high | penalize | False |  | 14 |
| reversal_risk_penalty | none | 808 | 310 | 498 | 38.37 | 42.76 | -4.39 | high | penalize | False |  | 14 |
| final_price_signal_score_v2 | score_20_30 | 530 | 199 | 331 | 37.55 | 42.76 | -5.21 | high | penalize | False |  | 14 |
| candidate_rank | rank_51_100 | 378 | 140 | 238 | 37.04 | 42.76 | -5.72 | high | penalize | False |  | 10 |
| volume_confirmation_score | none | 383 | 137 | 246 | 35.77 | 42.76 | -6.99 | high | penalize | False |  | 14 |
| liquidity_score | none | 84 | 3 | 81 | 3.57 | 42.76 | -39.19 | low | penalize | True | large_lift_with_under_100_cases | 14 |
| final_price_signal_score_v2 | score_lt_20 | 153 | 57 | 96 | 37.25 | 42.76 | -5.51 | medium | penalize | False |  | 14 |
| reversal_risk_penalty | low | 238 | 87 | 151 | 36.55 | 42.76 | -6.21 | medium | penalize | False |  | 14 |
| reversal_risk_penalty | medium | 318 | 132 | 186 | 41.51 | 42.76 | -1.25 | high | neutral | False |  | 14 |
| selected_pick | broad_pool | 1809 | 747 | 1062 | 41.29 | 42.76 | -1.47 | high | neutral | False |  | 21 |
| score_version | v2_conservative_ranker | 1606 | 655 | 951 | 40.78 | 42.76 | -1.98 | high | neutral | False |  | 14 |
| attention_noise_penalty | none | 1537 | 625 | 912 | 40.66 | 42.76 | -2.1 | high | neutral | False |  | 14 |
| volume_confirmation_score | negative | 874 | 354 | 520 | 40.5 | 42.76 | -2.26 | high | neutral | False |  | 14 |
| liquidity_score | basic | 1043 | 420 | 623 | 40.27 | 42.76 | -2.49 | high | neutral | False |  | 14 |
| attention_noise_penalty | high | 61 | 27 | 34 | 44.26 | 42.76 | 1.5 | low | neutral | False |  | 11 |
| volume_confirmation_score | moderate | 241 | 101 | 140 | 41.91 | 42.76 | -0.85 | medium | neutral | False |  | 14 |
| news_risk_penalty | high | 21 | 15 | 6 | 71.43 | 42.76 | 28.67 | insufficient | watch | True | large_lift_with_under_100_cases | 4 |
| news_risk_penalty | low | 22 | 13 | 9 | 59.09 | 42.76 | 16.33 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| candidate_rank | rank_11_20 | 43 | 24 | 19 | 55.81 | 42.76 | 13.05 | insufficient | watch | True | large_lift_with_under_100_cases | 6 |
| attention_noise_penalty | low | 6 | 3 | 3 | 50.0 | 42.76 | 7.24 | insufficient | watch | False |  | 4 |
| attention_noise_penalty | medium | 2 | 0 | 2 | 0.0 | 42.76 | -42.76 | insufficient | watch | True | large_lift_with_under_100_cases; only_one_or_two_signal_dates | 2 |