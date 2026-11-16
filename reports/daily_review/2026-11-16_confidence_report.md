# Confidence Report - 2026-11-16

Generated at: 2026-11-16 02:53:24

ML dataset: `data/processed/ml_dataset_20261116.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 131 |
| Pending rows | 0 |
| Success rows | 43 |
| Failure rows | 88 |
| Trainable rows | 131 |
| Overall accuracy | 32.82% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| major_shareholder_change | 47 | 20 | 27 | 42.55% |
| convertible_bond | 26 | 6 | 20 | 23.08% |
| supply_contract | 18 | 2 | 16 | 11.11% |
| paid_in_capital_increase | 15 | 7 | 8 | 46.67% |
| investment_decision | 7 | 2 | 5 | 28.57% |
| bond_with_warrant | 7 | 1 | 6 | 14.29% |
| merger | 4 | 2 | 2 | 50.00% |
| lawsuit | 4 | 1 | 3 | 25.00% |
| disclosure_violation | 3 | 2 | 1 | 66.67% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 58 | 24 | 34 | 41.38% |
| negative | 55 | 17 | 38 | 30.91% |
| positive | 18 | 2 | 16 | 11.11% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
