# Event-Type Performance Report - 2026-10-23

Generated at: 2026-10-23 01:25:44

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **8751**
- Evaluated rows: **6487**
- Success rows: **2842**
- Failure rows: **3645**
- Pending rows: **2264**
- Overall success rate: **43.81%**

## Best Event Types So Far

- `earnings_guidance`: success rate 81.82% from 11 evaluated cases.
- `paid_in_capital_increase`: success rate 57.82% from 1752 evaluated cases.
- `lawsuit`: success rate 55.17% from 319 evaluated cases.

## Weak Event Types So Far

- `merger`: success rate 19.89% from 352 evaluated cases.
- `bond_with_warrant`: success rate 23.81% from 105 evaluated cases.
- `supply_contract`: success rate 30.57% from 988 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2272 | 1752 | 1013 | 739 | 520 | 57.82% | -8.30% | -0.00% | positive |
| major_shareholder_change | 2182 | 1549 | 541 | 1008 | 633 | 34.93% | -12.09% | -0.65% | conservative |
| supply_contract | 1314 | 988 | 302 | 686 | 326 | 30.57% | -2.39% | -0.70% | conservative |
| convertible_bond | 1145 | 812 | 415 | 397 | 333 | 51.11% | -8.05% | 1.02% | positive |
| merger | 447 | 352 | 70 | 282 | 95 | 19.89% | -12.83% | 0.27% | conservative |
| lawsuit | 440 | 319 | 176 | 143 | 121 | 55.17% | -18.37% | -0.62% | positive |
| investment_decision | 421 | 306 | 159 | 147 | 115 | 51.96% | -5.33% | -0.24% | positive |
| disclosure_violation | 182 | 112 | 49 | 63 | 70 | 43.75% | -19.84% | -0.36% | conservative |
| bond_with_warrant | 117 | 105 | 25 | 80 | 12 | 23.81% | -0.63% | 0.47% | conservative |
| bonus_issue | 103 | 100 | 42 | 58 | 3 | 42.00% | 0.46% | -0.37% | conservative |
| spin_off | 113 | 81 | 41 | 40 | 32 | 50.62% | -26.56% | 1.76% | positive |
| earnings_guidance | 15 | 11 | 9 | 2 | 4 | 81.82% | 0.95% | 2.91% | positive |

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
