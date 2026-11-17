# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-17 05:41:19

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=21785, success rate=50.99%
Candidates with avoid_model_score populated: N=6821

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 682 | 53.52% | 49.8 | 2153 | 47.56% | 45.5 |
| 20% | 1364 | 51.47% | 48.8 | 4306 | 49.33% | 47.8 |
| 30% | 2046 | 52.93% | 50.8 | 6460 | 49.55% | 48.3 |