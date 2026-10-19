# Event-Type Performance Report - 2026-10-19

Generated at: 2026-10-19 00:40:09

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **8226**
- Evaluated rows: **5964**
- Success rows: **2635**
- Failure rows: **3329**
- Pending rows: **2262**
- Overall success rate: **44.18%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 4 evaluated cases.
- `lawsuit`: success rate 57.99% from 288 evaluated cases.
- `paid_in_capital_increase`: success rate 57.86% from 1661 evaluated cases.

## Weak Event Types So Far

- `merger`: success rate 18.99% from 316 evaluated cases.
- `bond_with_warrant`: success rate 23.08% from 104 evaluated cases.
- `supply_contract`: success rate 30.29% from 865 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2181 | 1661 | 961 | 700 | 520 | 57.86% | -7.66% | 0.19% | positive |
| major_shareholder_change | 2075 | 1442 | 501 | 941 | 633 | 34.74% | -12.90% | -0.55% | conservative |
| supply_contract | 1191 | 865 | 262 | 603 | 326 | 30.29% | -2.56% | -0.79% | conservative |
| convertible_bond | 1074 | 742 | 383 | 359 | 332 | 51.62% | -8.49% | 0.94% | positive |
| merger | 411 | 316 | 60 | 256 | 95 | 18.99% | -13.28% | 0.43% | conservative |
| lawsuit | 408 | 288 | 167 | 121 | 120 | 57.99% | -14.26% | -0.77% | positive |
| investment_decision | 382 | 267 | 143 | 124 | 115 | 53.56% | -6.13% | -0.06% | positive |
| bond_with_warrant | 116 | 104 | 24 | 80 | 12 | 23.08% | -0.63% | 0.54% | conservative |
| bonus_issue | 102 | 99 | 41 | 58 | 3 | 41.41% | 0.45% | -0.40% | conservative |
| disclosure_violation | 166 | 96 | 48 | 48 | 70 | 50.00% | -13.89% | -0.51% | neutral |
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
