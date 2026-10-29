# Price Candidate Learned Rules Report - 2026-10-07

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261007.csv`
- Baseline evaluated count: **9512**
- Baseline success rate: **46.47%**
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
| reversal_risk_penalty | high | 666 | 340 | 326 | 51.05 | 46.47 | 4.58 | high | boost | True | boost_on_semantically_risky_bucket | 48 |
| candidate_rank | missing | 332 | 167 | 165 | 50.3 | 46.47 | 3.83 | high | boost | False |  | 6 |
| volume_confirmation_score | moderate | 704 | 304 | 400 | 43.18 | 46.47 | -3.29 | high | penalize | False |  | 48 |
| reversal_risk_penalty | low | 970 | 415 | 555 | 42.78 | 46.47 | -3.69 | high | penalize | False |  | 48 |
| candidate_rank | rank_51_100 | 467 | 177 | 290 | 37.9 | 46.47 | -8.57 | high | penalize | False |  | 22 |
| volume_confirmation_score | none | 1289 | 477 | 812 | 37.01 | 46.47 | -9.46 | high | penalize | False |  | 48 |
| liquidity_score | none | 363 | 18 | 345 | 4.96 | 46.47 | -41.51 | high | penalize | False |  | 48 |
| overextension_penalty | low | 242 | 104 | 138 | 42.98 | 46.47 | -3.49 | medium | penalize | False |  | 46 |
| final_price_signal_score_v2 | score_40_50 | 151 | 60 | 91 | 39.74 | 46.47 | -6.73 | medium | penalize | False |  | 7 |
| score_version | legacy_or_unknown | 394 | 193 | 201 | 48.98 | 46.47 | 2.51 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 394 | 193 | 201 | 48.98 | 46.47 | 2.51 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 394 | 193 | 201 | 48.98 | 46.47 | 2.51 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 394 | 193 | 201 | 48.98 | 46.47 | 2.51 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 394 | 193 | 201 | 48.98 | 46.47 | 2.51 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 394 | 193 | 201 | 48.98 | 46.47 | 2.51 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 394 | 193 | 201 | 48.98 | 46.47 | 2.51 | high | neutral | False |  | 7 |
| liquidity_score | missing | 394 | 193 | 201 | 48.98 | 46.47 | 2.51 | high | neutral | False |  | 7 |
| overextension_penalty | high | 833 | 407 | 426 | 48.86 | 46.47 | 2.39 | high | neutral | False |  | 48 |
| reversal_risk_penalty | medium | 1129 | 550 | 579 | 48.72 | 46.47 | 2.25 | high | neutral | False |  | 48 |
| volume_confirmation_score | negative | 6761 | 3274 | 3487 | 48.42 | 46.47 | 1.95 | high | neutral | False |  | 48 |
| liquidity_score | basic | 7265 | 3498 | 3767 | 48.15 | 46.47 | 1.68 | high | neutral | False |  | 48 |
| liquidity_score | confirmed | 1490 | 711 | 779 | 47.72 | 46.47 | 1.25 | high | neutral | False |  | 48 |
| volume_confirmation_score | high | 364 | 172 | 192 | 47.25 | 46.47 | 0.78 | high | neutral | False |  | 47 |
| final_price_signal_score_v2 | score_30_40 | 5328 | 2512 | 2816 | 47.15 | 46.47 | 0.68 | high | neutral | False |  | 48 |
| candidate_rank | rank_101_plus | 7483 | 3515 | 3968 | 46.97 | 46.47 | 0.5 | high | neutral | False |  | 48 |
| selected_pick | broad_pool | 8769 | 4080 | 4689 | 46.53 | 46.47 | 0.06 | high | neutral | False |  | 55 |
| news_risk_penalty | none | 8770 | 4070 | 4700 | 46.41 | 46.47 | -0.06 | high | neutral | False |  | 48 |
| attention_noise_penalty | none | 8571 | 3975 | 4596 | 46.38 | 46.47 | -0.09 | high | neutral | False |  | 48 |
| score_version | v2_conservative_ranker | 9118 | 4227 | 4891 | 46.36 | 46.47 | -0.11 | high | neutral | False |  | 48 |
| candidate_rank | top_10 | 408 | 189 | 219 | 46.32 | 46.47 | -0.15 | high | neutral | False |  | 49 |
| overextension_penalty | none | 7844 | 3622 | 4222 | 46.18 | 46.47 | -0.29 | high | neutral | False |  | 48 |
| final_price_signal_score_v2 | score_lt_20 | 358 | 165 | 193 | 46.09 | 46.47 | -0.38 | high | neutral | False |  | 48 |
| reversal_risk_penalty | none | 6353 | 2922 | 3431 | 45.99 | 46.47 | -0.48 | high | neutral | False |  | 48 |
| selected_pick | selected | 743 | 340 | 403 | 45.76 | 46.47 | -0.71 | high | neutral | False |  | 49 |
| final_price_signal_score_v2 | score_20_30 | 1850 | 842 | 1008 | 45.51 | 46.47 | -0.96 | high | neutral | False |  | 48 |
| candidate_rank | rank_21_50 | 487 | 221 | 266 | 45.38 | 46.47 | -1.09 | high | neutral | False |  | 35 |
| final_price_signal_score_v2 | score_50_plus | 1431 | 648 | 783 | 45.28 | 46.47 | -1.19 | high | neutral | False |  | 48 |
| candidate_rank | rank_11_20 | 335 | 151 | 184 | 45.07 | 46.47 | -1.4 | high | neutral | False |  | 41 |
| attention_noise_penalty | high | 487 | 218 | 269 | 44.76 | 46.47 | -1.71 | high | neutral | False |  | 38 |
| overextension_penalty | medium | 199 | 94 | 105 | 47.24 | 46.47 | 0.77 | medium | neutral | False |  | 44 |
| news_risk_penalty | medium | 126 | 57 | 69 | 45.24 | 46.47 | -1.23 | medium | neutral | False |  | 43 |
| news_risk_penalty | high | 203 | 89 | 114 | 43.84 | 46.47 | -2.63 | medium | neutral | False |  | 36 |
| news_risk_penalty | low | 19 | 11 | 8 | 57.89 | 46.47 | 11.42 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| attention_noise_penalty | low | 42 | 24 | 18 | 57.14 | 46.47 | 10.67 | insufficient | watch | True | large_lift_with_under_100_cases | 19 |
| attention_noise_penalty | medium | 18 | 10 | 8 | 55.56 | 46.47 | 9.09 | insufficient | watch | False |  | 11 |