# Confidence Report - 2026-11-23

Generated at: 2026-11-23 03:33:10

ML dataset: `data/processed/ml_dataset_20261123.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 471 |
| Pending rows | 0 |
| Success rows | 279 |
| Failure rows | 192 |
| Trainable rows | 471 |
| Overall accuracy | 59.24% |

Current readiness level: **WATCHLIST**

## Readiness Interpretation

The model is showing some predictive signal, but it still needs monitoring.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| supply_contract | 181 | 7 | 174 | 3.87% |
| paid_in_capital_increase | 137 | 137 | 0 | 100.00% |
| convertible_bond | 80 | 65 | 15 | 81.25% |
| major_shareholder_change | 58 | 56 | 2 | 96.55% |
| investment_decision | 13 | 13 | 0 | 100.00% |
| lawsuit | 2 | 1 | 1 | 50.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 219 | 203 | 16 | 92.69% |
| positive | 181 | 7 | 174 | 3.87% |
| volatile | 71 | 69 | 2 | 97.18% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
