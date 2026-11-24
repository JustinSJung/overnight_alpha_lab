# Market-Adjusted Score Integration Report - 2026-11-24

Generated at: 2026-11-24 06:54:18

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261124.csv`

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

- Total rows: **221**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **221**

## Market-Adjusted Result Counts

- market_data_missing: **221**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 009830 | 한화솔루션 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 009830 | 한화솔루션 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 290560 | 파라택시스이더리움 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 276040 | 스코넥 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 320000 | 한울반도체 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 0153R0 | 바로팜 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 006370 | 대구백화점 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 262260 | 에이프로 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 262260 | 에이프로 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 033270 | 유나이티드 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 033270 | 유나이티드 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 0220W0 | 한화머시너리앤서비스홀딩스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 053210 | 케이티스카이라이프 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 358570 | 지아이이노베이션 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 000720 | 현대건설 | positive | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
