# Price Candidate Learned Rules Report - 2026-09-01

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260901.csv`
- Baseline evaluated count: **3520**
- Baseline success rate: **43.04%**
- Total rule rows: **45**
- Boost rules: **14**
- Penalize rules: **6**
- Watch rules: **4**
- Suspicious rules: **4**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 407 | 216 | 191 | 53.07 | 43.04 | 10.03 | high | boost | True | boost_on_semantically_risky_bucket | 28 |
| candidate_rank | missing | 320 | 162 | 158 | 50.62 | 43.04 | 7.58 | high | boost | False |  | 6 |
| overextension_penalty | high | 407 | 205 | 202 | 50.37 | 43.04 | 7.33 | high | boost | True | boost_on_semantically_risky_bucket | 28 |
| score_version | legacy_or_unknown | 384 | 188 | 196 | 48.96 | 43.04 | 5.92 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 384 | 188 | 196 | 48.96 | 43.04 | 5.92 | high | boost | False |  | 7 |
| overextension_penalty | missing | 384 | 188 | 196 | 48.96 | 43.04 | 5.92 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 384 | 188 | 196 | 48.96 | 43.04 | 5.92 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 384 | 188 | 196 | 48.96 | 43.04 | 5.92 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 384 | 188 | 196 | 48.96 | 43.04 | 5.92 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 384 | 188 | 196 | 48.96 | 43.04 | 5.92 | high | boost | False |  | 7 |
| liquidity_score | missing | 384 | 188 | 196 | 48.96 | 43.04 | 5.92 | high | boost | False |  | 7 |
| liquidity_score | confirmed | 926 | 432 | 494 | 46.65 | 43.04 | 3.61 | high | boost | False |  | 28 |
| volume_confirmation_score | high | 217 | 103 | 114 | 47.47 | 43.04 | 4.43 | medium | boost | False |  | 27 |
| candidate_rank | top_10 | 235 | 111 | 124 | 47.23 | 43.04 | 4.19 | medium | boost | False |  | 29 |
| reversal_risk_penalty | none | 1635 | 645 | 990 | 39.45 | 43.04 | -3.59 | high | penalize | False |  | 28 |
| reversal_risk_penalty | low | 528 | 207 | 321 | 39.2 | 43.04 | -3.84 | high | penalize | False |  | 28 |
| volume_confirmation_score | none | 743 | 277 | 466 | 37.28 | 43.04 | -5.76 | high | penalize | False |  | 28 |
| candidate_rank | rank_51_100 | 330 | 119 | 211 | 36.06 | 43.04 | -6.98 | high | penalize | False |  | 16 |
| overextension_penalty | medium | 101 | 40 | 61 | 39.6 | 43.04 | -3.44 | medium | penalize | False |  | 23 |
| liquidity_score | none | 159 | 6 | 153 | 3.77 | 43.04 | -39.27 | medium | penalize | False |  | 28 |
| selected_pick | selected | 397 | 182 | 215 | 45.84 | 43.04 | 2.8 | high | neutral | False |  | 29 |
| reversal_risk_penalty | medium | 566 | 259 | 307 | 45.76 | 43.04 | 2.72 | high | neutral | False |  | 28 |
| volume_confirmation_score | negative | 1730 | 760 | 970 | 43.93 | 43.04 | 0.89 | high | neutral | False |  | 28 |
| liquidity_score | basic | 2051 | 889 | 1162 | 43.34 | 43.04 | 0.3 | high | neutral | False |  | 28 |
| final_price_signal_score_v2 | score_30_40 | 1519 | 656 | 863 | 43.19 | 43.04 | 0.15 | high | neutral | False |  | 28 |
| candidate_rank | rank_101_plus | 2252 | 963 | 1289 | 42.76 | 43.04 | -0.28 | high | neutral | False |  | 28 |
| selected_pick | broad_pool | 3123 | 1333 | 1790 | 42.68 | 43.04 | -0.36 | high | neutral | False |  | 35 |
| score_version | v2_conservative_ranker | 3136 | 1327 | 1809 | 42.32 | 43.04 | -0.72 | high | neutral | False |  | 28 |
| final_price_signal_score_v2 | score_50_plus | 621 | 262 | 359 | 42.19 | 43.04 | -0.85 | high | neutral | False |  | 28 |
| attention_noise_penalty | none | 2990 | 1261 | 1729 | 42.17 | 43.04 | -0.87 | high | neutral | False |  | 28 |
| news_risk_penalty | none | 2905 | 1225 | 1680 | 42.17 | 43.04 | -0.87 | high | neutral | False |  | 28 |
| volume_confirmation_score | moderate | 446 | 187 | 259 | 41.93 | 43.04 | -1.11 | high | neutral | False |  | 28 |
| overextension_penalty | none | 2497 | 1026 | 1471 | 41.09 | 43.04 | -1.95 | high | neutral | False |  | 28 |
| final_price_signal_score_v2 | score_20_30 | 771 | 313 | 458 | 40.6 | 43.04 | -2.44 | high | neutral | False |  | 28 |
| news_risk_penalty | medium | 88 | 40 | 48 | 45.45 | 43.04 | 2.41 | low | neutral | False |  | 26 |
| attention_noise_penalty | high | 137 | 62 | 75 | 45.26 | 43.04 | 2.22 | medium | neutral | False |  | 20 |
| candidate_rank | rank_11_20 | 162 | 71 | 91 | 43.83 | 43.04 | 0.79 | medium | neutral | False |  | 21 |
| overextension_penalty | low | 131 | 56 | 75 | 42.75 | 43.04 | -0.29 | medium | neutral | False |  | 26 |
| final_price_signal_score_v2 | score_lt_20 | 205 | 87 | 118 | 42.44 | 43.04 | -0.6 | medium | neutral | False |  | 28 |
| news_risk_penalty | high | 124 | 52 | 72 | 41.94 | 43.04 | -1.1 | medium | neutral | False |  | 18 |
| candidate_rank | rank_21_50 | 221 | 89 | 132 | 40.27 | 43.04 | -2.77 | medium | neutral | False |  | 17 |
| attention_noise_penalty | low | 5 | 3 | 2 | 60.0 | 43.04 | 16.96 | insufficient | watch | True | large_lift_with_under_100_cases | 5 |
| news_risk_penalty | low | 19 | 10 | 9 | 52.63 | 43.04 | 9.59 | insufficient | watch | False |  | 10 |
| final_price_signal_score_v2 | score_40_50 | 20 | 9 | 11 | 45.0 | 43.04 | 1.96 | insufficient | watch | False |  | 4 |
| attention_noise_penalty | medium | 4 | 1 | 3 | 25.0 | 43.04 | -18.04 | insufficient | watch | True | large_lift_with_under_100_cases | 4 |