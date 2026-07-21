# Market-Adjusted Daily Candidate Report - 2026-07-21

Generated at: 2026-07-21 23:15:37

ML dataset source: `data/processed/ml_dataset_20260721.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260721.csv`

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

- Total rows: **30**
- risk_or_avoid_review: **19**
- positive_candidate: **6**
- watchlist_candidate: **4**
- volatile_watchlist: **1**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 053580 | 웹케시 | supply_contract | positive | pending | pending | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 119850 | 지엔씨에너지 | supply_contract | positive | pending | pending | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 008470 | 부스타 | bonus_issue | positive | pending | pending | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 348950 | 제이알글로벌리츠 | investment_decision | volatile | pending | pending | 61.00 | 0.00 | 61.00 | N/A |
| 1970-01-01 | 397030 | 에이프릴바이오 | investment_decision | volatile | pending | pending | 61.00 | 0.00 | 61.00 | N/A |
| 1970-01-01 | 011420 | 갤럭시아에스엠 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 000500 | 가온전선 | major_shareholder_change | volatile | pending | pending | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 000500 | 가온전선 | major_shareholder_change | volatile | pending | pending | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 000500 | 가온전선 | major_shareholder_change | volatile | pending | pending | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 000500 | 가온전선 | major_shareholder_change | volatile | pending | pending | 31.00 | 0.00 | 31.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 066790 | 씨씨에스 | major_shareholder_change | volatile | pending | pending | 1.00 | 0.00 | 1.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 106240 | 파인테크닉스 | convertible_bond | negative | pending | pending | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | pending | pending | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | pending | pending | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | pending | pending | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | pending | pending | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | pending | pending | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | pending | pending | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 340810 | 시선AI | paid_in_capital_increase | negative | pending | pending | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 340810 | 시선AI | paid_in_capital_increase | negative | pending | pending | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | convertible_bond | negative | pending | pending | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | convertible_bond | negative | pending | pending | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 159910 | 에코글로우 | convertible_bond | negative | pending | pending | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 066430 | 아이로보틱스 | lawsuit | negative | pending | pending | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 006220 | 제주은행 | disclosure_violation | negative | pending | pending | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | paid_in_capital_increase | negative | pending | pending | -80.00 | 0.00 | -80.00 | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | paid_in_capital_increase | negative | pending | pending | -80.00 | 0.00 | -80.00 | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | paid_in_capital_increase | negative | pending | pending | -80.00 | 0.00 | -80.00 | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | paid_in_capital_increase | negative | pending | pending | -80.00 | 0.00 | -80.00 | N/A |
| 1970-01-01 | 071950 | 코아스 | paid_in_capital_increase | negative | pending | pending | -100.00 | 0.00 | -100.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
