# Confidence Report - 2026-09-03

Generated at: 2026-09-03 00:55:17

ML dataset: `data/processed/ml_dataset_20260903.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 2275 |
| Pending rows | 0 |
| Success rows | 2003 |
| Failure rows | 272 |
| Trainable rows | 2275 |
| Overall accuracy | 88.04% |

Current readiness level: **HIGH_CONFIDENCE**

## Readiness Interpretation

The model is showing high confidence based on current data. Continue monitoring for stability.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 1948 | 1819 | 129 | 93.38% |
| bonus_issue | 114 | 96 | 18 | 84.21% |
| supply_contract | 81 | 3 | 78 | 3.70% |
| investment_decision | 67 | 64 | 3 | 95.52% |
| major_shareholder_change | 40 | 5 | 35 | 12.50% |
| convertible_bond | 12 | 11 | 1 | 91.67% |
| lawsuit | 9 | 5 | 4 | 55.56% |
| merger | 3 | 0 | 3 | 0.00% |
| disclosure_violation | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 1970 | 1835 | 135 | 93.15% |
| positive | 195 | 99 | 96 | 50.77% |
| volatile | 110 | 69 | 41 | 62.73% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
