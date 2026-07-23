# Market-Adjusted Score Integration Report - 2026-07-23

Generated at: 2026-07-23 03:21:04

Source evaluation file: `data/predictions/market_adjusted_evaluation_20260723.csv`

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

- Total rows: **23**
- Total adjustment score: **0.00**
- Average adjustment score: **0.00**

## Adjustment Label Counts

- neutral_adjustment: **23**

## Market-Adjusted Result Counts

- pending: **23**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | market_adjusted_result | market_adjusted_score_adjustment | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|
| 1970-01-01 | 006490 | 프리티 | volatile | pending | 0 | N/A |
| 1970-01-01 | 348340 | 뉴로메카 | positive | pending | 0 | N/A |
| 1970-01-01 | 348340 | 뉴로메카 | positive | pending | 0 | N/A |
| 1970-01-01 | 348340 | 뉴로메카 | positive | pending | 0 | N/A |
| 1970-01-01 | 348340 | 뉴로메카 | positive | pending | 0 | N/A |
| 1970-01-01 | 191410 | 육일씨엔에쓰 | volatile | pending | 0 | N/A |
| 1970-01-01 | 397030 | 에이프릴바이오 | negative | pending | 0 | N/A |
| 1970-01-01 | 397030 | 에이프릴바이오 | negative | pending | 0 | N/A |
| 1970-01-01 | 397030 | 에이프릴바이오 | negative | pending | 0 | N/A |
| 1970-01-01 | 340570 | 티앤엘 | positive | pending | 0 | N/A |
| 1970-01-01 | 340570 | 티앤엘 | positive | pending | 0 | N/A |
| 1970-01-01 | 340570 | 티앤엘 | positive | pending | 0 | N/A |
| 1970-01-01 | 340570 | 티앤엘 | positive | pending | 0 | N/A |
| 1970-01-01 | 340570 | 티앤엘 | positive | pending | 0 | N/A |
| 1970-01-01 | 340570 | 티앤엘 | positive | pending | 0 | N/A |
| 1970-01-01 | 340570 | 티앤엘 | positive | pending | 0 | N/A |
| 1970-01-01 | 340570 | 티앤엘 | positive | pending | 0 | N/A |
| 1970-01-01 | 176750 | 듀켐바이오 | volatile | pending | 0 | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | negative | pending | 0 | N/A |
| 1970-01-01 | 348340 | 뉴로메카 | negative | pending | 0 | N/A |

## Next Step

The next step is to connect this adjustment score directly into the daily stock recommender's final adjusted score.
