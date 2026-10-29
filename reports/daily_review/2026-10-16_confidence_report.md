# Confidence Report - 2026-10-16

Generated at: 2026-10-16 00:50:14

ML dataset: `data/processed/ml_dataset_20261016.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 577 |
| Pending rows | 0 |
| Success rows | 106 |
| Failure rows | 471 |
| Trainable rows | 577 |
| Overall accuracy | 18.37% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| merger | 228 | 2 | 226 | 0.88% |
| convertible_bond | 171 | 1 | 170 | 0.58% |
| major_shareholder_change | 74 | 40 | 34 | 54.05% |
| supply_contract | 49 | 42 | 7 | 85.71% |
| bond_with_warrant | 21 | 0 | 21 | 0.00% |
| spin_off | 20 | 20 | 0 | 100.00% |
| paid_in_capital_increase | 11 | 1 | 10 | 9.09% |
| disclosure_violation | 2 | 0 | 2 | 0.00% |
| lawsuit | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 322 | 62 | 260 | 19.25% |
| negative | 206 | 2 | 204 | 0.97% |
| positive | 49 | 42 | 7 | 85.71% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
