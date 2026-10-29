# Confidence Report - 2026-09-30

Generated at: 2026-09-30 02:55:43

ML dataset: `data/processed/ml_dataset_20260930.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 1015 |
| Pending rows | 0 |
| Success rows | 423 |
| Failure rows | 592 |
| Trainable rows | 1015 |
| Overall accuracy | 41.67% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| merger | 518 | 128 | 390 | 24.71% |
| paid_in_capital_increase | 162 | 20 | 142 | 12.35% |
| lawsuit | 149 | 146 | 3 | 97.99% |
| bonus_issue | 96 | 96 | 0 | 100.00% |
| major_shareholder_change | 39 | 10 | 29 | 25.64% |
| supply_contract | 32 | 17 | 15 | 53.12% |
| investment_decision | 11 | 2 | 9 | 18.18% |
| convertible_bond | 5 | 3 | 2 | 60.00% |
| spin_off | 2 | 1 | 1 | 50.00% |
| disclosure_violation | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 570 | 141 | 429 | 24.74% |
| negative | 317 | 169 | 148 | 53.31% |
| positive | 128 | 113 | 15 | 88.28% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
