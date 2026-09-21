# Confidence Report - 2026-09-21

Generated at: 2026-09-21 01:03:36

ML dataset: `data/processed/ml_dataset_20260921.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 1120 |
| Pending rows | 0 |
| Success rows | 88 |
| Failure rows | 1032 |
| Trainable rows | 1120 |
| Overall accuracy | 7.86% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| investment_decision | 832 | 2 | 830 | 0.24% |
| lawsuit | 77 | 8 | 69 | 10.39% |
| merger | 70 | 3 | 67 | 4.29% |
| major_shareholder_change | 41 | 16 | 25 | 39.02% |
| paid_in_capital_increase | 40 | 32 | 8 | 80.00% |
| supply_contract | 30 | 9 | 21 | 30.00% |
| convertible_bond | 26 | 18 | 8 | 69.23% |
| spin_off | 3 | 0 | 3 | 0.00% |
| disclosure_violation | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| volatile | 946 | 21 | 925 | 2.22% |
| negative | 144 | 58 | 86 | 40.28% |
| positive | 30 | 9 | 21 | 30.00% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
