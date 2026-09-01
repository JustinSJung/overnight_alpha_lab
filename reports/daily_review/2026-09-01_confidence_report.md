# Confidence Report - 2026-09-01

Generated at: 2026-09-01 02:02:00

ML dataset: `data/processed/ml_dataset_20260901.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 945 |
| Pending rows | 0 |
| Success rows | 523 |
| Failure rows | 422 |
| Trainable rows | 945 |
| Overall accuracy | 55.34% |

Current readiness level: **WATCHLIST**

## Readiness Interpretation

The model is showing some predictive signal, but it still needs monitoring.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 359 | 226 | 133 | 62.95% |
| supply_contract | 349 | 112 | 237 | 32.09% |
| major_shareholder_change | 106 | 74 | 32 | 69.81% |
| lawsuit | 68 | 66 | 2 | 97.06% |
| convertible_bond | 35 | 31 | 4 | 88.57% |
| investment_decision | 18 | 10 | 8 | 55.56% |
| merger | 6 | 1 | 5 | 16.67% |
| disclosure_violation | 2 | 1 | 1 | 50.00% |
| bond_with_warrant | 1 | 1 | 0 | 100.00% |
| spin_off | 1 | 1 | 0 | 100.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 465 | 325 | 140 | 69.89% |
| positive | 349 | 112 | 237 | 32.09% |
| volatile | 131 | 86 | 45 | 65.65% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
