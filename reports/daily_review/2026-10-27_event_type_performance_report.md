# Event-Type Performance Report - 2026-10-27

Generated at: 2026-10-27 02:03:14

## Purpose

This report summarizes prediction performance by disclosure event type. It helps identify which event types have historically produced stronger or weaker prediction results.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Overall Summary

- Total error-note rows: **9124**
- Evaluated rows: **6860**
- Success rows: **3008**
- Failure rows: **3852**
- Pending rows: **2264**
- Overall success rate: **43.85%**

## Best Event Types So Far

- `earnings_guidance`: success rate 88.24% from 17 evaluated cases.
- `paid_in_capital_increase`: success rate 57.29% from 1831 evaluated cases.
- `lawsuit`: success rate 53.04% from 345 evaluated cases.

## Weak Event Types So Far

- `merger`: success rate 23.29% from 425 evaluated cases.
- `bond_with_warrant`: success rate 23.81% from 105 evaluated cases.
- `supply_contract`: success rate 32.55% from 1060 evaluated cases.

## Event-Type Performance Table

| Event Type | Total | Evaluated | Success | Failure | Pending | Success Rate | Avg Next Open | Avg Next Close | Bias |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---|
| paid_in_capital_increase | 2351 | 1831 | 1049 | 782 | 520 | 57.29% | -8.28% | -0.04% | positive |
| major_shareholder_change | 2270 | 1637 | 568 | 1069 | 633 | 34.70% | -11.44% | -0.63% | conservative |
| supply_contract | 1386 | 1060 | 345 | 715 | 326 | 32.55% | -2.43% | -0.64% | conservative |
| convertible_bond | 1158 | 825 | 424 | 401 | 333 | 51.39% | -8.06% | 0.97% | positive |
| merger | 520 | 425 | 99 | 326 | 95 | 23.29% | -10.85% | 0.43% | conservative |
| lawsuit | 466 | 345 | 183 | 162 | 121 | 53.04% | -17.51% | -0.21% | positive |
| investment_decision | 435 | 320 | 168 | 152 | 115 | 52.50% | -5.00% | -0.06% | positive |
| disclosure_violation | 182 | 112 | 49 | 63 | 70 | 43.75% | -19.84% | -0.36% | conservative |
| bond_with_warrant | 117 | 105 | 25 | 80 | 12 | 23.81% | -0.63% | 0.47% | conservative |
| bonus_issue | 104 | 101 | 42 | 59 | 3 | 41.58% | 0.45% | -0.49% | conservative |
| spin_off | 114 | 82 | 41 | 41 | 32 | 50.00% | -26.23% | 1.75% | neutral |
| earnings_guidance | 21 | 17 | 15 | 2 | 4 | 88.24% | 1.17% | 4.25% | positive |

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
