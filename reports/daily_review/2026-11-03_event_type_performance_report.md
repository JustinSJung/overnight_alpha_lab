# Event-Type Performance Report - 2026-11-03

Generated at: 2026-11-03 04:09:35

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **10471**
- Evaluated rows: **8205**
- Success rows: **3884**
- Failure rows: **4321**
- Pending rows: **2266**
- Overall success rate: **47.34%**

## Best Event Types So Far

- `convertible_bond`: success rate 57.52% from 1017 evaluated cases.
- `paid_in_capital_increase`: success rate 57.33% from 2034 evaluated cases.
- `lawsuit`: success rate 56.14% from 383 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 27.12% from 59 evaluated cases.
- `supply_contract`: success rate 34.42% from 1258 evaluated cases.
- `major_shareholder_change`: success rate 39.47% from 1951 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2555 | 2034 | 1166 | 868 | 521 | 57.33% | -7.70% | -0.17% | positive |
| major_shareholder_change | 2584 | 1951 | 770 | 1181 | 633 | 39.47% | -9.70% | -0.76% | conservative |
| supply_contract | 1584 | 1258 | 433 | 825 | 326 | 34.42% | -2.55% | -0.65% | conservative |
| convertible_bond | 1350 | 1017 | 585 | 432 | 333 | 57.52% | -7.27% | 0.43% | positive |
| merger | 754 | 658 | 311 | 347 | 96 | 47.26% | -2.58% | 5.70% | conservative |
| investment_decision | 508 | 393 | 196 | 197 | 115 | 49.87% | -4.88% | -0.13% | conservative |
| lawsuit | 504 | 383 | 215 | 168 | 121 | 56.14% | -16.61% | -0.48% | positive |
| bond_with_warrant | 145 | 133 | 53 | 80 | 12 | 39.85% | 0.05% | 0.23% | conservative |
| disclosure_violation | 202 | 132 | 53 | 79 | 70 | 40.15% | -20.53% | -0.26% | conservative |
| bonus_issue | 105 | 102 | 42 | 60 | 3 | 41.18% | 0.43% | -0.58% | conservative |
| spin_off | 117 | 85 | 44 | 41 | 32 | 51.76% | -25.34% | 1.61% | positive |
| earnings_guidance | 63 | 59 | 16 | 43 | 4 | 27.12% | -0.11% | 0.28% | conservative |

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
