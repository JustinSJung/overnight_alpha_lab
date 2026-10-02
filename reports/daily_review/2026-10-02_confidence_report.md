# Confidence Report - 2026-10-02

Generated at: 2026-10-02 03:11:23

ML dataset: `data/processed/ml_dataset_20261002.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 486 |
| Pending rows | 0 |
| Success rows | 382 |
| Failure rows | 104 |
| Trainable rows | 486 |
| Overall accuracy | 78.60% |

Current readiness level: **HIGH_CONFIDENCE**

## Readiness Interpretation

The model is showing high confidence based on current data. Continue monitoring for stability.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| paid_in_capital_increase | 266 | 259 | 7 | 97.37% |
| major_shareholder_change | 92 | 81 | 11 | 88.04% |
| merger | 76 | 9 | 67 | 11.84% |
| supply_contract | 21 | 9 | 12 | 42.86% |
| convertible_bond | 14 | 14 | 0 | 100.00% |
| lawsuit | 9 | 9 | 0 | 100.00% |
| investment_decision | 2 | 1 | 1 | 50.00% |
| bonus_issue | 2 | 0 | 2 | 0.00% |
| disclosure_violation | 2 | 0 | 2 | 0.00% |
| spin_off | 2 | 0 | 2 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| negative | 291 | 282 | 9 | 96.91% |
| volatile | 172 | 91 | 81 | 52.91% |
| positive | 23 | 9 | 14 | 39.13% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
