# Market-Adjusted Score Integration Report - 2026-10-27

Generated at: 2026-10-27 02:02:54

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261027.csv`

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

- Total rows: **234**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **234**

## Market-Adjusted Result Counts

- market_data_missing: **234**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 186230 | 그린플러스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 186230 | 그린플러스 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 217730 | 강스템바이오텍 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 090150 | 아이윈 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 090150 | 아이윈 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 060900 | 에이전트AI | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 095700 | 제넥신 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 095700 | 제넥신 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 095700 | 제넥신 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 095700 | 제넥신 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 095700 | 제넥신 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 095700 | 제넥신 | negative | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
