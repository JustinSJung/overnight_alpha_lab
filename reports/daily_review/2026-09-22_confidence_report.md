# Confidence Report - 2026-09-22

Generated at: 2026-09-22 02:11:37

ML dataset: `data/processed/ml_dataset_20260922.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 2575 |
| Pending rows | 0 |
| Success rows | 275 |
| Failure rows | 2300 |
| Trainable rows | 2575 |
| Overall accuracy | 10.68% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 1634 | 170 | 1464 | 10.40% |
| convertible_bond | 346 | 11 | 335 | 3.18% |
| bond_with_warrant | 324 | 4 | 320 | 1.23% |
| supply_contract | 92 | 8 | 84 | 8.70% |
| lawsuit | 84 | 74 | 10 | 88.10% |
| major_shareholder_change | 83 | 3 | 80 | 3.61% |
| investment_decision | 6 | 2 | 4 | 33.33% |
| disclosure_violation | 3 | 3 | 0 | 100.00% |
| merger | 3 | 0 | 3 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 2391 | 262 | 2129 | 10.96% |
| positive | 92 | 8 | 84 | 8.70% |
| volatile | 92 | 5 | 87 | 5.43% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
