# Market-Adjusted Score Integration Report - 2026-07-07

Generated at: 2026-07-07 06:47:39

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260707.csv`

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

- Total rows: **28**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **28**

## Market-Adjusted Result Counts

- pending: **28**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 288980 | 모아데이타 | negative | pending | 0 | N/A |
| 1970-01-01 | 019570 | 플루토스 | negative | pending | 0 | N/A |
| 1970-01-01 | 013520 | 화승코퍼레이션 | volatile | pending | 0 | N/A |
| 1970-01-01 | 013720 | 청보 | volatile | pending | 0 | N/A |
| 1970-01-01 | 253450 | 스튜디오드래곤 | volatile | pending | 0 | N/A |
| 1970-01-01 | 010140 | 삼성중공업 | volatile | pending | 0 | N/A |
| 1970-01-01 | 010140 | 삼성중공업 | volatile | pending | 0 | N/A |
| 1970-01-01 | 010140 | 삼성중공업 | volatile | pending | 0 | N/A |
| 1970-01-01 | 010140 | 삼성중공업 | volatile | pending | 0 | N/A |
| 1970-01-01 | 101970 | 우양에이치씨 | positive | pending | 0 | N/A |
| 1970-01-01 | 068240 | 다원시스 | positive | pending | 0 | N/A |
| 1970-01-01 | 000720 | 현대건설 | negative | pending | 0 | N/A |
| 1970-01-01 | 047040 | 대우건설 | positive | pending | 0 | N/A |
| 1970-01-01 | 368970 | 오에스피 | negative | pending | 0 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | volatile | pending | 0 | N/A |
| 1970-01-01 | 187870 | 디바이스 | positive | pending | 0 | N/A |
| 1970-01-01 | 007980 | TP | volatile | pending | 0 | N/A |
| 1970-01-01 | 007980 | TP | volatile | pending | 0 | N/A |
| 1970-01-01 | 007980 | TP | volatile | pending | 0 | N/A |
| 1970-01-01 | 007980 | TP | volatile | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
