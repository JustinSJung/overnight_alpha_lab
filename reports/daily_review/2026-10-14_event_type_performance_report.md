# Event-Type Performance Report - 2026-10-14

Generated at: 2026-10-14 02:04:06

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **7618**
- Evaluated rows: **5358**
- Success rows: **2354**
- Failure rows: **3004**
- Pending rows: **2260**
- Overall success rate: **43.93%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 4 evaluated cases.
- `lawsuit`: success rate 58.30% from 259 evaluated cases.
- `paid_in_capital_increase`: success rate 57.38% from 1518 evaluated cases.

## Weak Event Types So Far

- `merger`: success rate 19.70% from 269 evaluated cases.
- `bond_with_warrant`: success rate 20.27% from 74 evaluated cases.
- `supply_contract`: success rate 27.92% from 788 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2036 | 1518 | 871 | 647 | 518 | 57.38% | -6.45% | 0.20% | positive |
| major_shareholder_change | 1911 | 1278 | 442 | 836 | 633 | 34.59% | -12.29% | -0.75% | conservative |
| supply_contract | 1114 | 788 | 220 | 568 | 326 | 27.92% | -2.75% | -0.85% | conservative |
| convertible_bond | 997 | 665 | 355 | 310 | 332 | 53.38% | -5.86% | 1.03% | positive |
| merger | 364 | 269 | 53 | 216 | 95 | 19.70% | -14.89% | 0.56% | conservative |
| investment_decision | 378 | 263 | 141 | 122 | 115 | 53.61% | -6.21% | -0.02% | positive |
| lawsuit | 379 | 259 | 151 | 108 | 120 | 58.30% | -11.86% | -0.62% | positive |
| bonus_issue | 102 | 99 | 41 | 58 | 3 | 41.41% | 0.45% | -0.40% | conservative |
| disclosure_violation | 153 | 83 | 41 | 42 | 70 | 49.40% | -12.44% | -0.32% | conservative |
| bond_with_warrant | 86 | 74 | 15 | 59 | 12 | 20.27% | -0.79% | -0.04% | conservative |
| spin_off | 90 | 58 | 20 | 38 | 32 | 34.48% | -38.07% | 0.21% | conservative |
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
