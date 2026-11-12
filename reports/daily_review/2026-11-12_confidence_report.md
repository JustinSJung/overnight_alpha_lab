# Confidence Report - 2026-11-12

Generated at: 2026-11-12 03:55:03

ML dataset: `data/processed/ml_dataset_20261112.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 434 |
| Pending rows | 0 |
| Success rows | 184 |
| Failure rows | 250 |
| Trainable rows | 434 |
| Overall accuracy | 42.40% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 117 | 14 | 103 | 11.97% |
| earnings_guidance | 102 | 0 | 102 | 0.00% |
| major_shareholder_change | 94 | 77 | 17 | 81.91% |
| convertible_bond | 85 | 73 | 12 | 85.88% |
| supply_contract | 12 | 4 | 8 | 33.33% |
| bond_with_warrant | 8 | 8 | 0 | 100.00% |
| investment_decision | 5 | 0 | 5 | 0.00% |
| spin_off | 4 | 4 | 0 | 100.00% |
| merger | 3 | 1 | 2 | 33.33% |
| lawsuit | 2 | 2 | 0 | 100.00% |
| disclosure_violation | 2 | 1 | 1 | 50.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 214 | 98 | 116 | 45.79% |
| volatile | 106 | 82 | 24 | 77.36% |
| neutral_positive | 102 | 0 | 102 | 0.00% |
| positive | 12 | 4 | 8 | 33.33% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
