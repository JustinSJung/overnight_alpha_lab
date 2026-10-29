# Supervised Price Forecast Model

Target: close_t_plus_horizon / signal_close - 1 > cost_assumption

Classifier: logistic_regression

## Time-separated validation

| Partition | Rows | Signal start | Signal end | Latest label available |
|---|---:|---|---|---|
| train | 13604 | 2023-02-01 | 2025-02-05 | 2025-02-12 |
| calibration | 4493 | 2025-02-13 | 2025-10-10 | 2025-10-17 |
| test | 4778 | 2025-10-20 | 2026-06-23 | 2026-06-30 |

Labels crossing the next partition boundary are purged. Classifier selection uses only purged expanding folds within training. Probability calibration uses only the middle period. Final test labels do not choose models or thresholds.

## Held-out results

| Metric | Value |
|---|---:|
| evaluated_rows | 4778 |
| signal_dates | 166 |
| base_rate | 0.4506069485140226 |
| accuracy_at_half | 0.5493930514859774 |
| majority_class_accuracy | 0.5493930514859774 |
| balanced_accuracy | 0.5 |
| roc_auc | 0.5275404861433659 |
| brier_score | 0.24764205420815733 |
| baseline_brier_score | 0.24769646171014484 |
| return_mae | 0.06575088084467695 |
| selected_count | 0 |
| selected_dates | 0 |
| selected_success_rate | None |
| selected_mean_net_return_proxy | None |
| selected_daily_mean_net_return_proxy | None |
| selected_daily_return_lower_95 | None |
| recommendation_gate_passed | False |
| baseline_return_mae | 0.06472127967772402 |

History provenance: {
  "source": "kis_adjusted_daily",
  "retrieved_at": "2026-10-20T09:20:39.616115+00:00",
  "scope": "pilot",
  "stocks": 30,
  "historical_limitations": "Current observed universe and retrospectively adjusted prices; not a survivorship-free point-in-time universe."
}


Recommendation gate reasons: insufficient_fixed_policy_selection_history, selected_precision_lift_below_3_percentage_points, positive_daily_return_edge_not_established, return_forecast_does_not_beat_training_median, pilot_universe_not_production_validated

Probabilities are calibrated model estimates, not guaranteed hit rates. Return predictions are point estimates. Neither is the legacy dashboard Wilson score.

Close-to-close research target; not an executable next-open trading return.
Historical collected universe; not a survivorship-free whole-market backtest.

Five-session outcomes and stocks on the same date overlap. Daily return uncertainty uses five-day block resampling; individual-stock sample counts are not independent trial counts.

Source ref: kis_completed_history_pilot_protocol_v1
Dataset SHA256: 7897fc6c4bd4faf27764ae1ccbb5f182dd1e24667da05f7cb2ea27a5cd87ad2c
