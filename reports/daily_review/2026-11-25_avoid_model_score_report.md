# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-25 05:32:45

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=24961, success rate=51.42%
Candidates with avoid_model_score populated: N=10477

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 1048 | 54.48% | 51.5 | 2477 | 48.45% | 46.5 |
| 20% | 2095 | 52.89% | 50.7 | 4954 | 49.62% | 48.2 |
| 30% | 3143 | 54.06% | 52.3 | 7432 | 49.92% | 48.8 |