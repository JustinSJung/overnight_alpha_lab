# Event-Type Performance Report - 2026-09-11

Generated at: 2026-09-11 01:09:58

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **4110**
- Evaluated rows: **2424**
- Success rows: **1037**
- Failure rows: **1387**
- Pending rows: **1686**
- Overall success rate: **42.78%**

## Best Event Types So Far

- `lawsuit`: success rate 78.72% from 94 evaluated cases.
- `investment_decision`: success rate 62.24% from 98 evaluated cases.
- `paid_in_capital_increase`: success rate 59.81% from 729 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 6.25% from 16 evaluated cases.
- `spin_off`: success rate 20.59% from 34 evaluated cases.
- `merger`: success rate 20.69% from 87 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 1032 | 729 | 436 | 293 | 303 | 59.81% | -7.19% | 0.79% | positive |
| major_shareholder_change | 1114 | 631 | 167 | 464 | 483 | 26.47% | -15.29% | -0.66% | conservative |
| supply_contract | 638 | 376 | 100 | 276 | 262 | 26.60% | -2.62% | -0.81% | conservative |
| convertible_bond | 575 | 302 | 156 | 146 | 273 | 51.66% | -11.69% | 2.43% | positive |
| investment_decision | 199 | 98 | 61 | 37 | 101 | 62.24% | 1.95% | -0.68% | positive |
| lawsuit | 191 | 94 | 74 | 20 | 97 | 78.72% | -7.52% | -2.62% | positive |
| merger | 165 | 87 | 18 | 69 | 78 | 20.69% | -7.92% | 1.27% | conservative |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -0.82% | 0.37% | conservative |
| spin_off | 56 | 34 | 7 | 27 | 22 | 20.59% | -50.23% | -0.17% | conservative |
| disclosure_violation | 69 | 19 | 5 | 14 | 50 | 26.32% | -21.32% | 0.23% | conservative |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -3.30% | -0.16% | conservative |
| earnings_guidance | 4 | 0 | 0 | 0 | 4 | N/A | N/A | N/A | neutral |

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
