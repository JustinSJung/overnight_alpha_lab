# Price Candidate Learned Rules Report - 2026-11-12

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261112.csv`
- Baseline evaluated count: **22434**
- Baseline success rate: **48.86%**
- Total rule rows: **45**
- Boost rules: **1**
- Penalize rules: **15**
- Watch rules: **2**
- Suspicious rules: **1**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| attention_noise_penalty | low | 86 | 47 | 39 | 54.65 | 48.86 | 5.79 | low | boost | False |  | 38 |
| final_price_signal_score_v2 | score_40_50 | 313 | 143 | 170 | 45.69 | 48.86 | -3.17 | high | penalize | False |  | 9 |
| overextension_penalty | low | 410 | 187 | 223 | 45.61 | 48.86 | -3.25 | high | penalize | False |  | 69 |
| final_price_signal_score_v2 | score_lt_20 | 643 | 293 | 350 | 45.57 | 48.86 | -3.29 | high | penalize | False |  | 71 |
| candidate_rank | rank_11_20 | 498 | 222 | 276 | 44.58 | 48.86 | -4.28 | high | penalize | False |  | 62 |
| volume_confirmation_score | moderate | 1825 | 812 | 1013 | 44.49 | 48.86 | -4.37 | high | penalize | False |  | 71 |
| selected_pick | selected | 1130 | 498 | 632 | 44.07 | 48.86 | -4.79 | high | penalize | False |  | 72 |
| candidate_rank | top_10 | 632 | 276 | 356 | 43.67 | 48.86 | -5.19 | high | penalize | False |  | 72 |
| volume_confirmation_score | high | 820 | 355 | 465 | 43.29 | 48.86 | -5.57 | high | penalize | False |  | 67 |
| final_price_signal_score_v2 | score_50_plus | 2271 | 981 | 1290 | 43.2 | 48.86 | -5.66 | high | penalize | False |  | 71 |
| candidate_rank | rank_21_50 | 750 | 323 | 427 | 43.07 | 48.86 | -5.79 | high | penalize | False |  | 51 |
| news_risk_penalty | high | 321 | 137 | 184 | 42.68 | 48.86 | -6.18 | high | penalize | False |  | 58 |
| volume_confirmation_score | none | 3073 | 1240 | 1833 | 40.35 | 48.86 | -8.51 | high | penalize | False |  | 71 |
| candidate_rank | rank_51_100 | 617 | 240 | 377 | 38.9 | 48.86 | -9.96 | high | penalize | False |  | 30 |
| liquidity_score | none | 612 | 36 | 576 | 5.88 | 48.86 | -42.98 | high | penalize | False |  | 71 |
| news_risk_penalty | medium | 187 | 82 | 105 | 43.85 | 48.86 | -5.01 | medium | penalize | False |  | 63 |
| volume_confirmation_score | negative | 16310 | 8356 | 7954 | 51.23 | 48.86 | 2.37 | high | neutral | False |  | 71 |
| overextension_penalty | high | 1197 | 611 | 586 | 51.04 | 48.86 | 2.18 | high | neutral | False |  | 71 |
| liquidity_score | basic | 17796 | 9060 | 8736 | 50.91 | 48.86 | 2.05 | high | neutral | False |  | 71 |
| candidate_rank | missing | 338 | 172 | 166 | 50.89 | 48.86 | 2.03 | high | neutral | False |  | 6 |
| final_price_signal_score_v2 | score_30_40 | 12754 | 6443 | 6311 | 50.52 | 48.86 | 1.66 | high | neutral | False |  | 71 |
| reversal_risk_penalty | high | 973 | 490 | 483 | 50.36 | 48.86 | 1.5 | high | neutral | False |  | 71 |
| candidate_rank | rank_101_plus | 19599 | 9729 | 9870 | 49.64 | 48.86 | 0.78 | high | neutral | False |  | 71 |
| selected_pick | broad_pool | 21304 | 10464 | 10840 | 49.12 | 48.86 | 0.26 | high | neutral | False |  | 78 |
| reversal_risk_penalty | none | 16962 | 8331 | 8631 | 49.12 | 48.86 | 0.26 | high | neutral | False |  | 71 |
| score_version | legacy_or_unknown | 406 | 199 | 207 | 49.01 | 48.86 | 0.15 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 406 | 199 | 207 | 49.01 | 48.86 | 0.15 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 406 | 199 | 207 | 49.01 | 48.86 | 0.15 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 406 | 199 | 207 | 49.01 | 48.86 | 0.15 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 406 | 199 | 207 | 49.01 | 48.86 | 0.15 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 406 | 199 | 207 | 49.01 | 48.86 | 0.15 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 406 | 199 | 207 | 49.01 | 48.86 | 0.15 | high | neutral | False |  | 7 |
| liquidity_score | missing | 406 | 199 | 207 | 49.01 | 48.86 | 0.15 | high | neutral | False |  | 7 |
| news_risk_penalty | none | 21500 | 10533 | 10967 | 48.99 | 48.86 | 0.13 | high | neutral | False |  | 71 |
| attention_noise_penalty | none | 21039 | 10294 | 10745 | 48.93 | 48.86 | 0.07 | high | neutral | False |  | 71 |
| score_version | v2_conservative_ranker | 22028 | 10763 | 11265 | 48.86 | 48.86 | 0.0 | high | neutral | False |  | 71 |
| overextension_penalty | none | 20121 | 9823 | 10298 | 48.82 | 48.86 | -0.04 | high | neutral | False |  | 71 |
| reversal_risk_penalty | medium | 2086 | 1011 | 1075 | 48.47 | 48.86 | -0.39 | high | neutral | False |  | 71 |
| final_price_signal_score_v2 | score_20_30 | 6047 | 2903 | 3144 | 48.01 | 48.86 | -0.85 | high | neutral | False |  | 71 |
| overextension_penalty | medium | 300 | 142 | 158 | 47.33 | 48.86 | -1.53 | high | neutral | False |  | 65 |
| reversal_risk_penalty | low | 2007 | 931 | 1076 | 46.39 | 48.86 | -2.47 | high | neutral | False |  | 71 |
| attention_noise_penalty | high | 873 | 404 | 469 | 46.28 | 48.86 | -2.58 | high | neutral | False |  | 59 |
| liquidity_score | confirmed | 3620 | 1667 | 1953 | 46.05 | 48.86 | -2.81 | high | neutral | False |  | 71 |
| attention_noise_penalty | medium | 30 | 18 | 12 | 60.0 | 48.86 | 11.14 | insufficient | watch | True | large_lift_with_under_100_cases | 19 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 48.86 | 6.14 | insufficient | watch | False |  | 10 |