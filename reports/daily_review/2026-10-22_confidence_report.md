# Confidence Report - 2026-10-22

Generated at: 2026-10-22 01:26:00

ML dataset: `data/processed/ml_dataset_20261022.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 467 |
| Pending rows | 0 |
| Success rows | 110 |
| Failure rows | 357 |
| Trainable rows | 467 |
| Overall accuracy | 23.55% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| supply_contract | 224 | 75 | 149 | 33.48% |
| lawsuit | 74 | 4 | 70 | 5.41% |
| investment_decision | 64 | 0 | 64 | 0.00% |
| convertible_bond | 41 | 14 | 27 | 34.15% |
| paid_in_capital_increase | 30 | 14 | 16 | 46.67% |
| major_shareholder_change | 18 | 2 | 16 | 11.11% |
| disclosure_violation | 13 | 1 | 12 | 7.69% |
| earnings_guidance | 2 | 0 | 2 | 0.00% |
| merger | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| positive | 224 | 75 | 149 | 33.48% |
| negative | 158 | 33 | 125 | 20.89% |
| volatile | 83 | 2 | 81 | 2.41% |
| neutral_positive | 2 | 0 | 2 | 0.00% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
