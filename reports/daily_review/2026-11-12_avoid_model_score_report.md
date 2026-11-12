# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-12 03:56:49

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=20096, success rate=49.64%
Candidates with avoid_model_score populated: N=5107

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 511 | 48.53% | 44.2 | 1980 | 46.31% | 44.1 |
| 20% | 1021 | 46.82% | 43.8 | 3959 | 47.56% | 46.0 |
| 30% | 1532 | 47.78% | 45.3 | 5938 | 47.81% | 46.5 |