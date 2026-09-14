# Event-Type Performance Report - 2026-09-14

Generated at: 2026-09-14 00:59:57

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **4289**
- Evaluated rows: **2603**
- Success rows: **1119**
- Failure rows: **1484**
- Pending rows: **1686**
- Overall success rate: **42.99%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 2 evaluated cases.
- `lawsuit`: success rate 77.32% from 97 evaluated cases.
- `investment_decision`: success rate 63.81% from 105 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 6.25% from 16 evaluated cases.
- `spin_off`: success rate 20.00% from 35 evaluated cases.
- `merger`: success rate 21.35% from 89 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 1079 | 776 | 462 | 314 | 303 | 59.54% | -6.79% | 0.86% | positive |
| major_shareholder_change | 1142 | 659 | 175 | 484 | 483 | 26.56% | -14.68% | -0.66% | conservative |
| supply_contract | 679 | 417 | 116 | 301 | 262 | 27.82% | -2.37% | -0.72% | conservative |
| convertible_bond | 600 | 327 | 170 | 157 | 273 | 51.99% | -11.05% | 2.14% | positive |
| investment_decision | 206 | 105 | 67 | 38 | 101 | 63.81% | 1.88% | 0.30% | positive |
| lawsuit | 194 | 97 | 75 | 22 | 97 | 77.32% | -9.36% | -2.56% | positive |
| merger | 167 | 89 | 19 | 70 | 78 | 21.35% | -7.72% | 1.22% | conservative |
| disclosure_violation | 92 | 42 | 13 | 29 | 50 | 30.95% | -11.86% | 1.10% | conservative |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -0.82% | 0.37% | conservative |
| spin_off | 57 | 35 | 7 | 28 | 22 | 20.00% | -51.65% | -0.17% | conservative |
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
