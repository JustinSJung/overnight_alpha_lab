# Event-Type Performance Report - 2026-11-13

Generated at: 2026-11-13 04:20:52

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **12104**
- Evaluated rows: **9833**
- Success rows: **4537**
- Failure rows: **5296**
- Pending rows: **2271**
- Overall success rate: **46.14%**

## Best Event Types So Far

- `convertible_bond`: success rate 57.19% from 1210 evaluated cases.
- `paid_in_capital_increase`: success rate 54.94% from 2370 evaluated cases.
- `investment_decision`: success rate 51.15% from 477 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 23.26% from 86 evaluated cases.
- `supply_contract`: success rate 36.75% from 1442 evaluated cases.
- `major_shareholder_change`: success rate 37.75% from 2477 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| major_shareholder_change | 3111 | 2477 | 935 | 1542 | 634 | 37.75% | -14.73% | -0.66% | conservative |
| paid_in_capital_increase | 2891 | 2370 | 1302 | 1068 | 521 | 54.94% | -8.25% | -0.13% | positive |
| supply_contract | 1768 | 1442 | 530 | 912 | 326 | 36.75% | -2.59% | -0.55% | conservative |
| convertible_bond | 1543 | 1210 | 692 | 518 | 333 | 57.19% | -6.70% | 0.55% | positive |
| merger | 858 | 762 | 352 | 410 | 96 | 46.19% | -2.53% | 5.04% | conservative |
| lawsuit | 609 | 488 | 238 | 250 | 121 | 48.77% | -17.88% | -0.26% | conservative |
| investment_decision | 592 | 477 | 244 | 233 | 115 | 51.15% | -5.12% | 0.25% | positive |
| disclosure_violation | 214 | 144 | 59 | 85 | 70 | 40.97% | -22.30% | -0.34% | conservative |
| bond_with_warrant | 154 | 142 | 62 | 80 | 12 | 43.66% | -0.08% | 0.05% | conservative |
| spin_off | 155 | 119 | 47 | 72 | 36 | 39.50% | -20.82% | 0.89% | conservative |
| bonus_issue | 119 | 116 | 56 | 60 | 3 | 48.28% | 2.27% | 0.38% | conservative |
| earnings_guidance | 90 | 86 | 20 | 66 | 4 | 23.26% | -0.15% | -1.74% | conservative |

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
