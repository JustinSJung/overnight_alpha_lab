# Confidence Report - 2026-11-11

Generated at: 2026-11-11 06:03:13

ML dataset: `data/processed/ml_dataset_20261111.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 1290 |
| Pending rows | 0 |
| Success rows | 972 |
| Failure rows | 318 |
| Trainable rows | 1290 |
| Overall accuracy | 75.35% |

Current readiness level: **HIGH_CONFIDENCE**

## Readiness Interpretation

The model is showing high confidence based on current data. Continue monitoring for stability.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| convertible_bond | 797 | 731 | 66 | 91.72% |
| merger | 135 | 3 | 132 | 2.22% |
| paid_in_capital_increase | 124 | 40 | 84 | 32.26% |
| bonus_issue | 96 | 96 | 0 | 100.00% |
| supply_contract | 81 | 77 | 4 | 95.06% |
| major_shareholder_change | 35 | 17 | 18 | 48.57% |
| lawsuit | 10 | 6 | 4 | 60.00% |
| investment_decision | 9 | 2 | 7 | 22.22% |
| earnings_guidance | 2 | 0 | 2 | 0.00% |
| disclosure_violation | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 932 | 777 | 155 | 83.37% |
| volatile | 179 | 22 | 157 | 12.29% |
| positive | 177 | 173 | 4 | 97.74% |
| neutral_positive | 2 | 0 | 2 | 0.00% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
