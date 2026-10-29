# Market Context and Date-Balanced Learning

RESEARCH_ONLY. No production model replacement, scoring change, or trading.

## Fixed Comparison

Previously inspected historical dates: development comparison, not an untouched final test.
All four arms use identical observations, temporal boundaries, five-session labels, and the unchanged 60%/0.3% selection policy.
Classifier selection uses three purged expanding folds inside training only. Final historical scores do not select a winner or tune thresholds.
Date-balanced arms weight each signal date equally in scaling, fitting, calibration and training-fold loss.
Market context is an active observed-universe proxy, not KOSPI/KOSDAQ. It uses only completed same-day/past quotes.
No forward predictions are backdated. Every arm remains recommendation-disabled pending future validation.

Common rows: 685620; excluded for context: 0.
Common dataset SHA256: e4482c55342c26285fd4faef160f32e70eb40f42d8fe2c9396275031a573cab3

## Comparable Metrics

| Arm | Classifier | Pooled AUC | Mean daily AUC | Date Brier | Constant date Brier | Date return MAE |
|---|---|---:|---:|---:|---:|---:|
| price_row | hist_gradient_boosting | 0.515569 | 0.521683 | 0.244244 | 0.243851 | 0.068851 |
| price_date | hist_gradient_boosting | 0.515824 | 0.521590 | 0.244220 | 0.243851 | 0.068850 |
| market_row | hist_gradient_boosting | 0.511819 | 0.519634 | 0.244219 | 0.243851 | 0.070278 |
| market_date | hist_gradient_boosting | 0.512074 | 0.519818 | 0.244243 | 0.243851 | 0.070164 |

Smaller Brier/MAE is better. The constant date baseline is the same past calibration-period date-weighted prevalence for every arm.
Mean daily AUC averages cross-sectional AUC only on dates containing both classes; dates are correlated and five-session labels overlap.

## Fixed Policy Selection

| Arm | Selected rows | Signal dates | Pooled success | Date-equal success | Top-two-date share | Selected-date five-session net proxy | Selected-date block lower 95% |
|---|---:|---:|---:|---:|---:|---:|---:|
| price_row | 1081 | 105 | 68.27% | 45.37% | 44.50% | -0.44% | -2.96% |
| price_date | 1044 | 104 | 67.91% | 47.25% | 44.35% | -0.16% | -2.55% |
| market_row | 0 | 0 | n/a | n/a | n/a | n/a | n/a |
| market_date | 0 | 0 | n/a | n/a | n/a | n/a | n/a |

Per-date selection metrics include dates with selections only. These are overlapping close-to-close research returns after assumed cost, not executable daily portfolio returns.
A pooled success rate is not model reliability. No recommendation gate is relaxed.

Selected-date block resampling uses the sequence of selected dates, which may have gaps.

## All Signal Dates

| Arm | All-date mean five-session net proxy | Calendar-sequence block lower 95% |
|---|---:|---:|
| price_row | -0.28% | -1.88% |
| price_date | -0.10% | -1.50% |
| market_row | 0.00% | 0.00% |
| market_date | 0.00% | 0.00% |

Includes every test signal date; dates with no policy selection have zero exposure proxy, not failed prediction labels. Blocks contain five consecutive observed signal dates.
Zero from an abstaining model is not evidence of useful predictive performance. These proxies are not compounded portfolio returns.

## Monthly Diagnostics

| Arm | Month | Rows | AUC | Date Brier | Constant date Brier |
|---|---|---:|---:|---:|---:|
| price_row | 2025-10 | 8583 | 0.532423 | 0.232786 | 0.233346 |
| price_row | 2025-11 | 17170 | 0.521134 | 0.250650 | 0.251275 |
| price_row | 2025-12 | 18040 | 0.520587 | 0.241519 | 0.241596 |
| price_row | 2026-01 | 18115 | 0.538904 | 0.253313 | 0.254544 |
| price_row | 2026-02 | 14692 | 0.482665 | 0.244866 | 0.242750 |
| price_row | 2026-03 | 18111 | 0.591195 | 0.240484 | 0.247796 |
| price_row | 2026-04 | 18233 | 0.558432 | 0.259555 | 0.261208 |
| price_row | 2026-05 | 14781 | 0.522305 | 0.230345 | 0.215584 |
| price_row | 2026-06 | 13579 | 0.651353 | 0.233931 | 0.233985 |
| price_date | 2025-10 | 8583 | 0.532350 | 0.232817 | 0.233346 |
| price_date | 2025-11 | 17170 | 0.521528 | 0.250629 | 0.251275 |
| price_date | 2025-12 | 18040 | 0.519206 | 0.241546 | 0.241596 |
| price_date | 2026-01 | 18115 | 0.539391 | 0.253289 | 0.254544 |
| price_date | 2026-02 | 14692 | 0.483349 | 0.244828 | 0.242750 |
| price_date | 2026-03 | 18111 | 0.590787 | 0.240544 | 0.247796 |
| price_date | 2026-04 | 18233 | 0.557063 | 0.259579 | 0.261208 |
| price_date | 2026-05 | 14781 | 0.523117 | 0.230110 | 0.215584 |
| price_date | 2026-06 | 13579 | 0.650964 | 0.233880 | 0.233985 |
| market_row | 2025-10 | 8583 | 0.444813 | 0.234029 | 0.233346 |
| market_row | 2025-11 | 17170 | 0.552904 | 0.249408 | 0.251275 |
| market_row | 2025-12 | 18040 | 0.522125 | 0.241629 | 0.241596 |
| market_row | 2026-01 | 18115 | 0.466888 | 0.254400 | 0.254544 |
| market_row | 2026-02 | 14692 | 0.523491 | 0.242846 | 0.242750 |
| market_row | 2026-03 | 18111 | 0.637538 | 0.240342 | 0.247796 |
| market_row | 2026-04 | 18233 | 0.620399 | 0.255346 | 0.261208 |
| market_row | 2026-05 | 14781 | 0.552403 | 0.230500 | 0.215584 |
| market_row | 2026-06 | 13579 | 0.715817 | 0.240820 | 0.233985 |
| market_date | 2025-10 | 8583 | 0.459173 | 0.233826 | 0.233346 |
| market_date | 2025-11 | 17170 | 0.544522 | 0.249664 | 0.251275 |
| market_date | 2025-12 | 18040 | 0.514092 | 0.241638 | 0.241596 |
| market_date | 2026-01 | 18115 | 0.458678 | 0.254654 | 0.254544 |
| market_date | 2026-02 | 14692 | 0.547664 | 0.242569 | 0.242750 |
| market_date | 2026-03 | 18111 | 0.632239 | 0.240362 | 0.247796 |
| market_date | 2026-04 | 18233 | 0.617972 | 0.255477 | 0.261208 |
| market_date | 2026-05 | 14781 | 0.551285 | 0.229499 | 0.215584 |
| market_date | 2026-06 | 13579 | 0.725538 | 0.241745 | 0.233985 |

## Regime Diagnostics

| Arm | Known-at-close regime | Rows | AUC | Date Brier |
|---|---|---:|---:|---:|
| price_row | down_or_flat_proxy | 55474 | 0.530672 | 0.243187 |
| price_row | up_proxy | 85830 | 0.511207 | 0.244925 |
| price_date | down_or_flat_proxy | 55474 | 0.531146 | 0.243141 |
| price_date | up_proxy | 85830 | 0.511114 | 0.244915 |
| market_row | down_or_flat_proxy | 55474 | 0.521737 | 0.244168 |
| market_row | up_proxy | 85830 | 0.514113 | 0.244252 |
| market_date | down_or_flat_proxy | 55474 | 0.523981 | 0.244321 |
| market_date | up_proxy | 85830 | 0.513199 | 0.244193 |

Regimes split on the observed-universe trailing 20-session return, not future outcomes.

## Artifacts

- price_row: /Users/justin/Desktop/overnight_alpha_lab/data/models/price_forecaster_context/price_row/runs/20261021T040048Z_4b8d62bf0f_1ecb11
  Gate: weak_out_of_time_discrimination, probabilities_do_not_beat_constant_baseline, positive_daily_return_edge_not_established, development_experiment_requires_future_validation
- price_date: /Users/justin/Desktop/overnight_alpha_lab/data/models/price_forecaster_context/price_date/runs/20261021T040054Z_4b8d62bf0f_03e379
  Gate: weak_out_of_time_discrimination, probabilities_do_not_beat_constant_baseline, positive_daily_return_edge_not_established, development_experiment_requires_future_validation
- market_row: /Users/justin/Desktop/overnight_alpha_lab/data/models/price_forecaster_context/market_row/runs/20261021T040100Z_b25eb669ba_c6bc91
  Gate: insufficient_fixed_policy_selection_history, weak_out_of_time_discrimination, probabilities_do_not_beat_constant_baseline, selected_precision_lift_below_3_percentage_points, positive_daily_return_edge_not_established, return_forecast_does_not_beat_training_median, development_experiment_requires_future_validation
- market_date: /Users/justin/Desktop/overnight_alpha_lab/data/models/price_forecaster_context/market_date/runs/20261021T040108Z_b25eb669ba_6b710e
  Gate: insufficient_fixed_policy_selection_history, weak_out_of_time_discrimination, probabilities_do_not_beat_constant_baseline, selected_precision_lift_below_3_percentage_points, positive_daily_return_edge_not_established, return_forecast_does_not_beat_training_median, development_experiment_requires_future_validation

Current-universe/survivorship and retrospective adjusted-price limitations remain. Future timestamped predictions on multiple dates are required.
