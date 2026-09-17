# Confidence Report - 2026-09-17

Generated at: 2026-09-17 01:41:27

ML dataset: `data/processed/ml_dataset_20260917.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 320 |
| Pending rows | 0 |
| Success rows | 84 |
| Failure rows | 236 |
| Trainable rows | 320 |
| Overall accuracy | 26.25% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 179 | 41 | 138 | 22.91% |
| major_shareholder_change | 72 | 16 | 56 | 22.22% |
| disclosure_violation | 17 | 16 | 1 | 94.12% |
| lawsuit | 16 | 0 | 16 | 0.00% |
| investment_decision | 13 | 1 | 12 | 7.69% |
| supply_contract | 12 | 7 | 5 | 58.33% |
| bonus_issue | 6 | 0 | 6 | 0.00% |
| spin_off | 2 | 1 | 1 | 50.00% |
| convertible_bond | 1 | 1 | 0 | 100.00% |
| merger | 1 | 1 | 0 | 100.00% |
| bond_with_warrant | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 214 | 58 | 156 | 27.10% |
| volatile | 88 | 19 | 69 | 21.59% |
| positive | 18 | 7 | 11 | 38.89% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
