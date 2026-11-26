# Event-Type Performance Report - 2026-11-26

Generated at: 2026-11-26 05:02:15

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **13534**
- Evaluated rows: **11263**
- Success rows: **5386**
- Failure rows: **5877**
- Pending rows: **2271**
- Overall success rate: **47.82%**

## Best Event Types So Far

- `convertible_bond`: success rate 59.87% from 1388 evaluated cases.
- `paid_in_capital_increase`: success rate 56.15% from 2668 evaluated cases.
- `bonus_issue`: success rate 52.71% from 129 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 29.17% from 96 evaluated cases.
- `supply_contract`: success rate 36.27% from 1704 evaluated cases.
- `spin_off`: success rate 39.02% from 123 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| major_shareholder_change | 3453 | 2819 | 1126 | 1693 | 634 | 39.94% | -13.61% | -0.77% | conservative |
| paid_in_capital_increase | 3189 | 2668 | 1498 | 1170 | 521 | 56.15% | -7.50% | -0.23% | positive |
| supply_contract | 2030 | 1704 | 618 | 1086 | 326 | 36.27% | -2.37% | -0.63% | conservative |
| convertible_bond | 1721 | 1388 | 831 | 557 | 333 | 59.87% | -7.45% | 0.15% | positive |
| merger | 1008 | 912 | 466 | 446 | 96 | 51.10% | -2.41% | 4.76% | positive |
| lawsuit | 679 | 558 | 288 | 270 | 121 | 51.61% | -16.94% | -0.43% | positive |
| investment_decision | 667 | 552 | 282 | 270 | 115 | 51.09% | -5.39% | 0.19% | positive |
| disclosure_violation | 233 | 163 | 70 | 93 | 70 | 42.94% | -20.90% | -0.80% | conservative |
| bond_with_warrant | 163 | 151 | 63 | 88 | 12 | 41.72% | -4.04% | 0.04% | conservative |
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
