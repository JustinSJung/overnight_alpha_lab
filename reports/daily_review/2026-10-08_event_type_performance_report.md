# Event-Type Performance Report - 2026-10-08

Generated at: 2026-10-08 04:06:04

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **6970**
- Evaluated rows: **4977**
- Success rows: **2190**
- Failure rows: **2787**
- Pending rows: **1993**
- Overall success rate: **44.00%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 2 evaluated cases.
- `paid_in_capital_increase`: success rate 58.70% from 1385 evaluated cases.
- `lawsuit`: success rate 56.63% from 249 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 9.23% from 65 evaluated cases.
- `merger`: success rate 19.70% from 264 evaluated cases.
- `supply_contract`: success rate 29.01% from 724 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 1791 | 1385 | 813 | 572 | 406 | 58.70% | -4.92% | 0.35% | positive |
| major_shareholder_change | 1747 | 1182 | 402 | 780 | 565 | 34.01% | -10.09% | -0.68% | conservative |
| supply_contract | 1024 | 724 | 210 | 514 | 300 | 29.01% | -2.40% | -0.72% | conservative |
| convertible_bond | 931 | 633 | 336 | 297 | 298 | 53.08% | -5.53% | 1.05% | positive |
| merger | 355 | 264 | 52 | 212 | 91 | 19.70% | -14.80% | 0.59% | conservative |
| investment_decision | 364 | 251 | 131 | 120 | 113 | 52.19% | -5.64% | 0.09% | positive |
| lawsuit | 366 | 249 | 141 | 108 | 117 | 56.63% | -12.29% | -0.52% | positive |
| bonus_issue | 93 | 90 | 41 | 49 | 3 | 45.56% | 1.37% | 0.40% | conservative |
| disclosure_violation | 132 | 77 | 38 | 39 | 55 | 49.35% | -13.35% | -0.12% | conservative |
| bond_with_warrant | 76 | 65 | 6 | 59 | 11 | 9.23% | -0.84% | 0.07% | conservative |
| spin_off | 85 | 55 | 18 | 37 | 30 | 32.73% | -38.23% | 0.50% | conservative |
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
