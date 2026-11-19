# Market-Adjusted Score Integration Report - 2026-11-19

Generated at: 2026-11-19 04:22:38

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261119.csv`

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

- Total rows: **121**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **121**

## Market-Adjusted Result Counts

- market_data_missing: **121**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 372320 | 큐로셀 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 032800 | 판타지오 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 457600 | 벡트로보틱스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 900100 | 파이온엑스 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 320000 | 한울반도체 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 258790 | 소프트캠프 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 258790 | 소프트캠프 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 089150 | 케이씨티 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | volatile | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
