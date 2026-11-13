# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-13 04:22:50

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=20522, success rate=50.24%
Candidates with avoid_model_score populated: N=5771

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 577 | 50.78% | 46.7 | 2023 | 46.91% | 44.7 |
| 20% | 1154 | 48.01% | 45.1 | 4046 | 48.52% | 47.0 |
| 30% | 1731 | 49.68% | 47.3 | 6069 | 48.74% | 47.5 |