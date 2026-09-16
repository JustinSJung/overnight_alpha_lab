# Confidence Report - 2026-09-16

Generated at: 2026-09-16 01:20:08

ML dataset: `data/processed/ml_dataset_20260916.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 1362 |
| Pending rows | 0 |
| Success rows | 1003 |
| Failure rows | 359 |
| Trainable rows | 1362 |
| Overall accuracy | 73.64% |

Current readiness level: **HIGH_CONFIDENCE**

## Readiness Interpretation

The model is showing high confidence based on current data. Continue monitoring for stability.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| major_shareholder_change | 676 | 549 | 127 | 81.21% |
| paid_in_capital_increase | 552 | 356 | 196 | 64.49% |
| convertible_bond | 47 | 42 | 5 | 89.36% |
| supply_contract | 42 | 16 | 26 | 38.10% |
| investment_decision | 27 | 26 | 1 | 96.30% |
| lawsuit | 7 | 6 | 1 | 85.71% |
| spin_off | 6 | 5 | 1 | 83.33% |
| disclosure_violation | 3 | 2 | 1 | 66.67% |
| bonus_issue | 1 | 1 | 0 | 100.00% |
| merger | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 710 | 580 | 130 | 81.69% |
| negative | 609 | 406 | 203 | 66.67% |
| positive | 43 | 17 | 26 | 39.53% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
