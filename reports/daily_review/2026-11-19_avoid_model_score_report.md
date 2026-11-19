# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-19 04:23:49

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=22625, success rate=51.02%
Candidates with avoid_model_score populated: N=7625

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 762 | 54.72% | 51.2 | 2244 | 47.77% | 45.7 |
| 20% | 1525 | 52.72% | 50.2 | 4487 | 49.23% | 47.8 |
| 30% | 2288 | 53.45% | 51.4 | 6731 | 49.53% | 48.3 |