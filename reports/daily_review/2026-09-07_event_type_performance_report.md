# Event-Type Performance Report - 2026-09-07

Generated at: 2026-09-07 00:27:33

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **3356**
- Evaluated rows: **1671**
- Success rows: **759**
- Failure rows: **912**
- Pending rows: **1685**
- Overall success rate: **45.42%**

## Best Event Types So Far

- `lawsuit`: success rate 77.61% from 67 evaluated cases.
- `paid_in_capital_increase`: success rate 65.59% from 494 evaluated cases.
- `convertible_bond`: success rate 63.68% from 212 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 6.25% from 16 evaluated cases.
- `disclosure_violation`: success rate 8.33% from 12 evaluated cases.
- `merger`: success rate 17.78% from 45 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 797 | 494 | 324 | 170 | 303 | 65.59% | -6.99% | 0.28% | positive |
| major_shareholder_change | 931 | 448 | 128 | 320 | 483 | 28.57% | -14.94% | -0.56% | conservative |
| supply_contract | 546 | 284 | 68 | 216 | 262 | 23.94% | -2.70% | -1.04% | conservative |
| convertible_bond | 485 | 212 | 135 | 77 | 273 | 63.68% | -6.49% | -1.19% | positive |
| lawsuit | 163 | 67 | 52 | 15 | 96 | 77.61% | -3.86% | -1.02% | positive |
| merger | 123 | 45 | 8 | 37 | 78 | 17.78% | 0.39% | 1.88% | conservative |
| investment_decision | 145 | 44 | 26 | 18 | 101 | 59.09% | 5.45% | 4.66% | positive |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -0.82% | 0.37% | conservative |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -3.30% | -0.16% | conservative |
| disclosure_violation | 62 | 12 | 1 | 11 | 50 | 8.33% | -33.15% | 0.72% | conservative |
| spin_off | 33 | 11 | 4 | 7 | 22 | 36.36% | 0.14% | 0.41% | conservative |
| earnings_guidance | 4 | 0 | 0 | 0 | 4 | N/A | N/A | N/A | neutral |

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
