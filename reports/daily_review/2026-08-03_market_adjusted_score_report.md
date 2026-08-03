# Market-Adjusted Score Integration Report - 2026-08-03

Generated at: 2026-08-03 23:23:52

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260803.csv`

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

- Total rows: **25**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **25**

## Market-Adjusted Result Counts

- pending: **25**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 031860 | 디에이치엑스컴퍼니 | volatile | pending | 0 | N/A |
| 1970-01-01 | 031860 | 디에이치엑스컴퍼니 | volatile | pending | 0 | N/A |
| 1970-01-01 | 347700 | 스피어 | positive | pending | 0 | N/A |
| 1970-01-01 | 001260 | 남광토건 | volatile | pending | 0 | N/A |
| 1970-01-01 | 255220 | SG | positive | pending | 0 | N/A |
| 1970-01-01 | 148250 | 알엔투테크놀로지 | negative | pending | 0 | N/A |
| 1970-01-01 | 148250 | 알엔투테크놀로지 | negative | pending | 0 | N/A |
| 1970-01-01 | 178320 | 서진시스템 | volatile | pending | 0 | N/A |
| 1970-01-01 | 020150 | 롯데에너지머티리얼즈 | volatile | pending | 0 | N/A |
| 1970-01-01 | 028100 | 동아지질 | positive | pending | 0 | N/A |
| 1970-01-01 | 033310 | 엠투엔 | volatile | pending | 0 | N/A |
| 1970-01-01 | 027580 | 상보 | volatile | pending | 0 | N/A |
| 1970-01-01 | 047920 | HLB제약 | negative | pending | 0 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | 0 | N/A |
| 1970-01-01 | 060230 | 제이케이시냅스 | negative | pending | 0 | N/A |
| 1970-01-01 | 473980 | 노머스 | negative | pending | 0 | N/A |
| 1970-01-01 | 473980 | 노머스 | negative | pending | 0 | N/A |
| 1970-01-01 | 012630 | HDC | volatile | pending | 0 | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | volatile | pending | 0 | N/A |
| 1970-01-01 | 187660 | 페니트리움바이오 | negative | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
