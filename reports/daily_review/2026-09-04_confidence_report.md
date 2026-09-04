# Confidence Report - 2026-09-04

Generated at: 2026-09-04 00:45:08

ML dataset: `data/processed/ml_dataset_20260904.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 1547 |
| Pending rows | 0 |
| Success rows | 1172 |
| Failure rows | 375 |
| Trainable rows | 1547 |
| Overall accuracy | 75.76% |

Current readiness level: **HIGH_CONFIDENCE**

## Readiness Interpretation

The model is showing high confidence based on current data. Continue monitoring for stability.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 691 | 581 | 110 | 84.08% |
| major_shareholder_change | 463 | 281 | 182 | 60.69% |
| convertible_bond | 214 | 144 | 70 | 67.29% |
| lawsuit | 151 | 144 | 7 | 95.36% |
| supply_contract | 24 | 21 | 3 | 87.50% |
| disclosure_violation | 3 | 0 | 3 | 0.00% |
| investment_decision | 1 | 1 | 0 | 100.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 1059 | 869 | 190 | 82.06% |
| volatile | 464 | 282 | 182 | 60.78% |
| positive | 24 | 21 | 3 | 87.50% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
