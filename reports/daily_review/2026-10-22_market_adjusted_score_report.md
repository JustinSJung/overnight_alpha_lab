# Market-Adjusted Score Integration Report - 2026-10-22

Generated at: 2026-10-22 01:25:55

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261022.csv`

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

- Total rows: **169**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **169**

## Market-Adjusted Result Counts

- market_data_missing: **169**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 011000 | 진원생명과학 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 043100 | 알파AI | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 043100 | 알파AI | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 043100 | 알파AI | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 305090 | 마이크로디지탈 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 305090 | 마이크로디지탈 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 305090 | 마이크로디지탈 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 305090 | 마이크로디지탈 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 084110 | 휴온스글로벌 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 243070 | 휴온스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 038060 | 루멘스바이오스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 038060 | 루멘스바이오스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 038060 | 루멘스바이오스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 192410 | 오늘이엔엠 | negative | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
