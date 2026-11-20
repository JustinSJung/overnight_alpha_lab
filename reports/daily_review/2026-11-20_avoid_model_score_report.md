# AVOID Model Score Report (diagnostic only)

Generated at: 2026-11-20 04:04:34

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=23018, success rate=50.54%
Candidates with avoid_model_score populated: N=8320

| Top % | Model N | Model success rate | Model Wilson | v2 raw N | v2 raw success rate | v2 raw Wilson |
|---|---|---|---|---|---|---|
| 10% | 832 | 53.61% | 50.2 | 2283 | 48.01% | 46.0 |
| 20% | 1664 | 51.38% | 49.0 | 4566 | 48.93% | 47.5 |
| 30% | 2496 | 52.36% | 50.4 | 6849 | 49.07% | 47.9 |