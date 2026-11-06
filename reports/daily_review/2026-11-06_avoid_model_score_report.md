# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-06 03:22:09

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=17310, success rate=50.78%
Candidates with avoid_model_score populated: N=2354

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 235 | 50.64% | 44.3 | 1701 | 49.09% | 46.7 |
| 20% | 471 | 49.47% | 45.0 | 3402 | 49.65% | 48.0 |
| 30% | 706 | 52.27% | 48.6 | 5103 | 49.66% | 48.3 |