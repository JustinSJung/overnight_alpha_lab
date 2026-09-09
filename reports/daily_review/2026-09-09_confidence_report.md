# Confidence Report - 2026-09-09

Generated at: 2026-09-09 00:53:49

ML dataset: `data/processed/ml_dataset_20260909.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 499 |
| Pending rows | 0 |
| Success rows | 145 |
| Failure rows | 354 |
| Trainable rows | 499 |
| Overall accuracy | 29.06% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 365 | 130 | 235 | 35.62% |
| merger | 68 | 0 | 68 | 0.00% |
| major_shareholder_change | 28 | 0 | 28 | 0.00% |
| supply_contract | 14 | 9 | 5 | 64.29% |
| convertible_bond | 14 | 2 | 12 | 14.29% |
| investment_decision | 4 | 3 | 1 | 75.00% |
| spin_off | 3 | 1 | 2 | 33.33% |
| lawsuit | 3 | 0 | 3 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 382 | 132 | 250 | 34.55% |
| volatile | 103 | 4 | 99 | 3.88% |
| positive | 14 | 9 | 5 | 64.29% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
