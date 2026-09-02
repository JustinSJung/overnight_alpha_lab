# Market-Adjusted Score Integration Report - 2026-09-02

Generated at: 2026-09-02 00:49:25

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260902.csv`

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

- Total rows: **361**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **361**

## Market-Adjusted Result Counts

- market_data_missing: **360**
- pending: **1**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 064290 | 인텍플러스 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 066430 | 아이로보틱스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 368770 | 파이버프로 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 045660 | 에이텍 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 034020 | 두산에너빌리티 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 034020 | 두산에너빌리티 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 034020 | 두산에너빌리티 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 034020 | 두산에너빌리티 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 090080 | 평화산업 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 090080 | 평화산업 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 090080 | 평화산업 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 021320 | KCC건설 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 002990 | 금호건설 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 092790 | 넥스틸 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 003920 | 남양유업 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 003920 | 남양유업 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 003920 | 남양유업 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 003920 | 남양유업 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 027410 | BGF | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 026960 | 동서 | volatile | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
