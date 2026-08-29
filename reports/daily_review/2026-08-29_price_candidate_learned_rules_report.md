# Price Candidate Learned Rules Report - 2026-08-29

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260829.csv`
- Baseline evaluated count: **3301**
- Baseline success rate: **42.2%**
- Total rule rows: **45**
- Boost rules: **18**
- Penalize rules: **7**
- Watch rules: **4**
- Suspicious rules: **4**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 376 | 195 | 181 | 51.86 | 42.2 | 9.66 | high | boost | True | boost_on_semantically_risky_bucket | 26 |
| candidate_rank | missing | 323 | 166 | 157 | 51.39 | 42.2 | 9.19 | high | boost | False |  | 6 |
| score_version | legacy_or_unknown | 388 | 194 | 194 | 50.0 | 42.2 | 7.8 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 388 | 194 | 194 | 50.0 | 42.2 | 7.8 | high | boost | False |  | 7 |
| overextension_penalty | missing | 388 | 194 | 194 | 50.0 | 42.2 | 7.8 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 388 | 194 | 194 | 50.0 | 42.2 | 7.8 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 388 | 194 | 194 | 50.0 | 42.2 | 7.8 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 388 | 194 | 194 | 50.0 | 42.2 | 7.8 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 388 | 194 | 194 | 50.0 | 42.2 | 7.8 | high | boost | False |  | 7 |
| liquidity_score | missing | 388 | 194 | 194 | 50.0 | 42.2 | 7.8 | high | boost | False |  | 7 |
| overextension_penalty | high | 364 | 181 | 183 | 49.73 | 42.2 | 7.53 | high | boost | True | boost_on_semantically_risky_bucket | 26 |
| selected_pick | selected | 358 | 169 | 189 | 47.21 | 42.2 | 5.01 | high | boost | False |  | 26 |
| reversal_risk_penalty | medium | 550 | 254 | 296 | 46.18 | 42.2 | 3.98 | high | boost | False |  | 26 |
| liquidity_score | confirmed | 886 | 404 | 482 | 45.6 | 42.2 | 3.4 | high | boost | False |  | 26 |
| news_risk_penalty | medium | 86 | 40 | 46 | 46.51 | 42.2 | 4.31 | low | boost | False |  | 25 |
| candidate_rank | top_10 | 216 | 103 | 113 | 47.69 | 42.2 | 5.49 | medium | boost | False |  | 26 |
| candidate_rank | rank_11_20 | 142 | 66 | 76 | 46.48 | 42.2 | 4.28 | medium | boost | False |  | 19 |
| volume_confirmation_score | high | 199 | 91 | 108 | 45.73 | 42.2 | 3.53 | medium | boost | False |  | 25 |
| final_price_signal_score_v2 | score_20_30 | 750 | 291 | 459 | 38.8 | 42.2 | -3.4 | high | penalize | False |  | 26 |
| reversal_risk_penalty | none | 1491 | 565 | 926 | 37.89 | 42.2 | -4.31 | high | penalize | False |  | 26 |
| reversal_risk_penalty | low | 496 | 185 | 311 | 37.3 | 42.2 | -4.9 | high | penalize | False |  | 26 |
| volume_confirmation_score | none | 713 | 263 | 450 | 36.89 | 42.2 | -5.31 | high | penalize | False |  | 26 |
| candidate_rank | rank_51_100 | 340 | 120 | 220 | 35.29 | 42.2 | -6.91 | high | penalize | False |  | 15 |
| candidate_rank | rank_21_50 | 185 | 72 | 113 | 38.92 | 42.2 | -3.28 | medium | penalize | False |  | 15 |
| liquidity_score | none | 153 | 5 | 148 | 3.27 | 42.2 | -38.93 | medium | penalize | False |  | 26 |
| volume_confirmation_score | negative | 1562 | 665 | 897 | 42.57 | 42.2 | 0.37 | high | neutral | False |  | 26 |
| final_price_signal_score_v2 | score_50_plus | 540 | 229 | 311 | 42.41 | 42.2 | 0.21 | high | neutral | False |  | 25 |
| liquidity_score | basic | 1874 | 790 | 1084 | 42.16 | 42.2 | -0.04 | high | neutral | False |  | 26 |
| final_price_signal_score_v2 | score_30_40 | 1406 | 589 | 817 | 41.89 | 42.2 | -0.31 | high | neutral | False |  | 26 |
| selected_pick | broad_pool | 2943 | 1224 | 1719 | 41.59 | 42.2 | -0.61 | high | neutral | False |  | 33 |
| candidate_rank | rank_101_plus | 2095 | 866 | 1229 | 41.34 | 42.2 | -0.86 | high | neutral | False |  | 26 |
| score_version | v2_conservative_ranker | 2913 | 1199 | 1714 | 41.16 | 42.2 | -1.04 | high | neutral | False |  | 26 |
| attention_noise_penalty | none | 2815 | 1158 | 1657 | 41.14 | 42.2 | -1.06 | high | neutral | False |  | 26 |
| volume_confirmation_score | moderate | 439 | 180 | 259 | 41.0 | 42.2 | -1.2 | high | neutral | False |  | 26 |
| news_risk_penalty | none | 2705 | 1103 | 1602 | 40.78 | 42.2 | -1.42 | high | neutral | False |  | 26 |
| overextension_penalty | none | 2328 | 925 | 1403 | 39.73 | 42.2 | -2.47 | high | neutral | False |  | 26 |
| attention_noise_penalty | high | 91 | 39 | 52 | 42.86 | 42.2 | 0.66 | low | neutral | False |  | 18 |
| news_risk_penalty | high | 106 | 46 | 60 | 43.4 | 42.2 | 1.2 | medium | neutral | False |  | 16 |
| overextension_penalty | medium | 101 | 43 | 58 | 42.57 | 42.2 | 0.37 | medium | neutral | False |  | 23 |
| overextension_penalty | low | 120 | 50 | 70 | 41.67 | 42.2 | -0.53 | medium | neutral | False |  | 23 |
| final_price_signal_score_v2 | score_lt_20 | 202 | 84 | 118 | 41.58 | 42.2 | -0.62 | medium | neutral | False |  | 26 |
| news_risk_penalty | low | 16 | 10 | 6 | 62.5 | 42.2 | 20.3 | insufficient | watch | True | large_lift_with_under_100_cases | 9 |
| final_price_signal_score_v2 | score_40_50 | 15 | 6 | 9 | 40.0 | 42.2 | -2.2 | insufficient | watch | False |  | 3 |
| attention_noise_penalty | low | 3 | 1 | 2 | 33.33 | 42.2 | -8.87 | insufficient | watch | False |  | 3 |
| attention_noise_penalty | medium | 4 | 1 | 3 | 25.0 | 42.2 | -17.2 | insufficient | watch | True | large_lift_with_under_100_cases | 4 |