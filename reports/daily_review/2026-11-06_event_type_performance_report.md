# Event-Type Performance Report - 2026-11-06

Generated at: 2026-11-06 03:20:38

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **11006**
- Evaluated rows: **8736**
- Success rows: **4106**
- Failure rows: **4630**
- Pending rows: **2270**
- Overall success rate: **47.00%**

## Best Event Types So Far

- `paid_in_capital_increase`: success rate 57.85% from 2152 evaluated cases.
- `convertible_bond`: success rate 57.83% from 1060 evaluated cases.
- `lawsuit`: success rate 51.99% from 427 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 27.12% from 59 evaluated cases.
- `supply_contract`: success rate 33.36% from 1310 evaluated cases.
- `spin_off`: success rate 38.60% from 114 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2673 | 2152 | 1245 | 907 | 521 | 57.85% | -7.41% | -0.34% | positive |
| major_shareholder_change | 2760 | 2127 | 853 | 1274 | 633 | 40.10% | -9.06% | -0.89% | conservative |
| supply_contract | 1636 | 1310 | 437 | 873 | 326 | 33.36% | -2.74% | -0.76% | conservative |
| convertible_bond | 1393 | 1060 | 613 | 447 | 333 | 57.83% | -7.33% | 0.39% | positive |
| merger | 787 | 691 | 314 | 377 | 96 | 45.44% | -2.81% | 5.38% | conservative |
| lawsuit | 548 | 427 | 222 | 205 | 121 | 51.99% | -15.80% | -0.44% | positive |
| investment_decision | 536 | 421 | 210 | 211 | 115 | 49.88% | -6.02% | -0.00% | conservative |
| disclosure_violation | 209 | 139 | 56 | 83 | 70 | 40.29% | -22.37% | -0.28% | conservative |
| bond_with_warrant | 146 | 134 | 54 | 80 | 12 | 40.30% | 0.04% | 0.21% | conservative |
| spin_off | 150 | 114 | 44 | 70 | 36 | 38.60% | -21.78% | 0.99% | conservative |
| bonus_issue | 105 | 102 | 42 | 60 | 3 | 41.18% | 0.43% | -0.58% | conservative |
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
