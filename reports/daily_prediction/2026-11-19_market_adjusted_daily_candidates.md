# Market-Adjusted Daily Candidate Report - 2026-11-19

Generated at: 2026-11-19 04:22:39

ML dataset source: `data/processed/ml_dataset_20261119.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261119.csv`

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

- Total rows: **255**
- positive_candidate: **172**
- risk_or_avoid_review: **56**
- watchlist_candidate: **17**
- volatile_watchlist: **10**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 010960 | 삼호개발 | supply_contract | positive | success | market_data_missing | 150.00 | 0.00 | 150.00 | N/A |
| 1970-01-01 | 464080 | 에스오에스랩 | supply_contract | positive | failure | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 077970 | STX엔진 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 083650 | 비에이치아이 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 0015G0 | 그린광학 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 115480 | 씨유메디칼 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 094860 | 네오리진 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 003540 | 대신증권 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 015230 | 대창단조 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 015230 | 대창단조 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 005830 | DB손해보험 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 005830 | DB손해보험 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 061250 | 화일약품 | major_shareholder_change | volatile | success | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 006370 | 대구백화점 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 053270 | 구영테크 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 457600 | 벡트로보틱스 | major_shareholder_change | volatile | success | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 021240 | 코웨이 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | major_shareholder_change | volatile | success | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | major_shareholder_change | volatile | success | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | major_shareholder_change | volatile | success | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | major_shareholder_change | volatile | success | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 021240 | 코웨이 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |
| 1970-01-01 | 002810 | 삼영무역 | major_shareholder_change | volatile | failure | market_data_missing | -9.00 | 0.00 | -9.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 131400 | 이브이첨단소재 | convertible_bond | negative | success | market_data_missing | 10.00 | 0.00 | 10.00 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | success | market_data_missing | 10.00 | 0.00 | 10.00 | N/A |
| 1970-01-01 | 131400 | 이브이첨단소재 | convertible_bond | negative | success | market_data_missing | 10.00 | 0.00 | 10.00 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | success | market_data_missing | 10.00 | 0.00 | 10.00 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | success | market_data_missing | 10.00 | 0.00 | 10.00 | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | convertible_bond | negative | success | market_data_missing | 10.00 | 0.00 | 10.00 | N/A |
| 1970-01-01 | 258790 | 소프트캠프 | convertible_bond | negative | success | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 258790 | 소프트캠프 | convertible_bond | negative | success | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 123010 | MSDI | paid_in_capital_increase | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 123010 | MSDI | paid_in_capital_increase | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 353190 | 휴럼 | convertible_bond | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 071050 | 한국금융지주 | paid_in_capital_increase | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 071050 | 한국금융지주 | paid_in_capital_increase | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 071050 | 한국금융지주 | paid_in_capital_increase | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 071050 | 한국금융지주 | paid_in_capital_increase | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 071050 | 한국금융지주 | paid_in_capital_increase | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 071050 | 한국금융지주 | paid_in_capital_increase | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 032800 | 판타지오 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 096690 | 에이루트 | convertible_bond | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 900100 | 파이온엑스 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
