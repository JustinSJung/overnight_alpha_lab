# Event-Type Performance Report - 2026-11-04

Generated at: 2026-11-04 02:54:16

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **10597**
- Evaluated rows: **8331**
- Success rows: **3938**
- Failure rows: **4393**
- Pending rows: **2266**
- Overall success rate: **47.27%**

## Best Event Types So Far

- `convertible_bond`: success rate 57.92% from 1036 evaluated cases.
- `paid_in_capital_increase`: success rate 57.59% from 2056 evaluated cases.
- `lawsuit`: success rate 56.48% from 386 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 27.12% from 59 evaluated cases.
- `supply_contract`: success rate 34.23% from 1271 evaluated cases.
- `major_shareholder_change`: success rate 39.13% from 2006 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2577 | 2056 | 1184 | 872 | 521 | 57.59% | -7.61% | -0.20% | positive |
| major_shareholder_change | 2639 | 2006 | 785 | 1221 | 633 | 39.13% | -9.43% | -0.77% | conservative |
| supply_contract | 1597 | 1271 | 435 | 836 | 326 | 34.23% | -2.52% | -0.66% | conservative |
| convertible_bond | 1369 | 1036 | 600 | 436 | 333 | 57.92% | -7.42% | 0.36% | positive |
| merger | 759 | 663 | 311 | 352 | 96 | 46.91% | -2.71% | 5.67% | conservative |
| investment_decision | 515 | 400 | 196 | 204 | 115 | 49.00% | -4.80% | -0.11% | conservative |
| lawsuit | 507 | 386 | 218 | 168 | 121 | 56.48% | -16.51% | -0.52% | positive |
| disclosure_violation | 203 | 133 | 54 | 79 | 70 | 40.60% | -20.37% | -0.28% | conservative |
| bond_with_warrant | 145 | 133 | 53 | 80 | 12 | 39.85% | 0.05% | 0.23% | conservative |
| bonus_issue | 105 | 102 | 42 | 60 | 3 | 41.18% | 0.43% | -0.58% | conservative |
| spin_off | 118 | 86 | 44 | 42 | 32 | 51.16% | -25.03% | 1.62% | positive |
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
