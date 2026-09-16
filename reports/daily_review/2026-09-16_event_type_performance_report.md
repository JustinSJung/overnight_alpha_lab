# Event-Type Performance Report - 2026-09-16

Generated at: 2026-09-16 01:20:10

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **4850**
- Evaluated rows: **3162**
- Success rows: **1488**
- Failure rows: **1674**
- Pending rows: **1688**
- Overall success rate: **47.06%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 2 evaluated cases.
- `lawsuit`: success rate 73.45% from 113 evaluated cases.
- `investment_decision`: success rate 70.83% from 144 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 6.25% from 16 evaluated cases.
- `merger`: success rate 21.98% from 91 evaluated cases.
- `supply_contract`: success rate 28.12% from 480 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 1249 | 946 | 585 | 361 | 303 | 61.84% | -5.96% | 0.08% | positive |
| major_shareholder_change | 1323 | 840 | 294 | 546 | 483 | 35.00% | -12.93% | -1.46% | conservative |
| supply_contract | 742 | 480 | 135 | 345 | 262 | 28.12% | -2.30% | -0.79% | conservative |
| convertible_bond | 659 | 386 | 208 | 178 | 273 | 53.89% | -9.23% | 1.51% | positive |
| investment_decision | 245 | 144 | 102 | 42 | 101 | 70.83% | 2.88% | 0.06% | positive |
| lawsuit | 211 | 113 | 83 | 30 | 98 | 73.45% | -8.39% | -2.05% | positive |
| merger | 169 | 91 | 20 | 71 | 78 | 21.98% | -7.53% | 1.12% | conservative |
| bonus_issue | 58 | 55 | 29 | 26 | 3 | 52.73% | 0.04% | 0.86% | positive |
| disclosure_violation | 98 | 48 | 17 | 31 | 50 | 35.42% | -12.41% | 0.87% | conservative |
| spin_off | 64 | 41 | 12 | 29 | 23 | 29.27% | -44.10% | 0.25% | conservative |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -3.30% | -0.16% | conservative |
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
