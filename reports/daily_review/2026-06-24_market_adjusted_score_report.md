# Market-Adjusted Score Integration Report - 2026-06-24

Generated at: 2026-06-24 22:23:50

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260624.csv`

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

- Total rows: **11**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **11**

## Market-Adjusted Result Counts

- pending: **11**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 043260 | 성호전자 | volatile | pending | 0 | N/A |
| 1970-01-01 | 083790 | CG인바이츠 | negative | pending | 0 | N/A |
| 1970-01-01 | 061040 | 알에프텍 | volatile | pending | 0 | N/A |
| 1970-01-01 | 396470 | 워트 | positive | pending | 0 | N/A |
| 1970-01-01 | 452260 | 한화갤러리아 | volatile | pending | 0 | N/A |
| 1970-01-01 | 036620 | 감성코퍼레이션 | volatile | pending | 0 | N/A |
| 1970-01-01 | 307870 | 비투엔 | volatile | pending | 0 | N/A |
| 1970-01-01 | 097780 | 에코볼트 | volatile | pending | 0 | N/A |
| 1970-01-01 | 052710 | 아모텍 | negative | pending | 0 | N/A |
| 1970-01-01 | 123690 | 한국화장품 | volatile | pending | 0 | N/A |
| 1970-01-01 | 003350 | 한국화장품제조 | volatile | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
