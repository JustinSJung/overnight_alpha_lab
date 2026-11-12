# Event-Type Performance Report - 2026-11-12

Generated at: 2026-11-12 03:55:07

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **11757**
- Evaluated rows: **9486**
- Success rows: **4459**
- Failure rows: **5027**
- Pending rows: **2271**
- Overall success rate: **47.01%**

## Best Event Types So Far

- `convertible_bond`: success rate 57.76% from 1198 evaluated cases.
- `paid_in_capital_increase`: success rate 55.96% from 2325 evaluated cases.
- `lawsuit`: success rate 52.08% from 457 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 19.51% from 82 evaluated cases.
- `supply_contract`: success rate 35.83% from 1415 evaluated cases.
- `spin_off`: success rate 38.98% from 118 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2846 | 2325 | 1301 | 1024 | 521 | 55.96% | -7.26% | -0.19% | positive |
| major_shareholder_change | 2930 | 2296 | 923 | 1373 | 634 | 40.20% | -9.46% | -0.71% | conservative |
| supply_contract | 1741 | 1415 | 507 | 908 | 326 | 35.83% | -2.60% | -0.65% | conservative |
| convertible_bond | 1531 | 1198 | 692 | 506 | 333 | 57.76% | -6.76% | 0.52% | positive |
| merger | 824 | 728 | 319 | 409 | 96 | 43.82% | -2.70% | 5.12% | conservative |
| investment_decision | 580 | 465 | 240 | 225 | 115 | 51.61% | -5.28% | 0.24% | positive |
| lawsuit | 578 | 457 | 238 | 219 | 121 | 52.08% | -17.10% | -0.47% | positive |
| disclosure_violation | 214 | 144 | 59 | 85 | 70 | 40.97% | -22.30% | -0.34% | conservative |
| bond_with_warrant | 154 | 142 | 62 | 80 | 12 | 43.66% | -0.08% | 0.05% | conservative |
| spin_off | 154 | 118 | 46 | 72 | 36 | 38.98% | -20.99% | 0.93% | conservative |
| bonus_issue | 119 | 116 | 56 | 60 | 3 | 48.28% | 2.27% | 0.38% | conservative |
| earnings_guidance | 86 | 82 | 16 | 66 | 4 | 19.51% | -0.20% | -1.89% | conservative |

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
