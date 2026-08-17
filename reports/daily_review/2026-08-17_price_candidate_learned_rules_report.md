# Price Candidate Learned Rules Report - 2026-08-17

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260817.csv`
- Baseline evaluated count: **2415**
- Baseline success rate: **41.9%**
- Total rule rows: **44**
- Boost rules: **20**
- Penalize rules: **9**
- Watch rules: **3**
- Suspicious rules: **5**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| candidate_rank | missing | 304 | 163 | 141 | 53.62 | 41.9 | 11.72 | high | boost | False |  | 6 |
| reversal_risk_penalty | high | 310 | 160 | 150 | 51.61 | 41.9 | 9.71 | high | boost | True | boost_on_semantically_risky_bucket | 18 |
| score_version | legacy_or_unknown | 378 | 194 | 184 | 51.32 | 41.9 | 9.42 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 378 | 194 | 184 | 51.32 | 41.9 | 9.42 | high | boost | False |  | 7 |
| overextension_penalty | missing | 378 | 194 | 184 | 51.32 | 41.9 | 9.42 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 378 | 194 | 184 | 51.32 | 41.9 | 9.42 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 378 | 194 | 184 | 51.32 | 41.9 | 9.42 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 378 | 194 | 184 | 51.32 | 41.9 | 9.42 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 378 | 194 | 184 | 51.32 | 41.9 | 9.42 | high | boost | False |  | 7 |
| liquidity_score | missing | 378 | 194 | 184 | 51.32 | 41.9 | 9.42 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | score_50_plus | 395 | 188 | 207 | 47.59 | 41.9 | 5.69 | high | boost | False |  | 18 |
| liquidity_score | confirmed | 643 | 300 | 343 | 46.66 | 41.9 | 4.76 | high | boost | False |  | 18 |
| news_risk_penalty | high | 54 | 28 | 26 | 51.85 | 41.9 | 9.95 | low | boost | True | boost_on_semantically_risky_bucket | 8 |
| news_risk_penalty | medium | 71 | 36 | 35 | 50.7 | 41.9 | 8.8 | low | boost | False |  | 18 |
| candidate_rank | rank_11_20 | 83 | 41 | 42 | 49.4 | 41.9 | 7.5 | low | boost | False |  | 10 |
| overextension_penalty | low | 91 | 43 | 48 | 47.25 | 41.9 | 5.35 | low | boost | False |  | 16 |
| candidate_rank | top_10 | 164 | 87 | 77 | 53.05 | 41.9 | 11.15 | medium | boost | False |  | 19 |
| selected_pick | selected | 247 | 128 | 119 | 51.82 | 41.9 | 9.92 | medium | boost | False |  | 19 |
| overextension_penalty | high | 269 | 133 | 136 | 49.44 | 41.9 | 7.54 | medium | boost | True | boost_on_semantically_risky_bucket | 18 |
| volume_confirmation_score | high | 154 | 76 | 78 | 49.35 | 41.9 | 7.45 | medium | boost | False |  | 17 |
| candidate_rank | rank_101_plus | 1299 | 500 | 799 | 38.49 | 41.9 | -3.41 | high | penalize | False |  | 18 |
| final_price_signal_score_v2 | score_30_40 | 889 | 342 | 547 | 38.47 | 41.9 | -3.43 | high | penalize | False |  | 18 |
| reversal_risk_penalty | none | 1059 | 403 | 656 | 38.05 | 41.9 | -3.85 | high | penalize | False |  | 18 |
| overextension_penalty | none | 1607 | 611 | 996 | 38.02 | 41.9 | -3.88 | high | penalize | False |  | 18 |
| final_price_signal_score_v2 | score_20_30 | 586 | 222 | 364 | 37.88 | 41.9 | -4.02 | high | penalize | False |  | 18 |
| candidate_rank | rank_51_100 | 397 | 147 | 250 | 37.03 | 41.9 | -4.87 | high | penalize | False |  | 13 |
| volume_confirmation_score | none | 503 | 184 | 319 | 36.58 | 41.9 | -5.32 | high | penalize | False |  | 18 |
| reversal_risk_penalty | low | 289 | 99 | 190 | 34.26 | 41.9 | -7.64 | medium | penalize | False |  | 18 |
| liquidity_score | none | 110 | 5 | 105 | 4.55 | 41.9 | -37.35 | medium | penalize | False |  | 18 |
| volume_confirmation_score | moderate | 319 | 134 | 185 | 42.01 | 41.9 | 0.11 | high | neutral | False |  | 18 |
| reversal_risk_penalty | medium | 379 | 156 | 223 | 41.16 | 41.9 | -0.74 | high | neutral | False |  | 18 |
| selected_pick | broad_pool | 2168 | 884 | 1284 | 40.77 | 41.9 | -1.13 | high | neutral | False |  | 25 |
| score_version | v2_conservative_ranker | 2037 | 818 | 1219 | 40.16 | 41.9 | -1.74 | high | neutral | False |  | 18 |
| attention_noise_penalty | none | 1961 | 786 | 1175 | 40.08 | 41.9 | -1.82 | high | neutral | False |  | 18 |
| volume_confirmation_score | negative | 1061 | 424 | 637 | 39.96 | 41.9 | -1.94 | high | neutral | False |  | 18 |
| liquidity_score | basic | 1284 | 513 | 771 | 39.95 | 41.9 | -1.95 | high | neutral | False |  | 18 |
| news_risk_penalty | none | 1890 | 741 | 1149 | 39.21 | 41.9 | -2.69 | high | neutral | False |  | 18 |
| overextension_penalty | medium | 70 | 31 | 39 | 44.29 | 41.9 | 2.39 | low | neutral | False |  | 15 |
| attention_noise_penalty | high | 67 | 29 | 38 | 43.28 | 41.9 | 1.38 | low | neutral | False |  | 14 |
| candidate_rank | rank_21_50 | 168 | 74 | 94 | 44.05 | 41.9 | 2.15 | medium | neutral | False |  | 9 |
| final_price_signal_score_v2 | score_lt_20 | 167 | 66 | 101 | 39.52 | 41.9 | -2.38 | medium | neutral | False |  | 18 |
| news_risk_penalty | low | 22 | 13 | 9 | 59.09 | 41.9 | 17.19 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| attention_noise_penalty | low | 6 | 3 | 3 | 50.0 | 41.9 | 8.1 | insufficient | watch | False |  | 4 |
| attention_noise_penalty | medium | 3 | 0 | 3 | 0.0 | 41.9 | -41.9 | insufficient | watch | True | large_lift_with_under_100_cases | 3 |