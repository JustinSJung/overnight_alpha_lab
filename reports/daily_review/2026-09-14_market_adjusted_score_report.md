# Market-Adjusted Score Integration Report - 2026-09-14

Generated at: 2026-09-14 00:59:51

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260914.csv`

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

- Total rows: **179**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **179**

## Market-Adjusted Result Counts

- market_data_missing: **179**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 002990 | 금호건설 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 256940 | 킵스파마 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 203400 | 에이비온 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 119830 | 아이텍 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 119830 | 아이텍 | negative | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
