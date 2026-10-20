# Market-Adjusted Score Integration Report - 2026-10-20

Generated at: 2026-10-20 01:45:22

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261020.csv`

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

- Total rows: **140**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **140**

## Market-Adjusted Result Counts

- market_data_missing: **139**
- pending: **1**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 059270 | 해성에어로보틱스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 302550 | 리메드 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 302550 | 리메드 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 207490 | 에이펙스인텍 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 032820 | 우리기술 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 032820 | 우리기술 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 032820 | 우리기술 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 032820 | 우리기술 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 377450 | 리파인 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 018500 | 동원모빌리티 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 465770 | STX그린로지스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 010960 | 삼호개발 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 000210 | DL | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 000210 | DL | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 000210 | DL | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 375500 | DL이앤씨 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 033310 | 엠투엔 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
