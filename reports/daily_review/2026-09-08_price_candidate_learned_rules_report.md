# Price Candidate Learned Rules Report - 2026-09-08

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260908.csv`
- Baseline evaluated count: **4456**
- Baseline success rate: **43.63%**
- Total rule rows: **45**
- Boost rules: **14**
- Penalize rules: **5**
- Watch rules: **3**
- Suspicious rules: **5**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 452 | 247 | 205 | 54.65 | 43.63 | 11.02 | high | boost | True | boost_on_semantically_risky_bucket | 32 |
| overextension_penalty | high | 483 | 247 | 236 | 51.14 | 43.63 | 7.51 | high | boost | True | boost_on_semantically_risky_bucket | 32 |
| candidate_rank | missing | 329 | 168 | 161 | 51.06 | 43.63 | 7.43 | high | boost | False |  | 6 |
| score_version | legacy_or_unknown | 394 | 195 | 199 | 49.49 | 43.63 | 5.86 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 394 | 195 | 199 | 49.49 | 43.63 | 5.86 | high | boost | False |  | 7 |
| overextension_penalty | missing | 394 | 195 | 199 | 49.49 | 43.63 | 5.86 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 394 | 195 | 199 | 49.49 | 43.63 | 5.86 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 394 | 195 | 199 | 49.49 | 43.63 | 5.86 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 394 | 195 | 199 | 49.49 | 43.63 | 5.86 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 394 | 195 | 199 | 49.49 | 43.63 | 5.86 | high | boost | False |  | 7 |
| liquidity_score | missing | 394 | 195 | 199 | 49.49 | 43.63 | 5.86 | high | boost | False |  | 7 |
| reversal_risk_penalty | medium | 683 | 323 | 360 | 47.29 | 43.63 | 3.66 | high | boost | False |  | 32 |
| final_price_signal_score_v2 | score_40_50 | 50 | 28 | 22 | 56.0 | 43.63 | 12.37 | low | boost | True | large_lift_with_under_100_cases | 5 |
| candidate_rank | top_10 | 273 | 129 | 144 | 47.25 | 43.63 | 3.62 | medium | boost | False |  | 33 |
| reversal_risk_penalty | none | 2302 | 932 | 1370 | 40.49 | 43.63 | -3.14 | high | penalize | False |  | 32 |
| reversal_risk_penalty | low | 625 | 247 | 378 | 39.52 | 43.63 | -4.11 | high | penalize | False |  | 32 |
| volume_confirmation_score | none | 854 | 325 | 529 | 38.06 | 43.63 | -5.57 | high | penalize | False |  | 32 |
| candidate_rank | rank_51_100 | 360 | 124 | 236 | 34.44 | 43.63 | -9.19 | high | penalize | False |  | 17 |
| liquidity_score | none | 201 | 8 | 193 | 3.98 | 43.63 | -39.65 | medium | penalize | False |  | 32 |
| liquidity_score | confirmed | 1018 | 474 | 544 | 46.56 | 43.63 | 2.93 | high | neutral | False |  | 32 |
| selected_pick | selected | 462 | 208 | 254 | 45.02 | 43.63 | 1.39 | high | neutral | False |  | 33 |
| volume_confirmation_score | negative | 2479 | 1111 | 1368 | 44.82 | 43.63 | 1.19 | high | neutral | False |  | 32 |
| liquidity_score | basic | 2843 | 1267 | 1576 | 44.57 | 43.63 | 0.94 | high | neutral | False |  | 32 |
| final_price_signal_score_v2 | score_30_40 | 2087 | 926 | 1161 | 44.37 | 43.63 | 0.74 | high | neutral | False |  | 32 |
| candidate_rank | rank_101_plus | 3074 | 1350 | 1724 | 43.92 | 43.63 | 0.29 | high | neutral | False |  | 32 |
| selected_pick | broad_pool | 3994 | 1736 | 2258 | 43.47 | 43.63 | -0.16 | high | neutral | False |  | 39 |
| score_version | v2_conservative_ranker | 4062 | 1749 | 2313 | 43.06 | 43.63 | -0.57 | high | neutral | False |  | 32 |
| news_risk_penalty | none | 3803 | 1633 | 2170 | 42.94 | 43.63 | -0.69 | high | neutral | False |  | 32 |
| attention_noise_penalty | none | 3802 | 1631 | 2171 | 42.9 | 43.63 | -0.73 | high | neutral | False |  | 32 |
| overextension_penalty | none | 3319 | 1389 | 1930 | 41.85 | 43.63 | -1.78 | high | neutral | False |  | 32 |
| final_price_signal_score_v2 | score_50_plus | 712 | 298 | 414 | 41.85 | 43.63 | -1.78 | high | neutral | False |  | 32 |
| volume_confirmation_score | moderate | 494 | 204 | 290 | 41.3 | 43.63 | -2.33 | high | neutral | False |  | 32 |
| final_price_signal_score_v2 | score_20_30 | 979 | 399 | 580 | 40.76 | 43.63 | -2.87 | high | neutral | False |  | 32 |
| news_risk_penalty | medium | 96 | 43 | 53 | 44.79 | 43.63 | 1.16 | low | neutral | False |  | 29 |
| volume_confirmation_score | high | 235 | 109 | 126 | 46.38 | 43.63 | 2.75 | medium | neutral | False |  | 31 |
| attention_noise_penalty | high | 237 | 105 | 132 | 44.3 | 43.63 | 0.67 | medium | neutral | False |  | 24 |
| overextension_penalty | low | 146 | 64 | 82 | 43.84 | 43.63 | 0.21 | medium | neutral | False |  | 30 |
| news_risk_penalty | high | 143 | 62 | 81 | 43.36 | 43.63 | -0.27 | medium | neutral | False |  | 20 |
| overextension_penalty | medium | 114 | 49 | 65 | 42.98 | 43.63 | -0.65 | medium | neutral | False |  | 29 |
| final_price_signal_score_v2 | score_lt_20 | 234 | 98 | 136 | 41.88 | 43.63 | -1.75 | medium | neutral | False |  | 32 |
| candidate_rank | rank_11_20 | 189 | 79 | 110 | 41.8 | 43.63 | -1.83 | medium | neutral | False |  | 25 |
| candidate_rank | rank_21_50 | 231 | 94 | 137 | 40.69 | 43.63 | -2.94 | medium | neutral | False |  | 19 |
| attention_noise_penalty | low | 15 | 9 | 6 | 60.0 | 43.63 | 16.37 | insufficient | watch | True | large_lift_with_under_100_cases | 9 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 43.63 | 11.37 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| attention_noise_penalty | medium | 8 | 4 | 4 | 50.0 | 43.63 | 6.37 | insufficient | watch | False |  | 5 |