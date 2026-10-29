# Market-Adjusted Score Integration Report - 2026-10-07

Generated at: 2026-10-07 02:53:49

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261007.csv`

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

- Total rows: **237**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **237**

## Market-Adjusted Result Counts

- market_data_missing: **237**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 145210 | 다이나믹디자인 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 145210 | 다이나믹디자인 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 101360 | 에코앤드림 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 119830 | 아이텍 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 031860 | 디에이치엑스컴퍼니 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 418620 | E8 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 070300 | 퀀텀레일 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 070300 | 퀀텀레일 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 070300 | 퀀텀레일 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 002720 | 국제약품 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 002720 | 국제약품 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 002720 | 국제약품 | volatile | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
