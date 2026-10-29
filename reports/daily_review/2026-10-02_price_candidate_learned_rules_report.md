# Price Candidate Learned Rules Report - 2026-10-02

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261002.csv`
- Baseline evaluated count: **8891**
- Baseline success rate: **46.87%**
- Total rule rows: **45**
- Boost rules: **2**
- Penalize rules: **7**
- Watch rules: **3**
- Suspicious rules: **3**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 644 | 330 | 314 | 51.24 | 46.87 | 4.37 | high | boost | True | boost_on_semantically_risky_bucket | 46 |
| candidate_rank | missing | 339 | 173 | 166 | 51.03 | 46.87 | 4.16 | high | boost | False |  | 6 |
| volume_confirmation_score | moderate | 618 | 263 | 355 | 42.56 | 46.87 | -4.31 | high | penalize | False |  | 46 |
| candidate_rank | rank_51_100 | 401 | 152 | 249 | 37.91 | 46.87 | -8.96 | high | penalize | False |  | 20 |
| volume_confirmation_score | none | 1156 | 435 | 721 | 37.63 | 46.87 | -9.24 | high | penalize | False |  | 46 |
| liquidity_score | none | 316 | 17 | 299 | 5.38 | 46.87 | -41.49 | high | penalize | False |  | 46 |
| overextension_penalty | low | 211 | 92 | 119 | 43.6 | 46.87 | -3.27 | medium | penalize | False |  | 44 |
| news_risk_penalty | high | 198 | 85 | 113 | 42.93 | 46.87 | -3.94 | medium | penalize | False |  | 34 |
| final_price_signal_score_v2 | score_40_50 | 109 | 45 | 64 | 41.28 | 46.87 | -5.59 | medium | penalize | False |  | 6 |
| reversal_risk_penalty | medium | 1100 | 545 | 555 | 49.55 | 46.87 | 2.68 | high | neutral | False |  | 46 |
| overextension_penalty | high | 774 | 382 | 392 | 49.35 | 46.87 | 2.48 | high | neutral | False |  | 46 |
| score_version | legacy_or_unknown | 408 | 201 | 207 | 49.26 | 46.87 | 2.39 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 408 | 201 | 207 | 49.26 | 46.87 | 2.39 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 408 | 201 | 207 | 49.26 | 46.87 | 2.39 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 408 | 201 | 207 | 49.26 | 46.87 | 2.39 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 408 | 201 | 207 | 49.26 | 46.87 | 2.39 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 408 | 201 | 207 | 49.26 | 46.87 | 2.39 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 408 | 201 | 207 | 49.26 | 46.87 | 2.39 | high | neutral | False |  | 7 |
| liquidity_score | missing | 408 | 201 | 207 | 49.26 | 46.87 | 2.39 | high | neutral | False |  | 7 |
| volume_confirmation_score | negative | 6410 | 3125 | 3285 | 48.75 | 46.87 | 1.88 | high | neutral | False |  | 46 |
| liquidity_score | basic | 6869 | 3327 | 3542 | 48.43 | 46.87 | 1.56 | high | neutral | False |  | 46 |
| liquidity_score | confirmed | 1298 | 622 | 676 | 47.92 | 46.87 | 1.05 | high | neutral | False |  | 46 |
| final_price_signal_score_v2 | score_30_40 | 4990 | 2373 | 2617 | 47.56 | 46.87 | 0.69 | high | neutral | False |  | 46 |
| candidate_rank | rank_101_plus | 6980 | 3302 | 3678 | 47.31 | 46.87 | 0.44 | high | neutral | False |  | 46 |
| selected_pick | broad_pool | 8160 | 3832 | 4328 | 46.96 | 46.87 | 0.09 | high | neutral | False |  | 53 |
| news_risk_penalty | none | 8147 | 3817 | 4330 | 46.85 | 46.87 | -0.02 | high | neutral | False |  | 46 |
| candidate_rank | top_10 | 410 | 192 | 218 | 46.83 | 46.87 | -0.04 | high | neutral | False |  | 47 |
| score_version | v2_conservative_ranker | 8483 | 3966 | 4517 | 46.75 | 46.87 | -0.12 | high | neutral | False |  | 46 |
| attention_noise_penalty | none | 7962 | 3722 | 4240 | 46.75 | 46.87 | -0.12 | high | neutral | False |  | 46 |
| candidate_rank | rank_21_50 | 440 | 205 | 235 | 46.59 | 46.87 | -0.28 | high | neutral | False |  | 33 |
| overextension_penalty | none | 7323 | 3410 | 3913 | 46.57 | 46.87 | -0.3 | high | neutral | False |  | 46 |
| final_price_signal_score_v2 | score_lt_20 | 368 | 170 | 198 | 46.2 | 46.87 | -0.67 | high | neutral | False |  | 46 |
| reversal_risk_penalty | none | 5844 | 2695 | 3149 | 46.12 | 46.87 | -0.75 | high | neutral | False |  | 46 |
| final_price_signal_score_v2 | score_20_30 | 1781 | 817 | 964 | 45.87 | 46.87 | -1.0 | high | neutral | False |  | 46 |
| selected_pick | selected | 731 | 335 | 396 | 45.83 | 46.87 | -1.04 | high | neutral | False |  | 47 |
| attention_noise_penalty | high | 466 | 212 | 254 | 45.49 | 46.87 | -1.38 | high | neutral | False |  | 36 |
| final_price_signal_score_v2 | score_50_plus | 1235 | 561 | 674 | 45.43 | 46.87 | -1.44 | high | neutral | False |  | 46 |
| candidate_rank | rank_11_20 | 321 | 143 | 178 | 44.55 | 46.87 | -2.32 | high | neutral | False |  | 39 |
| reversal_risk_penalty | low | 895 | 396 | 499 | 44.25 | 46.87 | -2.62 | high | neutral | False |  | 46 |
| volume_confirmation_score | high | 299 | 143 | 156 | 47.83 | 46.87 | 0.96 | medium | neutral | False |  | 45 |
| overextension_penalty | medium | 175 | 82 | 93 | 46.86 | 46.87 | -0.01 | medium | neutral | False |  | 42 |
| news_risk_penalty | medium | 118 | 53 | 65 | 44.92 | 46.87 | -1.95 | medium | neutral | False |  | 41 |
| attention_noise_penalty | medium | 17 | 10 | 7 | 58.82 | 46.87 | 11.95 | insufficient | watch | True | large_lift_with_under_100_cases | 11 |
| attention_noise_penalty | low | 38 | 22 | 16 | 57.89 | 46.87 | 11.02 | insufficient | watch | True | large_lift_with_under_100_cases | 18 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 46.87 | 8.13 | insufficient | watch | False |  | 10 |