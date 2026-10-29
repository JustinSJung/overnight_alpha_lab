# Event-Type Performance Report - 2026-10-13

Generated at: 2026-10-13 03:54:07

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **7426**
- Evaluated rows: **5166**
- Success rows: **2306**
- Failure rows: **2860**
- Pending rows: **2260**
- Overall success rate: **44.64%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 2 evaluated cases.
- `paid_in_capital_increase`: success rate 59.90% from 1439 evaluated cases.
- `lawsuit`: success rate 57.98% from 257 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 9.23% from 65 evaluated cases.
- `merger`: success rate 19.62% from 265 evaluated cases.
- `supply_contract`: success rate 27.89% from 760 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 1957 | 1439 | 862 | 577 | 518 | 59.90% | -5.15% | 0.17% | positive |
| major_shareholder_change | 1862 | 1229 | 441 | 788 | 633 | 35.88% | -9.85% | -0.78% | conservative |
| supply_contract | 1086 | 760 | 212 | 548 | 326 | 27.89% | -2.66% | -0.83% | conservative |
| convertible_bond | 984 | 652 | 344 | 308 | 332 | 52.76% | -5.98% | 1.06% | positive |
| merger | 360 | 265 | 52 | 213 | 95 | 19.62% | -14.74% | 0.58% | conservative |
| investment_decision | 373 | 258 | 136 | 122 | 115 | 52.71% | -6.29% | -0.01% | positive |
| lawsuit | 377 | 257 | 149 | 108 | 120 | 57.98% | -11.93% | -0.62% | positive |
| bonus_issue | 102 | 99 | 41 | 58 | 3 | 41.41% | 0.45% | -0.40% | conservative |
| disclosure_violation | 152 | 82 | 41 | 41 | 70 | 50.00% | -12.61% | -0.32% | neutral |
| bond_with_warrant | 77 | 65 | 6 | 59 | 12 | 9.23% | -0.84% | 0.07% | conservative |
| spin_off | 90 | 58 | 20 | 38 | 32 | 34.48% | -38.07% | 0.21% | conservative |
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
