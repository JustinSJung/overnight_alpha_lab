# Supervised Price Forecast Model

Target: close_t_plus_horizon / signal_close - 1 > cost_assumption

Classifier: hist_gradient_boosting

## Time-separated validation

| Partition | Rows | Signal start | Signal end | Latest label available |
|---|---:|---|---|---|
| train | 398764 | 2023-02-01 | 2025-02-05 | 2025-02-12 |
| calibration | 137002 | 2025-02-13 | 2025-10-10 | 2025-10-17 |
| test | 141304 | 2025-10-20 | 2026-06-23 | 2026-06-30 |

Labels crossing the next partition boundary are purged. Classifier selection uses only purged expanding folds within training. Probability calibration uses only the middle period. Final test labels do not choose models or thresholds.

## Held-out results

| Metric | Value |
|---|---:|
| evaluated_rows | 141304 |
| signal_dates | 166 |
| base_rate | 0.4209788824095567 |
| accuracy_at_half | 0.5708401743758138 |
| majority_class_accuracy | 0.5790211175904433 |
| balanced_accuracy | 0.5060584461102977 |
| roc_auc | 0.515569002515538 |
| brier_score | 0.2443146606151731 |
| baseline_brier_score | 0.24397113575735196 |
| return_mae | 0.06875559832905402 |
| selected_count | 1081 |
| selected_dates | 105 |
| selected_success_rate | 0.6827012025901943 |
| selected_mean_net_return_proxy | 0.04760119967720476 |
| selected_daily_mean_net_return_proxy | -0.004392426209274806 |
| selected_daily_return_lower_95 | -0.029619819607526035 |
| recommendation_gate_passed | False |
| baseline_return_mae | 0.06901200528093901 |

History provenance: {
  "source": "kis_adjusted_daily",
  "retrieved_at": "2026-10-21T00:53:54.685833+00:00",
  "scope": "expanded_current_universe_research",
  "stocks": 901,
  "historical_limitations": "Current observed universe and retrospectively adjusted prices; not a survivorship-free point-in-time universe.",
  "requested_stocks": 901,
  "failed_stocks": 0,
  "unreadable_stocks": 0
}


Recommendation gate reasons: weak_out_of_time_discrimination, probabilities_do_not_beat_constant_baseline, positive_daily_return_edge_not_established, reconstructed_history_requires_forward_validation

Probabilities are calibrated model estimates, not guaranteed hit rates. Return predictions are point estimates. Neither is the legacy dashboard Wilson score.

Close-to-close research target; not an executable next-open trading return.
Historical collected universe; not a survivorship-free whole-market backtest.

Five-session outcomes and stocks on the same date overlap. Daily return uncertainty uses five-day block resampling; individual-stock sample counts are not independent trial counts.

Source ref: expanded_current_universe_history_v1
Dataset SHA256: 4b8d62bf0f6cf6cdc7d1570a422246e3531fc7b96982434eca5fc0738d192189
