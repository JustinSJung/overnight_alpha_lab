# Event-Type Performance Report - 2026-09-04

Generated at: 2026-09-04 00:45:10

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **2974**
- Evaluated rows: **1480**
- Success rows: **690**
- Failure rows: **790**
- Pending rows: **1494**
- Overall success rate: **46.62%**

## Best Event Types So Far

- `lawsuit`: success rate 77.42% from 62 evaluated cases.
- `paid_in_capital_increase`: success rate 67.34% from 447 evaluated cases.
- `convertible_bond`: success rate 67.20% from 186 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 6.25% from 16 evaluated cases.
- `merger`: success rate 7.14% from 28 evaluated cases.
- `disclosure_violation`: success rate 10.00% from 10 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 703 | 447 | 301 | 146 | 256 | 67.34% | -8.18% | -0.17% | positive |
| major_shareholder_change | 805 | 385 | 116 | 269 | 420 | 30.13% | -17.41% | -0.53% | conservative |
| supply_contract | 508 | 265 | 61 | 204 | 243 | 23.02% | -1.47% | -1.34% | conservative |
| convertible_bond | 433 | 186 | 125 | 61 | 247 | 67.20% | -7.64% | -1.48% | positive |
| lawsuit | 153 | 62 | 48 | 14 | 91 | 77.42% | -4.60% | -1.08% | positive |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -0.82% | 0.37% | conservative |
| investment_decision | 127 | 35 | 20 | 15 | 92 | 57.14% | 6.66% | 5.23% | positive |
| merger | 89 | 28 | 2 | 26 | 61 | 7.14% | -2.19% | -0.20% | conservative |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -3.30% | -0.16% | conservative |
| disclosure_violation | 58 | 10 | 1 | 9 | 48 | 10.00% | -29.82% | 0.85% | conservative |
| spin_off | 27 | 8 | 3 | 5 | 19 | 37.50% | 0.66% | 1.02% | conservative |
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
