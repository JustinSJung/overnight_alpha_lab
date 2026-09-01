# Event-Type Performance Report - 2026-09-01

Generated at: 2026-09-01 02:02:03

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **2088**
- Evaluated rows: **595**
- Success rows: **221**
- Failure rows: **374**
- Pending rows: **1493**
- Overall success rate: **37.14%**

## Best Event Types So Far

- `bond_with_warrant`: success rate 100.00% from 1 evaluated cases.
- `lawsuit`: success rate 87.50% from 16 evaluated cases.
- `convertible_bond`: success rate 64.52% from 62 evaluated cases.

## Weak Event Types So Far

- `merger`: success rate 6.25% from 16 evaluated cases.
- `disclosure_violation`: success rate 16.67% from 6 evaluated cases.
- `supply_contract`: success rate 19.65% from 173 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| supply_contract | 416 | 173 | 34 | 139 | 243 | 19.65% | -1.31% | -1.44% | conservative |
| major_shareholder_change | 576 | 156 | 40 | 116 | 420 | 25.64% | -32.99% | -0.12% | conservative |
| paid_in_capital_increase | 392 | 136 | 77 | 59 | 256 | 56.62% | -19.67% | 2.28% | positive |
| convertible_bond | 309 | 62 | 40 | 22 | 247 | 64.52% | -10.02% | -1.69% | positive |
| investment_decision | 114 | 22 | 10 | 12 | 92 | 45.45% | -0.68% | -2.07% | conservative |
| lawsuit | 107 | 16 | 14 | 2 | 91 | 87.50% | -12.51% | -1.20% | positive |
| merger | 77 | 16 | 1 | 15 | 61 | 6.25% | 3.11% | 0.41% | conservative |
| spin_off | 25 | 7 | 3 | 4 | 18 | 42.86% | 0.90% | 1.42% | conservative |
| disclosure_violation | 54 | 6 | 1 | 5 | 48 | 16.67% | -50.25% | 0.02% | conservative |
| bond_with_warrant | 11 | 1 | 1 | 0 | 10 | 100.00% | 0.00% | -2.57% | positive |
| earnings_guidance | 4 | 0 | 0 | 0 | 4 | N/A | N/A | N/A | neutral |
| bonus_issue | 3 | 0 | 0 | 0 | 3 | N/A | N/A | N/A | neutral |

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
