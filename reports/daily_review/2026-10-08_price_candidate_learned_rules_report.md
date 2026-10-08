# Price Candidate Learned Rules Report - 2026-10-08

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261008.csv`
- Baseline evaluated count: **9926**
- Baseline success rate: **46.76%**
- Total rule rows: **45**
- Boost rules: **2**
- Penalize rules: **7**
- Watch rules: **3**
- Suspicious rules: **2**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| candidate_rank | missing | 333 | 171 | 162 | 51.35 | 46.76 | 4.59 | high | boost | False |  | 6 |
| reversal_risk_penalty | high | 678 | 339 | 339 | 50.0 | 46.76 | 3.24 | high | boost | True | boost_on_semantically_risky_bucket | 49 |
| volume_confirmation_score | moderate | 752 | 327 | 425 | 43.48 | 46.76 | -3.28 | high | penalize | False |  | 49 |
| reversal_risk_penalty | low | 989 | 425 | 564 | 42.97 | 46.76 | -3.79 | high | penalize | False |  | 49 |
| candidate_rank | rank_51_100 | 548 | 205 | 343 | 37.41 | 46.76 | -9.35 | high | penalize | False |  | 23 |
| volume_confirmation_score | none | 1335 | 487 | 848 | 36.48 | 46.76 | -10.28 | high | penalize | False |  | 49 |
| liquidity_score | none | 373 | 19 | 354 | 5.09 | 46.76 | -41.67 | high | penalize | False |  | 49 |
| news_risk_penalty | medium | 133 | 58 | 75 | 43.61 | 46.76 | -3.15 | medium | penalize | False |  | 44 |
| final_price_signal_score_v2 | score_40_50 | 149 | 57 | 92 | 38.26 | 46.76 | -8.5 | medium | penalize | False |  | 7 |
| score_version | legacy_or_unknown | 401 | 197 | 204 | 49.13 | 46.76 | 2.37 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 401 | 197 | 204 | 49.13 | 46.76 | 2.37 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 401 | 197 | 204 | 49.13 | 46.76 | 2.37 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 401 | 197 | 204 | 49.13 | 46.76 | 2.37 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 401 | 197 | 204 | 49.13 | 46.76 | 2.37 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 401 | 197 | 204 | 49.13 | 46.76 | 2.37 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 401 | 197 | 204 | 49.13 | 46.76 | 2.37 | high | neutral | False |  | 7 |
| liquidity_score | missing | 401 | 197 | 204 | 49.13 | 46.76 | 2.37 | high | neutral | False |  | 7 |
| volume_confirmation_score | negative | 7063 | 3456 | 3607 | 48.93 | 46.76 | 2.17 | high | neutral | False |  | 49 |
| reversal_risk_penalty | medium | 1149 | 562 | 587 | 48.91 | 46.76 | 2.15 | high | neutral | False |  | 49 |
| liquidity_score | basic | 7591 | 3688 | 3903 | 48.58 | 46.76 | 1.82 | high | neutral | False |  | 49 |
| overextension_penalty | high | 846 | 408 | 438 | 48.23 | 46.76 | 1.47 | high | neutral | False |  | 49 |
| final_price_signal_score_v2 | score_30_40 | 5544 | 2659 | 2885 | 47.96 | 46.76 | 1.2 | high | neutral | False |  | 49 |
| candidate_rank | rank_101_plus | 7736 | 3677 | 4059 | 47.53 | 46.76 | 0.77 | high | neutral | False |  | 49 |
| liquidity_score | confirmed | 1561 | 737 | 824 | 47.21 | 46.76 | 0.45 | high | neutral | False |  | 49 |
| selected_pick | broad_pool | 9146 | 4292 | 4854 | 46.93 | 46.76 | 0.17 | high | neutral | False |  | 56 |
| news_risk_penalty | none | 9158 | 4281 | 4877 | 46.75 | 46.76 | -0.01 | high | neutral | False |  | 49 |
| score_version | v2_conservative_ranker | 9525 | 4444 | 5081 | 46.66 | 46.76 | -0.1 | high | neutral | False |  | 49 |
| attention_noise_penalty | none | 8986 | 4193 | 4793 | 46.66 | 46.76 | -0.1 | high | neutral | False |  | 49 |
| overextension_penalty | none | 8215 | 3826 | 4389 | 46.57 | 46.76 | -0.19 | high | neutral | False |  | 49 |
| reversal_risk_penalty | none | 6709 | 3118 | 3591 | 46.47 | 46.76 | -0.29 | high | neutral | False |  | 49 |
| volume_confirmation_score | high | 375 | 174 | 201 | 46.4 | 46.76 | -0.36 | high | neutral | False |  | 48 |
| final_price_signal_score_v2 | score_20_30 | 1891 | 865 | 1026 | 45.74 | 46.76 | -1.02 | high | neutral | False |  | 49 |
| final_price_signal_score_v2 | score_lt_20 | 360 | 163 | 197 | 45.28 | 46.76 | -1.48 | high | neutral | False |  | 49 |
| candidate_rank | top_10 | 431 | 195 | 236 | 45.24 | 46.76 | -1.52 | high | neutral | False |  | 50 |
| attention_noise_penalty | high | 480 | 217 | 263 | 45.21 | 46.76 | -1.55 | high | neutral | False |  | 38 |
| candidate_rank | rank_21_50 | 529 | 239 | 290 | 45.18 | 46.76 | -1.58 | high | neutral | False |  | 36 |
| selected_pick | selected | 780 | 349 | 431 | 44.74 | 46.76 | -2.02 | high | neutral | False |  | 50 |
| final_price_signal_score_v2 | score_50_plus | 1581 | 700 | 881 | 44.28 | 46.76 | -2.48 | high | neutral | False |  | 49 |
| candidate_rank | rank_11_20 | 349 | 154 | 195 | 44.13 | 46.76 | -2.63 | high | neutral | False |  | 42 |
| overextension_penalty | medium | 199 | 93 | 106 | 46.73 | 46.76 | -0.03 | medium | neutral | False |  | 44 |
| news_risk_penalty | high | 217 | 96 | 121 | 44.24 | 46.76 | -2.52 | medium | neutral | False |  | 37 |
| overextension_penalty | low | 265 | 117 | 148 | 44.15 | 46.76 | -2.61 | medium | neutral | False |  | 47 |
| attention_noise_penalty | low | 41 | 24 | 17 | 58.54 | 46.76 | 11.78 | insufficient | watch | True | large_lift_with_under_100_cases | 19 |
| attention_noise_penalty | medium | 18 | 10 | 8 | 55.56 | 46.76 | 8.8 | insufficient | watch | False |  | 11 |
| news_risk_penalty | low | 17 | 9 | 8 | 52.94 | 46.76 | 6.18 | insufficient | watch | False |  | 10 |