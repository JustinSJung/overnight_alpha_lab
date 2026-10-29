# Confidence Report - 2026-10-27

Generated at: 2026-10-27 02:03:11

ML dataset: `data/processed/ml_dataset_20261027.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 964 |
| Pending rows | 0 |
| Success rows | 509 |
| Failure rows | 455 |
| Trainable rows | 964 |
| Overall accuracy | 52.80% |

Current readiness level: **WATCHLIST**

## Readiness Interpretation

The model is showing some predictive signal, but it still needs monitoring.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| merger | 409 | 163 | 246 | 39.85% |
| supply_contract | 316 | 303 | 13 | 95.89% |
| paid_in_capital_increase | 157 | 5 | 152 | 3.18% |
| major_shareholder_change | 48 | 15 | 33 | 31.25% |
| investment_decision | 12 | 8 | 4 | 66.67% |
| lawsuit | 8 | 4 | 4 | 50.00% |
| convertible_bond | 7 | 5 | 2 | 71.43% |
| earnings_guidance | 6 | 6 | 0 | 100.00% |
| spin_off | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 470 | 186 | 284 | 39.57% |
| positive | 316 | 303 | 13 | 95.89% |
| negative | 172 | 14 | 158 | 8.14% |
| neutral_positive | 6 | 6 | 0 | 100.00% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
