# Event-Type Performance Report - 2026-10-29

Generated at: 2026-10-29 02:25:51

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **9509**
- Evaluated rows: **7244**
- Success rows: **3302**
- Failure rows: **3942**
- Pending rows: **2265**
- Overall success rate: **45.58%**

## Best Event Types So Far

- `paid_in_capital_increase`: success rate 58.51% from 1887 evaluated cases.
- `lawsuit`: success rate 56.45% from 372 evaluated cases.
- `convertible_bond`: success rate 54.01% from 872 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 23.81% from 105 evaluated cases.
- `merger`: success rate 32.58% from 488 evaluated cases.
- `earnings_guidance`: success rate 32.61% from 46 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2407 | 1887 | 1104 | 783 | 520 | 58.51% | -8.06% | -0.16% | positive |
| major_shareholder_change | 2396 | 1763 | 658 | 1105 | 633 | 37.32% | -10.68% | -0.77% | conservative |
| supply_contract | 1411 | 1085 | 354 | 731 | 326 | 32.63% | -2.58% | -0.67% | conservative |
| convertible_bond | 1205 | 872 | 471 | 401 | 333 | 54.01% | -7.67% | 0.69% | positive |
| merger | 584 | 488 | 159 | 329 | 96 | 32.58% | -9.49% | 0.05% | conservative |
| lawsuit | 493 | 372 | 210 | 162 | 121 | 56.45% | -16.27% | -0.37% | positive |
| investment_decision | 436 | 321 | 169 | 152 | 115 | 52.65% | -4.99% | -0.07% | positive |
| disclosure_violation | 188 | 118 | 51 | 67 | 70 | 43.22% | -20.41% | -0.27% | conservative |
| bond_with_warrant | 117 | 105 | 25 | 80 | 12 | 23.81% | -0.63% | 0.47% | conservative |
| bonus_issue | 105 | 102 | 42 | 60 | 3 | 41.18% | 0.43% | -0.58% | conservative |
| spin_off | 117 | 85 | 44 | 41 | 32 | 51.76% | -25.34% | 1.61% | positive |
| earnings_guidance | 50 | 46 | 15 | 31 | 4 | 32.61% | 0.58% | 0.97% | conservative |

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
