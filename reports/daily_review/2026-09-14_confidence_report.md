# Confidence Report - 2026-09-14

Generated at: 2026-09-14 00:59:55

ML dataset: `data/processed/ml_dataset_20260914.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 321 |
| Pending rows | 0 |
| Success rows | 102 |
| Failure rows | 219 |
| Trainable rows | 321 |
| Overall accuracy | 31.78% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 103 | 26 | 77 | 25.24% |
| convertible_bond | 101 | 34 | 67 | 33.66% |
| supply_contract | 41 | 16 | 25 | 39.02% |
| disclosure_violation | 33 | 8 | 25 | 24.24% |
| major_shareholder_change | 28 | 8 | 20 | 28.57% |
| investment_decision | 7 | 6 | 1 | 85.71% |
| lawsuit | 3 | 1 | 2 | 33.33% |
| earnings_guidance | 2 | 2 | 0 | 100.00% |
| merger | 2 | 1 | 1 | 50.00% |
| spin_off | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 240 | 69 | 171 | 28.75% |
| positive | 41 | 16 | 25 | 39.02% |
| volatile | 38 | 15 | 23 | 39.47% |
| neutral_positive | 2 | 2 | 0 | 100.00% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
