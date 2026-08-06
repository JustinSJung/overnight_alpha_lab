# Market-Adjusted Score Integration Report - 2026-08-06

Generated at: 2026-08-06 23:59:34

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260806.csv`

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
| 1970-01-01 | 042370 | 비츠로테크 | positive | pending | 0 | N/A |
| 1970-01-01 | 163730 | 핑거 | negative | pending | 0 | N/A |
| 1970-01-01 | 064800 | 포니링크 | negative | pending | 0 | N/A |
| 1970-01-01 | 457600 | 벡트 | volatile | pending | 0 | N/A |
| 1970-01-01 | 457600 | 벡트 | volatile | pending | 0 | N/A |
| 1970-01-01 | 488900 | 비츠로넥스텍 | positive | pending | 0 | N/A |
| 1970-01-01 | 009190 | 대양금속 | volatile | pending | 0 | N/A |
| 1970-01-01 | 009190 | 대양금속 | volatile | pending | 0 | N/A |
| 1970-01-01 | 009190 | 대양금속 | volatile | pending | 0 | N/A |
| 1970-01-01 | 009190 | 대양금속 | volatile | pending | 0 | N/A |
| 1970-01-01 | 079950 | 인베니아 | negative | pending | 0 | N/A |
| 1970-01-01 | 215570 | 크로넥스 | negative | pending | 0 | N/A |
| 1970-01-01 | 009190 | 대양금속 | volatile | pending | 0 | N/A |
| 1970-01-01 | 009190 | 대양금속 | volatile | pending | 0 | N/A |
| 1970-01-01 | 009190 | 대양금속 | volatile | pending | 0 | N/A |
| 1970-01-01 | 009190 | 대양금속 | volatile | pending | 0 | N/A |
| 1970-01-01 | 115450 | HLB테라퓨틱스 | negative | pending | 0 | N/A |
| 1970-01-01 | 376270 | HEM파마 | negative | pending | 0 | N/A |
| 1970-01-01 | 199800 | 툴젠 | negative | pending | 0 | N/A |
| 1970-01-01 | 043260 | 성호전자 | negative | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
