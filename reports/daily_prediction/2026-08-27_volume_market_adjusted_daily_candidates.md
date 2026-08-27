# Volume + Market-Adjusted Daily Candidate Report - 2026-08-27

Generated at: 2026-08-27 03:24:06

ML dataset source: `data/processed/ml_dataset_20260827.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260827.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20260827.csv`

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

- Total rows: **4**
- strong_volume_market_adjusted_candidate: **3**
- volatile_watchlist: **1**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 032580 | 피델릭스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 302430 | 이노메트리 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 010400 | 우진아이엔에스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

No candidates in this section.

## Watchlist Candidates

No candidates in this section.

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 268280 | 미원에스씨 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

No candidates in this section.

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
