# Event-Type Performance Report - 2026-10-30

Generated at: 2026-10-30 02:32:23

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **9822**
- Evaluated rows: **7557**
- Success rows: **3489**
- Failure rows: **4068**
- Pending rows: **2265**
- Overall success rate: **46.17%**

## Best Event Types So Far

- `paid_in_capital_increase`: success rate 57.95% from 1962 evaluated cases.
- `convertible_bond`: success rate 57.42% from 970 evaluated cases.
- `lawsuit`: success rate 56.12% from 376 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 25.86% from 58 evaluated cases.
- `supply_contract`: success rate 31.61% from 1139 evaluated cases.
- `merger`: success rate 33.54% from 495 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2482 | 1962 | 1137 | 825 | 520 | 57.95% | -7.82% | -0.18% | positive |
| major_shareholder_change | 2427 | 1794 | 682 | 1112 | 633 | 38.02% | -10.51% | -0.78% | conservative |
| supply_contract | 1465 | 1139 | 360 | 779 | 326 | 31.61% | -2.50% | -0.77% | conservative |
| convertible_bond | 1303 | 970 | 557 | 413 | 333 | 57.42% | -7.22% | 0.53% | positive |
| merger | 591 | 495 | 166 | 329 | 96 | 33.54% | -9.35% | 0.01% | conservative |
| lawsuit | 497 | 376 | 211 | 165 | 121 | 56.12% | -16.88% | -0.38% | positive |
| investment_decision | 439 | 324 | 171 | 153 | 115 | 52.78% | -5.26% | -0.09% | positive |
| bond_with_warrant | 145 | 133 | 53 | 80 | 12 | 39.85% | 0.05% | 0.23% | conservative |
| disclosure_violation | 189 | 119 | 51 | 68 | 70 | 42.86% | -21.08% | -0.27% | conservative |
| bonus_issue | 105 | 102 | 42 | 60 | 3 | 41.18% | 0.43% | -0.58% | conservative |
| spin_off | 117 | 85 | 44 | 41 | 32 | 51.76% | -25.34% | 1.61% | positive |
| earnings_guidance | 62 | 58 | 15 | 43 | 4 | 25.86% | -0.11% | 0.17% | conservative |

## How to Read This Report

- Total: total error-note rows for the event type.
- Evaluated: rows with success or failure status.
- Pending: rows waiting for next trading day price data.
- Success Rate: success / evaluated rows.
- Avg Next Open: average next-day open return.
- Avg Next Close: average next-day close return.
- Bias: confidence adjustment direction based on historical error notes.

## Next Step

The next step is to use this report to improve event-type weights in the daily recommender.
