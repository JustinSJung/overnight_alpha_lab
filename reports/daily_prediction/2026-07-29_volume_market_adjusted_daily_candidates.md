# Volume + Market-Adjusted Daily Candidate Report - 2026-07-29

Generated at: 2026-07-29 23:18:04

ML dataset source: `data/processed/ml_dataset_20260729.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260729.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20260729.csv`

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

- Total rows: **24**
- risk_or_avoid_review: **10**
- strong_volume_market_adjusted_candidate: **8**
- volatile_watchlist: **6**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 054220 | 비츠로시스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 010780 | 아이에스동서 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 001260 | 남광토건 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 110.00 | 0.00 | 0.00 | 110.00 | N/A | N/A | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 105.00 | 0.00 | 0.00 | 105.00 | N/A | N/A | N/A |
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 75.00 | 0.00 | 0.00 | 75.00 | N/A | N/A | N/A |

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
| 1970-01-01 | 066790 | 씨씨에스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 6.00 | 0.00 | 0.00 | 6.00 | N/A | N/A | N/A |
| 1970-01-01 | 043260 | 성호전자 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 043260 | 성호전자 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 043260 | 성호전자 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |
| 1970-01-01 | 043260 | 성호전자 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 115530 | 씨엔플러스 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | 0.00 | 0.00 | 0.00 | 0.00 | N/A | N/A | N/A |
| 1970-01-01 | 115530 | 씨엔플러스 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | 0.00 | 0.00 | 0.00 | 0.00 | N/A | N/A | N/A |
| 1970-01-01 | 115530 | 씨엔플러스 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | 0.00 | 0.00 | 0.00 | 0.00 | N/A | N/A | N/A |
| 1970-01-01 | 115530 | 씨엔플러스 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | 0.00 | 0.00 | 0.00 | 0.00 | N/A | N/A | N/A |
| 1970-01-01 | 017810 | 풀무원 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 017810 | 풀무원 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 027040 | 서울전자통신 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 340360 | 다보링크 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 340360 | 다보링크 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 121440 | 골프존홀딩스 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
