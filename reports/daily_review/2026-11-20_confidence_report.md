# Confidence Report - 2026-11-20

Generated at: 2026-11-20 04:02:20

ML dataset: `data/processed/ml_dataset_20261120.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 406 |
| Pending rows | 0 |
| Success rows | 258 |
| Failure rows | 148 |
| Trainable rows | 406 |
| Overall accuracy | 63.55% |

Current readiness level: **MODERATE_CONFIDENCE**

## Readiness Interpretation

The model is showing moderate confidence, but more data is needed before relying on it.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| merger | 165 | 64 | 101 | 38.79% |
| lawsuit | 68 | 65 | 3 | 95.59% |
| investment_decision | 65 | 64 | 1 | 98.46% |
| paid_in_capital_increase | 32 | 26 | 6 | 81.25% |
| major_shareholder_change | 24 | 10 | 14 | 41.67% |
| convertible_bond | 22 | 20 | 2 | 90.91% |
| supply_contract | 20 | 0 | 20 | 0.00% |
| disclosure_violation | 9 | 9 | 0 | 100.00% |
| spin_off | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 255 | 138 | 117 | 54.12% |
| negative | 131 | 120 | 11 | 91.60% |
| positive | 20 | 0 | 20 | 0.00% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
