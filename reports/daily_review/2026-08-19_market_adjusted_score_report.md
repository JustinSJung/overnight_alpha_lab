# Market-Adjusted Score Integration Report - 2026-08-19

Generated at: 2026-08-19 22:48:38

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260819.csv`

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

- Total rows: **31**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **31**

## Market-Adjusted Result Counts

- pending: **31**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 322780 | 코퍼스코리아 | volatile | pending | 0 | N/A |
| 1970-01-01 | 352940 | 인바이오 | negative | pending | 0 | N/A |
| 1970-01-01 | 002020 | 코오롱 | positive | pending | 0 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | positive | pending | 0 | N/A |
| 1970-01-01 | 033530 | SJG세종 | volatile | pending | 0 | N/A |
| 1970-01-01 | 033530 | SJG세종 | volatile | pending | 0 | N/A |
| 1970-01-01 | 073190 | 듀오백 | volatile | pending | 0 | N/A |
| 1970-01-01 | 073190 | 듀오백 | volatile | pending | 0 | N/A |
| 1970-01-01 | 073190 | 듀오백 | volatile | pending | 0 | N/A |
| 1970-01-01 | 073190 | 듀오백 | volatile | pending | 0 | N/A |
| 1970-01-01 | 389680 | 유디엠텍 | negative | pending | 0 | N/A |
| 1970-01-01 | 290270 | 휴네시온 | negative | pending | 0 | N/A |
| 1970-01-01 | 148250 | 알엔투테크놀로지 | negative | pending | 0 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | pending | 0 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | pending | 0 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | pending | 0 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | pending | 0 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | volatile | pending | 0 | N/A |
| 1970-01-01 | 351320 | 넥사다이내믹스 | negative | pending | 0 | N/A |
| 1970-01-01 | 028260 | 삼성물산 | positive | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
