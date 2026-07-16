# Market-Adjusted Score Integration Report - 2026-07-16

Generated at: 2026-07-16 23:14:06

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260716.csv`

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

- Total rows: **18**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **18**

## Market-Adjusted Result Counts

- pending: **18**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 009320 | 아진전자부품 | volatile | pending | 0 | N/A |
| 1970-01-01 | 080010 | 이상네트웍스 | negative | pending | 0 | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | 0 | N/A |
| 1970-01-01 | 011000 | 진원생명과학 | volatile | pending | 0 | N/A |
| 1970-01-01 | 011000 | 진원생명과학 | volatile | pending | 0 | N/A |
| 1970-01-01 | 097230 | HJ중공업 | positive | pending | 0 | N/A |
| 1970-01-01 | 042940 | 상지건설 | negative | pending | 0 | N/A |
| 1970-01-01 | 066790 | 씨씨에스 | negative | pending | 0 | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | negative | pending | 0 | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | negative | pending | 0 | N/A |
| 1970-01-01 | 054940 | 엑사이엔씨 | volatile | pending | 0 | N/A |
| 1970-01-01 | 320000 | 한울반도체 | negative | pending | 0 | N/A |
| 1970-01-01 | 320000 | 한울반도체 | negative | pending | 0 | N/A |
| 1970-01-01 | 320000 | 한울반도체 | negative | pending | 0 | N/A |
| 1970-01-01 | 320000 | 한울반도체 | negative | pending | 0 | N/A |
| 1970-01-01 | 002810 | 삼영무역 | volatile | pending | 0 | N/A |
| 1970-01-01 | 002810 | 삼영무역 | volatile | pending | 0 | N/A |
| 1970-01-01 | 004890 | 동일산업 | volatile | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
