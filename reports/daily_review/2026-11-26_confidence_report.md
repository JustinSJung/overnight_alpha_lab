# Confidence Report - 2026-11-26

Generated at: 2026-11-26 05:02:11

ML dataset: `data/processed/ml_dataset_20261126.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 2861 |
| Pending rows | 0 |
| Success rows | 2718 |
| Failure rows | 143 |
| Trainable rows | 2861 |
| Overall accuracy | 95.00% |

Current readiness level: **HIGH_CONFIDENCE**

## Readiness Interpretation

The model is showing high confidence based on current data. Continue monitoring for stability.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| merger | 2516 | 2514 | 2 | 99.92% |
| paid_in_capital_increase | 101 | 0 | 101 | 0.00% |
| bonus_issue | 96 | 96 | 0 | 100.00% |
| supply_contract | 82 | 76 | 6 | 92.68% |
| major_shareholder_change | 39 | 13 | 26 | 33.33% |
| convertible_bond | 10 | 8 | 2 | 80.00% |
| lawsuit | 7 | 4 | 3 | 57.14% |
| investment_decision | 5 | 3 | 2 | 60.00% |
| earnings_guidance | 4 | 4 | 0 | 100.00% |
| disclosure_violation | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 2560 | 2530 | 30 | 98.83% |
| positive | 178 | 172 | 6 | 96.63% |
| negative | 119 | 12 | 107 | 10.08% |
| neutral_positive | 4 | 4 | 0 | 100.00% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
