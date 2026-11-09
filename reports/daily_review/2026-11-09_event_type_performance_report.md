# Event-Type Performance Report - 2026-11-09

Generated at: 2026-11-09 02:28:15

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **11208**
- Evaluated rows: **8938**
- Success rows: **4188**
- Failure rows: **4750**
- Pending rows: **2270**
- Overall success rate: **46.86%**

## Best Event Types So Far

- `convertible_bond`: success rate 58.03% from 1089 evaluated cases.
- `paid_in_capital_increase`: success rate 57.43% from 2187 evaluated cases.
- `lawsuit`: success rate 51.15% from 436 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 27.12% from 59 evaluated cases.
- `supply_contract`: success rate 34.70% from 1363 evaluated cases.
- `spin_off`: success rate 38.60% from 114 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| major_shareholder_change | 2823 | 2190 | 865 | 1325 | 633 | 39.50% | -9.91% | -0.85% | conservative |
| paid_in_capital_increase | 2708 | 2187 | 1256 | 931 | 521 | 57.43% | -7.36% | -0.32% | positive |
| supply_contract | 1689 | 1363 | 473 | 890 | 326 | 34.70% | -2.71% | -0.72% | conservative |
| convertible_bond | 1422 | 1089 | 632 | 457 | 333 | 58.03% | -7.29% | 0.36% | positive |
| merger | 797 | 701 | 315 | 386 | 96 | 44.94% | -2.79% | 5.30% | conservative |
| lawsuit | 557 | 436 | 223 | 213 | 121 | 51.15% | -17.32% | -0.43% | positive |
| investment_decision | 537 | 422 | 210 | 212 | 115 | 49.76% | -6.01% | -0.01% | conservative |
| disclosure_violation | 209 | 139 | 56 | 83 | 70 | 40.29% | -22.37% | -0.28% | conservative |
| bond_with_warrant | 146 | 134 | 54 | 80 | 12 | 40.30% | 0.04% | 0.21% | conservative |
| spin_off | 150 | 114 | 44 | 70 | 36 | 38.60% | -21.78% | 0.99% | conservative |
| bonus_issue | 107 | 104 | 44 | 60 | 3 | 42.31% | 0.46% | -0.51% | conservative |
| earnings_guidance | 63 | 59 | 16 | 43 | 4 | 27.12% | -0.11% | 0.28% | conservative |

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
