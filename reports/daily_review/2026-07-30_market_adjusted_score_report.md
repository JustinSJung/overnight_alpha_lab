# Market-Adjusted Score Integration Report - 2026-07-30

Generated at: 2026-07-30 02:43:24

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260730.csv`

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

- Total rows: **14**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **14**

## Market-Adjusted Result Counts

- pending: **14**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 107640 | 한중엔시에스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 007570 | 일양약품 | volatile | pending | 0 | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | positive | pending | 0 | N/A |
| 1970-01-01 | 080420 | 모다이노칩 | volatile | pending | 0 | N/A |
| 1970-01-01 | 080420 | 모다이노칩 | volatile | pending | 0 | N/A |
| 1970-01-01 | 080420 | 모다이노칩 | volatile | pending | 0 | N/A |
| 1970-01-01 | 420770 | 기가비스 | positive | pending | 0 | N/A |
| 1970-01-01 | 025560 | 미래산업 | positive | pending | 0 | N/A |
| 1970-01-01 | 460940 | 피앤에스로보틱스 | positive | pending | 0 | N/A |
| 1970-01-01 | 011330 | 유니켐 | negative | pending | 0 | N/A |
| 1970-01-01 | 402490 | 그린리소스 | negative | pending | 0 | N/A |
| 1970-01-01 | 402490 | 그린리소스 | negative | pending | 0 | N/A |
| 1970-01-01 | 104460 | 디와이피엔에프 | positive | pending | 0 | N/A |
| 1970-01-01 | 119850 | 지엔씨에너지 | positive | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
