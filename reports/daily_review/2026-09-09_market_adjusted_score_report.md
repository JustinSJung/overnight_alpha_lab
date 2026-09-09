# Market-Adjusted Score Integration Report - 2026-09-09

Generated at: 2026-09-09 00:53:42

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260909.csv`

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

- Total rows: **135**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **135**

## Market-Adjusted Result Counts

- market_data_missing: **135**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 203400 | 에이비온 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 005930 | 삼성전자 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 199730 | 바이오인프라 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 199730 | 바이오인프라 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 020120 | 키다리스튜디오 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 009320 | 아진전자부품 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 009320 | 아진전자부품 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 010960 | 삼호개발 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 027410 | BGF | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 027040 | 서울전자통신 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 027040 | 서울전자통신 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 126600 | BGF에코머티리얼즈 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | negative | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
