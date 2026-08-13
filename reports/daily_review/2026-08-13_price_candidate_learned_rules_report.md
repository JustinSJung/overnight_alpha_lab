# Price Candidate Learned Rules Report - 2026-08-13

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20260813.csv`
- Baseline evaluated count: **2321**
- Baseline success rate: **42.09%**
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
| candidate_rank | missing | 301 | 161 | 140 | 53.49 | 42.09 | 11.4 | high | boost | False |  | 6 |
| score_version | legacy_or_unknown | 375 | 192 | 183 | 51.2 | 42.09 | 9.11 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | missing | 375 | 192 | 183 | 51.2 | 42.09 | 9.11 | high | boost | False |  | 7 |
| overextension_penalty | missing | 375 | 192 | 183 | 51.2 | 42.09 | 9.11 | high | boost | False |  | 7 |
| reversal_risk_penalty | missing | 375 | 192 | 183 | 51.2 | 42.09 | 9.11 | high | boost | False |  | 7 |
| news_risk_penalty | missing | 375 | 192 | 183 | 51.2 | 42.09 | 9.11 | high | boost | False |  | 7 |
| attention_noise_penalty | missing | 375 | 192 | 183 | 51.2 | 42.09 | 9.11 | high | boost | False |  | 7 |
| volume_confirmation_score | missing | 375 | 192 | 183 | 51.2 | 42.09 | 9.11 | high | boost | False |  | 7 |
| liquidity_score | missing | 375 | 192 | 183 | 51.2 | 42.09 | 9.11 | high | boost | False |  | 7 |
| final_price_signal_score_v2 | score_50_plus | 356 | 172 | 184 | 48.31 | 42.09 | 6.22 | high | boost | False |  | 17 |
| liquidity_score | confirmed | 599 | 280 | 319 | 46.74 | 42.09 | 4.65 | high | boost | False |  | 17 |
| news_risk_penalty | high | 51 | 28 | 23 | 54.9 | 42.09 | 12.81 | low | boost | True | boost_on_semantically_risky_bucket; large_lift_with_under_100_cases | 7 |
| news_risk_penalty | medium | 66 | 33 | 33 | 50.0 | 42.09 | 7.91 | low | boost | False |  | 17 |
| candidate_rank | rank_11_20 | 73 | 35 | 38 | 47.95 | 42.09 | 5.86 | low | boost | False |  | 9 |
| overextension_penalty | low | 85 | 39 | 46 | 45.88 | 42.09 | 3.79 | low | boost | False |  | 15 |
| candidate_rank | top_10 | 154 | 85 | 69 | 55.19 | 42.09 | 13.1 | medium | boost | False |  | 18 |
| selected_pick | selected | 227 | 120 | 107 | 52.86 | 42.09 | 10.77 | medium | boost | False |  | 18 |
| reversal_risk_penalty | high | 295 | 154 | 141 | 52.2 | 42.09 | 10.11 | medium | boost | True | boost_on_semantically_risky_bucket | 17 |
| volume_confirmation_score | high | 138 | 70 | 68 | 50.72 | 42.09 | 8.63 | medium | boost | False |  | 16 |
| overextension_penalty | high | 256 | 128 | 128 | 50.0 | 42.09 | 7.91 | medium | boost | True | boost_on_semantically_risky_bucket | 17 |
| candidate_rank | rank_101_plus | 1247 | 483 | 764 | 38.73 | 42.09 | -3.36 | high | penalize | False |  | 17 |
| final_price_signal_score_v2 | score_30_40 | 855 | 331 | 524 | 38.71 | 42.09 | -3.38 | high | penalize | False |  | 17 |
| overextension_penalty | none | 1538 | 588 | 950 | 38.23 | 42.09 | -3.86 | high | penalize | False |  | 17 |
| final_price_signal_score_v2 | score_20_30 | 572 | 218 | 354 | 38.11 | 42.09 | -3.98 | high | penalize | False |  | 17 |
| reversal_risk_penalty | none | 1010 | 384 | 626 | 38.02 | 42.09 | -4.07 | high | penalize | False |  | 17 |
| candidate_rank | rank_51_100 | 397 | 147 | 250 | 37.03 | 42.09 | -5.06 | high | penalize | False |  | 13 |
| volume_confirmation_score | none | 475 | 171 | 304 | 36.0 | 42.09 | -6.09 | high | penalize | False |  | 17 |
| reversal_risk_penalty | low | 278 | 98 | 180 | 35.25 | 42.09 | -6.84 | medium | penalize | False |  | 17 |
| liquidity_score | none | 103 | 3 | 100 | 2.91 | 42.09 | -39.18 | medium | penalize | False |  | 17 |
| volume_confirmation_score | moderate | 301 | 127 | 174 | 42.19 | 42.09 | 0.1 | high | neutral | False |  | 17 |
| reversal_risk_penalty | medium | 363 | 149 | 214 | 41.05 | 42.09 | -1.04 | high | neutral | False |  | 17 |
| selected_pick | broad_pool | 2094 | 857 | 1237 | 40.93 | 42.09 | -1.16 | high | neutral | False |  | 24 |
| volume_confirmation_score | negative | 1032 | 417 | 615 | 40.41 | 42.09 | -1.68 | high | neutral | False |  | 17 |
| liquidity_score | basic | 1244 | 502 | 742 | 40.35 | 42.09 | -1.74 | high | neutral | False |  | 17 |
| score_version | v2_conservative_ranker | 1946 | 785 | 1161 | 40.34 | 42.09 | -1.75 | high | neutral | False |  | 17 |
| attention_noise_penalty | none | 1872 | 754 | 1118 | 40.28 | 42.09 | -1.81 | high | neutral | False |  | 17 |
| news_risk_penalty | none | 1807 | 711 | 1096 | 39.35 | 42.09 | -2.74 | high | neutral | False |  | 17 |
| overextension_penalty | medium | 67 | 30 | 37 | 44.78 | 42.09 | 2.69 | low | neutral | False |  | 14 |
| attention_noise_penalty | high | 65 | 28 | 37 | 43.08 | 42.09 | 0.99 | low | neutral | False |  | 13 |
| candidate_rank | rank_21_50 | 149 | 66 | 83 | 44.3 | 42.09 | 2.21 | medium | neutral | False |  | 8 |
| final_price_signal_score_v2 | score_lt_20 | 163 | 64 | 99 | 39.26 | 42.09 | -2.83 | medium | neutral | False |  | 17 |
| news_risk_penalty | low | 22 | 13 | 9 | 59.09 | 42.09 | 17.0 | insufficient | watch | True | large_lift_with_under_100_cases | 10 |
| attention_noise_penalty | low | 6 | 3 | 3 | 50.0 | 42.09 | 7.91 | insufficient | watch | False |  | 4 |
| attention_noise_penalty | medium | 3 | 0 | 3 | 0.0 | 42.09 | -42.09 | insufficient | watch | True | large_lift_with_under_100_cases | 3 |