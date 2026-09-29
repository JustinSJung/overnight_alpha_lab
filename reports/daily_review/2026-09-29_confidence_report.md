# Confidence Report - 2026-09-29

Generated at: 2026-09-29 03:32:21

ML dataset: `data/processed/ml_dataset_20260929.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 1470 |
| Pending rows | 0 |
| Success rows | 913 |
| Failure rows | 557 |
| Trainable rows | 1470 |
| Overall accuracy | 62.11% |

Current readiness level: **MODERATE_CONFIDENCE**

## Readiness Interpretation

The model is showing moderate confidence, but more data is needed before relying on it.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| convertible_bond | 827 | 817 | 10 | 98.79% |
| lawsuit | 211 | 2 | 209 | 0.95% |
| paid_in_capital_increase | 173 | 8 | 165 | 4.62% |
| supply_contract | 155 | 8 | 147 | 5.16% |
| investment_decision | 67 | 67 | 0 | 100.00% |
| major_shareholder_change | 30 | 9 | 21 | 30.00% |
| merger | 3 | 0 | 3 | 0.00% |
| bond_with_warrant | 2 | 1 | 1 | 50.00% |
| disclosure_violation | 1 | 1 | 0 | 100.00% |
| spin_off | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 1214 | 829 | 385 | 68.29% |
| positive | 155 | 8 | 147 | 5.16% |
| volatile | 101 | 76 | 25 | 75.25% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
