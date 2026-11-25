# Event-Type Performance Report - 2026-11-25

Generated at: 2026-11-25 05:31:01

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **13327**
- Evaluated rows: **11056**
- Success rows: **5238**
- Failure rows: **5818**
- Pending rows: **2271**
- Overall success rate: **47.38%**

## Best Event Types So Far

- `convertible_bond`: success rate 59.72% from 1378 evaluated cases.
- `paid_in_capital_increase`: success rate 56.51% from 2651 evaluated cases.
- `lawsuit`: success rate 51.54% from 551 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 26.09% from 92 evaluated cases.
- `supply_contract`: success rate 35.64% from 1678 evaluated cases.
- `spin_off`: success rate 39.02% from 123 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| major_shareholder_change | 3414 | 2780 | 1113 | 1667 | 634 | 40.04% | -13.82% | -0.81% | conservative |
| paid_in_capital_increase | 3172 | 2651 | 1498 | 1153 | 521 | 56.51% | -7.41% | -0.23% | positive |
| supply_contract | 2004 | 1678 | 598 | 1080 | 326 | 35.64% | -2.43% | -0.70% | conservative |
| convertible_bond | 1711 | 1378 | 823 | 555 | 333 | 59.72% | -7.49% | 0.16% | positive |
| merger | 922 | 826 | 382 | 444 | 96 | 46.25% | -2.83% | 4.82% | conservative |
| lawsuit | 672 | 551 | 284 | 267 | 121 | 51.54% | -17.15% | -0.42% | positive |
| investment_decision | 662 | 547 | 279 | 268 | 115 | 51.01% | -5.46% | 0.16% | positive |
| disclosure_violation | 232 | 162 | 70 | 92 | 70 | 43.21% | -21.06% | -0.85% | conservative |
| bond_with_warrant | 163 | 151 | 63 | 88 | 12 | 41.72% | -4.04% | 0.04% | conservative |
| spin_off | 159 | 123 | 48 | 75 | 36 | 39.02% | -20.11% | 0.81% | conservative |
| bonus_issue | 120 | 117 | 56 | 61 | 3 | 47.86% | 2.30% | 0.36% | conservative |
| earnings_guidance | 96 | 92 | 24 | 68 | 4 | 26.09% | -0.16% | -1.87% | conservative |

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
