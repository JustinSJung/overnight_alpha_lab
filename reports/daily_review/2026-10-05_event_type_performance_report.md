# Event-Type Performance Report - 2026-10-05

Generated at: 2026-10-05 01:19:32

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **6599**
- Evaluated rows: **4607**
- Success rows: **2061**
- Failure rows: **2546**
- Pending rows: **1992**
- Overall success rate: **44.74%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 2 evaluated cases.
- `lawsuit`: success rate 58.87% from 231 evaluated cases.
- `paid_in_capital_increase`: success rate 57.81% from 1299 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 9.52% from 63 evaluated cases.
- `merger`: success rate 26.88% from 186 evaluated cases.
- `supply_contract`: success rate 29.82% from 674 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 1704 | 1299 | 751 | 548 | 405 | 57.81% | -5.16% | 0.33% | positive |
| major_shareholder_change | 1685 | 1120 | 382 | 738 | 565 | 34.11% | -10.58% | -0.86% | conservative |
| supply_contract | 974 | 674 | 201 | 473 | 300 | 29.82% | -2.29% | -0.65% | conservative |
| convertible_bond | 887 | 589 | 315 | 274 | 298 | 53.48% | -5.96% | 0.69% | positive |
| investment_decision | 353 | 240 | 123 | 117 | 113 | 51.25% | -5.42% | 0.26% | positive |
| lawsuit | 348 | 231 | 136 | 95 | 117 | 58.87% | -11.49% | -0.61% | positive |
| merger | 277 | 186 | 50 | 136 | 91 | 26.88% | -12.66% | 1.34% | conservative |
| bonus_issue | 79 | 76 | 41 | 35 | 3 | 53.95% | 1.47% | 0.64% | positive |
| disclosure_violation | 129 | 74 | 38 | 36 | 55 | 51.35% | -11.21% | -0.13% | positive |
| bond_with_warrant | 74 | 63 | 6 | 57 | 11 | 9.52% | -0.90% | 0.01% | conservative |
| spin_off | 83 | 53 | 16 | 37 | 30 | 30.19% | -39.63% | 0.50% | conservative |
| earnings_guidance | 6 | 2 | 2 | 0 | 4 | 100.00% | 1.78% | 2.14% | positive |

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
