# Market-Adjusted Score Integration Report - 2026-07-06

Generated at: 2026-07-06 23:35:33

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260706.csv`

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

- Total rows: **31**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **31**

## Market-Adjusted Result Counts

- pending: **31**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 003490 | 대한항공 | volatile | pending | 0 | N/A |
| 1970-01-01 | 020560 | 아시아나항공 | volatile | pending | 0 | N/A |
| 1970-01-01 | 088790 | 진도 | negative | pending | 0 | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | 0 | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | 0 | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | 0 | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | 0 | N/A |
| 1970-01-01 | 023440 | 제이스코홀딩스 | negative | pending | 0 | N/A |
| 1970-01-01 | 322780 | 코퍼스코리아 | negative | pending | 0 | N/A |
| 1970-01-01 | 004990 | 롯데지주 | negative | pending | 0 | N/A |
| 1970-01-01 | 049950 | 미래컴퍼니 | positive | pending | 0 | N/A |
| 1970-01-01 | 321370 | 센서뷰 | negative | pending | 0 | N/A |
| 1970-01-01 | 236810 | 엔비티 | neutral_positive | pending | 0 | N/A |
| 1970-01-01 | 236810 | 엔비티 | neutral_positive | pending | 0 | N/A |
| 1970-01-01 | 025980 | 아난티 | negative | pending | 0 | N/A |
| 1970-01-01 | 018260 | 삼성에스디에스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | 0 | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | 0 | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | 0 | N/A |
| 1970-01-01 | 001470 | 삼부토건 | volatile | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
