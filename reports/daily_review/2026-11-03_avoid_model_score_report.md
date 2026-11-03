# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-03 04:10:19

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=15732, success rate=49.1%
Candidates with avoid_model_score populated: N=619

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 62 | 25.81% | 16.6 | 1544 | 45.4% | 42.9 |
| 20% | 124 | 25.81% | 18.9 | 3087 | 45.93% | 44.2 |
| 30% | 186 | 31.18% | 25.0 | 4631 | 45.93% | 44.5 |