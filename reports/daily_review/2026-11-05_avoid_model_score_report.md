# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-05 03:24:02

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=17032, success rate=49.71%
Candidates with avoid_model_score populated: N=1677

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 168 | 44.64% | 37.3 | 1673 | 46.8% | 44.4 |
| 20% | 335 | 43.28% | 38.1 | 3346 | 47.4% | 45.7 |
| 30% | 503 | 45.92% | 41.6 | 5019 | 47.46% | 46.1 |