# Market-Adjusted Score Integration Report - 2026-11-20

Generated at: 2026-11-20 04:02:13

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261120.csv`

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

- Total rows: **144**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **144**

## Market-Adjusted Result Counts

- market_data_missing: **144**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 028300 | HLB | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 424870 | 이뮨온시아 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 900270 | 헝셩그룹 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 290690 | 아리바이오홀딩스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 078350 | 한양디지텍 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 078350 | 한양디지텍 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 078350 | 한양디지텍 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 431190 | 케이쓰리아이 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 028260 | 삼성물산 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 028260 | 삼성물산 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 053210 | 케이티스카이라이프 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 053210 | 케이티스카이라이프 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 053210 | 케이티스카이라이프 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 053210 | 케이티스카이라이프 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 053210 | 케이티스카이라이프 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 053210 | 케이티스카이라이프 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 067630 | HLB생명과학 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 067630 | HLB생명과학 | volatile | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
