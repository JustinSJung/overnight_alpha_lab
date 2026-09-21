# Event-Type Performance Report - 2026-09-21

Generated at: 2026-09-21 01:03:37

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **5270**
- Evaluated rows: **3582**
- Success rows: **1636**
- Failure rows: **1946**
- Pending rows: **1688**
- Overall success rate: **45.67%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 2 evaluated cases.
- `paid_in_capital_increase`: success rate 60.74% from 1047 evaluated cases.
- `lawsuit`: success rate 60.67% from 150 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 5.88% from 17 evaluated cases.
- `merger`: success rate 22.64% from 106 evaluated cases.
- `spin_off`: success rate 28.26% from 46 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 1350 | 1047 | 636 | 411 | 303 | 60.74% | -6.72% | 0.24% | positive |
| major_shareholder_change | 1436 | 953 | 326 | 627 | 483 | 34.21% | -11.39% | -1.13% | conservative |
| supply_contract | 780 | 518 | 149 | 369 | 262 | 28.76% | -2.32% | -0.76% | conservative |
| convertible_bond | 686 | 413 | 227 | 186 | 273 | 54.96% | -8.56% | 1.39% | positive |
| investment_decision | 304 | 203 | 105 | 98 | 101 | 51.72% | -6.52% | 0.29% | positive |
| lawsuit | 248 | 150 | 91 | 59 | 98 | 60.67% | -11.23% | -0.57% | positive |
| merger | 184 | 106 | 24 | 82 | 78 | 22.64% | -14.08% | 0.87% | conservative |
| disclosure_violation | 116 | 66 | 33 | 33 | 50 | 50.00% | -11.12% | -0.08% | neutral |
| bonus_issue | 64 | 61 | 29 | 32 | 3 | 47.54% | 1.82% | 0.59% | conservative |
| spin_off | 69 | 46 | 13 | 33 | 23 | 28.26% | -43.62% | 0.14% | conservative |
| bond_with_warrant | 27 | 17 | 1 | 16 | 10 | 5.88% | -3.06% | -0.11% | conservative |
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
