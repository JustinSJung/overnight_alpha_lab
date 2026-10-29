# Event-Type Performance Report - 2026-10-15

Generated at: 2026-10-15 01:06:54

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **7756**
- Evaluated rows: **5494**
- Success rows: **2415**
- Failure rows: **3079**
- Pending rows: **2262**
- Overall success rate: **43.96%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 4 evaluated cases.
- `paid_in_capital_increase`: success rate 57.03% from 1550 evaluated cases.
- `lawsuit`: success rate 56.73% from 275 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 20.27% from 74 evaluated cases.
- `merger`: success rate 21.01% from 276 evaluated cases.
- `supply_contract`: success rate 27.33% from 805 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2070 | 1550 | 884 | 666 | 520 | 57.03% | -7.22% | 0.18% | positive |
| major_shareholder_change | 1946 | 1313 | 454 | 859 | 633 | 34.58% | -13.43% | -0.76% | conservative |
| supply_contract | 1131 | 805 | 220 | 585 | 326 | 27.33% | -2.81% | -0.97% | conservative |
| convertible_bond | 1019 | 687 | 377 | 310 | 332 | 54.88% | -5.76% | 0.81% | positive |
| merger | 371 | 276 | 58 | 218 | 95 | 21.01% | -15.18% | 0.60% | conservative |
| lawsuit | 395 | 275 | 156 | 119 | 120 | 56.73% | -13.97% | -0.52% | positive |
| investment_decision | 381 | 266 | 143 | 123 | 115 | 53.76% | -6.15% | -0.06% | positive |
| bonus_issue | 102 | 99 | 41 | 58 | 3 | 41.41% | 0.45% | -0.40% | conservative |
| disclosure_violation | 155 | 85 | 42 | 43 | 70 | 49.41% | -13.36% | -0.37% | conservative |
| bond_with_warrant | 86 | 74 | 15 | 59 | 12 | 20.27% | -0.79% | -0.04% | conservative |
| spin_off | 92 | 60 | 21 | 39 | 32 | 35.00% | -36.81% | 0.14% | conservative |
| earnings_guidance | 8 | 4 | 4 | 0 | 4 | 100.00% | 2.69% | 1.92% | positive |

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
