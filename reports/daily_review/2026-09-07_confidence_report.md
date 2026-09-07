# Confidence Report - 2026-09-07

Generated at: 2026-09-07 00:27:30

ML dataset: `data/processed/ml_dataset_20260907.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 446 |
| Pending rows | 0 |
| Success rows | 156 |
| Failure rows | 290 |
| Trainable rows | 446 |
| Overall accuracy | 34.98% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 187 | 107 | 80 | 57.22% |
| convertible_bond | 138 | 10 | 128 | 7.25% |
| major_shareholder_change | 63 | 12 | 51 | 19.05% |
| supply_contract | 22 | 10 | 12 | 45.45% |
| merger | 17 | 6 | 11 | 35.29% |
| investment_decision | 9 | 6 | 3 | 66.67% |
| lawsuit | 5 | 4 | 1 | 80.00% |
| spin_off | 3 | 1 | 2 | 33.33% |
| disclosure_violation | 2 | 0 | 2 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 332 | 121 | 211 | 36.45% |
| volatile | 92 | 25 | 67 | 27.17% |
| positive | 22 | 10 | 12 | 45.45% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
