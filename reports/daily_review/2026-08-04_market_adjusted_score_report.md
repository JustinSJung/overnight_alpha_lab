# Market-Adjusted Score Integration Report - 2026-08-04

Generated at: 2026-08-04 16:21:25

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260804.csv`

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

- Total rows: **55**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **55**

## Market-Adjusted Result Counts

- pending: **55**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 011000 | 진원생명과학 | negative | pending | 0 | N/A |
| 1970-01-01 | 011000 | 진원생명과학 | negative | pending | 0 | N/A |
| 1970-01-01 | 011000 | 진원생명과학 | negative | pending | 0 | N/A |
| 1970-01-01 | 011000 | 진원생명과학 | negative | pending | 0 | N/A |
| 1970-01-01 | 031860 | 디에이치엑스컴퍼니 | negative | pending | 0 | N/A |
| 1970-01-01 | 092040 | 아미코젠 | negative | pending | 0 | N/A |
| 1970-01-01 | 092040 | 아미코젠 | negative | pending | 0 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | 0 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | 0 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | 0 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | 0 | N/A |
| 1970-01-01 | 229640 | LS에코에너지 | negative | pending | 0 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | negative | pending | 0 | N/A |
| 1970-01-01 | 109740 | 디에스케이 | volatile | pending | 0 | N/A |
| 1970-01-01 | 109740 | 디에스케이 | volatile | pending | 0 | N/A |
| 1970-01-01 | 002990 | 금호건설 | positive | pending | 0 | N/A |
| 1970-01-01 | 166090 | 하나머티리얼즈 | volatile | pending | 0 | N/A |
| 1970-01-01 | 166090 | 하나머티리얼즈 | volatile | pending | 0 | N/A |
| 1970-01-01 | 208640 | 썸에이지 | negative | pending | 0 | N/A |
| 1970-01-01 | 208640 | 썸에이지 | negative | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
