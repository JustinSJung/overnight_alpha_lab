# Market-Adjusted Daily Candidate Report - 2026-08-25

Generated at: 2026-08-25 22:50:25

ML dataset source: `data/processed/ml_dataset_20260825.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260825.csv`

## Purpose

This report applies market-adjusted score adjustments to daily candidate scoring.

It is a safer v2 report and does not replace the existing daily stock recommender yet.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Score Formula

```text
base_recommendation_score_v2
+ market_adjusted_score_adjustment
= final_market_adjusted_score
```

## Summary

- Total rows: **15**
- positive_candidate: **11**
- risk_or_avoid_review: **4**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 000210 | DL | supply_contract | positive | pending | pending | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 375500 | DL이앤씨 | supply_contract | positive | pending | pending | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 009540 | HD한국조선해양 | supply_contract | positive | pending | pending | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | pending | pending | 85.00 | 0.00 | 85.00 | N/A |
| 1970-01-01 | 006260 | LS | major_shareholder_change | volatile | pending | pending | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 006260 | LS | major_shareholder_change | volatile | pending | pending | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 034730 | SK | merger | volatile | pending | pending | 66.00 | 0.00 | 66.00 | N/A |
| 1970-01-01 | 034730 | SK | merger | volatile | pending | pending | 66.00 | 0.00 | 66.00 | N/A |
| 1970-01-01 | 270520 | 앱튼 | investment_decision | volatile | pending | pending | 56.00 | 0.00 | 56.00 | N/A |
| 1970-01-01 | 000950 | 전방 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 000950 | 전방 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |

## Watchlist Candidates

No candidates in this section.

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 216400 | 인바이츠바이오코아 | disclosure_violation | negative | pending | pending | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 216400 | 인바이츠바이오코아 | disclosure_violation | negative | pending | pending | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | pending | pending | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 014970 | 삼륭물산 | disclosure_violation | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
