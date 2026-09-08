# Market-Adjusted Score Integration Report - 2026-09-08

Generated at: 2026-09-08 01:05:16

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260908.csv`

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

- Total rows: **147**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **147**

## Market-Adjusted Result Counts

- market_data_missing: **147**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 294870 | IPARK현대산업개발 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 012630 | HDC | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 083790 | CG인바이츠 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 056090 | 시지메드텍 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 320000 | 한울반도체 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 001260 | 남광토건 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 001260 | 남광토건 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 001260 | 남광토건 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 001260 | 남광토건 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 001260 | 남광토건 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 001260 | 남광토건 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 006490 | 프리티 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 078930 | GS | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 023440 | 제이스코홀딩스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 310210 | 보로노이 | volatile | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
