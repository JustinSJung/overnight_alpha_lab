# Market-Adjusted Score Integration Report - 2026-10-26

Generated at: 2026-10-26 00:56:11

Source evaluation file: `data/predictions/market_adjusted_evaluation_20261026.csv`

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

- Total rows: **139**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **139**

## Market-Adjusted Result Counts

- market_data_missing: **139**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 322780 | 코퍼스코리아 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 010130 | 고려아연 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 010130 | 고려아연 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 005320 | 온타이드 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 005320 | 온타이드 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 005320 | 온타이드 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 282720 | 금양그린파워 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 282720 | 금양그린파워 | positive | market_data_missing | 0 | N/A |
| 1970-01-01 | 040350 | 크레오에스지 | volatile | market_data_missing | 0 | N/A |
| 1970-01-01 | 030200 | 케이티 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 030200 | 케이티 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 018500 | 동원모빌리티 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | market_data_missing | 0 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | market_data_missing | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
