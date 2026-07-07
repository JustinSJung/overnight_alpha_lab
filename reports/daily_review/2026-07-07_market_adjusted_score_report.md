# Market-Adjusted Score Integration Report - 2026-07-07

Generated at: 2026-07-07 23:19:46

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

- Total rows: **36**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **36**

## Market-Adjusted Result Counts

- pending: **36**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 288980 | 모아데이타 | volatile | pending | 0 | N/A |
| 1970-01-01 | 216080 | 제테마 | negative | pending | 0 | N/A |
| 1970-01-01 | 380540 | 옵티코어 | positive | pending | 0 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 263800 | 데이타솔루션 | positive | pending | 0 | N/A |
| 1970-01-01 | 263800 | 데이타솔루션 | positive | pending | 0 | N/A |
| 1970-01-01 | 263800 | 데이타솔루션 | positive | pending | 0 | N/A |
| 1970-01-01 | 263800 | 데이타솔루션 | positive | pending | 0 | N/A |
| 1970-01-01 | 263800 | 데이타솔루션 | positive | pending | 0 | N/A |
| 1970-01-01 | 263800 | 데이타솔루션 | positive | pending | 0 | N/A |
| 1970-01-01 | 263800 | 데이타솔루션 | positive | pending | 0 | N/A |
| 1970-01-01 | 263800 | 데이타솔루션 | positive | pending | 0 | N/A |
| 1970-01-01 | 024720 | 콜마홀딩스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 024720 | 콜마홀딩스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 189330 | 씨이랩 | positive | pending | 0 | N/A |
| 1970-01-01 | 189330 | 씨이랩 | positive | pending | 0 | N/A |
| 1970-01-01 | 189330 | 씨이랩 | positive | pending | 0 | N/A |
| 1970-01-01 | 189330 | 씨이랩 | positive | pending | 0 | N/A |
| 1970-01-01 | 189330 | 씨이랩 | positive | pending | 0 | N/A |
| 1970-01-01 | 189330 | 씨이랩 | positive | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
