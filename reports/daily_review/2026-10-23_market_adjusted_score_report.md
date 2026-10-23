# Market-Adjusted Score Integration Report - 2026-10-23

Generated at: 2026-10-23 01:25:37

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261023.csv`

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

- Total rows: **144**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **144**

## Market-Adjusted Result Counts

- market_data_missing: **143**
- pending: **1**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 006370 | 대구백화점 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 011560 | 세보엠이씨 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 396470 | 워트 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 000490 | 대동 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 002990 | 금호건설 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 002990 | 금호건설 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 030610 | 교보증권 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 030610 | 교보증권 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 030610 | 교보증권 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 030610 | 교보증권 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 030610 | 교보증권 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 030610 | 교보증권 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 317770 | 엑스페릭스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 317770 | 엑스페릭스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 066790 | 씨씨에스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 066790 | 씨씨에스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 078130 | 에스엠국일 | volatile | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
