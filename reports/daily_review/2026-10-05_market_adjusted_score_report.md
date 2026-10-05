# Market-Adjusted Score Integration Report - 2026-10-05

Generated at: 2026-10-05 01:19:24

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261005.csv`

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

- Total rows: **120**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **120**

## Market-Adjusted Result Counts

- pending: **120**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 235980 | 메드팩토 | volatile | pending | 0 | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | pending | 0 | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | pending | 0 | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | pending | 0 | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | pending | 0 | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | pending | 0 | N/A |
| 1970-01-01 | 003060 | 에이프로젠바이오로직스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 003060 | 에이프로젠바이오로직스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 003060 | 에이프로젠바이오로직스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 001040 | CJ | volatile | pending | 0 | N/A |
| 1970-01-01 | 001040 | CJ | volatile | pending | 0 | N/A |
| 1970-01-01 | 097950 | CJ제일제당 | volatile | pending | 0 | N/A |
| 1970-01-01 | 005930 | 삼성전자 | volatile | pending | 0 | N/A |
| 1970-01-01 | 205100 | 엑셈 | volatile | pending | 0 | N/A |
| 1970-01-01 | 469480 | IBKS제24호스팩 | volatile | pending | 0 | N/A |
| 1970-01-01 | 469480 | IBKS제24호스팩 | volatile | pending | 0 | N/A |
| 1970-01-01 | 469480 | IBKS제24호스팩 | volatile | pending | 0 | N/A |
| 1970-01-01 | 066790 | 씨씨에스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 027040 | 서울전자통신 | negative | pending | 0 | N/A |
| 1970-01-01 | 027040 | 서울전자통신 | negative | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
