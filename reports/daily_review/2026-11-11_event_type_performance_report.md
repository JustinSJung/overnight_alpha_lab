# Event-Type Performance Report - 2026-11-11

Generated at: 2026-11-11 06:03:15

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **11611**
- Evaluated rows: **9340**
- Success rows: **4392**
- Failure rows: **4948**
- Pending rows: **2271**
- Overall success rate: **47.02%**

## Best Event Types So Far

- `convertible_bond`: success rate 57.74% from 1169 evaluated cases.
- `paid_in_capital_increase`: success rate 56.14% from 2298 evaluated cases.
- `investment_decision`: success rate 52.17% from 460 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 25.00% from 64 evaluated cases.
- `supply_contract`: success rate 35.85% from 1403 evaluated cases.
- `spin_off`: success rate 37.93% from 116 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2819 | 2298 | 1290 | 1008 | 521 | 56.14% | -7.22% | -0.18% | positive |
| major_shareholder_change | 2892 | 2258 | 902 | 1356 | 634 | 39.95% | -9.65% | -0.81% | conservative |
| supply_contract | 1729 | 1403 | 503 | 900 | 326 | 35.85% | -2.62% | -0.64% | conservative |
| convertible_bond | 1502 | 1169 | 675 | 494 | 333 | 57.74% | -7.00% | 0.35% | positive |
| merger | 821 | 725 | 318 | 407 | 96 | 43.86% | -2.70% | 5.15% | conservative |
| investment_decision | 575 | 460 | 240 | 220 | 115 | 52.17% | -5.12% | 0.25% | positive |
| lawsuit | 576 | 455 | 236 | 219 | 121 | 51.87% | -17.17% | -0.46% | positive |
| disclosure_violation | 212 | 142 | 58 | 84 | 70 | 40.85% | -22.61% | -0.31% | conservative |
| bond_with_warrant | 146 | 134 | 54 | 80 | 12 | 40.30% | 0.04% | 0.21% | conservative |
| spin_off | 152 | 116 | 44 | 72 | 36 | 37.93% | -21.37% | 0.98% | conservative |
| bonus_issue | 119 | 116 | 56 | 60 | 3 | 48.28% | 2.27% | 0.38% | conservative |
| earnings_guidance | 68 | 64 | 16 | 48 | 4 | 25.00% | -0.20% | -0.17% | conservative |

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
