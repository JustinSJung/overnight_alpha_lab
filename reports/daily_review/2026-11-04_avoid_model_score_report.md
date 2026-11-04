# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-04 02:55:06

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=16354, success rate=50.26%
Candidates with avoid_model_score populated: N=1183

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 118 | 46.61% | 37.9 | 1605 | 47.66% | 45.2 |
| 20% | 237 | 48.52% | 42.2 | 3210 | 47.73% | 46.0 |
| 30% | 355 | 53.24% | 48.0 | 4816 | 47.78% | 46.4 |