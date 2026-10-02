# Market-Adjusted Score Integration Report - 2026-10-02

Generated at: 2026-10-02 03:11:16

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261002.csv`

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

- Total rows: **168**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **168**

## Market-Adjusted Result Counts

- market_data_missing: **168**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 007610 | 선도전기 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 028260 | 삼성물산 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 0126Z0 | 삼성에피스홀딩스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 393970 | 대진첨단소재 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 066590 | 스모트로닉 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 207490 | 에이펙스인텍 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 181710 | NHN | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 010950 | S-Oil | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 010950 | S-Oil | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 010950 | S-Oil | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 010950 | S-Oil | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 115160 | 휴맥스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 115160 | 휴맥스 | volatile | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
