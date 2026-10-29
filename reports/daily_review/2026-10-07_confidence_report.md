# Confidence Report - 2026-10-07

Generated at: 2026-10-07 02:54:09

ML dataset: `data/processed/ml_dataset_20261007.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 952 |
| Pending rows | 0 |
| Success rows | 205 |
| Failure rows | 747 |
| Trainable rows | 952 |
| Overall accuracy | 21.53% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| merger | 595 | 2 | 593 | 0.34% |
| paid_in_capital_increase | 117 | 108 | 9 | 92.31% |
| major_shareholder_change | 98 | 73 | 25 | 74.49% |
| lawsuit | 73 | 5 | 68 | 6.85% |
| supply_contract | 44 | 4 | 40 | 9.09% |
| convertible_bond | 14 | 9 | 5 | 64.29% |
| investment_decision | 6 | 3 | 3 | 50.00% |
| bond_with_warrant | 2 | 0 | 2 | 0.00% |
| bonus_issue | 2 | 0 | 2 | 0.00% |
| spin_off | 1 | 1 | 0 | 100.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 700 | 79 | 621 | 11.29% |
| negative | 206 | 122 | 84 | 59.22% |
| positive | 46 | 4 | 42 | 8.70% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
