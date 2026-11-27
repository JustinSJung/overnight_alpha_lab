# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-27 05:34:31

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=26101, success rate=51.55%
Candidates with avoid_model_score populated: N=11927

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 1193 | 54.4% | 51.6 | 2591 | 48.67% | 46.7 |
| 20% | 2385 | 53.29% | 51.3 | 5182 | 50.08% | 48.7 |
| 30% | 3578 | 53.77% | 52.1 | 7774 | 50.39% | 49.3 |