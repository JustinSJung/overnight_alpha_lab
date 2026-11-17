# Event-Type Performance Report - 2026-11-17

Generated at: 2026-11-17 05:39:54

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **12432**
- Evaluated rows: **10161**
- Success rows: **4695**
- Failure rows: **5466**
- Pending rows: **2271**
- Overall success rate: **46.21%**

## Best Event Types So Far

- `convertible_bond`: success rate 57.65% from 1275 evaluated cases.
- `paid_in_capital_increase`: success rate 55.17% from 2416 evaluated cases.
- `investment_decision`: success rate 51.02% from 490 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 26.09% from 92 evaluated cases.
- `supply_contract`: success rate 36.22% from 1513 evaluated cases.
- `major_shareholder_change`: success rate 38.05% from 2570 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| major_shareholder_change | 3204 | 2570 | 978 | 1592 | 634 | 38.05% | -14.72% | -0.70% | conservative |
| paid_in_capital_increase | 2937 | 2416 | 1333 | 1083 | 521 | 55.17% | -8.18% | -0.17% | positive |
| supply_contract | 1839 | 1513 | 548 | 965 | 326 | 36.22% | -2.33% | -0.57% | conservative |
| convertible_bond | 1608 | 1275 | 735 | 540 | 333 | 57.65% | -7.74% | 0.41% | positive |
| merger | 869 | 773 | 354 | 419 | 96 | 45.80% | -2.49% | 4.98% | conservative |
| lawsuit | 620 | 499 | 246 | 253 | 121 | 49.30% | -17.89% | -0.30% | conservative |
| investment_decision | 605 | 490 | 250 | 240 | 115 | 51.02% | -6.02% | 0.21% | positive |
| bond_with_warrant | 162 | 150 | 63 | 87 | 12 | 42.00% | -4.08% | 0.03% | conservative |
| disclosure_violation | 218 | 148 | 61 | 87 | 70 | 41.22% | -21.63% | -0.38% | conservative |
| spin_off | 155 | 119 | 47 | 72 | 36 | 39.50% | -20.82% | 0.89% | conservative |
| bonus_issue | 119 | 116 | 56 | 60 | 3 | 48.28% | 2.27% | 0.38% | conservative |
| earnings_guidance | 96 | 92 | 24 | 68 | 4 | 26.09% | -0.16% | -1.87% | conservative |

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
