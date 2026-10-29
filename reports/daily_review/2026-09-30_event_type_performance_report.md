# Event-Type Performance Report - 2026-09-30

Generated at: 2026-09-30 02:55:46

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **6311**
- Evaluated rows: **4439**
- Success rows: **1941**
- Failure rows: **2498**
- Pending rows: **1872**
- Overall success rate: **43.73%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 2 evaluated cases.
- `lawsuit`: success rate 57.21% from 222 evaluated cases.
- `paid_in_capital_increase`: success rate 56.34% from 1239 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 9.52% from 63 evaluated cases.
- `merger`: success rate 24.70% from 166 evaluated cases.
- `supply_contract`: success rate 29.40% from 653 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 1610 | 1239 | 698 | 541 | 371 | 56.34% | -5.44% | 0.46% | positive |
| major_shareholder_change | 1623 | 1084 | 357 | 727 | 539 | 32.93% | -10.94% | -0.92% | conservative |
| supply_contract | 931 | 653 | 192 | 461 | 278 | 29.40% | -2.35% | -0.65% | conservative |
| convertible_bond | 863 | 575 | 301 | 274 | 288 | 52.35% | -6.14% | 0.80% | positive |
| investment_decision | 344 | 238 | 122 | 116 | 106 | 51.26% | -5.46% | 0.28% | positive |
| lawsuit | 335 | 222 | 127 | 95 | 113 | 57.21% | -11.96% | -0.47% | positive |
| merger | 246 | 166 | 41 | 125 | 80 | 24.70% | -9.28% | 1.46% | conservative |
| bonus_issue | 77 | 74 | 41 | 33 | 3 | 55.41% | 1.53% | 0.75% | positive |
| disclosure_violation | 127 | 72 | 38 | 34 | 55 | 52.78% | -11.55% | -0.17% | positive |
| bond_with_warrant | 74 | 63 | 6 | 57 | 11 | 9.52% | -0.90% | 0.01% | conservative |
| spin_off | 75 | 51 | 16 | 35 | 24 | 31.37% | -39.34% | 0.56% | conservative |
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
