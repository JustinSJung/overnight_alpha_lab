# Event-Type Performance Report - 2026-09-02

Generated at: 2026-09-02 00:49:30

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **2449**
- Evaluated rows: **955**
- Success rows: **364**
- Failure rows: **591**
- Pending rows: **1494**
- Overall success rate: **38.12%**

## Best Event Types So Far

- `lawsuit`: success rate 91.18% from 34 evaluated cases.
- `convertible_bond`: success rate 69.93% from 153 evaluated cases.
- `paid_in_capital_increase`: success rate 53.18% from 220 evaluated cases.

## Weak Event Types So Far

- `bonus_issue`: success rate 0.00% from 8 evaluated cases.
- `bond_with_warrant`: success rate 6.25% from 16 evaluated cases.
- `merger`: success rate 8.00% from 25 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| major_shareholder_change | 666 | 246 | 54 | 192 | 420 | 21.95% | -21.83% | -0.47% | conservative |
| paid_in_capital_increase | 476 | 220 | 117 | 103 | 256 | 53.18% | -15.39% | 1.54% | positive |
| supply_contract | 459 | 216 | 37 | 179 | 243 | 17.13% | -1.42% | -1.50% | conservative |
| convertible_bond | 400 | 153 | 107 | 46 | 247 | 69.93% | -9.74% | -2.17% | positive |
| lawsuit | 125 | 34 | 31 | 3 | 91 | 91.18% | -6.86% | -1.39% | positive |
| merger | 86 | 25 | 2 | 23 | 61 | 8.00% | -2.30% | -0.11% | conservative |
| investment_decision | 115 | 23 | 11 | 12 | 92 | 47.83% | -0.59% | -2.14% | conservative |
| bond_with_warrant | 26 | 16 | 1 | 15 | 10 | 6.25% | -3.30% | -0.16% | conservative |
| spin_off | 27 | 8 | 3 | 5 | 19 | 37.50% | 0.66% | 1.02% | conservative |
| bonus_issue | 11 | 8 | 0 | 8 | 3 | 0.00% | -2.31% | -0.36% | conservative |
| disclosure_violation | 54 | 6 | 1 | 5 | 48 | 16.67% | -50.25% | 0.02% | conservative |
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
