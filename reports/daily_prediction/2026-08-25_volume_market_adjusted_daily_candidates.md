# Volume + Market-Adjusted Daily Candidate Report - 2026-08-25

Generated at: 2026-08-25 22:50:26

ML dataset source: `data/processed/ml_dataset_20260825.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260825.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20260825.csv`

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

- Total rows: **15**
- strong_volume_market_adjusted_candidate: **8**
- risk_or_avoid_review: **4**
- positive_candidate: **3**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 000210 | DL | supply_contract | positive | pending | pending | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 375500 | DL이앤씨 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 85.00 | 0.00 | 0.00 | 85.00 | N/A | N/A | N/A |
| 1970-01-01 | 006260 | LS | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 71.00 | 0.00 | 0.00 | 71.00 | N/A | N/A | N/A |
| 1970-01-01 | 006260 | LS | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 71.00 | 0.00 | 0.00 | 71.00 | N/A | N/A | N/A |
| 1970-01-01 | 034730 | SK | merger | volatile | pending | pending | insufficient_volume_baseline | 66.00 | 0.00 | 0.00 | 66.00 | N/A | N/A | N/A |
| 1970-01-01 | 034730 | SK | merger | volatile | pending | pending | insufficient_volume_baseline | 66.00 | 0.00 | 0.00 | 66.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 270520 | 앱튼 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 000950 | 전방 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 000950 | 전방 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |

## Watchlist Candidates

No candidates in this section.

## Volatile Watchlist

No candidates in this section.

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 216400 | 인바이츠바이오코아 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 216400 | 인바이츠바이오코아 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 014970 | 삼륭물산 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
