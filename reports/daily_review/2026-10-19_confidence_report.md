# Confidence Report - 2026-10-19

Generated at: 2026-10-19 00:40:06

ML dataset: `data/processed/ml_dataset_20261019.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 1913 |
| Pending rows | 0 |
| Success rows | 1580 |
| Failure rows | 333 |
| Trainable rows | 1913 |
| Overall accuracy | 82.59% |

Current readiness level: **HIGH_CONFIDENCE**

## Readiness Interpretation

The model is showing high confidence based on current data. Continue monitoring for stability.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 1644 | 1536 | 108 | 93.43% |
| major_shareholder_change | 195 | 7 | 188 | 3.59% |
| supply_contract | 19 | 6 | 13 | 31.58% |
| convertible_bond | 16 | 5 | 11 | 31.25% |
| lawsuit | 12 | 11 | 1 | 91.67% |
| bond_with_warrant | 9 | 9 | 0 | 100.00% |
| disclosure_violation | 9 | 6 | 3 | 66.67% |
| merger | 8 | 0 | 8 | 0.00% |
| investment_decision | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 1690 | 1567 | 123 | 92.72% |
| volatile | 204 | 7 | 197 | 3.43% |
| positive | 19 | 6 | 13 | 31.58% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
