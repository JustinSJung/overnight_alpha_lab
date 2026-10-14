# Confidence Report - 2026-10-14

Generated at: 2026-10-14 02:04:02

ML dataset: `data/processed/ml_dataset_20261014.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 783 |
| Pending rows | 0 |
| Success rows | 54 |
| Failure rows | 729 |
| Trainable rows | 783 |
| Overall accuracy | 6.90% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 362 | 15 | 347 | 4.14% |
| major_shareholder_change | 301 | 1 | 300 | 0.33% |
| supply_contract | 84 | 8 | 76 | 9.52% |
| convertible_bond | 13 | 11 | 2 | 84.62% |
| bond_with_warrant | 9 | 9 | 0 | 100.00% |
| investment_decision | 5 | 5 | 0 | 100.00% |
| merger | 4 | 1 | 3 | 25.00% |
| earnings_guidance | 2 | 2 | 0 | 100.00% |
| lawsuit | 2 | 2 | 0 | 100.00% |
| disclosure_violation | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 387 | 37 | 350 | 9.56% |
| volatile | 310 | 7 | 303 | 2.26% |
| positive | 84 | 8 | 76 | 9.52% |
| neutral_positive | 2 | 2 | 0 | 100.00% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
