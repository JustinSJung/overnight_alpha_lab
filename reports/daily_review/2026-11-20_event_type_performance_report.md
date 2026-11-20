# Event-Type Performance Report - 2026-11-20

Generated at: 2026-11-20 04:02:24

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **12812**
- Evaluated rows: **10541**
- Success rows: **4922**
- Failure rows: **5619**
- Pending rows: **2271**
- Overall success rate: **46.69%**

## Best Event Types So Far

- `convertible_bond`: success rate 59.57% from 1343 evaluated cases.
- `paid_in_capital_increase`: success rate 56.08% from 2491 evaluated cases.
- `investment_decision`: success rate 50.78% from 510 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 26.09% from 92 evaluated cases.
- `supply_contract`: success rate 35.92% from 1584 evaluated cases.
- `major_shareholder_change`: success rate 37.97% from 2652 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| major_shareholder_change | 3286 | 2652 | 1007 | 1645 | 634 | 37.97% | -14.35% | -0.72% | conservative |
| paid_in_capital_increase | 3012 | 2491 | 1397 | 1094 | 521 | 56.08% | -7.83% | -0.10% | positive |
| supply_contract | 1910 | 1584 | 569 | 1015 | 326 | 35.92% | -2.26% | -0.62% | conservative |
| convertible_bond | 1676 | 1343 | 800 | 543 | 333 | 59.57% | -7.46% | 0.17% | positive |
| merger | 895 | 799 | 363 | 436 | 96 | 45.43% | -2.74% | 5.01% | conservative |
| lawsuit | 645 | 524 | 266 | 258 | 121 | 50.76% | -18.05% | -0.43% | positive |
| investment_decision | 625 | 510 | 259 | 251 | 115 | 50.78% | -5.81% | 0.22% | positive |
| disclosure_violation | 228 | 158 | 70 | 88 | 70 | 44.30% | -20.98% | -0.93% | conservative |
| bond_with_warrant | 162 | 150 | 63 | 87 | 12 | 42.00% | -4.08% | 0.03% | conservative |
| spin_off | 158 | 122 | 48 | 74 | 36 | 39.34% | -20.29% | 0.83% | conservative |
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
