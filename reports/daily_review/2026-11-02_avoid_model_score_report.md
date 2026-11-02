# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-02 02:03:54

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=14476, success rate=49.9%
Candidates with avoid_model_score populated: N=60

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 6 | insufficient sample | 3.0 | 1419 | 45.24% | 42.7 |
| 20% | 12 | insufficient sample | 13.8 | 2838 | 46.09% | 44.3 |
| 30% | 18 | insufficient sample | 9.0 | 4258 | 46.48% | 45.0 |