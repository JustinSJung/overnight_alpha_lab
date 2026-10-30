# Confidence Report - 2026-10-30

Generated at: 2026-10-30 02:32:19

ML dataset: `data/processed/ml_dataset_20261030.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 2799 |
| Pending rows | 0 |
| Success rows | 2308 |
| Failure rows | 491 |
| Trainable rows | 2799 |
| Overall accuracy | 82.46% |

Current readiness level: **HIGH_CONFIDENCE**

## Readiness Interpretation

The model is showing high confidence based on current data. Continue monitoring for stability.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| convertible_bond | 1976 | 1958 | 18 | 99.09% |
| paid_in_capital_increase | 453 | 167 | 286 | 36.87% |
| supply_contract | 169 | 6 | 163 | 3.55% |
| major_shareholder_change | 143 | 136 | 7 | 95.10% |
| bond_with_warrant | 28 | 28 | 0 | 100.00% |
| earnings_guidance | 12 | 0 | 12 | 0.00% |
| merger | 10 | 10 | 0 | 100.00% |
| lawsuit | 4 | 1 | 3 | 25.00% |
| investment_decision | 3 | 2 | 1 | 66.67% |
| disclosure_violation | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 2462 | 2154 | 308 | 87.49% |
| positive | 169 | 6 | 163 | 3.55% |
| volatile | 156 | 148 | 8 | 94.87% |
| neutral_positive | 12 | 0 | 12 | 0.00% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
