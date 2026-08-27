# Price Candidate Learned Rules Report - 2026-08-27

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260827.csv`
- Baseline evaluated count: **3553**
- Baseline success rate: **42.08%**
- Total rule rows: **44**
- Boost rules: **17**
- Penalize rules: **6**
- Watch rules: **3**
- Suspicious rules: **4**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 441 | 236 | 205 | 53.51 | 42.08 | 11.43 | high | boost | True | boost_on_semantically_risky_bucket | 25 |
| candidate_rank | missing | 307 | 161 | 146 | 52.44 | 42.08 | 10.36 | high | boost | False |  | 6 |
| overextension_penalty | high | 380 | 194 | 186 | 51.05 | 42.08 | 8.97 | high | boost | True | boost_on_semantically_risky_bucket | 25 |
| score_version | legacy_or_unknown | 380 | 192 | 188 | 50.53 | 42.08 | 8.45 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 380 | 192 | 188 | 50.53 | 42.08 | 8.45 | high | boost | False |  | 7 |
| overextension_penalty | missing | 380 | 192 | 188 | 50.53 | 42.08 | 8.45 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 380 | 192 | 188 | 50.53 | 42.08 | 8.45 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 380 | 192 | 188 | 50.53 | 42.08 | 8.45 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 380 | 192 | 188 | 50.53 | 42.08 | 8.45 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 380 | 192 | 188 | 50.53 | 42.08 | 8.45 | high | boost | False |  | 7 |
| liquidity_score | missing | 380 | 192 | 188 | 50.53 | 42.08 | 8.45 | high | boost | False |  | 7 |
| selected_pick | selected | 399 | 187 | 212 | 46.87 | 42.08 | 4.79 | high | boost | False |  | 26 |
| liquidity_score | confirmed | 965 | 445 | 520 | 46.11 | 42.08 | 4.03 | high | boost | False |  | 25 |
| reversal_risk_penalty | medium | 588 | 267 | 321 | 45.41 | 42.08 | 3.33 | high | boost | False |  | 25 |
| candidate_rank | rank_11_20 | 155 | 73 | 82 | 47.1 | 42.08 | 5.02 | medium | boost | False |  | 17 |
| candidate_rank | top_10 | 244 | 114 | 130 | 46.72 | 42.08 | 4.64 | medium | boost | False |  | 26 |
| volume_confirmation_score | high | 219 | 101 | 118 | 46.12 | 42.08 | 4.04 | medium | boost | False |  | 24 |
| reversal_risk_penalty | none | 1630 | 610 | 1020 | 37.42 | 42.08 | -4.66 | high | penalize | False |  | 25 |
| reversal_risk_penalty | low | 514 | 190 | 324 | 36.96 | 42.08 | -5.12 | high | penalize | False |  | 25 |
| volume_confirmation_score | none | 780 | 286 | 494 | 36.67 | 42.08 | -5.41 | high | penalize | False |  | 25 |
| candidate_rank | rank_51_100 | 402 | 146 | 256 | 36.32 | 42.08 | -5.76 | high | penalize | False |  | 14 |
| candidate_rank | rank_21_50 | 233 | 84 | 149 | 36.05 | 42.08 | -6.03 | medium | penalize | False |  | 13 |
| liquidity_score | none | 174 | 6 | 168 | 3.45 | 42.08 | -38.63 | medium | penalize | False |  | 25 |
| volume_confirmation_score | negative | 1700 | 720 | 980 | 42.35 | 42.08 | 0.27 | high | neutral | False |  | 25 |
| liquidity_score | basic | 2034 | 852 | 1182 | 41.89 | 42.08 | -0.19 | high | neutral | False |  | 25 |
| final_price_signal_score_v2 | score_30_40 | 1501 | 626 | 875 | 41.71 | 42.08 | -0.37 | high | neutral | False |  | 25 |
| selected_pick | broad_pool | 3154 | 1308 | 1846 | 41.47 | 42.08 | -0.61 | high | neutral | False |  | 32 |
| candidate_rank | rank_101_plus | 2212 | 917 | 1295 | 41.46 | 42.08 | -0.62 | high | neutral | False |  | 25 |
| final_price_signal_score_v2 | score_50_plus | 621 | 257 | 364 | 41.38 | 42.08 | -0.7 | high | neutral | False |  | 25 |
| volume_confirmation_score | moderate | 474 | 196 | 278 | 41.35 | 42.08 | -0.73 | high | neutral | False |  | 25 |
| score_version | v2_conservative_ranker | 3173 | 1303 | 1870 | 41.07 | 42.08 | -1.01 | high | neutral | False |  | 25 |
| attention_noise_penalty | none | 3052 | 1251 | 1801 | 40.99 | 42.08 | -1.09 | high | neutral | False |  | 25 |
| news_risk_penalty | none | 2949 | 1202 | 1747 | 40.76 | 42.08 | -1.32 | high | neutral | False |  | 25 |
| overextension_penalty | none | 2558 | 1012 | 1546 | 39.56 | 42.08 | -2.52 | high | neutral | False |  | 25 |
| final_price_signal_score_v2 | score_20_30 | 831 | 328 | 503 | 39.47 | 42.08 | -2.61 | high | neutral | False |  | 25 |
| news_risk_penalty | medium | 91 | 41 | 50 | 45.05 | 42.08 | 2.97 | low | neutral | False |  | 24 |
| attention_noise_penalty | high | 111 | 48 | 63 | 43.24 | 42.08 | 1.16 | medium | neutral | False |  | 19 |
| news_risk_penalty | high | 111 | 47 | 64 | 42.34 | 42.08 | 0.26 | medium | neutral | False |  | 15 |
| overextension_penalty | low | 128 | 54 | 74 | 42.19 | 42.08 | 0.11 | medium | neutral | False |  | 23 |
| final_price_signal_score_v2 | score_lt_20 | 220 | 92 | 128 | 41.82 | 42.08 | -0.26 | medium | neutral | False |  | 25 |
| overextension_penalty | medium | 107 | 43 | 64 | 40.19 | 42.08 | -1.89 | medium | neutral | False |  | 22 |
| news_risk_penalty | low | 22 | 13 | 9 | 59.09 | 42.08 | 17.01 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| attention_noise_penalty | low | 6 | 3 | 3 | 50.0 | 42.08 | 7.92 | insufficient | watch | False |  | 4 |
| attention_noise_penalty | medium | 4 | 1 | 3 | 25.0 | 42.08 | -17.08 | insufficient | watch | True | large_lift_with_under_100_cases | 4 |