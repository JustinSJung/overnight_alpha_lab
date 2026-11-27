# Confidence Report - 2026-11-27

Generated at: 2026-11-27 05:32:06

ML dataset: `data/processed/ml_dataset_20261127.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 723 |
| Pending rows | 0 |
| Success rows | 141 |
| Failure rows | 582 |
| Trainable rows | 723 |
| Overall accuracy | 19.50% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| convertible_bond | 453 | 3 | 450 | 0.66% |
| supply_contract | 93 | 17 | 76 | 18.28% |
| lawsuit | 75 | 73 | 2 | 97.33% |
| major_shareholder_change | 46 | 30 | 16 | 65.22% |
| paid_in_capital_increase | 35 | 14 | 21 | 40.00% |
| investment_decision | 10 | 1 | 9 | 10.00% |
| bond_with_warrant | 8 | 0 | 8 | 0.00% |
| merger | 3 | 3 | 0 | 100.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 571 | 90 | 481 | 15.76% |
| positive | 93 | 17 | 76 | 18.28% |
| volatile | 59 | 34 | 25 | 57.63% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
