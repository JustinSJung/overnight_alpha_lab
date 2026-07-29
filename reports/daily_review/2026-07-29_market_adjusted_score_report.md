# Market-Adjusted Score Integration Report - 2026-07-29

Generated at: 2026-07-29 23:18:02

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260729.csv`

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

- Total rows: **20**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **20**

## Market-Adjusted Result Counts

- pending: **20**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 115530 | 씨엔플러스 | negative | pending | 0 | N/A |
| 1970-01-01 | 115530 | 씨엔플러스 | negative | pending | 0 | N/A |
| 1970-01-01 | 017810 | 풀무원 | negative | pending | 0 | N/A |
| 1970-01-01 | 017810 | 풀무원 | negative | pending | 0 | N/A |
| 1970-01-01 | 066790 | 씨씨에스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 043260 | 성호전자 | volatile | pending | 0 | N/A |
| 1970-01-01 | 043260 | 성호전자 | volatile | pending | 0 | N/A |
| 1970-01-01 | 043260 | 성호전자 | volatile | pending | 0 | N/A |
| 1970-01-01 | 043260 | 성호전자 | volatile | pending | 0 | N/A |
| 1970-01-01 | 047040 | 대우건설 | positive | pending | 0 | N/A |
| 1970-01-01 | 054220 | 비츠로시스 | positive | pending | 0 | N/A |
| 1970-01-01 | 001260 | 남광토건 | positive | pending | 0 | N/A |
| 1970-01-01 | 027040 | 서울전자통신 | negative | pending | 0 | N/A |
| 1970-01-01 | 010780 | 아이에스동서 | positive | pending | 0 | N/A |
| 1970-01-01 | 340360 | 다보링크 | negative | pending | 0 | N/A |
| 1970-01-01 | 340360 | 다보링크 | negative | pending | 0 | N/A |
| 1970-01-01 | 114190 | 강원에너지 | positive | pending | 0 | N/A |
| 1970-01-01 | 114190 | 강원에너지 | positive | pending | 0 | N/A |
| 1970-01-01 | 121440 | 골프존홀딩스 | negative | pending | 0 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | volatile | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
