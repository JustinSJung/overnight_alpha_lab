# Price Candidate Learned Rules Report - 2026-08-28

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260828.csv`
- Baseline evaluated count: **3679**
- Baseline success rate: **42.29%**
- Total rule rows: **44**
- Boost rules: **18**
- Penalize rules: **6**
- Watch rules: **3**
- Suspicious rules: **4**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 451 | 239 | 212 | 52.99 | 42.29 | 10.7 | high | boost | True | boost_on_semantically_risky_bucket | 26 |
| candidate_rank | missing | 311 | 164 | 147 | 52.73 | 42.29 | 10.44 | high | boost | False |  | 6 |
| score_version | legacy_or_unknown | 385 | 195 | 190 | 50.65 | 42.29 | 8.36 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 385 | 195 | 190 | 50.65 | 42.29 | 8.36 | high | boost | False |  | 7 |
| overextension_penalty | missing | 385 | 195 | 190 | 50.65 | 42.29 | 8.36 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 385 | 195 | 190 | 50.65 | 42.29 | 8.36 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 385 | 195 | 190 | 50.65 | 42.29 | 8.36 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 385 | 195 | 190 | 50.65 | 42.29 | 8.36 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 385 | 195 | 190 | 50.65 | 42.29 | 8.36 | high | boost | False |  | 7 |
| liquidity_score | missing | 385 | 195 | 190 | 50.65 | 42.29 | 8.36 | high | boost | False |  | 7 |
| overextension_penalty | high | 407 | 206 | 201 | 50.61 | 42.29 | 8.32 | high | boost | True | boost_on_semantically_risky_bucket | 26 |
| selected_pick | selected | 419 | 197 | 222 | 47.02 | 42.29 | 4.73 | high | boost | False |  | 27 |
| liquidity_score | confirmed | 990 | 455 | 535 | 45.96 | 42.29 | 3.67 | high | boost | False |  | 26 |
| reversal_risk_penalty | medium | 614 | 281 | 333 | 45.77 | 42.29 | 3.48 | high | boost | False |  | 26 |
| news_risk_penalty | medium | 92 | 42 | 50 | 45.65 | 42.29 | 3.36 | low | boost | False |  | 25 |
| candidate_rank | top_10 | 254 | 120 | 134 | 47.24 | 42.29 | 4.95 | medium | boost | False |  | 27 |
| candidate_rank | rank_11_20 | 165 | 77 | 88 | 46.67 | 42.29 | 4.38 | medium | boost | False |  | 18 |
| volume_confirmation_score | high | 226 | 104 | 122 | 46.02 | 42.29 | 3.73 | medium | boost | False |  | 25 |
| reversal_risk_penalty | none | 1688 | 641 | 1047 | 37.97 | 42.29 | -4.32 | high | penalize | False |  | 26 |
| reversal_risk_penalty | low | 541 | 200 | 341 | 36.97 | 42.29 | -5.32 | high | penalize | False |  | 26 |
| volume_confirmation_score | none | 796 | 291 | 505 | 36.56 | 42.29 | -5.73 | high | penalize | False |  | 26 |
| candidate_rank | rank_51_100 | 406 | 147 | 259 | 36.21 | 42.29 | -6.08 | high | penalize | False |  | 14 |
| candidate_rank | rank_21_50 | 235 | 84 | 151 | 35.74 | 42.29 | -6.55 | medium | penalize | False |  | 14 |
| liquidity_score | none | 178 | 6 | 172 | 3.37 | 42.29 | -38.92 | medium | penalize | False |  | 26 |
| volume_confirmation_score | negative | 1787 | 766 | 1021 | 42.87 | 42.29 | 0.58 | high | neutral | False |  | 26 |
| liquidity_score | basic | 2126 | 900 | 1226 | 42.33 | 42.29 | 0.04 | high | neutral | False |  | 26 |
| final_price_signal_score_v2 | score_30_40 | 1577 | 666 | 911 | 42.23 | 42.29 | -0.06 | high | neutral | False |  | 26 |
| candidate_rank | rank_101_plus | 2308 | 964 | 1344 | 41.77 | 42.29 | -0.52 | high | neutral | False |  | 26 |
| selected_pick | broad_pool | 3260 | 1359 | 1901 | 41.69 | 42.29 | -0.6 | high | neutral | False |  | 33 |
| final_price_signal_score_v2 | score_50_plus | 643 | 267 | 376 | 41.52 | 42.29 | -0.77 | high | neutral | False |  | 26 |
| score_version | v2_conservative_ranker | 3294 | 1361 | 1933 | 41.32 | 42.29 | -0.97 | high | neutral | False |  | 26 |
| attention_noise_penalty | none | 3171 | 1309 | 1862 | 41.28 | 42.29 | -1.01 | high | neutral | False |  | 26 |
| volume_confirmation_score | moderate | 485 | 200 | 285 | 41.24 | 42.29 | -1.05 | high | neutral | False |  | 26 |
| news_risk_penalty | none | 3066 | 1256 | 1810 | 40.97 | 42.29 | -1.32 | high | neutral | False |  | 26 |
| overextension_penalty | none | 2643 | 1054 | 1589 | 39.88 | 42.29 | -2.41 | high | neutral | False |  | 26 |
| final_price_signal_score_v2 | score_20_30 | 851 | 336 | 515 | 39.48 | 42.29 | -2.81 | high | neutral | False |  | 26 |
| news_risk_penalty | high | 114 | 50 | 64 | 43.86 | 42.29 | 1.57 | medium | neutral | False |  | 16 |
| attention_noise_penalty | high | 113 | 48 | 65 | 42.48 | 42.29 | 0.19 | medium | neutral | False |  | 20 |
| overextension_penalty | low | 130 | 55 | 75 | 42.31 | 42.29 | 0.02 | medium | neutral | False |  | 24 |
| final_price_signal_score_v2 | score_lt_20 | 223 | 92 | 131 | 41.26 | 42.29 | -1.03 | medium | neutral | False |  | 26 |
| overextension_penalty | medium | 114 | 46 | 68 | 40.35 | 42.29 | -1.94 | medium | neutral | False |  | 23 |
| news_risk_penalty | low | 22 | 13 | 9 | 59.09 | 42.29 | 16.8 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| attention_noise_penalty | low | 6 | 3 | 3 | 50.0 | 42.29 | 7.71 | insufficient | watch | False |  | 4 |
| attention_noise_penalty | medium | 4 | 1 | 3 | 25.0 | 42.29 | -17.29 | insufficient | watch | True | large_lift_with_under_100_cases | 4 |