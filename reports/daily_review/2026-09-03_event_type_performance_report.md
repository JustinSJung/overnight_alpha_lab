# Event-Type Performance Report - 2026-09-03

Generated at: 2026-09-03 00:55:19

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **2699**
- Evaluated rows: **1205**
- Success rows: **510**
- Failure rows: **695**
- Pending rows: **1494**
- Overall success rate: **42.32%**

## Best Event Types So Far

- `lawsuit`: success rate 83.72% from 43 evaluated cases.
- `convertible_bond`: success rate 70.62% from 160 evaluated cases.
- `paid_in_capital_increase`: success rate 65.12% from 344 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 6.25% from 16 evaluated cases.
- `merger`: success rate 7.14% from 28 evaluated cases.
- `disclosure_violation`: success rate 14.29% from 7 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 600 | 344 | 224 | 120 | 256 | 65.12% | -9.30% | 0.61% | positive |
| major_shareholder_change | 706 | 286 | 59 | 227 | 420 | 20.63% | -18.91% | -0.50% | conservative |
| supply_contract | 484 | 241 | 40 | 201 | 243 | 16.60% | -1.68% | -1.61% | conservative |
| convertible_bond | 407 | 160 | 113 | 47 | 247 | 70.62% | -9.31% | -2.15% | positive |
| lawsuit | 134 | 43 | 36 | 7 | 91 | 83.72% | -5.48% | -1.26% | positive |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -0.82% | 0.37% | conservative |
| investment_decision | 126 | 34 | 19 | 15 | 92 | 55.88% | 6.85% | 5.57% | positive |
| merger | 89 | 28 | 2 | 26 | 61 | 7.14% | -2.19% | -0.20% | conservative |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -3.30% | -0.16% | conservative |
| spin_off | 27 | 8 | 3 | 5 | 19 | 37.50% | 0.66% | 1.02% | conservative |
| disclosure_violation | 55 | 7 | 1 | 6 | 48 | 14.29% | -42.46% | 0.72% | conservative |
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
