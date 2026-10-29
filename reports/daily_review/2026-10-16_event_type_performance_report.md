# Event-Type Performance Report - 2026-10-16

Generated at: 2026-10-16 00:50:16

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **7999**
- Evaluated rows: **5737**
- Success rows: **2515**
- Failure rows: **3222**
- Pending rows: **2262**
- Overall success rate: **43.84%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 4 evaluated cases.
- `paid_in_capital_increase`: success rate 56.69% from 1561 evaluated cases.
- `lawsuit`: success rate 56.52% from 276 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 15.79% from 95 evaluated cases.
- `merger`: success rate 19.48% from 308 evaluated cases.
- `supply_contract`: success rate 30.19% from 848 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2081 | 1561 | 885 | 676 | 520 | 56.69% | -7.28% | 0.20% | positive |
| major_shareholder_change | 2020 | 1387 | 494 | 893 | 633 | 35.62% | -12.65% | -0.53% | conservative |
| supply_contract | 1174 | 848 | 256 | 592 | 326 | 30.19% | -2.56% | -0.79% | conservative |
| convertible_bond | 1058 | 726 | 378 | 348 | 332 | 52.07% | -7.43% | 0.95% | positive |
| merger | 403 | 308 | 60 | 248 | 95 | 19.48% | -13.61% | 0.44% | conservative |
| lawsuit | 396 | 276 | 156 | 120 | 120 | 56.52% | -14.28% | -0.51% | positive |
| investment_decision | 381 | 266 | 143 | 123 | 115 | 53.76% | -6.15% | -0.06% | positive |
| bonus_issue | 102 | 99 | 41 | 58 | 3 | 41.41% | 0.45% | -0.40% | conservative |
| bond_with_warrant | 107 | 95 | 15 | 80 | 12 | 15.79% | -0.04% | 1.39% | conservative |
| disclosure_violation | 157 | 87 | 42 | 45 | 70 | 48.28% | -12.97% | -0.23% | conservative |
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
