# Event-Type Performance Report - 2026-11-19

Generated at: 2026-11-19 04:22:44

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **12668**
- Evaluated rows: **10397**
- Success rows: **4842**
- Failure rows: **5555**
- Pending rows: **2271**
- Overall success rate: **46.57%**

## Best Event Types So Far

- `convertible_bond`: success rate 59.17% from 1325 evaluated cases.
- `paid_in_capital_increase`: success rate 55.86% from 2465 evaluated cases.
- `lawsuit`: success rate 50.20% from 512 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 26.09% from 92 evaluated cases.
- `supply_contract`: success rate 36.38% from 1564 evaluated cases.
- `major_shareholder_change`: success rate 37.94% from 2628 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| major_shareholder_change | 3262 | 2628 | 997 | 1631 | 634 | 37.94% | -14.39% | -0.72% | conservative |
| paid_in_capital_increase | 2986 | 2465 | 1377 | 1088 | 521 | 55.86% | -7.99% | -0.16% | positive |
| supply_contract | 1890 | 1564 | 569 | 995 | 326 | 36.38% | -2.26% | -0.57% | conservative |
| convertible_bond | 1658 | 1325 | 784 | 541 | 333 | 59.17% | -7.45% | 0.29% | positive |
| merger | 870 | 774 | 355 | 419 | 96 | 45.87% | -2.49% | 5.00% | conservative |
| lawsuit | 633 | 512 | 257 | 255 | 121 | 50.20% | -17.83% | -0.34% | positive |
| investment_decision | 616 | 501 | 251 | 250 | 115 | 50.10% | -5.88% | 0.19% | positive |
| bond_with_warrant | 162 | 150 | 63 | 87 | 12 | 42.00% | -4.08% | 0.03% | conservative |
| disclosure_violation | 219 | 149 | 61 | 88 | 70 | 40.94% | -22.16% | -0.38% | conservative |
| spin_off | 157 | 121 | 48 | 73 | 36 | 39.67% | -20.46% | 0.84% | conservative |
| bonus_issue | 119 | 116 | 56 | 60 | 3 | 48.28% | 2.27% | 0.38% | conservative |
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
