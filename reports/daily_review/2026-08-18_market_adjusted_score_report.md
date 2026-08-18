# Market-Adjusted Score Integration Report - 2026-08-18

Generated at: 2026-08-18 22:47:57

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260818.csv`

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

- Total rows: **34**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **34**

## Market-Adjusted Result Counts

- pending: **34**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 033540 | 파라텍 | negative | pending | 0 | N/A |
| 1970-01-01 | 0009K0 | 에임드바이오 | volatile | pending | 0 | N/A |
| 1970-01-01 | 418620 | E8 | negative | pending | 0 | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | 0 | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | 0 | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | 0 | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | 0 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | pending | 0 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | pending | 0 | N/A |
| 1970-01-01 | 010960 | 삼호개발 | positive | pending | 0 | N/A |
| 1970-01-01 | 062970 | 한국첨단소재 | negative | pending | 0 | N/A |
| 1970-01-01 | 062970 | 한국첨단소재 | negative | pending | 0 | N/A |
| 1970-01-01 | 033310 | 엠투엔 | volatile | pending | 0 | N/A |
| 1970-01-01 | 001740 | SK네트웍스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 001740 | SK네트웍스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 038880 | 아이에이 | negative | pending | 0 | N/A |
| 1970-01-01 | 038880 | 아이에이 | negative | pending | 0 | N/A |
| 1970-01-01 | 038880 | 아이에이 | negative | pending | 0 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | negative | pending | 0 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
