# Event-Type Performance Report - 2026-11-16

Generated at: 2026-11-16 02:53:27

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **12235**
- Evaluated rows: **9964**
- Success rows: **4580**
- Failure rows: **5384**
- Pending rows: **2271**
- Overall success rate: **45.97%**

## Best Event Types So Far

- `convertible_bond`: success rate 56.47% from 1236 evaluated cases.
- `paid_in_capital_increase`: success rate 54.88% from 2385 evaluated cases.
- `investment_decision`: success rate 50.83% from 484 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 23.26% from 86 evaluated cases.
- `supply_contract`: success rate 36.44% from 1460 evaluated cases.
- `major_shareholder_change`: success rate 37.84% from 2524 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| major_shareholder_change | 3158 | 2524 | 955 | 1569 | 634 | 37.84% | -14.87% | -0.67% | conservative |
| paid_in_capital_increase | 2906 | 2385 | 1309 | 1076 | 521 | 54.88% | -8.25% | -0.12% | positive |
| supply_contract | 1786 | 1460 | 532 | 928 | 326 | 36.44% | -2.54% | -0.57% | conservative |
| convertible_bond | 1569 | 1236 | 698 | 538 | 333 | 56.47% | -7.93% | 0.52% | positive |
| merger | 862 | 766 | 354 | 412 | 96 | 46.21% | -2.51% | 5.01% | conservative |
| lawsuit | 613 | 492 | 239 | 253 | 121 | 48.58% | -18.14% | -0.26% | conservative |
| investment_decision | 599 | 484 | 246 | 238 | 115 | 50.83% | -6.08% | 0.21% | positive |
| bond_with_warrant | 161 | 149 | 63 | 86 | 12 | 42.28% | -4.10% | 0.01% | conservative |
| disclosure_violation | 217 | 147 | 61 | 86 | 70 | 41.50% | -21.88% | -0.48% | conservative |
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
