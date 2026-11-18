# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-18 04:52:54

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=22107, success rate=51.26%
Candidates with avoid_model_score populated: N=7157

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 716 | 54.33% | 50.7 | 2185 | 48.01% | 45.9 |
| 20% | 1431 | 53.18% | 50.6 | 4371 | 49.55% | 48.1 |
| 30% | 2147 | 54.22% | 52.1 | 6556 | 49.66% | 48.5 |