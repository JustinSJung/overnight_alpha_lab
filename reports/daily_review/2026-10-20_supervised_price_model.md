# Supervised Price Forecast Model

Target: close_t_plus_horizon / signal_close - 1 > cost_assumption

Classifier: logistic_regression

## Time-separated validation

| Partition | Rows | Signal start | Signal end | Latest label available |
|---|---:|---|---|---|
| train | 4310 | 2026-07-07 | 2026-08-20 | 2026-08-28 |
| calibration | 3737 | 2026-08-31 | 2026-09-11 | 2026-09-21 |
| test | 7806 | 2026-09-22 | 2026-10-13 | 2026-10-20 |

Labels crossing the next partition boundary are purged. Classifier selection uses only purged expanding folds within training. Probability calibration uses only the middle period. Final test labels do not choose models or thresholds.

## Held-out results

| Metric | Value |
|---|---:|
| evaluated_rows | 7806 |
| signal_dates | 11 |
| base_rate | 0.3403791954906482 |
| accuracy_at_half | 0.6596208045093518 |
| majority_class_accuracy | 0.6596208045093518 |
| balanced_accuracy | 0.5 |
| roc_auc | 0.4873807579666035 |
| brier_score | 0.2279286940525796 |
| baseline_brier_score | 0.2278931793552481 |
| return_mae | 0.07909776281171337 |
| selected_count | 0 |
| selected_dates | 0 |
| selected_success_rate | None |
| selected_mean_net_return_proxy | None |
| selected_daily_mean_net_return_proxy | None |
| selected_daily_return_lower_95 | None |
| recommendation_gate_passed | False |
| baseline_return_mae | 0.07494117423570866 |

Recommendation gate reasons: fewer_than_20_test_signal_dates, insufficient_fixed_policy_selection_history, weak_out_of_time_discrimination, probabilities_do_not_beat_constant_baseline, selected_precision_lift_below_3_percentage_points, positive_daily_return_edge_not_established, return_forecast_does_not_beat_training_median

Probabilities are calibrated model estimates, not guaranteed hit rates. Return predictions are point estimates. Neither is the legacy dashboard Wilson score.

Close-to-close research target; not an executable next-open trading return.
Historical collected universe; not a survivorship-free whole-market backtest.

Five-session outcomes and stocks on the same date overlap. Daily return uncertainty uses five-day block resampling; individual-stock sample counts are not independent trial counts.

Source ref: 51e4efa9337f6ffb84c09695c8438f19ba7f364e
Dataset SHA256: bf107d3a548865de5474f2a5040264c8bf11ff73f9af1ae8256389aa314fb1c7
