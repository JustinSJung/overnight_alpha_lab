# AVOID Model Score Report (diagnostic only)

Generated at: 2026-10-30 02:34:04

Compares avoid_lr_model_v1 (logistic regression, trained on first-snapshot features, diagnostic only) against the existing final_price_signal_score_v2, on AVOID-direction candidates whose outcome has already resolved. Does not affect candidate_action, final_price_signal_score, or selected_pick.

Overall AVOID evaluated pool: N=15024, success rate=50.23%
Candidates with avoid_model_score populated: N=0

**Fewer than 20 evaluated candidates have avoid_model_score so far.** The model was only added to candidate generation recently; T+1 outcomes take at least one more trading day to resolve, so this comparison is not yet meaningful with live data. Check back after upcoming daily runs.