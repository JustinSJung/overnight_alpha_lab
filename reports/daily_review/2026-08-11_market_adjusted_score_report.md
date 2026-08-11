# Market-Adjusted Score Integration Report - 2026-08-11

Generated at: 2026-08-11 23:08:31

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260811.csv`

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

- Total rows: **45**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **45**

## Market-Adjusted Result Counts

- pending: **45**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 006060 | 화승인더스트리 | volatile | pending | 0 | N/A |
| 1970-01-01 | 348370 | 엔켐 | volatile | pending | 0 | N/A |
| 1970-01-01 | 006370 | 대구백화점 | volatile | pending | 0 | N/A |
| 1970-01-01 | 006370 | 대구백화점 | volatile | pending | 0 | N/A |
| 1970-01-01 | 263750 | 펄어비스 | neutral_positive | pending | 0 | N/A |
| 1970-01-01 | 263750 | 펄어비스 | neutral_positive | pending | 0 | N/A |
| 1970-01-01 | 068240 | 다원시스 | positive | pending | 0 | N/A |
| 1970-01-01 | 065420 | 에스아이리소스 | negative | pending | 0 | N/A |
| 1970-01-01 | 378800 | 샤페론 | negative | pending | 0 | N/A |
| 1970-01-01 | 089860 | 롯데렌탈 | volatile | pending | 0 | N/A |
| 1970-01-01 | 089860 | 롯데렌탈 | volatile | pending | 0 | N/A |
| 1970-01-01 | 187660 | 페니트리움바이오 | negative | pending | 0 | N/A |
| 1970-01-01 | 033270 | 유나이티드 | volatile | pending | 0 | N/A |
| 1970-01-01 | 060230 | 제이케이시냅스 | negative | pending | 0 | N/A |
| 1970-01-01 | 060230 | 제이케이시냅스 | negative | pending | 0 | N/A |
| 1970-01-01 | 272110 | 케이엔제이 | volatile | pending | 0 | N/A |
| 1970-01-01 | 272110 | 케이엔제이 | volatile | pending | 0 | N/A |
| 1970-01-01 | 128940 | 한미약품 | volatile | pending | 0 | N/A |
| 1970-01-01 | 128940 | 한미약품 | volatile | pending | 0 | N/A |
| 1970-01-01 | 128940 | 한미약품 | volatile | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
