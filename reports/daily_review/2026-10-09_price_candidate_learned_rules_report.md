# Price Candidate Learned Rules Report - 2026-10-09

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261009.csv`
- Baseline evaluated count: **9806**
- Baseline success rate: **46.83%**
- Total rule rows: **45**
- Boost rules: **10**
- Penalize rules: **6**
- Watch rules: **3**
- Suspicious rules: **2**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| candidate_rank | missing | 336 | 173 | 163 | 51.49 | 46.83 | 4.66 | high | boost | False |  | 6 |
| reversal_risk_penalty | high | 693 | 348 | 345 | 50.22 | 46.83 | 3.39 | high | boost | True | boost_on_semantically_risky_bucket | 49 |
| score_version | legacy_or_unknown | 407 | 203 | 204 | 49.88 | 46.83 | 3.05 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 407 | 203 | 204 | 49.88 | 46.83 | 3.05 | high | boost | False |  | 7 |
| overextension_penalty | missing | 407 | 203 | 204 | 49.88 | 46.83 | 3.05 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 407 | 203 | 204 | 49.88 | 46.83 | 3.05 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 407 | 203 | 204 | 49.88 | 46.83 | 3.05 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 407 | 203 | 204 | 49.88 | 46.83 | 3.05 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 407 | 203 | 204 | 49.88 | 46.83 | 3.05 | high | boost | False |  | 7 |
| liquidity_score | missing | 407 | 203 | 204 | 49.88 | 46.83 | 3.05 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | score_50_plus | 1553 | 677 | 876 | 43.59 | 46.83 | -3.24 | high | penalize | False |  | 49 |
| volume_confirmation_score | moderate | 729 | 315 | 414 | 43.21 | 46.83 | -3.62 | high | penalize | False |  | 49 |
| candidate_rank | rank_51_100 | 527 | 200 | 327 | 37.95 | 46.83 | -8.88 | high | penalize | False |  | 23 |
| volume_confirmation_score | none | 1310 | 485 | 825 | 37.02 | 46.83 | -9.81 | high | penalize | False |  | 49 |
| liquidity_score | none | 355 | 18 | 337 | 5.07 | 46.83 | -41.76 | high | penalize | False |  | 49 |
| final_price_signal_score_v2 | score_40_50 | 149 | 60 | 89 | 40.27 | 46.83 | -6.56 | medium | penalize | False |  | 7 |
| reversal_risk_penalty | medium | 1137 | 562 | 575 | 49.43 | 46.83 | 2.6 | high | neutral | False |  | 49 |
| volume_confirmation_score | negative | 6993 | 3417 | 3576 | 48.86 | 46.83 | 2.03 | high | neutral | False |  | 49 |
| liquidity_score | basic | 7518 | 3652 | 3866 | 48.58 | 46.83 | 1.75 | high | neutral | False |  | 49 |
| overextension_penalty | high | 853 | 412 | 441 | 48.3 | 46.83 | 1.47 | high | neutral | False |  | 49 |
| final_price_signal_score_v2 | score_30_40 | 5463 | 2629 | 2834 | 48.12 | 46.83 | 1.29 | high | neutral | False |  | 49 |
| candidate_rank | rank_101_plus | 7657 | 3642 | 4015 | 47.56 | 46.83 | 0.73 | high | neutral | False |  | 49 |
| liquidity_score | confirmed | 1526 | 719 | 807 | 47.12 | 46.83 | 0.29 | high | neutral | False |  | 49 |
| selected_pick | broad_pool | 9045 | 4247 | 4798 | 46.95 | 46.83 | 0.12 | high | neutral | False |  | 56 |
| volume_confirmation_score | high | 367 | 172 | 195 | 46.87 | 46.83 | 0.04 | high | neutral | False |  | 47 |
| news_risk_penalty | none | 9038 | 4226 | 4812 | 46.76 | 46.83 | -0.07 | high | neutral | False |  | 49 |
| score_version | v2_conservative_ranker | 9399 | 4389 | 5010 | 46.7 | 46.83 | -0.13 | high | neutral | False |  | 49 |
| attention_noise_penalty | none | 8864 | 4138 | 4726 | 46.68 | 46.83 | -0.15 | high | neutral | False |  | 49 |
| overextension_penalty | none | 8085 | 3763 | 4322 | 46.54 | 46.83 | -0.29 | high | neutral | False |  | 49 |
| reversal_risk_penalty | none | 6611 | 3050 | 3561 | 46.14 | 46.83 | -0.69 | high | neutral | False |  | 49 |
| final_price_signal_score_v2 | score_20_30 | 1850 | 850 | 1000 | 45.95 | 46.83 | -0.88 | high | neutral | False |  | 49 |
| candidate_rank | top_10 | 418 | 191 | 227 | 45.69 | 46.83 | -1.14 | high | neutral | False |  | 50 |
| selected_pick | selected | 761 | 345 | 416 | 45.34 | 46.83 | -1.49 | high | neutral | False |  | 50 |
| attention_noise_penalty | high | 471 | 213 | 258 | 45.22 | 46.83 | -1.61 | high | neutral | False |  | 37 |
| final_price_signal_score_v2 | score_lt_20 | 384 | 173 | 211 | 45.05 | 46.83 | -1.78 | high | neutral | False |  | 49 |
| candidate_rank | rank_11_20 | 343 | 154 | 189 | 44.9 | 46.83 | -1.93 | high | neutral | False |  | 42 |
| reversal_risk_penalty | low | 958 | 429 | 529 | 44.78 | 46.83 | -2.05 | high | neutral | False |  | 49 |
| candidate_rank | rank_21_50 | 525 | 232 | 293 | 44.19 | 46.83 | -2.64 | high | neutral | False |  | 36 |
| overextension_penalty | medium | 204 | 99 | 105 | 48.53 | 46.83 | 1.7 | medium | neutral | False |  | 46 |
| news_risk_penalty | medium | 129 | 59 | 70 | 45.74 | 46.83 | -1.09 | medium | neutral | False |  | 43 |
| overextension_penalty | low | 257 | 115 | 142 | 44.75 | 46.83 | -2.08 | medium | neutral | False |  | 47 |
| news_risk_penalty | high | 212 | 93 | 119 | 43.87 | 46.83 | -2.96 | medium | neutral | False |  | 37 |
| attention_noise_penalty | low | 44 | 27 | 17 | 61.36 | 46.83 | 14.53 | insufficient | watch | True | large_lift_with_under_100_cases | 20 |
| news_risk_penalty | low | 20 | 11 | 9 | 55.0 | 46.83 | 8.17 | insufficient | watch | False |  | 10 |
| attention_noise_penalty | medium | 20 | 11 | 9 | 55.0 | 46.83 | 8.17 | insufficient | watch | False |  | 13 |