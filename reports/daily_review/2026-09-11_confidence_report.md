# Confidence Report - 2026-09-11

Generated at: 2026-09-11 01:09:55

ML dataset: `data/processed/ml_dataset_20260911.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 856 |
| Pending rows | 0 |
| Success rows | 309 |
| Failure rows | 547 |
| Trainable rows | 856 |
| Overall accuracy | 36.10% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 530 | 207 | 323 | 39.06% |
| merger | 128 | 64 | 64 | 50.00% |
| supply_contract | 94 | 12 | 82 | 12.77% |
| major_shareholder_change | 56 | 8 | 48 | 14.29% |
| convertible_bond | 36 | 10 | 26 | 27.78% |
| disclosure_violation | 4 | 4 | 0 | 100.00% |
| investment_decision | 3 | 2 | 1 | 66.67% |
| lawsuit | 3 | 2 | 1 | 66.67% |
| spin_off | 2 | 0 | 2 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 573 | 223 | 350 | 38.92% |
| volatile | 189 | 74 | 115 | 39.15% |
| positive | 94 | 12 | 82 | 12.77% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
