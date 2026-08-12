# Price Candidate Learned Rules Report - 2026-08-12

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260812.csv`
- Baseline evaluated count: **2209**
- Baseline success rate: **42.19%**
- Total rule rows: **44**
- Boost rules: **18**
- Penalize rules: **10**
- Watch rules: **4**
- Suspicious rules: **6**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| candidate_rank | missing | 301 | 161 | 140 | 53.49 | 42.19 | 11.3 | high | boost | False |  | 6 |
| score_version | legacy_or_unknown | 375 | 192 | 183 | 51.2 | 42.19 | 9.01 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 375 | 192 | 183 | 51.2 | 42.19 | 9.01 | high | boost | False |  | 7 |
| overextension_penalty | missing | 375 | 192 | 183 | 51.2 | 42.19 | 9.01 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 375 | 192 | 183 | 51.2 | 42.19 | 9.01 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 375 | 192 | 183 | 51.2 | 42.19 | 9.01 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 375 | 192 | 183 | 51.2 | 42.19 | 9.01 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 375 | 192 | 183 | 51.2 | 42.19 | 9.01 | high | boost | False |  | 7 |
| liquidity_score | missing | 375 | 192 | 183 | 51.2 | 42.19 | 9.01 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | score_50_plus | 303 | 151 | 152 | 49.83 | 42.19 | 7.64 | high | boost | False |  | 16 |
| liquidity_score | confirmed | 561 | 263 | 298 | 46.88 | 42.19 | 4.69 | high | boost | False |  | 16 |
| news_risk_penalty | medium | 63 | 32 | 31 | 50.79 | 42.19 | 8.6 | low | boost | False |  | 16 |
| candidate_rank | rank_11_20 | 63 | 31 | 32 | 49.21 | 42.19 | 7.02 | low | boost | False |  | 8 |
| candidate_rank | top_10 | 144 | 82 | 62 | 56.94 | 42.19 | 14.75 | medium | boost | False |  | 17 |
| selected_pick | selected | 207 | 113 | 94 | 54.59 | 42.19 | 12.4 | medium | boost | False |  | 17 |
| volume_confirmation_score | high | 127 | 68 | 59 | 53.54 | 42.19 | 11.35 | medium | boost | False |  | 15 |
| reversal_risk_penalty | high | 280 | 146 | 134 | 52.14 | 42.19 | 9.95 | medium | boost | True | boost_on_semantically_risky_bucket | 16 |
| overextension_penalty | high | 246 | 124 | 122 | 50.41 | 42.19 | 8.22 | medium | boost | True | boost_on_semantically_risky_bucket | 16 |
| final_price_signal_score_v2 | score_30_40 | 815 | 317 | 498 | 38.9 | 42.19 | -3.29 | high | penalize | False |  | 16 |
| candidate_rank | rank_101_plus | 1188 | 459 | 729 | 38.64 | 42.19 | -3.55 | high | penalize | False |  | 16 |
| overextension_penalty | none | 1446 | 554 | 892 | 38.31 | 42.19 | -3.88 | high | penalize | False |  | 16 |
| reversal_risk_penalty | none | 944 | 361 | 583 | 38.24 | 42.19 | -3.95 | high | penalize | False |  | 16 |
| final_price_signal_score_v2 | score_20_30 | 558 | 211 | 347 | 37.81 | 42.19 | -4.38 | high | penalize | False |  | 16 |
| candidate_rank | rank_51_100 | 394 | 146 | 248 | 37.06 | 42.19 | -5.13 | high | penalize | False |  | 12 |
| volume_confirmation_score | none | 446 | 160 | 286 | 35.87 | 42.19 | -6.32 | high | penalize | False |  | 16 |
| liquidity_score | none | 97 | 3 | 94 | 3.09 | 42.19 | -39.1 | low | penalize | True | large_lift_with_under_100_cases | 16 |
| final_price_signal_score_v2 | score_lt_20 | 158 | 61 | 97 | 38.61 | 42.19 | -3.58 | medium | penalize | False |  | 16 |
| reversal_risk_penalty | low | 261 | 92 | 169 | 35.25 | 42.19 | -6.94 | medium | penalize | False |  | 16 |
| selected_pick | broad_pool | 2002 | 819 | 1183 | 40.91 | 42.19 | -1.28 | high | neutral | False |  | 23 |
| reversal_risk_penalty | medium | 349 | 141 | 208 | 40.4 | 42.19 | -1.79 | high | neutral | False |  | 16 |
| score_version | v2_conservative_ranker | 1834 | 740 | 1094 | 40.35 | 42.19 | -1.84 | high | neutral | False |  | 16 |
| liquidity_score | basic | 1176 | 474 | 702 | 40.31 | 42.19 | -1.88 | high | neutral | False |  | 16 |
| volume_confirmation_score | negative | 978 | 394 | 584 | 40.29 | 42.19 | -1.9 | high | neutral | False |  | 16 |
| attention_noise_penalty | none | 1763 | 710 | 1053 | 40.27 | 42.19 | -1.92 | high | neutral | False |  | 16 |
| news_risk_penalty | none | 1705 | 671 | 1034 | 39.35 | 42.19 | -2.84 | high | neutral | False |  | 16 |
| overextension_penalty | medium | 61 | 27 | 34 | 44.26 | 42.19 | 2.07 | low | neutral | False |  | 13 |
| attention_noise_penalty | high | 62 | 27 | 35 | 43.55 | 42.19 | 1.36 | low | neutral | False |  | 12 |
| overextension_penalty | low | 81 | 35 | 46 | 43.21 | 42.19 | 1.02 | low | neutral | False |  | 14 |
| candidate_rank | rank_21_50 | 119 | 53 | 66 | 44.54 | 42.19 | 2.35 | medium | neutral | False |  | 7 |
| volume_confirmation_score | moderate | 283 | 118 | 165 | 41.7 | 42.19 | -0.49 | medium | neutral | False |  | 16 |
| news_risk_penalty | low | 22 | 13 | 9 | 59.09 | 42.19 | 16.9 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| news_risk_penalty | high | 44 | 24 | 20 | 54.55 | 42.19 | 12.36 | insufficient | watch | True | large_lift_with_under_100_cases | 6 |
| attention_noise_penalty | low | 6 | 3 | 3 | 50.0 | 42.19 | 7.81 | insufficient | watch | False |  | 4 |
| attention_noise_penalty | medium | 3 | 0 | 3 | 0.0 | 42.19 | -42.19 | insufficient | watch | True | large_lift_with_under_100_cases | 3 |