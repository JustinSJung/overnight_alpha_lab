# Event-Type Performance Report - 2026-09-15

Generated at: 2026-09-15 01:44:49

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **4483**
- Evaluated rows: **2795**
- Success rows: **1226**
- Failure rows: **1569**
- Pending rows: **1688**
- Overall success rate: **43.86%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 2 evaluated cases.
- `lawsuit`: success rate 72.64% from 106 evaluated cases.
- `investment_decision`: success rate 64.96% from 117 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 6.25% from 16 evaluated cases.
- `spin_off`: success rate 20.00% from 35 evaluated cases.
- `merger`: success rate 22.22% from 90 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 1145 | 842 | 509 | 333 | 303 | 60.45% | -6.83% | 0.67% | positive |
| major_shareholder_change | 1179 | 696 | 193 | 503 | 483 | 27.73% | -13.97% | -0.81% | conservative |
| supply_contract | 707 | 445 | 124 | 321 | 262 | 27.87% | -2.53% | -0.81% | conservative |
| convertible_bond | 620 | 347 | 174 | 173 | 273 | 50.14% | -10.53% | 2.16% | positive |
| investment_decision | 218 | 117 | 76 | 41 | 101 | 64.96% | 3.10% | 1.71% | positive |
| lawsuit | 204 | 106 | 77 | 29 | 98 | 72.64% | -8.03% | -2.11% | positive |
| merger | 168 | 90 | 20 | 70 | 78 | 22.22% | -7.67% | 1.15% | conservative |
| bonus_issue | 57 | 54 | 28 | 26 | 3 | 51.85% | -0.06% | 0.78% | positive |
| disclosure_violation | 95 | 45 | 15 | 30 | 50 | 33.33% | -11.03% | 1.03% | conservative |
| spin_off | 58 | 35 | 7 | 28 | 23 | 20.00% | -51.65% | -0.17% | conservative |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -3.30% | -0.16% | conservative |
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
