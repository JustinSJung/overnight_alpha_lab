# Market-Adjusted Score Integration Report - 2026-07-28

Generated at: 2026-07-28 23:19:19

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260728.csv`

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

- Total rows: **29**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **29**

## Market-Adjusted Result Counts

- pending: **29**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 217730 | 강스템바이오텍 | volatile | pending | 0 | N/A |
| 1970-01-01 | 217730 | 강스템바이오텍 | volatile | pending | 0 | N/A |
| 1970-01-01 | 083640 | 인콘 | volatile | pending | 0 | N/A |
| 1970-01-01 | 060900 | 에이전트AI | negative | pending | 0 | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | 0 | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | 0 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | pending | 0 | N/A |
| 1970-01-01 | 064350 | 현대로템 | volatile | pending | 0 | N/A |
| 1970-01-01 | 066410 | 버킷스튜디오 | volatile | pending | 0 | N/A |
| 1970-01-01 | 032800 | 판타지오 | negative | pending | 0 | N/A |
| 1970-01-01 | 210980 | SK디앤디 | negative | pending | 0 | N/A |
| 1970-01-01 | 210980 | SK디앤디 | negative | pending | 0 | N/A |
| 1970-01-01 | 210980 | SK디앤디 | negative | pending | 0 | N/A |
| 1970-01-01 | 210980 | SK디앤디 | negative | pending | 0 | N/A |
| 1970-01-01 | 082270 | 젬백스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 069460 | 대호에이엘 | negative | pending | 0 | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | volatile | pending | 0 | N/A |
| 1970-01-01 | 047040 | 대우건설 | volatile | pending | 0 | N/A |
| 1970-01-01 | 071200 | 인피니트헬스케어 | negative | pending | 0 | N/A |
| 1970-01-01 | 028260 | 삼성물산 | positive | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
