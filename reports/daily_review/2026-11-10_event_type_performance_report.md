# Event-Type Performance Report - 2026-11-10

Generated at: 2026-11-10 05:37:14

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **11405**
- Evaluated rows: **9134**
- Success rows: **4274**
- Failure rows: **4860**
- Pending rows: **2271**
- Overall success rate: **46.79%**

## Best Event Types So Far

- `convertible_bond`: success rate 57.17% from 1130 evaluated cases.
- `paid_in_capital_increase`: success rate 56.10% from 2246 evaluated cases.
- `investment_decision`: success rate 52.77% from 451 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 25.81% from 62 evaluated cases.
- `supply_contract`: success rate 35.07% from 1380 evaluated cases.
- `spin_off`: success rate 37.93% from 116 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2767 | 2246 | 1260 | 986 | 521 | 56.10% | -7.01% | -0.23% | positive |
| major_shareholder_change | 2857 | 2223 | 885 | 1338 | 634 | 39.81% | -9.74% | -0.80% | conservative |
| supply_contract | 1706 | 1380 | 484 | 896 | 326 | 35.07% | -2.65% | -0.67% | conservative |
| convertible_bond | 1463 | 1130 | 646 | 484 | 333 | 57.17% | -7.13% | 0.36% | positive |
| merger | 798 | 702 | 315 | 387 | 96 | 44.87% | -2.78% | 5.29% | conservative |
| investment_decision | 566 | 451 | 238 | 213 | 115 | 52.77% | -5.20% | 0.25% | positive |
| lawsuit | 566 | 445 | 230 | 215 | 121 | 51.69% | -16.92% | -0.46% | positive |
| disclosure_violation | 211 | 141 | 58 | 83 | 70 | 41.13% | -22.06% | -0.31% | conservative |
| bond_with_warrant | 146 | 134 | 54 | 80 | 12 | 40.30% | 0.04% | 0.21% | conservative |
| spin_off | 152 | 116 | 44 | 72 | 36 | 37.93% | -21.37% | 0.98% | conservative |
| bonus_issue | 107 | 104 | 44 | 60 | 3 | 42.31% | 0.46% | -0.51% | conservative |
| earnings_guidance | 66 | 62 | 16 | 46 | 4 | 25.81% | -0.12% | -0.08% | conservative |

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
