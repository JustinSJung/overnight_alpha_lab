# Market-Adjusted Score Integration Report - 2026-11-12

Generated at: 2026-11-12 03:54:55

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261112.csv`

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

- Total rows: **146**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **146**

## Market-Adjusted Result Counts

- market_data_missing: **146**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 007540 | 샘표 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 248170 | 샘표식품 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 009190 | 대양금속 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 026910 | 광진실업 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 026910 | 광진실업 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 026910 | 광진실업 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 026910 | 광진실업 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 026910 | 광진실업 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 026910 | 광진실업 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 026910 | 광진실업 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 026910 | 광진실업 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 115440 | 우리넷 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 004150 | 한솔홀딩스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 004150 | 한솔홀딩스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 213500 | 한솔제지 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 213500 | 한솔제지 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | negative | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
