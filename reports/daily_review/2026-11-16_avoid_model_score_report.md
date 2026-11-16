# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-16 02:55:12

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=21369, success rate=50.26%
Candidates with avoid_model_score populated: N=6344

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 634 | 51.1% | 47.2 | 2112 | 47.59% | 45.5 |
| 20% | 1269 | 49.49% | 46.7 | 4224 | 48.96% | 47.5 |
| 30% | 1903 | 50.6% | 48.4 | 6336 | 49.13% | 47.9 |