# Confidence Report - 2026-11-13

Generated at: 2026-11-13 04:20:49

ML dataset: `data/processed/ml_dataset_20261113.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 4764 |
| Pending rows | 0 |
| Success rows | 782 |
| Failure rows | 3982 |
| Trainable rows | 4764 |
| Overall accuracy | 16.41% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| major_shareholder_change | 3769 | 12 | 3757 | 0.32% |
| merger | 736 | 735 | 1 | 99.86% |
| lawsuit | 143 | 0 | 143 | 0.00% |
| paid_in_capital_increase | 52 | 1 | 51 | 1.92% |
| supply_contract | 29 | 25 | 4 | 86.21% |
| convertible_bond | 18 | 0 | 18 | 0.00% |
| investment_decision | 12 | 4 | 8 | 33.33% |
| earnings_guidance | 4 | 4 | 0 | 100.00% |
| spin_off | 1 | 1 | 0 | 100.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 4518 | 752 | 3766 | 16.64% |
| negative | 213 | 1 | 212 | 0.47% |
| positive | 29 | 25 | 4 | 86.21% |
| neutral_positive | 4 | 4 | 0 | 100.00% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
