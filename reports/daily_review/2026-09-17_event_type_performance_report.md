# Event-Type Performance Report - 2026-09-17

Generated at: 2026-09-17 01:41:30

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **5062**
- Evaluated rows: **3374**
- Success rows: **1560**
- Failure rows: **1814**
- Pending rows: **1688**
- Overall success rate: **46.24%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 2 evaluated cases.
- `investment_decision`: success rate 65.61% from 157 evaluated cases.
- `lawsuit`: success rate 64.34% from 129 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 5.88% from 17 evaluated cases.
- `merger`: success rate 22.83% from 92 evaluated cases.
- `supply_contract`: success rate 28.57% from 490 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 1322 | 1019 | 616 | 403 | 303 | 60.45% | -6.54% | 0.26% | positive |
| major_shareholder_change | 1395 | 912 | 310 | 602 | 483 | 33.99% | -11.73% | -1.17% | conservative |
| supply_contract | 752 | 490 | 140 | 350 | 262 | 28.57% | -2.26% | -0.77% | conservative |
| convertible_bond | 660 | 387 | 209 | 178 | 273 | 54.01% | -9.20% | 1.50% | positive |
| investment_decision | 258 | 157 | 103 | 54 | 101 | 65.61% | -5.00% | 0.08% | positive |
| lawsuit | 227 | 129 | 83 | 46 | 98 | 64.34% | -6.98% | -0.62% | positive |
| merger | 170 | 92 | 21 | 71 | 78 | 22.83% | -7.44% | 1.14% | conservative |
| disclosure_violation | 115 | 65 | 33 | 32 | 50 | 50.77% | -9.76% | -0.08% | positive |
| bonus_issue | 64 | 61 | 29 | 32 | 3 | 47.54% | 1.82% | 0.59% | conservative |
| spin_off | 66 | 43 | 13 | 30 | 23 | 30.23% | -44.34% | 0.19% | conservative |
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
