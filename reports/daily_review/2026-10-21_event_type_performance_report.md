# Event-Type Performance Report - 2026-10-21

Generated at: 2026-10-21 01:15:51

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **8438**
- Evaluated rows: **6175**
- Success rows: **2730**
- Failure rows: **3445**
- Pending rows: **2263**
- Overall success rate: **44.21%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 4 evaluated cases.
- `lawsuit`: success rate 58.31% from 295 evaluated cases.
- `paid_in_capital_increase`: success rate 57.30% from 1686 evaluated cases.

## Weak Event Types So Far

- `merger`: success rate 19.50% from 323 evaluated cases.
- `bond_with_warrant`: success rate 23.81% from 105 evaluated cases.
- `supply_contract`: success rate 30.73% from 921 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2206 | 1686 | 966 | 720 | 520 | 57.30% | -8.06% | 0.19% | positive |
| major_shareholder_change | 2142 | 1509 | 531 | 978 | 633 | 35.19% | -12.34% | -0.66% | conservative |
| supply_contract | 1247 | 921 | 283 | 638 | 326 | 30.73% | -2.35% | -0.79% | conservative |
| convertible_bond | 1097 | 765 | 398 | 367 | 332 | 52.03% | -8.24% | 0.90% | positive |
| merger | 418 | 323 | 63 | 260 | 95 | 19.50% | -13.64% | 0.35% | conservative |
| lawsuit | 416 | 295 | 172 | 123 | 121 | 58.31% | -14.60% | -0.79% | positive |
| investment_decision | 402 | 287 | 157 | 130 | 115 | 54.70% | -5.71% | -0.21% | positive |
| bond_with_warrant | 117 | 105 | 25 | 80 | 12 | 23.81% | -0.63% | 0.47% | conservative |
| bonus_issue | 103 | 100 | 42 | 58 | 3 | 42.00% | 0.46% | -0.37% | conservative |
| disclosure_violation | 169 | 99 | 48 | 51 | 70 | 48.48% | -13.40% | -0.42% | conservative |
| spin_off | 113 | 81 | 41 | 40 | 32 | 50.62% | -26.56% | 1.76% | positive |
| earnings_guidance | 8 | 4 | 4 | 0 | 4 | 100.00% | 2.69% | 1.92% | positive |

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
