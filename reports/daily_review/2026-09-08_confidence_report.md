# Confidence Report - 2026-09-08

Generated at: 2026-09-08 01:05:24

ML dataset: `data/processed/ml_dataset_20260908.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 441 |
| Pending rows | 0 |
| Success rows | 302 |
| Failure rows | 139 |
| Trainable rows | 441 |
| Overall accuracy | 68.48% |

Current readiness level: **MODERATE_CONFIDENCE**

## Readiness Interpretation

The model is showing moderate confidence, but more data is needed before relying on it.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| major_shareholder_change | 191 | 147 | 44 | 76.96% |
| paid_in_capital_increase | 151 | 144 | 7 | 95.36% |
| investment_decision | 71 | 0 | 71 | 0.00% |
| supply_contract | 19 | 6 | 13 | 31.58% |
| convertible_bond | 3 | 3 | 0 | 100.00% |
| disclosure_violation | 3 | 0 | 3 | 0.00% |
| lawsuit | 2 | 1 | 1 | 50.00% |
| spin_off | 1 | 1 | 0 | 100.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 263 | 148 | 115 | 56.27% |
| negative | 159 | 148 | 11 | 93.08% |
| positive | 19 | 6 | 13 | 31.58% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
