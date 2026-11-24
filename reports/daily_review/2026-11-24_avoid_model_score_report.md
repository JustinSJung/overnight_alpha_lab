# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-24 06:56:49

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=23912, success rate=52.47%
Candidates with avoid_model_score populated: N=9735

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 974 | 56.78% | 53.6 | 2372 | 49.87% | 47.9 |
| 20% | 1947 | 55.06% | 52.8 | 4745 | 51.32% | 49.9 |
| 30% | 2920 | 55.82% | 54.0 | 7117 | 51.52% | 50.4 |