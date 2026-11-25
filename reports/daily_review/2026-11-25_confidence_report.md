# Confidence Report - 2026-11-25

Generated at: 2026-11-25 05:30:58

ML dataset: `data/processed/ml_dataset_20261125.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 468 |
| Pending rows | 0 |
| Success rows | 159 |
| Failure rows | 309 |
| Trainable rows | 468 |
| Overall accuracy | 33.97% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 327 | 67 | 260 | 20.49% |
| convertible_bond | 74 | 70 | 4 | 94.59% |
| major_shareholder_change | 25 | 6 | 19 | 24.00% |
| supply_contract | 20 | 10 | 10 | 50.00% |
| merger | 8 | 5 | 3 | 62.50% |
| investment_decision | 7 | 0 | 7 | 0.00% |
| lawsuit | 4 | 1 | 3 | 25.00% |
| disclosure_violation | 2 | 0 | 2 | 0.00% |
| spin_off | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 407 | 138 | 269 | 33.91% |
| volatile | 41 | 11 | 30 | 26.83% |
| positive | 20 | 10 | 10 | 50.00% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
