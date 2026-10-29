# Event-Type Performance Report - 2026-10-20

Generated at: 2026-10-20 01:45:28

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **8366**
- Evaluated rows: **6103**
- Success rows: **2701**
- Failure rows: **3402**
- Pending rows: **2263**
- Overall success rate: **44.26%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 4 evaluated cases.
- `lawsuit`: success rate 58.22% from 292 evaluated cases.
- `paid_in_capital_increase`: success rate 57.58% from 1676 evaluated cases.

## Weak Event Types So Far

- `merger`: success rate 19.50% from 323 evaluated cases.
- `bond_with_warrant`: success rate 23.81% from 105 evaluated cases.
- `supply_contract`: success rate 29.83% from 905 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2196 | 1676 | 965 | 711 | 520 | 57.58% | -8.13% | 0.18% | positive |
| major_shareholder_change | 2120 | 1487 | 525 | 962 | 633 | 35.31% | -12.54% | -0.67% | conservative |
| supply_contract | 1231 | 905 | 270 | 635 | 326 | 29.83% | -2.31% | -0.84% | conservative |
| convertible_bond | 1087 | 755 | 396 | 359 | 332 | 52.45% | -8.36% | 0.89% | positive |
| merger | 418 | 323 | 63 | 260 | 95 | 19.50% | -13.64% | 0.35% | conservative |
| lawsuit | 413 | 292 | 170 | 122 | 121 | 58.22% | -14.40% | -0.78% | positive |
| investment_decision | 394 | 279 | 153 | 126 | 115 | 54.84% | -5.93% | -0.23% | positive |
| bond_with_warrant | 117 | 105 | 25 | 80 | 12 | 23.81% | -0.63% | 0.47% | conservative |
| bonus_issue | 102 | 99 | 41 | 58 | 3 | 41.41% | 0.45% | -0.40% | conservative |
| disclosure_violation | 168 | 98 | 48 | 50 | 70 | 48.98% | -13.56% | -0.46% | conservative |
| spin_off | 112 | 80 | 41 | 39 | 32 | 51.25% | -26.90% | 1.80% | positive |
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
