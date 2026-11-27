# Event-Type Performance Report - 2026-11-27

Generated at: 2026-11-27 05:32:10

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **13741**
- Evaluated rows: **11470**
- Success rows: **5465**
- Failure rows: **6005**
- Pending rows: **2271**
- Overall success rate: **47.65%**

## Best Event Types So Far

- `convertible_bond`: success rate 57.80% from 1443 evaluated cases.
- `paid_in_capital_increase`: success rate 55.94% from 2703 evaluated cases.
- `lawsuit`: success rate 52.86% from 577 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 29.17% from 96 evaluated cases.
- `supply_contract`: success rate 36.47% from 1741 evaluated cases.
- `spin_off`: success rate 39.02% from 123 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| major_shareholder_change | 3493 | 2859 | 1150 | 1709 | 634 | 40.22% | -13.44% | -0.71% | conservative |
| paid_in_capital_increase | 3224 | 2703 | 1512 | 1191 | 521 | 55.94% | -7.57% | -0.20% | positive |
| supply_contract | 2067 | 1741 | 635 | 1106 | 326 | 36.47% | -2.29% | -0.62% | conservative |
| convertible_bond | 1776 | 1443 | 834 | 609 | 333 | 57.80% | -7.23% | 0.38% | positive |
| merger | 1011 | 915 | 469 | 446 | 96 | 51.26% | -2.40% | 4.76% | positive |
| lawsuit | 698 | 577 | 305 | 272 | 121 | 52.86% | -16.30% | -0.43% | positive |
| investment_decision | 677 | 562 | 283 | 279 | 115 | 50.36% | -5.21% | 0.19% | positive |
| disclosure_violation | 233 | 163 | 70 | 93 | 70 | 42.94% | -20.90% | -0.80% | conservative |
| bond_with_warrant | 171 | 159 | 63 | 96 | 12 | 39.62% | -4.00% | 0.13% | conservative |
| bonus_issue | 132 | 129 | 68 | 61 | 3 | 52.71% | 2.63% | 0.58% | positive |
| spin_off | 159 | 123 | 48 | 75 | 36 | 39.02% | -20.11% | 0.81% | conservative |
| earnings_guidance | 100 | 96 | 28 | 68 | 4 | 29.17% | 0.03% | -1.54% | conservative |

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
