# Event-Type Performance Report - 2026-09-29

Generated at: 2026-09-29 03:32:25

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **6105**
- Evaluated rows: **4233**
- Success rows: **1852**
- Failure rows: **2381**
- Pending rows: **1872**
- Overall success rate: **43.75%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 2 evaluated cases.
- `paid_in_capital_increase`: success rate 57.10% from 1198 evaluated cases.
- `lawsuit`: success rate 55.12% from 205 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 9.52% from 63 evaluated cases.
- `merger`: success rate 20.83% from 120 evaluated cases.
- `supply_contract`: success rate 28.18% from 621 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 1569 | 1198 | 684 | 514 | 371 | 57.10% | -5.67% | 0.45% | positive |
| major_shareholder_change | 1584 | 1045 | 347 | 698 | 539 | 33.21% | -11.35% | -0.98% | conservative |
| supply_contract | 899 | 621 | 175 | 446 | 278 | 28.18% | -2.01% | -0.71% | conservative |
| convertible_bond | 858 | 570 | 298 | 272 | 288 | 52.28% | -6.19% | 0.81% | positive |
| investment_decision | 333 | 227 | 120 | 107 | 106 | 52.86% | -5.73% | 0.31% | positive |
| lawsuit | 318 | 205 | 113 | 92 | 113 | 55.12% | -12.47% | -0.51% | positive |
| merger | 200 | 120 | 25 | 95 | 80 | 20.83% | -12.41% | 0.81% | conservative |
| disclosure_violation | 126 | 71 | 38 | 33 | 55 | 53.52% | -10.31% | -0.17% | positive |
| bond_with_warrant | 74 | 63 | 6 | 57 | 11 | 9.52% | -0.90% | 0.01% | conservative |
| bonus_issue | 65 | 62 | 29 | 33 | 3 | 46.77% | 1.82% | 0.56% | conservative |
| spin_off | 73 | 49 | 15 | 34 | 24 | 30.61% | -41.04% | 0.30% | conservative |
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
