# Event-Type Performance Report - 2026-09-22

Generated at: 2026-09-22 02:11:40

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **5571**
- Evaluated rows: **3883**
- Success rows: **1715**
- Failure rows: **2168**
- Pending rows: **1688**
- Overall success rate: **44.17%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 2 evaluated cases.
- `lawsuit`: success rate 61.24% from 178 evaluated cases.
- `paid_in_capital_increase`: success rate 58.58% from 1137 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 8.20% from 61 evaluated cases.
- `merger`: success rate 22.02% from 109 evaluated cases.
- `spin_off`: success rate 28.26% from 46 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 1440 | 1137 | 666 | 471 | 303 | 58.58% | -6.12% | 0.25% | positive |
| major_shareholder_change | 1463 | 980 | 329 | 651 | 483 | 33.57% | -12.19% | -1.08% | conservative |
| supply_contract | 814 | 552 | 157 | 395 | 262 | 28.44% | -2.12% | -0.77% | conservative |
| convertible_bond | 752 | 479 | 238 | 241 | 273 | 49.69% | -7.39% | 1.20% | conservative |
| investment_decision | 310 | 209 | 107 | 102 | 101 | 51.20% | -6.30% | 0.27% | positive |
| lawsuit | 276 | 178 | 109 | 69 | 98 | 61.24% | -10.07% | -0.59% | positive |
| merger | 187 | 109 | 24 | 85 | 78 | 22.02% | -13.69% | 0.84% | conservative |
| disclosure_violation | 119 | 69 | 36 | 33 | 50 | 52.17% | -10.62% | -0.09% | positive |
| bond_with_warrant | 71 | 61 | 5 | 56 | 10 | 8.20% | -0.93% | -0.04% | conservative |
| bonus_issue | 64 | 61 | 29 | 32 | 3 | 47.54% | 1.82% | 0.59% | conservative |
| spin_off | 69 | 46 | 13 | 33 | 23 | 28.26% | -43.62% | 0.14% | conservative |
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
