# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-23 03:35:29

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=23485, success rate=51.64%
Candidates with avoid_model_score populated: N=9063

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 906 | 56.51% | 53.3 | 2330 | 48.93% | 46.9 |
| 20% | 1813 | 53.89% | 51.6 | 4659 | 50.23% | 48.8 |
| 30% | 2719 | 54.62% | 52.7 | 6989 | 50.71% | 49.5 |