# Market-Adjusted Daily Candidate Report - 2026-10-02

Generated at: 2026-10-02 03:11:16

ML dataset source: `data/processed/ml_dataset_20261002.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261002.csv`

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

- Total rows: **486**
- risk_or_avoid_review: **291**
- positive_candidate: **169**
- watchlist_candidate: **24**
- volatile_watchlist: **2**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 214430 | 아이쓰리시스템 | supply_contract | positive | failure | market_data_missing | 150.00 | 0.00 | 150.00 | N/A |
| 1970-01-01 | 003160 | 디아이 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 005880 | 대한해운 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 373220 | LG에너지솔루션 | supply_contract | positive | success | market_data_missing | 135.00 | 0.00 | 135.00 | N/A |
| 1970-01-01 | 386380 | 스카이랩스 | supply_contract | positive | success | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 480370 | 씨케이솔루션 | supply_contract | positive | failure | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 490470 | 세미파이브 | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 432720 | 퀄리타스반도체 | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 010780 | 아이에스동서 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 006260 | LS | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 028670 | 팬오션 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 399720 | 가온칩스 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 348340 | 뉴로메카 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 138080 | 오이솔루션 | major_shareholder_change | volatile | success | market_data_missing | 106.00 | 0.00 | 106.00 | N/A |
| 1970-01-01 | 138080 | 오이솔루션 | major_shareholder_change | volatile | success | market_data_missing | 106.00 | 0.00 | 106.00 | N/A |
| 1970-01-01 | 138080 | 오이솔루션 | major_shareholder_change | volatile | success | market_data_missing | 106.00 | 0.00 | 106.00 | N/A |
| 1970-01-01 | 023150 | MH에탄올 | bonus_issue | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 023150 | MH에탄올 | bonus_issue | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 406820 | 뷰티스킨 | supply_contract | positive | failure | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 034020 | 두산에너빌리티 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 181710 | NHN | merger | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 267260 | HD현대일렉트릭 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 082270 | 젬백스 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 001570 | 금양 | spin_off | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 000050 | 경방 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 007160 | 사조산업 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 007160 | 사조산업 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
