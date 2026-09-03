# Market-Adjusted Score Integration Report - 2026-09-03

Generated at: 2026-09-03 00:53:35

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260903.csv`

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

- Total rows: **250**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **250**

## Market-Adjusted Result Counts

- market_data_missing: **250**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 007110 | 일신석재 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 0009K0 | 에임드바이오 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 066790 | 씨씨에스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 476060 | 온코닉테라퓨틱스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 001040 | CJ | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 079160 | CJ CGV | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 027040 | 서울전자통신 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 027040 | 서울전자통신 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 268280 | 미원에스씨 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 086710 | 선진뷰티사이언스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 300080 | 플리토 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 213420 | 덕산네오룩스 | negative | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
