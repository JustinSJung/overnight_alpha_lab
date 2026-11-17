# Confidence Report - 2026-11-17

Generated at: 2026-11-17 05:39:52

ML dataset: `data/processed/ml_dataset_20261117.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 628 |
| Pending rows | 0 |
| Success rows | 370 |
| Failure rows | 258 |
| Trainable rows | 628 |
| Overall accuracy | 58.92% |

Current readiness level: **WATCHLIST**

## Readiness Interpretation

The model is showing some predictive signal, but it still needs monitoring.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| supply_contract | 313 | 100 | 213 | 31.95% |
| convertible_bond | 126 | 124 | 2 | 98.41% |
| paid_in_capital_increase | 115 | 108 | 7 | 93.91% |
| major_shareholder_change | 46 | 23 | 23 | 50.00% |
| lawsuit | 7 | 7 | 0 | 100.00% |
| merger | 7 | 0 | 7 | 0.00% |
| earnings_guidance | 6 | 4 | 2 | 66.67% |
| investment_decision | 6 | 4 | 2 | 66.67% |
| bond_with_warrant | 1 | 0 | 1 | 0.00% |
| disclosure_violation | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| positive | 313 | 100 | 213 | 31.95% |
| negative | 250 | 239 | 11 | 95.60% |
| volatile | 59 | 27 | 32 | 45.76% |
| neutral_positive | 6 | 4 | 2 | 66.67% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
