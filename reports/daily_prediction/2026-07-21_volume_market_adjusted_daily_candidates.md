# Volume + Market-Adjusted Daily Candidate Report - 2026-07-21

Generated at: 2026-07-21 23:15:38

ML dataset source: `data/processed/ml_dataset_20260721.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260721.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20260721.csv`

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

- Total rows: **30**
- risk_or_avoid_review: **19**
- strong_volume_market_adjusted_candidate: **5**
- watchlist_candidate: **4**
- positive_candidate: **1**
- volatile_watchlist: **1**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 053580 | 웹케시 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 119850 | 지엔씨에너지 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 008470 | 부스타 | bonus_issue | positive | pending | pending | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |
| 1970-01-01 | 348950 | 제이알글로벌리츠 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 61.00 | 0.00 | 0.00 | 61.00 | N/A | N/A | N/A |
| 1970-01-01 | 397030 | 에이프릴바이오 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 61.00 | 0.00 | 0.00 | 61.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 011420 | 갤럭시아에스엠 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 000500 | 가온전선 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 000500 | 가온전선 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 000500 | 가온전선 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 000500 | 가온전선 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 066790 | 씨씨에스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 1.00 | 0.00 | 0.00 | 1.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 106240 | 파인테크닉스 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -20.00 | 0.00 | 0.00 | -20.00 | N/A | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -35.00 | 0.00 | 0.00 | -35.00 | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -35.00 | 0.00 | 0.00 | -35.00 | N/A | N/A | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 159910 | 에코글로우 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -50.00 | 0.00 | 0.00 | -50.00 | N/A | N/A | N/A |
| 1970-01-01 | 066430 | 아이로보틱스 | lawsuit | negative | pending | pending | insufficient_volume_baseline | -55.00 | 0.00 | 0.00 | -55.00 | N/A | N/A | N/A |
| 1970-01-01 | 006220 | 제주은행 | disclosure_violation | negative | pending | pending | insufficient_volume_baseline | -65.00 | 0.00 | 0.00 | -65.00 | N/A | N/A | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -80.00 | 0.00 | 0.00 | -80.00 | N/A | N/A | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -80.00 | 0.00 | 0.00 | -80.00 | N/A | N/A | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -80.00 | 0.00 | 0.00 | -80.00 | N/A | N/A | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -80.00 | 0.00 | 0.00 | -80.00 | N/A | N/A | N/A |
| 1970-01-01 | 071950 | 코아스 | paid_in_capital_increase | negative | pending | pending | insufficient_volume_baseline | -100.00 | 0.00 | 0.00 | -100.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
