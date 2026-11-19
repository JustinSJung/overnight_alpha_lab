# Confidence Report - 2026-11-19

Generated at: 2026-11-19 04:22:42

ML dataset: `data/processed/ml_dataset_20261119.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 255 |
| Pending rows | 0 |
| Success rows | 206 |
| Failure rows | 49 |
| Trainable rows | 255 |
| Overall accuracy | 80.78% |

Current readiness level: **HIGH_CONFIDENCE**

## Readiness Interpretation

The model is showing high confidence based on current data. Continue monitoring for stability.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| supply_contract | 156 | 145 | 11 | 92.95% |
| major_shareholder_change | 33 | 9 | 24 | 27.27% |
| paid_in_capital_increase | 31 | 27 | 4 | 87.10% |
| convertible_bond | 21 | 21 | 0 | 100.00% |
| investment_decision | 9 | 0 | 9 | 0.00% |
| lawsuit | 3 | 3 | 0 | 100.00% |
| spin_off | 1 | 1 | 0 | 100.00% |
| disclosure_violation | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| positive | 156 | 145 | 11 | 92.95% |
| negative | 56 | 51 | 5 | 91.07% |
| volatile | 43 | 10 | 33 | 23.26% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
