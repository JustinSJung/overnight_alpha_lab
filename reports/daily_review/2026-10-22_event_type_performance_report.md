# Event-Type Performance Report - 2026-10-22

Generated at: 2026-10-22 01:26:02

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **8607**
- Evaluated rows: **6344**
- Success rows: **2782**
- Failure rows: **3562**
- Pending rows: **2263**
- Overall success rate: **43.85%**

## Best Event Types So Far

- `earnings_guidance`: success rate 66.67% from 6 evaluated cases.
- `paid_in_capital_increase`: success rate 57.21% from 1713 evaluated cases.
- `lawsuit`: success rate 56.23% from 313 evaluated cases.

## Weak Event Types So Far

- `merger`: success rate 19.44% from 324 evaluated cases.
- `bond_with_warrant`: success rate 23.81% from 105 evaluated cases.
- `supply_contract`: success rate 30.83% from 973 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2233 | 1713 | 980 | 733 | 520 | 57.21% | -8.26% | 0.17% | positive |
| major_shareholder_change | 2160 | 1527 | 533 | 994 | 633 | 34.91% | -12.19% | -0.64% | conservative |
| supply_contract | 1299 | 973 | 300 | 673 | 326 | 30.83% | -2.41% | -0.67% | conservative |
| convertible_bond | 1127 | 795 | 412 | 383 | 332 | 51.82% | -8.33% | 0.89% | positive |
| merger | 419 | 324 | 63 | 261 | 95 | 19.44% | -13.60% | 0.35% | conservative |
| lawsuit | 434 | 313 | 176 | 137 | 121 | 56.23% | -17.91% | -0.77% | positive |
| investment_decision | 410 | 295 | 157 | 138 | 115 | 53.22% | -5.56% | -0.24% | positive |
| disclosure_violation | 182 | 112 | 49 | 63 | 70 | 43.75% | -19.84% | -0.36% | conservative |
| bond_with_warrant | 117 | 105 | 25 | 80 | 12 | 23.81% | -0.63% | 0.47% | conservative |
| bonus_issue | 103 | 100 | 42 | 58 | 3 | 42.00% | 0.46% | -0.37% | conservative |
| spin_off | 113 | 81 | 41 | 40 | 32 | 50.62% | -26.56% | 1.76% | positive |
| earnings_guidance | 10 | 6 | 4 | 2 | 4 | 66.67% | 1.44% | 1.18% | positive |

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
