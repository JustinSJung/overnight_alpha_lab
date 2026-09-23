# Confidence Report - 2026-09-23

Generated at: 2026-09-23 02:02:32

ML dataset: `data/processed/ml_dataset_20260923.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 638 |
| Pending rows | 0 |
| Success rows | 108 |
| Failure rows | 530 |
| Trainable rows | 638 |
| Overall accuracy | 16.93% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| convertible_bond | 330 | 69 | 261 | 20.91% |
| paid_in_capital_increase | 160 | 10 | 150 | 6.25% |
| major_shareholder_change | 93 | 9 | 84 | 9.68% |
| supply_contract | 30 | 12 | 18 | 40.00% |
| merger | 10 | 1 | 9 | 10.00% |
| investment_decision | 7 | 2 | 5 | 28.57% |
| lawsuit | 4 | 2 | 2 | 50.00% |
| spin_off | 2 | 2 | 0 | 100.00% |
| disclosure_violation | 1 | 1 | 0 | 100.00% |
| bonus_issue | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 495 | 82 | 413 | 16.57% |
| volatile | 112 | 14 | 98 | 12.50% |
| positive | 31 | 12 | 19 | 38.71% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
