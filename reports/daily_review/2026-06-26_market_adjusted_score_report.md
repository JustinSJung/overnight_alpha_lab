# Market-Adjusted Score Integration Report - 2026-06-26

Generated at: 2026-06-26 16:24:22

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260626.csv`

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

- Total rows: **13**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **13**

## Market-Adjusted Result Counts

- pending: **13**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | negative | pending | 0 | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | negative | pending | 0 | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | negative | pending | 0 | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | negative | pending | 0 | N/A |
| 1970-01-01 | 011810 | STX | volatile | pending | 0 | N/A |
| 1970-01-01 | 011810 | STX | volatile | pending | 0 | N/A |
| 1970-01-01 | 221840 | 하이즈항공 | negative | pending | 0 | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | negative | pending | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | pending | 0 | N/A |
| 1970-01-01 | 014130 | 한익스프레스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 014130 | 한익스프레스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 014130 | 한익스프레스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 082740 | 한화엔진 | positive | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
