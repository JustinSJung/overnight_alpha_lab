# Confidence Report - 2026-11-18

Generated at: 2026-11-18 04:50:58

ML dataset: `data/processed/ml_dataset_20261118.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 301 |
| Pending rows | 0 |
| Success rows | 205 |
| Failure rows | 96 |
| Trainable rows | 301 |
| Overall accuracy | 68.11% |

Current readiness level: **MODERATE_CONFIDENCE**

## Readiness Interpretation

The model is showing moderate confidence, but more data is needed before relying on it.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| convertible_bond | 95 | 94 | 1 | 98.95% |
| supply_contract | 83 | 8 | 75 | 9.64% |
| lawsuit | 66 | 64 | 2 | 96.97% |
| paid_in_capital_increase | 28 | 27 | 1 | 96.43% |
| major_shareholder_change | 25 | 10 | 15 | 40.00% |
| investment_decision | 2 | 1 | 1 | 50.00% |
| merger | 1 | 1 | 0 | 100.00% |
| spin_off | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 189 | 185 | 4 | 97.88% |
| positive | 83 | 8 | 75 | 9.64% |
| volatile | 29 | 12 | 17 | 41.38% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
