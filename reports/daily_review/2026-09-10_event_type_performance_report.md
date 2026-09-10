# Event-Type Performance Report - 2026-09-10

Generated at: 2026-09-10 00:54:36

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **3866**
- Evaluated rows: **2180**
- Success rows: **964**
- Failure rows: **1216**
- Pending rows: **1686**
- Overall success rate: **44.22%**

## Best Event Types So Far

- `lawsuit`: success rate 79.12% from 91 evaluated cases.
- `paid_in_capital_increase`: success rate 63.38% from 639 evaluated cases.
- `investment_decision`: success rate 62.11% from 95 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 6.25% from 16 evaluated cases.
- `disclosure_violation`: success rate 6.67% from 15 evaluated cases.
- `merger`: success rate 14.08% from 71 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 942 | 639 | 405 | 234 | 303 | 63.38% | -5.40% | 0.66% | positive |
| major_shareholder_change | 1058 | 575 | 159 | 416 | 483 | 27.65% | -13.05% | -0.64% | conservative |
| supply_contract | 602 | 340 | 90 | 250 | 262 | 26.47% | -2.24% | -0.87% | conservative |
| convertible_bond | 541 | 268 | 148 | 120 | 273 | 55.22% | -5.37% | 2.73% | positive |
| investment_decision | 196 | 95 | 59 | 36 | 101 | 62.11% | 2.13% | -0.63% | positive |
| lawsuit | 188 | 91 | 72 | 19 | 97 | 79.12% | -6.68% | -2.70% | positive |
| merger | 149 | 71 | 10 | 61 | 78 | 14.08% | 0.69% | 0.69% | conservative |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -0.82% | 0.37% | conservative |
| spin_off | 54 | 32 | 7 | 25 | 22 | 21.88% | -53.35% | -0.22% | conservative |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -3.30% | -0.16% | conservative |
| disclosure_violation | 65 | 15 | 1 | 14 | 50 | 6.67% | -26.52% | 0.68% | conservative |
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
