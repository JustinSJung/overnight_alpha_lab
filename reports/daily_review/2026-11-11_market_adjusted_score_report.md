# Market-Adjusted Score Integration Report - 2026-11-11

Generated at: 2026-11-11 06:02:41

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261111.csv`

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

- Total rows: **206**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **206**

## Market-Adjusted Result Counts

- market_data_missing: **206**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 065420 | 에스아이리소스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 010960 | 삼호개발 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 010960 | 삼호개발 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 247540 | 에코프로비엠 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 247540 | 에코프로비엠 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 307180 | 아이엘 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 066790 | 씨씨에스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 300080 | 플리토 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 300080 | 플리토 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 005880 | 대한해운 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 005880 | 대한해운 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 005880 | 대한해운 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 001200 | 유진증권 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 185490 | 아이진 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 124500 | 아이티센글로벌 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
