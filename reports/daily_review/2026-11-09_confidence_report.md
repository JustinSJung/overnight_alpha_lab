# Confidence Report - 2026-11-09

Generated at: 2026-11-09 02:28:12

ML dataset: `data/processed/ml_dataset_20261109.csv`

## Overall Status

| Metric | Value |
|---|---:|
| Total rows | 818 |
| Pending rows | 0 |
| Success rows | 378 |
| Failure rows | 440 |
| Trainable rows | 818 |
| Overall accuracy | 46.21% |

Current readiness level: **LOW_CONFIDENCE**

## Readiness Interpretation

The model has enough samples to evaluate, but current accuracy is weak.

## Success Rate by Event Type

| event_type | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| supply_contract | 293 | 276 | 17 | 94.20% |
| major_shareholder_change | 231 | 12 | 219 | 5.19% |
| paid_in_capital_increase | 119 | 11 | 108 | 9.24% |
| convertible_bond | 97 | 75 | 22 | 77.32% |
| lawsuit | 65 | 1 | 64 | 1.54% |
| merger | 10 | 1 | 9 | 10.00% |
| bonus_issue | 2 | 2 | 0 | 100.00% |
| investment_decision | 1 | 0 | 1 | 0.00% |

## Success Rate by Prediction Direction

| prediction_direction | total_rows | success_rows | failure_rows | success_rate |
|---|---|---|---|---|
| positive | 295 | 278 | 17 | 94.24% |
| negative | 281 | 87 | 194 | 30.96% |
| volatile | 242 | 13 | 229 | 5.37% |

## Next Step

Continue running the daily pipeline and catch-up script. As pending rows become success/failure rows, the confidence report will become more meaningful.
