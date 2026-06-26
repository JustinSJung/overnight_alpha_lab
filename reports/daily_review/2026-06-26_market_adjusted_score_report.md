# Market-Adjusted Score Integration Report - 2026-06-26

Generated at: 2026-06-26 16:39:46

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260626.csv`

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

- Total rows: **21**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **21**

## Market-Adjusted Result Counts

- pending: **21**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 361610 | SK아이이테크놀로지 | negative | pending | 0 | N/A |
| 1970-01-01 | 187660 | 페니트리움바이오 | negative | pending | 0 | N/A |
| 1970-01-01 | 476830 | 알지노믹스 | positive | pending | 0 | N/A |
| 1970-01-01 | 005960 | 동부건설 | positive | pending | 0 | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | negative | pending | 0 | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | negative | pending | 0 | N/A |
| 1970-01-01 | 006740 | 블루산업개발 | negative | pending | 0 | N/A |
| 1970-01-01 | 138360 | 앤로보틱스 | negative | pending | 0 | N/A |
| 1970-01-01 | 214150 | 클래시스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 214150 | 클래시스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 214150 | 클래시스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 258610 | 케일럼 | positive | pending | 0 | N/A |
| 1970-01-01 | 277880 | 티에스아이 | positive | pending | 0 | N/A |
| nan | 003450 | 케이비증권 | negative | pending | 0 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | volatile | pending | 0 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | positive | pending | 0 | N/A |
| 1970-01-01 | 282720 | 금양그린파워 | positive | pending | 0 | N/A |
| 1970-01-01 | 105560 | KB금융 | negative | pending | 0 | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | negative | pending | 0 | N/A |
| 1970-01-01 | 194370 | 제이에스코퍼레이션 | negative | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
