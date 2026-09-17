# Market-Adjusted Score Integration Report - 2026-09-17

Generated at: 2026-09-17 01:41:22

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260917.csv`

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

- Total rows: **212**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **212**

## Market-Adjusted Result Counts

- market_data_missing: **212**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 261200 | 덴티스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 261200 | 덴티스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 261200 | 덴티스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 261200 | 덴티스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 261200 | 덴티스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 261200 | 덴티스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 226950 | 올릭스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 443250 | 레뷰코퍼레이션 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 092600 | 앤씨앤 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 014970 | 삼륭물산 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 079940 | 가비아 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
