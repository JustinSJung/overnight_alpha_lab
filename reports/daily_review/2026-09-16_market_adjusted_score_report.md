# Market-Adjusted Score Integration Report - 2026-09-16

Generated at: 2026-09-16 01:19:31

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260916.csv`

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

- Total rows: **367**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **367**

## Market-Adjusted Result Counts

- market_data_missing: **367**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 228670 | 레이 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 286750 | 나노실리칸첨단소재 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 286750 | 나노실리칸첨단소재 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 286750 | 나노실리칸첨단소재 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 286750 | 나노실리칸첨단소재 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 012630 | HDC | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 121440 | 골프존홀딩스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | positive | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
