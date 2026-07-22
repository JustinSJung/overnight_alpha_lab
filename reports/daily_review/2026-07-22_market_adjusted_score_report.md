# Market-Adjusted Score Integration Report - 2026-07-22

Generated at: 2026-07-22 10:29:31

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260722.csv`

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

- Total rows: **35**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **35**

## Market-Adjusted Result Counts

- pending: **35**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 005960 | 동부건설 | volatile | pending | 0 | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | 0 | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | 0 | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | 0 | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | 0 | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | 0 | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | 0 | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | 0 | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | 0 | N/A |
| 1970-01-01 | 002990 | 금호건설 | volatile | pending | 0 | N/A |
| 1970-01-01 | 114450 | 그린생명과학 | volatile | pending | 0 | N/A |
| 1970-01-01 | 0009K0 | 에임드바이오 | volatile | pending | 0 | N/A |
| 1970-01-01 | 009420 | 한올바이오파마 | volatile | pending | 0 | N/A |
| 1970-01-01 | 203650 | 드림시큐리티 | negative | pending | 0 | N/A |
| 1970-01-01 | 475040 | 스트라드비젼 | positive | pending | 0 | N/A |
| 1970-01-01 | 475040 | 스트라드비젼 | positive | pending | 0 | N/A |
| 1970-01-01 | 475040 | 스트라드비젼 | positive | pending | 0 | N/A |
| 1970-01-01 | 475040 | 스트라드비젼 | positive | pending | 0 | N/A |
| 1970-01-01 | 475040 | 스트라드비젼 | positive | pending | 0 | N/A |
| 1970-01-01 | 475040 | 스트라드비젼 | positive | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
