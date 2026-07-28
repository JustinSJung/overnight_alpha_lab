# Volume + Market-Adjusted Daily Candidate Report - 2026-07-28

Generated at: 2026-07-28 23:19:21

ML dataset source: `data/processed/ml_dataset_20260728.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260728.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20260728.csv`

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

- Total rows: **31**
- risk_or_avoid_review: **15**
- strong_volume_market_adjusted_candidate: **8**
- positive_candidate: **7**
- volatile_watchlist: **1**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 130660 | 한전산업 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 130660 | 한전산업 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 130660 | 한전산업 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 130660 | 한전산업 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 028260 | 삼성물산 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 80.00 | 0.00 | 0.00 | 80.00 | N/A | N/A | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 66.00 | 0.00 | 0.00 | 66.00 | N/A | N/A | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 66.00 | 0.00 | 0.00 | 66.00 | N/A | N/A | N/A |
| 1970-01-01 | 064350 | 현대로템 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 61.00 | 0.00 | 0.00 | 61.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 010060 | OCI홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 217730 | 강스템바이오텍 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 217730 | 강스템바이오텍 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 047040 | 대우건설 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 083640 | 인콘 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 066410 | 버킷스튜디오 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |

## Watchlist Candidates

No candidates in this section.

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 082270 | 젬백스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 6.00 | 0.00 | 0.00 | 6.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 060900 | 에이전트AI | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -35.00 | 0.00 | 0.00 | -35.00 | N/A | N/A | N/A |
| 1970-01-01 | 069460 | 대호에이엘 | lawsuit | negative | pending | pending | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 009810 | 플레이그램 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -60.00 | 0.00 | 0.00 | -60.00 | N/A | N/A | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 210980 | SK디앤디 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 210980 | SK디앤디 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 210980 | SK디앤디 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 210980 | SK디앤디 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 032800 | 판타지오 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 341170 | 퓨쳐메디신 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -70.00 | 0.00 | 0.00 | -70.00 | N/A | N/A | N/A |
| 1970-01-01 | 071200 | 인피니트헬스케어 | lawsuit | negative | pending | pending | insufficient_volume_baseline | -80.00 | 0.00 | 0.00 | -80.00 | N/A | N/A | N/A |
| 1970-01-01 | 004780 | 대륙제관 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -95.00 | 0.00 | 0.00 | -95.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
