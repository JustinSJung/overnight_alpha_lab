# Event-Type Performance Report - 2026-11-18

Generated at: 2026-11-18 04:51:02

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **12547**
- Evaluated rows: **10276**
- Success rows: **4770**
- Failure rows: **5506**
- Pending rows: **2271**
- Overall success rate: **46.42%**

## Best Event Types So Far

- `convertible_bond`: success rate 58.58% from 1306 evaluated cases.
- `paid_in_capital_increase`: success rate 55.46% from 2434 evaluated cases.
- `investment_decision`: success rate 51.02% from 492 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 26.09% from 92 evaluated cases.
- `supply_contract`: success rate 36.10% from 1540 evaluated cases.
- `major_shareholder_change`: success rate 38.07% from 2595 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| major_shareholder_change | 3229 | 2595 | 988 | 1607 | 634 | 38.07% | -14.58% | -0.72% | conservative |
| paid_in_capital_increase | 2955 | 2434 | 1350 | 1084 | 521 | 55.46% | -8.11% | -0.19% | positive |
| supply_contract | 1866 | 1540 | 556 | 984 | 326 | 36.10% | -2.29% | -0.58% | conservative |
| convertible_bond | 1639 | 1306 | 765 | 541 | 333 | 58.58% | -7.55% | 0.34% | positive |
| merger | 870 | 774 | 355 | 419 | 96 | 45.87% | -2.49% | 5.00% | conservative |
| lawsuit | 630 | 509 | 254 | 255 | 121 | 49.90% | -17.93% | -0.33% | conservative |
| investment_decision | 607 | 492 | 251 | 241 | 115 | 51.02% | -6.00% | 0.22% | positive |
| bond_with_warrant | 162 | 150 | 63 | 87 | 12 | 42.00% | -4.08% | 0.03% | conservative |
| disclosure_violation | 218 | 148 | 61 | 87 | 70 | 41.22% | -21.63% | -0.38% | conservative |
| spin_off | 156 | 120 | 47 | 73 | 36 | 39.17% | -20.62% | 0.87% | conservative |
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
