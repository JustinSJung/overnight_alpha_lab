# Confidence Report - 2026-11-04

Generated at: 2026-11-04 02:54:14

ML dataset: `data/processed/ml_dataset_20261104.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 213 |
| Pending rows | 0 |
| Success rows | 57 |
| Failure rows | 156 |
| Trainable rows | 213 |
| Overall accuracy | 26.76% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| major_shareholder_change | 139 | 15 | 124 | 10.79% |
| paid_in_capital_increase | 25 | 21 | 4 | 84.00% |
| convertible_bond | 19 | 15 | 4 | 78.95% |
| supply_contract | 13 | 2 | 11 | 15.38% |
| investment_decision | 7 | 0 | 7 | 0.00% |
| merger | 5 | 0 | 5 | 0.00% |
| lawsuit | 3 | 3 | 0 | 100.00% |
| disclosure_violation | 1 | 1 | 0 | 100.00% |
| spin_off | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 152 | 15 | 137 | 9.87% |
| negative | 48 | 40 | 8 | 83.33% |
| positive | 13 | 2 | 11 | 15.38% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
