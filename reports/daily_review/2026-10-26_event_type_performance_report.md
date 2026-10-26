# Event-Type Performance Report - 2026-10-26

Generated at: 2026-10-26 00:56:23

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **8890**
- Evaluated rows: **6626**
- Success rows: **2905**
- Failure rows: **3721**
- Pending rows: **2264**
- Overall success rate: **43.84%**

## Best Event Types So Far

- `earnings_guidance`: success rate 81.82% from 11 evaluated cases.
- `paid_in_capital_increase`: success rate 58.39% from 1788 evaluated cases.
- `lawsuit`: success rate 53.39% from 339 evaluated cases.

## Weak Event Types So Far

- `merger`: success rate 20.77% from 366 evaluated cases.
- `bond_with_warrant`: success rate 23.81% from 105 evaluated cases.
- `supply_contract`: success rate 30.36% from 1008 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2308 | 1788 | 1044 | 744 | 520 | 58.39% | -8.34% | -0.06% | positive |
| major_shareholder_change | 2222 | 1589 | 553 | 1036 | 633 | 34.80% | -11.81% | -0.65% | conservative |
| supply_contract | 1334 | 1008 | 306 | 702 | 326 | 30.36% | -2.36% | -0.71% | conservative |
| convertible_bond | 1151 | 818 | 419 | 399 | 333 | 51.22% | -8.00% | 0.98% | positive |
| merger | 461 | 366 | 76 | 290 | 95 | 20.77% | -12.33% | 0.25% | conservative |
| lawsuit | 460 | 339 | 181 | 158 | 121 | 53.39% | -17.60% | -0.16% | positive |
| investment_decision | 423 | 308 | 160 | 148 | 115 | 51.95% | -5.26% | -0.23% | positive |
| disclosure_violation | 182 | 112 | 49 | 63 | 70 | 43.75% | -19.84% | -0.36% | conservative |
| bond_with_warrant | 117 | 105 | 25 | 80 | 12 | 23.81% | -0.63% | 0.47% | conservative |
| bonus_issue | 104 | 101 | 42 | 59 | 3 | 41.58% | 0.45% | -0.49% | conservative |
| spin_off | 113 | 81 | 41 | 40 | 32 | 50.62% | -26.56% | 1.76% | positive |
| earnings_guidance | 15 | 11 | 9 | 2 | 4 | 81.82% | 0.95% | 2.91% | positive |

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
