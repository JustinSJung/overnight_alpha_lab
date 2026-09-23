# Event-Type Performance Report - 2026-09-23

Generated at: 2026-09-23 02:02:35

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **5719**
- Evaluated rows: **4031**
- Success rows: **1765**
- Failure rows: **2266**
- Pending rows: **1688**
- Overall success rate: **43.79%**

## Best Event Types So Far

- `earnings_guidance`: success rate 100.00% from 2 evaluated cases.
- `lawsuit`: success rate 60.99% from 182 evaluated cases.
- `paid_in_capital_increase`: success rate 58.03% from 1165 evaluated cases.

## Weak Event Types So Far

- `bond_with_warrant`: success rate 8.20% from 61 evaluated cases.
- `merger`: success rate 21.37% from 117 evaluated cases.
- `supply_contract`: success rate 28.79% from 580 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 1468 | 1165 | 676 | 489 | 303 | 58.03% | -5.97% | 0.28% | positive |
| major_shareholder_change | 1498 | 1015 | 338 | 677 | 483 | 33.30% | -11.78% | -1.06% | conservative |
| supply_contract | 842 | 580 | 167 | 413 | 262 | 28.79% | -2.19% | -0.74% | conservative |
| convertible_bond | 786 | 513 | 251 | 262 | 273 | 48.93% | -6.88% | 1.08% | conservative |
| investment_decision | 317 | 216 | 109 | 107 | 101 | 50.46% | -6.06% | 0.29% | positive |
| lawsuit | 280 | 182 | 111 | 71 | 98 | 60.99% | -9.85% | -0.58% | positive |
| merger | 195 | 117 | 25 | 92 | 78 | 21.37% | -12.75% | 0.83% | conservative |
| disclosure_violation | 120 | 70 | 37 | 33 | 50 | 52.86% | -10.47% | -0.13% | positive |
| bonus_issue | 65 | 62 | 29 | 33 | 3 | 46.77% | 1.82% | 0.56% | conservative |
| bond_with_warrant | 71 | 61 | 5 | 56 | 10 | 8.20% | -0.93% | -0.04% | conservative |
| spin_off | 71 | 48 | 15 | 33 | 23 | 31.25% | -41.87% | 0.28% | conservative |
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
