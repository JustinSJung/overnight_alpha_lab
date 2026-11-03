# Price Candidate Learned Rules Report - 2026-11-03

This report learns diagnostic groups from deduped KIS price-candidate evaluations. It does not change score weights or place trades.

## Summary

- Source CSV: `data/processed/price_candidate_learned_rules_20261103.csv`
- Baseline evaluated count: **17672**
- Baseline success rate: **48.23%**
- Total rule rows: **45**
- Boost rules: **3**
- Penalize rules: **12**
- Watch rules: **2**
- Suspicious rules: **4**

Conservative activation uses at least 50 evaluated rows and +/-3 percentage points lift versus baseline.
Suspicious rules are diagnostic only and are not applied to scoring.

## Learned Rule Table

| rule_group | rule_value | evaluated_count | success_count | failure_count | success_rate | baseline_success_rate | lift_vs_baseline | confidence_level | recommended_action | suspicious_flag | suspicious_reason | date_coverage_count |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| reversal_risk_penalty | high | 891 | 463 | 428 | 51.96 | 48.23 | 3.73 | high | boost | True | boost_on_semantically_risky_bucket | 63 |
| overextension_penalty | high | 1132 | 583 | 549 | 51.5 | 48.23 | 3.27 | high | boost | True | boost_on_semantically_risky_bucket | 63 |
| attention_noise_penalty | low | 69 | 41 | 28 | 59.42 | 48.23 | 11.19 | low | boost | True | large_lift_with_under_100_cases | 30 |
| candidate_rank | rank_11_20 | 425 | 191 | 234 | 44.94 | 48.23 | -3.29 | high | penalize | False |  | 55 |
| reversal_risk_penalty | low | 1572 | 706 | 866 | 44.91 | 48.23 | -3.32 | high | penalize | False |  | 64 |
| selected_pick | selected | 980 | 435 | 545 | 44.39 | 48.23 | -3.84 | high | penalize | False |  | 65 |
| candidate_rank | top_10 | 555 | 244 | 311 | 43.96 | 48.23 | -4.27 | high | penalize | False |  | 64 |
| volume_confirmation_score | moderate | 1042 | 452 | 590 | 43.38 | 48.23 | -4.85 | high | penalize | False |  | 64 |
| overextension_penalty | low | 348 | 149 | 199 | 42.82 | 48.23 | -5.41 | high | penalize | False |  | 61 |
| final_price_signal_score_v2 | score_50_plus | 1876 | 798 | 1078 | 42.54 | 48.23 | -5.69 | high | penalize | False |  | 64 |
| candidate_rank | rank_21_50 | 560 | 237 | 323 | 42.32 | 48.23 | -5.91 | high | penalize | False |  | 43 |
| candidate_rank | rank_51_100 | 550 | 206 | 344 | 37.45 | 48.23 | -10.78 | high | penalize | False |  | 25 |
| volume_confirmation_score | none | 1952 | 683 | 1269 | 34.99 | 48.23 | -13.24 | high | penalize | False |  | 64 |
| liquidity_score | none | 560 | 25 | 535 | 4.46 | 48.23 | -43.77 | high | penalize | False |  | 64 |
| news_risk_penalty | medium | 156 | 68 | 88 | 43.59 | 48.23 | -4.64 | medium | penalize | False |  | 56 |
| volume_confirmation_score | negative | 13752 | 6950 | 6802 | 50.54 | 48.23 | 2.31 | high | neutral | False |  | 64 |
| final_price_signal_score_v2 | score_30_40 | 10233 | 5156 | 5077 | 50.39 | 48.23 | 2.16 | high | neutral | False |  | 64 |
| liquidity_score | basic | 14538 | 7293 | 7245 | 50.17 | 48.23 | 1.94 | high | neutral | False |  | 64 |
| candidate_rank | missing | 335 | 168 | 167 | 50.15 | 48.23 | 1.92 | high | neutral | False |  | 6 |
| reversal_risk_penalty | medium | 1728 | 857 | 871 | 49.59 | 48.23 | 1.36 | high | neutral | False |  | 64 |
| candidate_rank | rank_101_plus | 15247 | 7478 | 7769 | 49.05 | 48.23 | 0.82 | high | neutral | False |  | 64 |
| score_version | legacy_or_unknown | 401 | 196 | 205 | 48.88 | 48.23 | 0.65 | high | neutral | False |  | 7 |
| final_price_signal_score_v2 | missing | 401 | 196 | 205 | 48.88 | 48.23 | 0.65 | high | neutral | False |  | 7 |
| overextension_penalty | missing | 401 | 196 | 205 | 48.88 | 48.23 | 0.65 | high | neutral | False |  | 7 |
| reversal_risk_penalty | missing | 401 | 196 | 205 | 48.88 | 48.23 | 0.65 | high | neutral | False |  | 7 |
| news_risk_penalty | missing | 401 | 196 | 205 | 48.88 | 48.23 | 0.65 | high | neutral | False |  | 7 |
| attention_noise_penalty | missing | 401 | 196 | 205 | 48.88 | 48.23 | 0.65 | high | neutral | False |  | 7 |
| volume_confirmation_score | missing | 401 | 196 | 205 | 48.88 | 48.23 | 0.65 | high | neutral | False |  | 7 |
| liquidity_score | missing | 401 | 196 | 205 | 48.88 | 48.23 | 0.65 | high | neutral | False |  | 7 |
| selected_pick | broad_pool | 16692 | 8089 | 8603 | 48.46 | 48.23 | 0.23 | high | neutral | False |  | 71 |
| news_risk_penalty | none | 16825 | 8126 | 8699 | 48.3 | 48.23 | 0.07 | high | neutral | False |  | 64 |
| score_version | v2_conservative_ranker | 17271 | 8328 | 8943 | 48.22 | 48.23 | -0.01 | high | neutral | False |  | 64 |
| attention_noise_penalty | none | 16443 | 7927 | 8516 | 48.21 | 48.23 | -0.02 | high | neutral | False |  | 64 |
| reversal_risk_penalty | none | 13080 | 6302 | 6778 | 48.18 | 48.23 | -0.05 | high | neutral | False |  | 64 |
| overextension_penalty | none | 15523 | 7467 | 8056 | 48.1 | 48.23 | -0.13 | high | neutral | False |  | 64 |
| attention_noise_penalty | high | 734 | 345 | 389 | 47.0 | 48.23 | -1.23 | high | neutral | False |  | 52 |
| final_price_signal_score_v2 | score_lt_20 | 534 | 250 | 284 | 46.82 | 48.23 | -1.41 | high | neutral | False |  | 63 |
| liquidity_score | confirmed | 2173 | 1010 | 1163 | 46.48 | 48.23 | -1.75 | high | neutral | False |  | 64 |
| volume_confirmation_score | high | 525 | 243 | 282 | 46.29 | 48.23 | -1.94 | high | neutral | False |  | 61 |
| final_price_signal_score_v2 | score_40_50 | 318 | 147 | 171 | 46.23 | 48.23 | -2.0 | high | neutral | False |  | 9 |
| final_price_signal_score_v2 | score_20_30 | 4310 | 1977 | 2333 | 45.87 | 48.23 | -2.36 | high | neutral | False |  | 64 |
| overextension_penalty | medium | 268 | 129 | 139 | 48.13 | 48.23 | -0.1 | medium | neutral | False |  | 59 |
| news_risk_penalty | high | 271 | 123 | 148 | 45.39 | 48.23 | -2.84 | medium | neutral | False |  | 51 |
| attention_noise_penalty | medium | 25 | 15 | 10 | 60.0 | 48.23 | 11.77 | insufficient | watch | True | large_lift_with_under_100_cases | 16 |
| news_risk_penalty | low | 19 | 11 | 8 | 57.89 | 48.23 | 9.66 | insufficient | watch | False |  | 10 |