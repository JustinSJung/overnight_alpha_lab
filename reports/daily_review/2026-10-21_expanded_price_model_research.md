# Expanded Price History Research Experiment

Status: RESEARCH_ONLY. No deployment, production scoring change, or automated trading.

## Protocol

- Current observed candidate universe, not the entire Korean market.
- All 901 requested codes remain in the candidate pool. Missing/insufficient training observations are not a candidate-generation filter.
- Completed KIS adjusted daily bars only; features and five-session labels come from the same series.
- Fixed protocol: docs/model_experiments/expanded_history_protocol_20261021.json.
- Training as-of: 2026-06-30. Later collected bars are excluded from fitting and historical validation.
- Calibration starts 2025-02-13; historical test starts 2025-10-20. Label windows crossing either boundary are purged.
- Nine price features, existing classifier candidates, fixed 60% selection threshold and 0.3% cost assumption are unchanged.
- Classifier selection uses training-only purged expanding folds.
- These test dates were already inspected for 30 pilot stocks. Expanded historical results are development evidence, not a new untouched final test.
- Retrospectively adjusted prices and a current universe are not survivorship-free point-in-time data.

## Collection Quality

| Item | Value |
|---|---:|
| requested_stocks | 901 |
| successful_stocks | 901 |
| failed_stocks | 0 |
| raw_bars | 795771 |
| zero_volume_bars | 27117 |
| invalid_active_ohlc_bars | 0 |
| nonpositive_close_bars | 0 |
| short_histories_under_26_bars | 0 |
| last_date_before_requested_end | 7 |

Zero-volume or stale series may reflect suspensions; these counts alone do not establish data errors.

## Time Partitions

| Partition | Rows | Dates | Positive rate |
|---|---:|---|---:|
| train | 398764 | 2023-02-01 to 2025-02-05 | 41.3453% |
| calibration | 137002 | 2025-02-13 to 2025-10-10 | 43.5658% |
| test | 141304 | 2025-10-20 to 2026-06-23 | 42.0979% |

Classifier: hist_gradient_boosting

## Historical Results

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

Brier baseline uses the known calibration-period prevalence. Return-MAE baseline uses the training-period median.
The reported majority-class accuracy is a descriptive test-set reference, not an executable trading strategy.

## Monthly Historical Results

| Month | Rows | Positive rate | AUC | Model Brier | Constant Brier |
|---|---:|---:|---:|---:|---:|
| 2025-10 | 8583 | 33.8110% | 0.53242 | 0.232779 | 0.233307 |
| 2025-11 | 17170 | 47.7810% | 0.52113 | 0.250644 | 0.251284 |
| 2025-12 | 18040 | 40.2384% | 0.52059 | 0.241512 | 0.241578 |
| 2026-01 | 18115 | 50.3340% | 0.53890 | 0.253317 | 0.254570 |
| 2026-02 | 14692 | 41.1380% | 0.48267 | 0.244862 | 0.242736 |
| 2026-03 | 18111 | 45.0886% | 0.59119 | 0.240494 | 0.247820 |
| 2026-04 | 18233 | 55.8877% | 0.55843 | 0.259981 | 0.261716 |
| 2026-05 | 14781 | 19.9107% | 0.52231 | 0.230385 | 0.215420 |
| 2026-06 | 13579 | 34.3177% | 0.65135 | 0.233948 | 0.233959 |

## Probability Diagnostics

Calibration slope: 0.76927708
Calibration intercept: 0.02179320
Prediction probability standard deviation: 0.03890416

| Probability band | Rows | Mean forecast | Observed rate |
|---|---:|---:|---:|
| [0.2, 0.4] | 8232 | 38.7007% | 36.6740% |
| [0.4, 0.6] | 131991 | 44.7699% | 42.2218% |
| [0.6, 0.8] | 1081 | 62.4863% | 68.2701% |

## Selection Concentration Check

The fixed policy selected 1,081 historical stock/date observations on 105 signal dates. Their pooled success rate was 68.27%, but the average of the per-signal-date success rates was only 45.37%.

| Signal date | Selected observations | Success rate | Mean five-session net return proxy |
|---|---:|---:|---:|
| 2026-03-04 | 344 | 96.22% | 11.22% |
| 2026-03-05 | 137 | 66.42% | 2.80% |
| 2026-06-23 | 89 | 55.06% | 2.04% |
| 2026-06-08 | 87 | 96.55% | 13.52% |

The first two dates contain 481/1,081 observations (44.50%). A pooled success rate is therefore not a reliable description of performance on a typical signal date. Averaging the per-date mean five-session net return proxies gives -0.4392%, with a five-day-block bootstrap lower bound of -2.9620%. These are overlapping close-to-close research outcomes after an assumed cost, not realized daily trading returns.

## Current Research Inference

The expanded model produced research-only predictions for 837 stocks with valid latest inputs. All 837 return ABSTAIN. The remaining inputs were not eligible for prediction; the underlying 901-stock candidate pool was not modified. Output: `data/predictions/ml_price_forecasts_expanded_20261021.csv`. These are retrospective/current research estimates based on stored prices, not new prospective forecasts frozen before their first outcome session.

## Recommendation Gate

- weak_out_of_time_discrimination
- probabilities_do_not_beat_constant_baseline
- positive_daily_return_edge_not_established
- reconstructed_history_requires_forward_validation

Historical reconstruction alone cannot enable recommendations. Fixed future predictions across multiple dates must be evaluated before production promotion.
The earlier 27-prediction forward ledger is preserved and belongs to the earlier pilot model, not this expanded model.
This expanded model was trained after the 2026-10-21 open. Older signal-day predictions are not backdated into a prospective test.
Next prospective recording requires a fresh completed signal close and a timestamp before the following session opens.

## Reproduction

```bash
bash scripts/price_model.sh train \
  --data-root data/ml_history/kis_expanded_20261019 \
  --model-dir data/models/price_forecaster_expanded \
  --source-ref expanded_current_universe_history_v1 \
  --as-of 2026-06-30 \
  --calibration-start 2025-02-13 --test-start 2025-10-20
```

## Artifacts

Run: 20261021T024717Z_4b8d62bf0f_a39ff6
Dataset SHA256: 4b8d62bf0f6cf6cdc7d1570a422246e3531fc7b96982434eca5fc0738d192189
Trained at UTC: 2026-10-21T02:47:17.290980+00:00

Raw data and model binaries are ignored by Git. Default/pilot model pointers are unchanged.
