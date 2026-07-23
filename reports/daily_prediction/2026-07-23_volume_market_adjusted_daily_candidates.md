# Volume + Market-Adjusted Daily Candidate Report - 2026-07-23

Generated at: 2026-07-23 03:21:06

ML dataset source: `data/processed/ml_dataset_20260723.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260723.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20260723.csv`

## Purpose

This report applies both market-adjusted score adjustments and trading volume score adjustments to daily candidate scoring.

It is a v3 candidate report for comparison and does not replace the main recommender yet.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Score Formula

```text
base_recommendation_score_v3
+ market_adjusted_score_adjustment
+ trading_volume_score_adjustment
= final_volume_market_adjusted_score
```

## Summary

- Total rows: **82**
- strong_volume_market_adjusted_candidate: **69**
- risk_or_avoid_review: **11**
- positive_candidate: **1**
- watchlist_candidate: **1**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 348340 | 뉴로메카 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 348340 | 뉴로메카 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 348340 | 뉴로메카 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 348340 | 뉴로메카 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 176750 | 듀켐바이오 | merger | volatile | pending | pending | insufficient_volume_baseline | 76.00 | 0.00 | 0.00 | 76.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 340570 | 티앤엘 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 191410 | 육일씨엔에쓰 | merger | volatile | pending | pending | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 006490 | 프리티 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |

## Volatile Watchlist

No candidates in this section.

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 397030 | 에이프릴바이오 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 397030 | 에이프릴바이오 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 397030 | 에이프릴바이오 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 397030 | 에이프릴바이오 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 397030 | 에이프릴바이오 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 397030 | 에이프릴바이오 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 348340 | 뉴로메카 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 348340 | 뉴로메카 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 348340 | 뉴로메카 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 348340 | 뉴로메카 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -45.00 | 0.00 | 0.00 | -45.00 | N/A | N/A | N/A |
| 1970-01-01 | 183490 | 엔지켐생명과학 | lawsuit | negative | pending | pending | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
