# Confidence Report - 2026-11-03

Generated at: 2026-11-03 04:09:33

ML dataset: `data/processed/ml_dataset_20261103.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 551 |
| Pending rows | 0 |
| Success rows | 256 |
| Failure rows | 295 |
| Trainable rows | 551 |
| Overall accuracy | 46.46% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| supply_contract | 187 | 110 | 77 | 58.82% |
| paid_in_capital_increase | 162 | 1 | 161 | 0.62% |
| merger | 85 | 68 | 17 | 80.00% |
| major_shareholder_change | 73 | 51 | 22 | 69.86% |
| investment_decision | 24 | 19 | 5 | 79.17% |
| disclosure_violation | 12 | 2 | 10 | 16.67% |
| convertible_bond | 8 | 5 | 3 | 62.50% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| positive | 187 | 110 | 77 | 58.82% |
| volatile | 182 | 138 | 44 | 75.82% |
| negative | 182 | 8 | 174 | 4.40% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
