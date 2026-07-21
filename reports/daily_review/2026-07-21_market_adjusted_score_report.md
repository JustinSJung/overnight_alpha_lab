# Market-Adjusted Score Integration Report - 2026-07-21

Generated at: 2026-07-21 23:15:36

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260721.csv`

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

- Total rows: **27**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **27**

## Market-Adjusted Result Counts

- pending: **27**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 066790 | 씨씨에스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 348950 | 제이알글로벌리츠 | volatile | pending | 0 | N/A |
| 1970-01-01 | 397030 | 에이프릴바이오 | volatile | pending | 0 | N/A |
| 1970-01-01 | 006220 | 제주은행 | negative | pending | 0 | N/A |
| 1970-01-01 | 066430 | 아이로보틱스 | negative | pending | 0 | N/A |
| 1970-01-01 | 106240 | 파인테크닉스 | negative | pending | 0 | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | negative | pending | 0 | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | negative | pending | 0 | N/A |
| 1970-01-01 | 053580 | 웹케시 | positive | pending | 0 | N/A |
| 1970-01-01 | 071950 | 코아스 | negative | pending | 0 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | pending | 0 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | pending | 0 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | pending | 0 | N/A |
| 1970-01-01 | 159910 | 에코글로우 | negative | pending | 0 | N/A |
| 1970-01-01 | 119850 | 지엔씨에너지 | positive | pending | 0 | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | 0 | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | 0 | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | negative | pending | 0 | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | negative | pending | 0 | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | negative | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
