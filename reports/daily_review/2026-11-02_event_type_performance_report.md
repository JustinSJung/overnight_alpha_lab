# Event-Type Performance Report - 2026-11-02

Generated at: 2026-11-02 02:02:35

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **10274**
- Evaluated rows: **8008**
- Success rows: **3774**
- Failure rows: **4234**
- Pending rows: **2266**
- Overall success rate: **47.13%**

## Best Event Types So Far

- `paid_in_capital_increase`: success rate 57.90% from 2012 evaluated cases.
- `convertible_bond`: success rate 57.48% from 1009 evaluated cases.
- `lawsuit`: success rate 56.14% from 383 evaluated cases.

## Weak Event Types So Far

- `earnings_guidance`: success rate 27.12% from 59 evaluated cases.
- `supply_contract`: success rate 33.61% from 1211 evaluated cases.
- `major_shareholder_change`: success rate 38.38% from 1881 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2533 | 2012 | 1165 | 847 | 521 | 57.90% | -7.79% | -0.22% | positive |
| major_shareholder_change | 2514 | 1881 | 722 | 1159 | 633 | 38.38% | -10.03% | -0.72% | conservative |
| supply_contract | 1537 | 1211 | 407 | 804 | 326 | 33.61% | -2.62% | -0.65% | conservative |
| convertible_bond | 1342 | 1009 | 580 | 429 | 333 | 57.48% | -7.13% | 0.44% | positive |
| merger | 737 | 641 | 299 | 342 | 96 | 46.65% | -2.62% | 5.87% | conservative |
| lawsuit | 504 | 383 | 215 | 168 | 121 | 56.14% | -16.61% | -0.48% | positive |
| investment_decision | 487 | 372 | 180 | 192 | 115 | 48.39% | -5.14% | 0.08% | conservative |
| bond_with_warrant | 145 | 133 | 53 | 80 | 12 | 39.85% | 0.05% | 0.23% | conservative |
| disclosure_violation | 190 | 120 | 51 | 69 | 70 | 42.50% | -20.90% | -0.26% | conservative |
| bonus_issue | 105 | 102 | 42 | 60 | 3 | 41.18% | 0.43% | -0.58% | conservative |
| spin_off | 117 | 85 | 44 | 41 | 32 | 51.76% | -25.34% | 1.61% | positive |
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
