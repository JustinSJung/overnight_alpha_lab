# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-26 05:04:45

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=25602, success rate=51.9%
Candidates with avoid_model_score populated: N=11254

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 1125 | 55.29% | 52.4 | 2541 | 49.82% | 47.9 |
| 20% | 2251 | 54.06% | 52.0 | 5083 | 50.9% | 49.5 |
| 30% | 3376 | 54.65% | 53.0 | 7624 | 50.93% | 49.8 |