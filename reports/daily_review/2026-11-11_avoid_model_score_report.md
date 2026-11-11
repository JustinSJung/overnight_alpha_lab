# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-11 06:04:32

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=19372, success rate=50.88%
Candidates with avoid_model_score populated: N=4373

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 437 | 51.95% | 47.3 | 1908 | 49.06% | 46.8 |
| 20% | 875 | 50.17% | 46.9 | 3816 | 50.0% | 48.4 |
| 30% | 1312 | 51.07% | 48.4 | 5723 | 50.1% | 48.8 |