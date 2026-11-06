# Confidence Report - 2026-11-06

Generated at: 2026-11-06 03:20:35

ML dataset: `data/processed/ml_dataset_20261106.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 1062 |
| Pending rows | 0 |
| Success rows | 610 |
| Failure rows | 452 |
| Trainable rows | 1062 |
| Overall accuracy | 57.44% |

Current readiness level: **WATCHLIST**

## Readiness Interpretation

The model is showing some predictive signal, but it still needs monitoring.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 493 | 365 | 128 | 74.04% |
| major_shareholder_change | 455 | 225 | 230 | 49.45% |
| merger | 27 | 2 | 25 | 7.41% |
| supply_contract | 27 | 0 | 27 | 0.00% |
| spin_off | 26 | 0 | 26 | 0.00% |
| investment_decision | 13 | 6 | 7 | 46.15% |
| lawsuit | 13 | 6 | 7 | 46.15% |
| convertible_bond | 8 | 6 | 2 | 75.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 521 | 233 | 288 | 44.72% |
| negative | 514 | 377 | 137 | 73.35% |
| positive | 27 | 0 | 27 | 0.00% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
