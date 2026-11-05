# Event-Type Performance Report - 2026-11-05

Generated at: 2026-11-05 03:22:36

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **10732**
- Evaluated rows: **8462**
- Success rows: **3976**
- Failure rows: **4486**
- Pending rows: **2270**
- Overall success rate: **46.99%**

## Best Event Types So Far

- `convertible_bond`: success rate 57.78% from 1054 evaluated cases.
- `paid_in_capital_increase`: success rate 57.14% from 2079 evaluated cases.
- `lawsuit`: success rate 52.40% from 416 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 27.12% from 59 evaluated cases.
- `supply_contract`: success rate 34.06% from 1283 evaluated cases.
- `major_shareholder_change`: success rate 39.10% from 2036 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2600 | 2079 | 1188 | 891 | 521 | 57.14% | -7.46% | -0.15% | positive |
| major_shareholder_change | 2669 | 2036 | 796 | 1240 | 633 | 39.10% | -9.28% | -0.77% | conservative |
| supply_contract | 1609 | 1283 | 437 | 846 | 326 | 34.06% | -2.66% | -0.67% | conservative |
| convertible_bond | 1387 | 1054 | 609 | 445 | 333 | 57.78% | -7.34% | 0.43% | positive |
| merger | 760 | 664 | 312 | 352 | 96 | 46.99% | -2.71% | 5.65% | conservative |
| lawsuit | 537 | 416 | 218 | 198 | 121 | 52.40% | -14.77% | -0.41% | positive |
| investment_decision | 523 | 408 | 204 | 204 | 115 | 50.00% | -4.67% | 0.07% | neutral |
| disclosure_violation | 209 | 139 | 56 | 83 | 70 | 40.29% | -22.37% | -0.28% | conservative |
| bond_with_warrant | 146 | 134 | 54 | 80 | 12 | 40.30% | 0.04% | 0.21% | conservative |
| bonus_issue | 105 | 102 | 42 | 60 | 3 | 41.18% | 0.43% | -0.58% | conservative |
| spin_off | 124 | 88 | 44 | 44 | 36 | 50.00% | -24.47% | 1.62% | neutral |
| earnings_guidance | 63 | 59 | 16 | 43 | 4 | 27.12% | -0.11% | 0.28% | conservative |

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
