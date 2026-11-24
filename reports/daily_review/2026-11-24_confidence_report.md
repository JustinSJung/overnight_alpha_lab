# Confidence Report - 2026-11-24

Generated at: 2026-11-24 06:54:33

ML dataset: `data/processed/ml_dataset_20261124.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 825 |
| Pending rows | 0 |
| Success rows | 651 |
| Failure rows | 174 |
| Trainable rows | 825 |
| Overall accuracy | 78.91% |

Current readiness level: **HIGH_CONFIDENCE**

## Readiness Interpretation

The model is showing high confidence based on current data. Continue monitoring for stability.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 567 | 432 | 135 | 76.19% |
| major_shareholder_change | 101 | 100 | 1 | 99.01% |
| merger | 77 | 70 | 7 | 90.91% |
| supply_contract | 31 | 24 | 7 | 77.42% |
| investment_decision | 23 | 9 | 14 | 39.13% |
| lawsuit | 21 | 16 | 5 | 76.19% |
| disclosure_violation | 2 | 0 | 2 | 0.00% |
| bond_with_warrant | 1 | 0 | 1 | 0.00% |
| bonus_issue | 1 | 0 | 1 | 0.00% |
| convertible_bond | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 592 | 448 | 144 | 75.68% |
| volatile | 201 | 179 | 22 | 89.05% |
| positive | 32 | 24 | 8 | 75.00% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
