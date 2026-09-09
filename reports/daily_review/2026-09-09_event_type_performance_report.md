# Event-Type Performance Report - 2026-09-09

Generated at: 2026-09-09 00:53:51

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **3638**
- Evaluated rows: **1953**
- Success rows: **856**
- Failure rows: **1097**
- Pending rows: **1685**
- Overall success rate: **43.83%**

## Best Event Types So Far

- `lawsuit`: success rate 73.61% from 72 evaluated cases.
- `paid_in_capital_increase`: success rate 63.39% from 590 evaluated cases.
- `convertible_bond`: success rate 61.14% from 229 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 6.25% from 16 evaluated cases.
- `disclosure_violation`: success rate 6.67% from 15 evaluated cases.
- `merger`: success rate 14.04% from 57 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 893 | 590 | 374 | 216 | 303 | 63.39% | -5.70% | 0.46% | positive |
| major_shareholder_change | 1024 | 541 | 149 | 392 | 483 | 27.54% | -13.47% | -0.64% | conservative |
| supply_contract | 579 | 317 | 83 | 234 | 262 | 26.18% | -2.34% | -0.89% | conservative |
| convertible_bond | 502 | 229 | 140 | 89 | 273 | 61.14% | -4.93% | 0.02% | positive |
| lawsuit | 168 | 72 | 53 | 19 | 96 | 73.61% | -4.84% | -0.92% | positive |
| investment_decision | 164 | 63 | 29 | 34 | 101 | 46.03% | 4.28% | 3.31% | conservative |
| merger | 135 | 57 | 8 | 49 | 78 | 14.04% | 0.50% | 1.34% | conservative |
| bonus_issue | 41 | 38 | 12 | 26 | 3 | 31.58% | -0.82% | 0.37% | conservative |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -3.30% | -0.16% | conservative |
| disclosure_violation | 65 | 15 | 1 | 14 | 50 | 6.67% | -26.52% | 0.68% | conservative |
| spin_off | 37 | 15 | 6 | 9 | 22 | 40.00% | -7.01% | -0.17% | conservative |
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
