# Confidence Report - 2026-10-21

Generated at: 2026-10-21 01:15:48

ML dataset: `data/processed/ml_dataset_20261021.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 77 |
| Pending rows | 0 |
| Success rows | 31 |
| Failure rows | 46 |
| Trainable rows | 77 |
| Overall accuracy | 40.26% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| major_shareholder_change | 22 | 6 | 16 | 27.27% |
| supply_contract | 18 | 15 | 3 | 83.33% |
| paid_in_capital_increase | 13 | 1 | 12 | 7.69% |
| convertible_bond | 10 | 2 | 8 | 20.00% |
| investment_decision | 8 | 4 | 4 | 50.00% |
| lawsuit | 3 | 2 | 1 | 66.67% |
| bonus_issue | 1 | 1 | 0 | 100.00% |
| disclosure_violation | 1 | 0 | 1 | 0.00% |
| spin_off | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 31 | 10 | 21 | 32.26% |
| negative | 27 | 5 | 22 | 18.52% |
| positive | 19 | 16 | 3 | 84.21% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
