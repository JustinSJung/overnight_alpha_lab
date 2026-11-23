# Event-Type Performance Report - 2026-11-23

Generated at: 2026-11-23 03:33:13

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **12976**
- Evaluated rows: **10705**
- Success rows: **5028**
- Failure rows: **5677**
- Pending rows: **2271**
- Overall success rate: **46.97%**

## Best Event Types So Far

- `convertible_bond`: success rate 59.53% from 1359 evaluated cases.
- `paid_in_capital_increase`: success rate 56.47% from 2513 evaluated cases.
- `investment_decision`: success rate 52.01% from 523 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 26.09% from 92 evaluated cases.
- `supply_contract`: success rate 35.06% from 1637 evaluated cases.
- `major_shareholder_change`: success rate 39.23% from 2710 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| major_shareholder_change | 3344 | 2710 | 1063 | 1647 | 634 | 39.23% | -14.19% | -0.84% | conservative |
| paid_in_capital_increase | 3034 | 2513 | 1419 | 1094 | 521 | 56.47% | -7.77% | -0.13% | positive |
| supply_contract | 1963 | 1637 | 574 | 1063 | 326 | 35.06% | -2.26% | -0.75% | conservative |
| convertible_bond | 1692 | 1359 | 809 | 550 | 333 | 59.53% | -7.52% | 0.23% | positive |
| merger | 895 | 799 | 363 | 436 | 96 | 45.43% | -2.74% | 5.01% | conservative |
| lawsuit | 647 | 526 | 267 | 259 | 121 | 50.76% | -17.99% | -0.43% | positive |
| investment_decision | 638 | 523 | 272 | 251 | 115 | 52.01% | -5.74% | 0.09% | positive |
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
