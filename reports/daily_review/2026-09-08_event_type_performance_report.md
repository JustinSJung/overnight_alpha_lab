# Event-Type Performance Report - 2026-09-08

Generated at: 2026-09-08 01:05:26

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **3503**
- Evaluated rows: **1818**
- Success rows: **823**
- Failure rows: **995**
- Pending rows: **1685**
- Overall success rate: **45.27%**

## Best Event Types So Far

- `lawsuit`: success rate 76.81% from 69 evaluated cases.
- `paid_in_capital_increase`: success rate 66.79% from 533 evaluated cases.
- `convertible_bond`: success rate 64.19% from 215 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 6.25% from 16 evaluated cases.
- `disclosure_violation`: success rate 6.67% from 15 evaluated cases.
- `merger`: success rate 17.78% from 45 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 836 | 533 | 356 | 177 | 303 | 66.79% | -6.38% | 0.01% | positive |
| major_shareholder_change | 996 | 513 | 149 | 364 | 483 | 29.04% | -13.43% | -0.68% | conservative |
| supply_contract | 565 | 303 | 74 | 229 | 262 | 24.42% | -2.47% | -0.98% | conservative |
| convertible_bond | 488 | 215 | 138 | 77 | 273 | 64.19% | -6.40% | -1.19% | positive |
| lawsuit | 165 | 69 | 53 | 16 | 96 | 76.81% | -3.66% | -0.99% | positive |
| investment_decision | 160 | 59 | 26 | 33 | 101 | 44.07% | 4.34% | 3.35% | conservative |
| merger | 123 | 45 | 8 | 37 | 78 | 17.78% | 0.39% | 1.88% | conservative |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -0.82% | 0.37% | conservative |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -3.30% | -0.16% | conservative |
| disclosure_violation | 65 | 15 | 1 | 14 | 50 | 6.67% | -26.52% | 0.68% | conservative |
| spin_off | 34 | 12 | 5 | 7 | 22 | 41.67% | 0.01% | 0.11% | conservative |
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
