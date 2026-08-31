# Event-Type Performance Report - 2026-08-31

Generated at: 2026-08-31 01:14:17

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **1785**
- Evaluated rows: **292**
- Success rows: **82**
- Failure rows: **210**
- Pending rows: **1493**
- Overall success rate: **28.08%**

## Best Event Types So Far

- `lawsuit`: success rate 100.00% from 4 evaluated cases.
- `convertible_bond`: success rate 48.57% from 35 evaluated cases.
- `paid_in_capital_increase`: success rate 39.68% from 63 evaluated cases.

## Weak Event Types So Far

- `merger`: success rate 0.00% from 10 evaluated cases.
- `investment_decision`: success rate 0.00% from 4 evaluated cases.
- `disclosure_violation`: success rate 0.00% from 4 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| major_shareholder_change | 526 | 106 | 22 | 84 | 420 | 20.75% | -43.85% | 0.03% | conservative |
| paid_in_capital_increase | 319 | 63 | 25 | 38 | 256 | 39.68% | -45.23% | -1.33% | conservative |
| supply_contract | 303 | 60 | 12 | 48 | 243 | 20.00% | -4.00% | -1.40% | conservative |
| convertible_bond | 282 | 35 | 17 | 18 | 247 | 48.57% | -9.87% | -1.60% | conservative |
| merger | 71 | 10 | 0 | 10 | 61 | 0.00% | 5.17% | 1.14% | conservative |
| spin_off | 24 | 6 | 2 | 4 | 18 | 33.33% | -1.41% | -0.57% | conservative |
| investment_decision | 96 | 4 | 0 | 4 | 92 | 0.00% | -0.13% | 0.40% | conservative |
| lawsuit | 95 | 4 | 4 | 0 | 91 | 100.00% | 0.13% | -1.27% | positive |
| disclosure_violation | 52 | 4 | 0 | 4 | 48 | 0.00% | -74.84% | 0.00% | conservative |
| bond_with_warrant | 10 | 0 | 0 | 0 | 10 | N/A | N/A | N/A | neutral |
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
