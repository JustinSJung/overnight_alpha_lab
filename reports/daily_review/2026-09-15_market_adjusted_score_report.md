# Market-Adjusted Score Integration Report - 2026-09-15

Generated at: 2026-09-15 01:44:42

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260915.csv`

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

- Total rows: **194**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **194**

## Market-Adjusted Result Counts

- market_data_missing: **192**
- pending: **2**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 079190 | 케스피온 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 079190 | 케스피온 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 079190 | 케스피온 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 079190 | 케스피온 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 079190 | 케스피온 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 079190 | 케스피온 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 331920 | 셀레믹스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 032790 | 엠젠솔루션 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 002780 | 진흥기업 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 058110 | 멕아이씨에스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 058110 | 멕아이씨에스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 058110 | 멕아이씨에스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 058110 | 멕아이씨에스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 389020 | 자람테크놀로지 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 222080 | SFA넥셀 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 027740 | 마니커 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 027740 | 마니커 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 027740 | 마니커 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 038870 | 에코심플렉스 | positive | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
