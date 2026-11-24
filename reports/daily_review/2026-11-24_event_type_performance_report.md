# Event-Type Performance Report - 2026-11-24

Generated at: 2026-11-24 06:54:37

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **13197**
- Evaluated rows: **10926**
- Success rows: **5193**
- Failure rows: **5733**
- Pending rows: **2271**
- Overall success rate: **47.53%**

## Best Event Types So Far

- `convertible_bond`: success rate 59.49% from 1360 evaluated cases.
- `paid_in_capital_increase`: success rate 57.10% from 2604 evaluated cases.
- `lawsuit`: success rate 51.74% from 547 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 26.09% from 92 evaluated cases.
- `supply_contract`: success rate 35.54% from 1660 evaluated cases.
- `spin_off`: success rate 39.34% from 122 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| major_shareholder_change | 3389 | 2755 | 1107 | 1648 | 634 | 40.18% | -13.94% | -0.81% | conservative |
| paid_in_capital_increase | 3125 | 2604 | 1487 | 1117 | 521 | 57.10% | -7.54% | -0.21% | positive |
| supply_contract | 1986 | 1660 | 590 | 1070 | 326 | 35.54% | -2.46% | -0.70% | conservative |
| convertible_bond | 1693 | 1360 | 809 | 551 | 333 | 59.49% | -7.51% | 0.24% | positive |
| merger | 914 | 818 | 377 | 441 | 96 | 46.09% | -2.74% | 4.89% | conservative |
| lawsuit | 668 | 547 | 283 | 264 | 121 | 51.74% | -17.28% | -0.45% | positive |
| investment_decision | 655 | 540 | 279 | 261 | 115 | 51.67% | -5.53% | 0.16% | positive |
| disclosure_violation | 230 | 160 | 70 | 90 | 70 | 43.75% | -21.32% | -0.91% | conservative |
| bond_with_warrant | 163 | 151 | 63 | 88 | 12 | 41.72% | -4.04% | 0.04% | conservative |
| spin_off | 158 | 122 | 48 | 74 | 36 | 39.34% | -20.29% | 0.83% | conservative |
| bonus_issue | 120 | 117 | 56 | 61 | 3 | 47.86% | 2.30% | 0.36% | conservative |
| earnings_guidance | 96 | 92 | 24 | 68 | 4 | 26.09% | -0.16% | -1.87% | conservative |

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
