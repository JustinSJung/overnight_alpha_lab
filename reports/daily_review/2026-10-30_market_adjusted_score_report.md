# Market-Adjusted Score Integration Report - 2026-10-30

Generated at: 2026-10-30 02:28:15

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261030.csv`

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

- Total rows: **313**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **313**

## Market-Adjusted Result Counts

- market_data_missing: **313**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 001470 | 삼부토건 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 072770 | 멤레이비티 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 072770 | 멤레이비티 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 072770 | 멤레이비티 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 088280 | 쏘닉스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 011000 | 진원생명과학 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 011000 | 진원생명과학 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 260870 | SK시그넷 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 260870 | SK시그넷 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 260870 | SK시그넷 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 445680 | 큐리옥스바이오시스템즈 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 246960 | SCL사이언스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 090410 | 덕신이피씨 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 129260 | 인터지스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 129260 | 인터지스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 217320 | 썬테크 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 217320 | 썬테크 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 217320 | 썬테크 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 217320 | 썬테크 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 217320 | 썬테크 | negative | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
