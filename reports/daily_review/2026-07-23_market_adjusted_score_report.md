# Market-Adjusted Score Integration Report - 2026-07-23

Generated at: 2026-07-23 23:15:38

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260723.csv`

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

- Total rows: **39**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **39**

## Market-Adjusted Result Counts

- pending: **39**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 039200 | 오스코텍 | volatile | pending | 0 | N/A |
| 1970-01-01 | 039200 | 오스코텍 | volatile | pending | 0 | N/A |
| 1970-01-01 | 039200 | 오스코텍 | volatile | pending | 0 | N/A |
| 1970-01-01 | 039200 | 오스코텍 | volatile | pending | 0 | N/A |
| 1970-01-01 | 039200 | 오스코텍 | volatile | pending | 0 | N/A |
| 1970-01-01 | 039200 | 오스코텍 | volatile | pending | 0 | N/A |
| 1970-01-01 | 039200 | 오스코텍 | volatile | pending | 0 | N/A |
| 1970-01-01 | 039200 | 오스코텍 | volatile | pending | 0 | N/A |
| 1970-01-01 | 025560 | 미래산업 | positive | pending | 0 | N/A |
| 1970-01-01 | 028080 | 휴맥스홀딩스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 089140 | 넥스턴앤롤코리아 | volatile | pending | 0 | N/A |
| 1970-01-01 | 071950 | 코아스 | negative | pending | 0 | N/A |
| 1970-01-01 | 001260 | 남광토건 | volatile | pending | 0 | N/A |
| 1970-01-01 | 001420 | 태원물산 | negative | pending | 0 | N/A |
| 1970-01-01 | 005940 | NH투자증권 | volatile | pending | 0 | N/A |
| 1970-01-01 | 309930 | 조이웍스앤코 | negative | pending | 0 | N/A |
| 1970-01-01 | 309930 | 조이웍스앤코 | negative | pending | 0 | N/A |
| 1970-01-01 | 309930 | 조이웍스앤코 | negative | pending | 0 | N/A |
| 1970-01-01 | 309930 | 조이웍스앤코 | negative | pending | 0 | N/A |
| 1970-01-01 | 045390 | 대아티아이 | positive | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
