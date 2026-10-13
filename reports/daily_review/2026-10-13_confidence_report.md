# Confidence Report - 2026-10-13

Generated at: 2026-10-13 03:54:05

ML dataset: `data/processed/ml_dataset_20261013.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 441 |
| Pending rows | 0 |
| Success rows | 312 |
| Failure rows | 129 |
| Trainable rows | 441 |
| Overall accuracy | 70.75% |

Current readiness level: **HIGH_CONFIDENCE**

## Readiness Interpretation

The model is showing high confidence based on current data. Continue monitoring for stability.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 250 | 245 | 5 | 98.00% |
| supply_contract | 92 | 2 | 90 | 2.17% |
| major_shareholder_change | 47 | 39 | 8 | 82.98% |
| convertible_bond | 19 | 8 | 11 | 42.11% |
| bonus_issue | 9 | 0 | 9 | 0.00% |
| lawsuit | 8 | 8 | 0 | 100.00% |
| investment_decision | 7 | 5 | 2 | 71.43% |
| disclosure_violation | 5 | 3 | 2 | 60.00% |
| spin_off | 3 | 2 | 1 | 66.67% |
| merger | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 282 | 264 | 18 | 93.62% |
| positive | 101 | 2 | 99 | 1.98% |
| volatile | 58 | 46 | 12 | 79.31% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
