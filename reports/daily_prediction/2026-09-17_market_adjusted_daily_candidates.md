# Market-Adjusted Daily Candidate Report - 2026-09-17

Generated at: 2026-09-17 01:41:22

ML dataset source: `data/processed/ml_dataset_20260917.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260917.csv`

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

- Total rows: **320**
- risk_or_avoid_review: **214**
- positive_candidate: **68**
- watchlist_candidate: **37**
- volatile_watchlist: **1**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 065450 | 빅텍 | supply_contract | positive | success | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 455180 | 케이지에이 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 267850 | 아시아나IDT | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 083650 | 비에이치아이 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 130660 | 한전산업 | supply_contract | positive | success | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 130660 | 한전산업 | supply_contract | positive | success | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 130660 | 한전산업 | supply_contract | positive | success | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 130660 | 한전산업 | supply_contract | positive | success | market_data_missing | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 021320 | KCC건설 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 257370 | 피엔티엠에스 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 296640 | 이노에이엑스 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 406820 | 뷰티스킨 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 220100 | 퓨쳐켐 | bonus_issue | positive | failure | market_data_missing | 80.00 | 0.00 | 80.00 | N/A |
| 1970-01-01 | 220100 | 퓨쳐켐 | bonus_issue | positive | failure | market_data_missing | 80.00 | 0.00 | 80.00 | N/A |
| 1970-01-01 | 220100 | 퓨쳐켐 | bonus_issue | positive | failure | market_data_missing | 80.00 | 0.00 | 80.00 | N/A |
| 1970-01-01 | 220100 | 퓨쳐켐 | bonus_issue | positive | failure | market_data_missing | 80.00 | 0.00 | 80.00 | N/A |
| 1970-01-01 | 220100 | 퓨쳐켐 | bonus_issue | positive | failure | market_data_missing | 80.00 | 0.00 | 80.00 | N/A |
| 1970-01-01 | 220100 | 퓨쳐켐 | bonus_issue | positive | failure | market_data_missing | 80.00 | 0.00 | 80.00 | N/A |
| 1970-01-01 | 278470 | 에이피알 | merger | volatile | success | market_data_missing | 76.00 | 0.00 | 76.00 | N/A |
| 1970-01-01 | 003850 | 보령 | spin_off | volatile | success | market_data_missing | 56.00 | 0.00 | 56.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 033340 | 좋은사람들 | spin_off | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 006730 | 서부T&D | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 261200 | 덴티스 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 261200 | 덴티스 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 261200 | 덴티스 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 261200 | 덴티스 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 261200 | 덴티스 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 261200 | 덴티스 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 083470 | 이엠앤아이 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 047400 | 유니온머티리얼 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 004150 | 한솔홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 004150 | 한솔홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 004150 | 한솔홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 047400 | 유니온머티리얼 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 047400 | 유니온머티리얼 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 083470 | 이엠앤아이 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 083470 | 이엠앤아이 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 083470 | 이엠앤아이 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 083470 | 이엠앤아이 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 083470 | 이엠앤아이 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 443250 | 레뷰코퍼레이션 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 474650 | 링크솔루션 | convertible_bond | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 006840 | AK홀딩스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 006840 | AK홀딩스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 006840 | AK홀딩스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 006840 | AK홀딩스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 006840 | AK홀딩스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 006840 | AK홀딩스 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 083470 | 이엠앤아이 | paid_in_capital_increase | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 083470 | 이엠앤아이 | paid_in_capital_increase | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 083470 | 이엠앤아이 | paid_in_capital_increase | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 083470 | 이엠앤아이 | paid_in_capital_increase | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 083470 | 이엠앤아이 | paid_in_capital_increase | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 083470 | 이엠앤아이 | paid_in_capital_increase | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | failure | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
