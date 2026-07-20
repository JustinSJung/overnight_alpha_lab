# Market-Adjusted Score Integration Report - 2026-07-20

Generated at: 2026-07-20 08:43:30

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260720.csv`

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

- Total rows: **36**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **36**

## Market-Adjusted Result Counts

- pending: **36**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 033310 | 엠투엔 | volatile | pending | 0 | N/A |
| 1970-01-01 | 290720 | 푸드나무 | negative | pending | 0 | N/A |
| 1970-01-01 | 389680 | 유디엠텍 | positive | pending | 0 | N/A |
| 1970-01-01 | 144510 | 지씨셀 | volatile | pending | 0 | N/A |
| 1970-01-01 | 078350 | 한양디지텍 | volatile | pending | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | pending | 0 | N/A |
| 1970-01-01 | 055550 | 신한지주 | volatile | pending | 0 | N/A |
| 1970-01-01 | 082270 | 젬백스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 033540 | 파라텍 | negative | pending | 0 | N/A |
| 1970-01-01 | 112610 | 씨에스윈드 | volatile | pending | 0 | N/A |
| 1970-01-01 | 112610 | 씨에스윈드 | volatile | pending | 0 | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | 0 | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | 0 | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | 0 | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | 0 | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | 0 | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | 0 | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | 0 | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | 0 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | volatile | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
