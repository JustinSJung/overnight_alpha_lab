# Market-Adjusted Score Integration Report - 2026-06-26

Generated at: 2026-06-26 08:30:34

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260626.csv`

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

- Total rows: **28**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **28**

## Market-Adjusted Result Counts

- pending: **28**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 007460 | 에이프로젠 | volatile | pending | 0 | N/A |
| 1970-01-01 | 085660 | 차바이오텍 | negative | pending | 0 | N/A |
| 1970-01-01 | 085660 | 차바이오텍 | negative | pending | 0 | N/A |
| 1970-01-01 | 085660 | 차바이오텍 | negative | pending | 0 | N/A |
| 1970-01-01 | 211270 | AP위성 | negative | pending | 0 | N/A |
| 1970-01-01 | 012510 | 더존비즈온 | volatile | pending | 0 | N/A |
| 1970-01-01 | 243070 | 휴온스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 243070 | 휴온스 | volatile | pending | 0 | N/A |
| 1970-01-01 | 054930 | 유신 | positive | pending | 0 | N/A |
| 1970-01-01 | 299660 | 셀리드 | volatile | pending | 0 | N/A |
| 1970-01-01 | 013700 | 까뮤이앤씨 | positive | pending | 0 | N/A |
| 1970-01-01 | 009730 | 이렘 | negative | pending | 0 | N/A |
| 1970-01-01 | 445090 | 에이직랜드 | positive | pending | 0 | N/A |
| 1970-01-01 | 043260 | 성호전자 | negative | pending | 0 | N/A |
| 1970-01-01 | 013580 | 계룡건설산업 | positive | pending | 0 | N/A |
| 1970-01-01 | 013580 | 계룡건설산업 | positive | pending | 0 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | pending | 0 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | pending | 0 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | pending | 0 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
