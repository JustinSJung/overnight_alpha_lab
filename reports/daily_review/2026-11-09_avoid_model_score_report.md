# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-09 02:29:43

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=18068, success rate=51.98%
Candidates with avoid_model_score populated: N=3025

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 302 | 59.27% | 53.6 | 1777 | 50.37% | 48.0 |
| 20% | 605 | 59.01% | 55.0 | 3555 | 51.53% | 49.9 |
| 30% | 908 | 59.03% | 55.8 | 5332 | 51.46% | 50.1 |