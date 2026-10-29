# Market-Adjusted Score Integration Report - 2026-10-29

Generated at: 2026-10-29 02:25:44

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261029.csv`

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

- Total rows: **385**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **385**

## Market-Adjusted Result Counts

- market_data_missing: **384**
- pending: **1**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 196170 | 알테오젠 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 009190 | 대양금속 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 009190 | 대양금속 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 002020 | 코오롱 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 299660 | 셀리드 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 299660 | 셀리드 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 299660 | 셀리드 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 299660 | 셀리드 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 065650 | 하이퍼코퍼레이션 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 424870 | 이뮨온시아 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 005300 | 롯데칠성음료 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 361610 | SK아이이테크놀로지 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 361610 | SK아이이테크놀로지 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 065060 | 지엔코 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 065060 | 지엔코 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 065060 | 지엔코 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 065060 | 지엔코 | negative | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
