# Volume + Market-Adjusted Daily Candidate Report - 2026-10-02

Generated at: 2026-10-02 03:11:21

ML dataset source: `data/processed/ml_dataset_20261002.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261002.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20261002.csv`

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

- Total rows: **486**
- risk_or_avoid_review: **291**
- strong_volume_market_adjusted_candidate: **98**
- positive_candidate: **73**
- watchlist_candidate: **22**
- volatile_watchlist: **2**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 214430 | 아이쓰리시스템 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 150.00 | 0.00 | 0.00 | 150.00 | N/A | N/A | N/A |
| 1970-01-01 | 003160 | 디아이 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 005880 | 대한해운 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 373220 | LG에너지솔루션 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 386380 | 스카이랩스 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 480370 | 씨케이솔루션 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 490470 | 세미파이브 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 432720 | 퀄리타스반도체 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 010780 | 아이에스동서 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 006260 | LS | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 028670 | 팬오션 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 399720 | 가온칩스 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 348340 | 뉴로메카 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 138080 | 오이솔루션 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 106.00 | 0.00 | 0.00 | 106.00 | N/A | N/A | N/A |
| 1970-01-01 | 138080 | 오이솔루션 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 106.00 | 0.00 | 0.00 | 106.00 | N/A | N/A | N/A |
| 1970-01-01 | 138080 | 오이솔루션 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 106.00 | 0.00 | 0.00 | 106.00 | N/A | N/A | N/A |
| 1970-01-01 | 023150 | MH에탄올 | bonus_issue | positive | failure | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 023150 | MH에탄올 | bonus_issue | positive | failure | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 406820 | 뷰티스킨 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 034020 | 두산에너빌리티 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 95.00 | 0.00 | 0.00 | 95.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 072770 | 멤레이비티 | spin_off | volatile | failure | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | merger | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | merger | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | merger | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | merger | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 010950 | S-Oil | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 082270 | 젬백스 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 115160 | 휴맥스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 001570 | 금양 | spin_off | volatile | failure | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 000050 | 경방 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 005800 | 신영와코루 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |
| 1970-01-01 | 005800 | 신영와코루 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 21.00 | 0.00 | 0.00 | 21.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 007160 | 사조산업 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 007160 | 사조산업 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
