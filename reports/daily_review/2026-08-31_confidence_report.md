# Confidence Report - 2026-08-31

Generated at: 2026-08-31 01:14:15

ML dataset: `data/processed/ml_dataset_20260831.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 951 |
| Pending rows | 0 |
| Success rows | 142 |
| Failure rows | 809 |
| Trainable rows | 951 |
| Overall accuracy | 14.93% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| major_shareholder_change | 400 | 22 | 378 | 5.50% |
| supply_contract | 236 | 16 | 220 | 6.78% |
| convertible_bond | 147 | 73 | 74 | 49.66% |
| paid_in_capital_increase | 84 | 25 | 59 | 29.76% |
| merger | 66 | 0 | 66 | 0.00% |
| spin_off | 6 | 2 | 4 | 33.33% |
| lawsuit | 4 | 4 | 0 | 100.00% |
| disclosure_violation | 4 | 0 | 4 | 0.00% |
| investment_decision | 4 | 0 | 4 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 476 | 24 | 452 | 5.04% |
| negative | 239 | 102 | 137 | 42.68% |
| positive | 236 | 16 | 220 | 6.78% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
