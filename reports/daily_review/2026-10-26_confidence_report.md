# Confidence Report - 2026-10-26

Generated at: 2026-10-26 00:56:20

ML dataset: `data/processed/ml_dataset_20261026.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 457 |
| Pending rows | 0 |
| Success rows | 237 |
| Failure rows | 220 |
| Trainable rows | 457 |
| Overall accuracy | 51.86% |

Current readiness level: **WATCHLIST**

## Readiness Interpretation

The model is showing some predictive signal, but it still needs monitoring.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 204 | 199 | 5 | 97.55% |
| lawsuit | 106 | 5 | 101 | 4.72% |
| merger | 74 | 10 | 64 | 13.51% |
| major_shareholder_change | 40 | 12 | 28 | 30.00% |
| supply_contract | 22 | 4 | 18 | 18.18% |
| convertible_bond | 8 | 6 | 2 | 75.00% |
| investment_decision | 2 | 1 | 1 | 50.00% |
| bonus_issue | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 318 | 210 | 108 | 66.04% |
| volatile | 116 | 23 | 93 | 19.83% |
| positive | 23 | 4 | 19 | 17.39% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
