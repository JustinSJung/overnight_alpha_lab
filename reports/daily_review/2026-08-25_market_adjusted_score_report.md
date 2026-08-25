# Market-Adjusted Score Integration Report - 2026-08-25

Generated at: 2026-08-25 22:50:24

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260825.csv`

## Purpose

This report converts market-adjusted evaluation results into recommendation score adjustment signals.

The goal is to reward predictions that outperform the market and penalize results that only appear successful because of broader market movement.

## Score Rules

| Market-Adjusted Result | Score Adjustment |
|---|---:|
| market_adjusted_success | 15 |
| market_driven_weak_success | -5 |
| relative_success_but_absolute_loss | 5 |
| market_adjusted_failure | -15 |
| relative_failure_despite_absolute_gain | -10 |
| market_adjusted_volatility_success | 10 |
| market_driven_volatility | -5 |
| volatility_overestimated | -10 |
| market_data_missing | 0 |
| pending | 0 |
| unknown | 0 |

## Summary

- Total rows: **15**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **15**

## Market-Adjusted Result Counts

- pending: **15**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 270520 | 앱튼 | volatile | pending | 0 | N/A |
| 1970-01-01 | 000210 | DL | positive | pending | 0 | N/A |
| 1970-01-01 | 014970 | 삼륭물산 | negative | pending | 0 | N/A |
| 1970-01-01 | 375500 | DL이앤씨 | positive | pending | 0 | N/A |
| 1970-01-01 | 267250 | HD현대 | positive | pending | 0 | N/A |
| 1970-01-01 | 216400 | 인바이츠바이오코아 | negative | pending | 0 | N/A |
| 1970-01-01 | 216400 | 인바이츠바이오코아 | negative | pending | 0 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | positive | pending | 0 | N/A |
| 1970-01-01 | 000950 | 전방 | volatile | pending | 0 | N/A |
| 1970-01-01 | 000950 | 전방 | volatile | pending | 0 | N/A |
| 1970-01-01 | 006260 | LS | volatile | pending | 0 | N/A |
| 1970-01-01 | 006260 | LS | volatile | pending | 0 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | pending | 0 | N/A |
| 1970-01-01 | 034730 | SK | volatile | pending | 0 | N/A |
| 1970-01-01 | 034730 | SK | volatile | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
