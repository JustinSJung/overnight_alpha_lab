# Monthly Price Walk-Forward Research

RESEARCH_ONLY. Retrospective development replay, not prospective validation or trading.

## Controls and Timing

Nine price features, the existing histogram-gradient-boosting classifier/regressor, sigmoid calibration, five-session target and 60%/0.3% policy are fixed.
For each training-window size, the frozen control is exactly the first monthly model. It is not the differently timed legacy fixed artifact.
Refits occur before the calendar month using only mature labels. The first partial evaluation month still fits before its calendar month starts.
Earlier evaluation outcomes can enter later refits only after becoming available. Already issued predictions are never regenerated with later models.
All four variants use identical stock/date evaluation rows. Complete-outcome filtering and retrospective current-universe/adjusted-price limitations remain.
No future-month evaluation labels or scores are attached to the as-of model bundles.

## Aggregate Results

| Variant | Rows | Dates | AUC | Date Brier | Own past-constant date Brier | Common monthly-constant date Brier |
|---|---:|---:|---:|---:|---:|---:|
| frozen_252 | 141304 | 166 | 0.523964 | 0.243632 | 0.243804 | 0.246509 |
| monthly_252 | 141304 | 166 | 0.500828 | 0.247721 | 0.246509 | 0.246509 |
| frozen_504 | 141304 | 166 | 0.520564 | 0.244097 | 0.243804 | 0.246509 |
| monthly_504 | 141304 | 166 | 0.504377 | 0.247253 | 0.246509 | 0.246509 |

Brier is lower-is-better. Own constants use each model's known calibration prevalence; common constants update monthly and are identical across windows.

## Paired Monthly Minus Frozen

| Window | Date Brier difference | Five-session-block 95% interval |
|---|---:|---|
| 252 | 0.004089 | [-0.001747, 0.010482] |
| 504 | 0.003156 | [-0.002339, 0.009178] |

Negative differences favor refitting. Intervals use 5,000 paired resamples of five consecutive observed signal dates, seed 42; they are development diagnostics, not guarantees.

## Fixed Policy and All Dates

| Variant | Selected rows | Selected dates | Pooled success | Date-equal selected success | All-date five-session net proxy | Calendar-block lower 95% |
|---|---:|---:|---:|---:|---:|---:|
| frozen_252 | 1483 | 125 | 62.64% | 48.74% | -0.41% | -2.30% |
| monthly_252 | 2198 | 77 | 40.49% | 42.65% | -0.12% | -1.35% |
| frozen_504 | 1723 | 132 | 59.08% | 49.46% | 0.48% | -1.39% |
| monthly_504 | 2421 | 102 | 51.30% | 40.59% | -1.55% | -3.19% |

No-selection dates are zero exposure proxies, not failed labels. Overlapping close-to-close outcomes after assumed cost are not executable portfolio returns. No gate is relaxed.

## Monthly Results

| Month | Variant | Rows | AUC | Date Brier | Common monthly-constant date Brier |
|---|---|---:|---:|---:|---:|
| 2025-10 | frozen_252 | 8583 | 0.549459 | 0.227602 | 0.228377 |
| 2025-10 | monthly_252 | 8583 | 0.549459 | 0.227602 | 0.228377 |
| 2025-10 | frozen_504 | 8583 | 0.545745 | 0.228026 | 0.228377 |
| 2025-10 | monthly_504 | 8583 | 0.545745 | 0.228026 | 0.228377 |
| 2025-11 | frozen_252 | 17170 | 0.510182 | 0.254190 | 0.254256 |
| 2025-11 | monthly_252 | 17170 | 0.514448 | 0.253617 | 0.254256 |
| 2025-11 | frozen_504 | 17170 | 0.517295 | 0.253607 | 0.254256 |
| 2025-11 | monthly_504 | 17170 | 0.517469 | 0.253361 | 0.254256 |
| 2025-12 | frozen_252 | 18040 | 0.524695 | 0.240677 | 0.240488 |
| 2025-12 | monthly_252 | 18040 | 0.523871 | 0.240423 | 0.240488 |
| 2025-12 | frozen_504 | 18040 | 0.526058 | 0.240713 | 0.240488 |
| 2025-12 | monthly_504 | 18040 | 0.530769 | 0.240297 | 0.240488 |
| 2026-01 | frozen_252 | 18115 | 0.534612 | 0.257146 | 0.258860 |
| 2026-01 | monthly_252 | 18115 | 0.537703 | 0.257611 | 0.258860 |
| 2026-01 | frozen_504 | 18115 | 0.540494 | 0.257300 | 0.258860 |
| 2026-01 | monthly_504 | 18115 | 0.542834 | 0.257543 | 0.258860 |
| 2026-02 | frozen_252 | 14692 | 0.504439 | 0.243937 | 0.243971 |
| 2026-02 | monthly_252 | 14692 | 0.506743 | 0.244661 | 0.243971 |
| 2026-02 | frozen_504 | 14692 | 0.503065 | 0.244381 | 0.243971 |
| 2026-02 | monthly_504 | 14692 | 0.499713 | 0.245141 | 0.243971 |
| 2026-03 | frozen_252 | 18111 | 0.597078 | 0.240225 | 0.249460 |
| 2026-03 | monthly_252 | 18111 | 0.586757 | 0.244853 | 0.249460 |
| 2026-03 | frozen_504 | 18111 | 0.589798 | 0.240541 | 0.249460 |
| 2026-03 | monthly_504 | 18111 | 0.592851 | 0.243536 | 0.249460 |
| 2026-04 | frozen_252 | 18233 | 0.552244 | 0.266032 | 0.255161 |
| 2026-04 | monthly_252 | 18233 | 0.569713 | 0.253326 | 0.255161 |
| 2026-04 | frozen_504 | 18233 | 0.553805 | 0.266292 | 0.255161 |
| 2026-04 | monthly_504 | 18233 | 0.571666 | 0.253730 | 0.255161 |
| 2026-05 | frozen_252 | 14781 | 0.520152 | 0.218807 | 0.242162 |
| 2026-05 | monthly_252 | 14781 | 0.506083 | 0.263782 | 0.242162 |
| 2026-05 | frozen_504 | 14781 | 0.514704 | 0.221266 | 0.242162 |
| 2026-05 | monthly_504 | 14781 | 0.512571 | 0.262009 | 0.242162 |
| 2026-06 | frozen_252 | 13579 | 0.629881 | 0.227871 | 0.231668 |
| 2026-06 | monthly_252 | 13579 | 0.576998 | 0.230760 | 0.231668 |
| 2026-06 | frozen_504 | 13579 | 0.639570 | 0.228899 | 0.231668 |
| 2026-06 | monthly_504 | 13579 | 0.632091 | 0.228870 | 0.231668 |

## Label-Time Audit

| Month | Window | Fit as-of | Train signal range | Latest train label | Calibration signal range | Latest calibration label | Evaluated signal range |
|---|---:|---|---|---|---|---|---|
| 2025-10 | 252 | 2025-09-30 | 2024-06-07 to 2025-06-23 | 2025-06-30 | 2025-07-01 to 2025-09-23 | 2025-09-30 | 2025-10-20 to 2025-10-31 |
| 2025-10 | 504 | 2025-09-30 | 2023-05-25 to 2025-06-23 | 2025-06-30 | 2025-07-01 to 2025-09-23 | 2025-09-30 | 2025-10-20 to 2025-10-31 |
| 2025-11 | 252 | 2025-10-31 | 2024-07-03 to 2025-07-17 | 2025-07-24 | 2025-07-25 to 2025-10-24 | 2025-10-31 | 2025-11-03 to 2025-11-28 |
| 2025-11 | 504 | 2025-10-31 | 2023-06-22 to 2025-07-17 | 2025-07-24 | 2025-07-25 to 2025-10-24 | 2025-10-31 | 2025-11-03 to 2025-11-28 |
| 2025-12 | 252 | 2025-11-28 | 2024-07-31 to 2025-08-14 | 2025-08-22 | 2025-08-25 to 2025-11-21 | 2025-11-28 | 2025-12-01 to 2025-12-30 |
| 2025-12 | 504 | 2025-11-28 | 2023-07-20 to 2025-08-14 | 2025-08-22 | 2025-08-25 to 2025-11-21 | 2025-11-28 | 2025-12-01 to 2025-12-30 |
| 2026-01 | 252 | 2025-12-30 | 2024-08-30 to 2025-09-15 | 2025-09-22 | 2025-09-23 to 2025-12-22 | 2025-12-30 | 2026-01-02 to 2026-01-30 |
| 2026-01 | 504 | 2025-12-30 | 2023-08-21 to 2025-09-15 | 2025-09-22 | 2025-09-23 to 2025-12-22 | 2025-12-30 | 2026-01-02 to 2026-01-30 |
| 2026-02 | 252 | 2026-01-30 | 2024-10-07 to 2025-10-21 | 2025-10-28 | 2025-10-29 to 2026-01-23 | 2026-01-30 | 2026-02-02 to 2026-02-27 |
| 2026-02 | 504 | 2026-01-30 | 2023-09-19 to 2025-10-21 | 2025-10-28 | 2025-10-29 to 2026-01-23 | 2026-01-30 | 2026-02-02 to 2026-02-27 |
| 2026-03 | 252 | 2026-02-27 | 2024-10-31 to 2025-11-13 | 2025-11-20 | 2025-11-21 to 2026-02-20 | 2026-02-27 | 2026-03-03 to 2026-03-31 |
| 2026-03 | 504 | 2026-02-27 | 2023-10-19 to 2025-11-13 | 2025-11-20 | 2025-11-21 to 2026-02-20 | 2026-02-27 | 2026-03-03 to 2026-03-31 |
| 2026-04 | 252 | 2026-03-31 | 2024-11-29 to 2025-12-12 | 2025-12-19 | 2025-12-22 to 2026-03-24 | 2026-03-31 | 2026-04-01 to 2026-04-30 |
| 2026-04 | 504 | 2026-03-31 | 2023-11-17 to 2025-12-12 | 2025-12-19 | 2025-12-22 to 2026-03-24 | 2026-03-31 | 2026-04-01 to 2026-04-30 |
| 2026-05 | 252 | 2026-04-30 | 2025-01-03 to 2026-01-16 | 2026-01-23 | 2026-01-26 to 2026-04-23 | 2026-04-30 | 2026-05-04 to 2026-05-29 |
| 2026-05 | 504 | 2026-04-30 | 2023-12-19 to 2026-01-16 | 2026-01-23 | 2026-01-26 to 2026-04-23 | 2026-04-30 | 2026-05-04 to 2026-05-29 |
| 2026-06 | 252 | 2026-05-29 | 2025-02-04 to 2026-02-11 | 2026-02-23 | 2026-02-24 to 2026-05-21 | 2026-05-29 | 2026-06-01 to 2026-06-23 |
| 2026-06 | 504 | 2026-05-29 | 2024-01-17 to 2026-02-11 | 2026-02-23 | 2026-02-24 to 2026-05-21 | 2026-05-29 | 2026-06-01 to 2026-06-23 |

## Probability Calibration

| Variant | Forecast band | Rows | Mean forecast | Observed rate |
|---|---|---:|---:|---:|
| frozen_252 | [0.2, 0.4] | 46074 | 37.60% | 39.22% |
| frozen_252 | [0.4, 0.6] | 93747 | 43.74% | 43.19% |
| frozen_252 | [0.6, 0.8] | 1483 | 63.76% | 62.64% |
| monthly_252 | [0.2, 0.4] | 25521 | 38.21% | 39.55% |
| monthly_252 | [0.4, 0.6] | 113485 | 45.54% | 42.72% |
| monthly_252 | [0.6, 0.8] | 2298 | 62.50% | 39.86% |
| frozen_504 | [0.2, 0.4] | 41688 | 37.08% | 39.17% |
| frozen_504 | [0.4, 0.6] | 97892 | 43.70% | 43.04% |
| frozen_504 | [0.6, 0.8] | 1724 | 64.01% | 59.05% |
| monthly_504 | [0.2, 0.4] | 23350 | 38.03% | 38.40% |
| monthly_504 | [0.4, 0.6] | 115508 | 45.64% | 42.65% |
| monthly_504 | [0.6, 0.8] | 2446 | 64.37% | 51.19% |

## Provenance

Common dataset SHA256: 4b8d62bf0f6cf6cdc7d1570a422246e3531fc7b96982434eca5fc0738d192189
Protocol SHA256: 9b59e54675ec1579569b80243607d5df2a37497246a20336892e3f1b66d4d2b7

No default model, candidate generator, dashboard, existing forward ledger or deployment was changed.
Model files, calibration-fit diagnostics and historical prediction ledgers stay in the ignored experiment output directory.
