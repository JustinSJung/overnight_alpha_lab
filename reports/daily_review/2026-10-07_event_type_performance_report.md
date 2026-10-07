# Event-Type Performance Report - 2026-10-07

Generated at: 2026-10-07 02:54:12

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **6836**
- Evaluated rows: **4844**
- Success rows: **2139**
- Failure rows: **2705**
- Pending rows: **1992**
- Overall success rate: **44.16%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 2 evaluated cases.
- `paid_in_capital_increase`: success rate 58.72% from 1342 evaluated cases.
- `lawsuit`: success rate 56.85% from 248 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 9.23% from 65 evaluated cases.
- `merger`: success rate 19.77% from 263 evaluated cases.
- `supply_contract`: success rate 29.00% from 707 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 1747 | 1342 | 788 | 554 | 405 | 58.72% | -5.29% | 0.23% | positive |
| major_shareholder_change | 1727 | 1162 | 399 | 763 | 565 | 34.34% | -10.18% | -0.68% | conservative |
| supply_contract | 1007 | 707 | 205 | 502 | 300 | 29.00% | -2.32% | -0.69% | conservative |
| convertible_bond | 901 | 603 | 324 | 279 | 298 | 53.73% | -5.99% | 0.70% | positive |
| merger | 354 | 263 | 52 | 211 | 91 | 19.77% | -14.85% | 0.59% | conservative |
| lawsuit | 365 | 248 | 141 | 107 | 117 | 56.85% | -12.34% | -0.56% | positive |
| investment_decision | 359 | 246 | 126 | 120 | 113 | 51.22% | -5.69% | 0.26% | positive |
| bonus_issue | 81 | 78 | 41 | 37 | 3 | 52.56% | 1.44% | 0.56% | positive |
| disclosure_violation | 129 | 74 | 38 | 36 | 55 | 51.35% | -11.21% | -0.13% | positive |
| bond_with_warrant | 76 | 65 | 6 | 59 | 11 | 9.23% | -0.84% | 0.07% | conservative |
| spin_off | 84 | 54 | 17 | 37 | 30 | 31.48% | -38.90% | 0.62% | conservative |
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
