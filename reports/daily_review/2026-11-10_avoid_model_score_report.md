# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-10 05:38:27

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=18647, success rate=52.0%
Candidates with avoid_model_score populated: N=3700

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 370 | 58.38% | 53.3 | 1835 | 49.97% | 47.7 |
| 20% | 740 | 57.7% | 54.1 | 3670 | 51.28% | 49.7 |
| 30% | 1110 | 58.11% | 55.2 | 5504 | 51.51% | 50.2 |