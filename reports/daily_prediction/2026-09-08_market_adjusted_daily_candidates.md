# Market-Adjusted Daily Candidate Report - 2026-09-08

Generated at: 2026-09-08 01:05:16

ML dataset source: `data/processed/ml_dataset_20260908.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260908.csv`

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

- Total rows: **441**
- watchlist_candidate: **169**
- risk_or_avoid_review: **159**
- positive_candidate: **103**
- volatile_watchlist: **10**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 112610 | 씨에스윈드 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 045100 | 한양이엔지 | supply_contract | positive | failure | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 112610 | 씨에스윈드 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 217190 | 제너셈 | supply_contract | positive | success | market_data_missing | 130.00 | 0.00 | 130.00 | N/A |
| 1970-01-01 | 067080 | 대화제약 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 126340 | 비나텍 | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 000210 | DL | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 046940 | 우원개발 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 459510 | 나우로보틱스 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 375500 | DL이앤씨 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 083790 | CG인바이츠 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 002780 | 진흥기업 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 040910 | 아이씨디 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 016610 | DB증권 | major_shareholder_change | volatile | failure | market_data_missing | 86.00 | 0.00 | 86.00 | N/A |
| 1970-01-01 | 016610 | DB증권 | major_shareholder_change | volatile | failure | market_data_missing | 86.00 | 0.00 | 86.00 | N/A |
| 1970-01-01 | 016610 | DB증권 | major_shareholder_change | volatile | failure | market_data_missing | 86.00 | 0.00 | 86.00 | N/A |
| 1970-01-01 | 016610 | DB증권 | major_shareholder_change | volatile | failure | market_data_missing | 86.00 | 0.00 | 86.00 | N/A |
| 1970-01-01 | 016610 | DB증권 | major_shareholder_change | volatile | failure | market_data_missing | 86.00 | 0.00 | 86.00 | N/A |
| 1970-01-01 | 001260 | 남광토건 | supply_contract | positive | failure | market_data_missing | 85.00 | 0.00 | 85.00 | N/A |
| 1970-01-01 | 001260 | 남광토건 | supply_contract | positive | failure | market_data_missing | 85.00 | 0.00 | 85.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 022100 | 포스코DX | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 022100 | 포스코DX | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 022100 | 포스코DX | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 010580 | 에스엠벡셀 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 091810 | 트리니티항공 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 010580 | 에스엠벡셀 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 001230 | 동국홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 001230 | 동국홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 091810 | 트리니티항공 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 010580 | 에스엠벡셀 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 001230 | 동국홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 091810 | 트리니티항공 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | major_shareholder_change | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 226340 | 본느 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 078930 | GS | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 023440 | 제이스코홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 010400 | 우진아이엔에스 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 010400 | 우진아이엔에스 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 009150 | 삼성전기 | major_shareholder_change | volatile | failure | market_data_missing | 6.00 | 0.00 | 6.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 006740 | 블루산업개발 | convertible_bond | negative | success | market_data_missing | -15.00 | 0.00 | -15.00 | N/A |
| 1970-01-01 | 033790 | 피노 | paid_in_capital_increase | negative | success | market_data_missing | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 067370 | 선바이오 | convertible_bond | negative | success | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 255220 | SG | paid_in_capital_increase | negative | failure | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 049120 | 파인디앤씨 | paid_in_capital_increase | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | lawsuit | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 290120 | DH오토리드 | convertible_bond | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | disclosure_violation | negative | failure | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | disclosure_violation | negative | failure | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 009190 | 대양금속 | paid_in_capital_increase | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 009190 | 대양금속 | paid_in_capital_increase | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | paid_in_capital_increase | negative | success | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | paid_in_capital_increase | negative | success | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | paid_in_capital_increase | negative | success | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | paid_in_capital_increase | negative | success | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | paid_in_capital_increase | negative | success | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | paid_in_capital_increase | negative | success | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | paid_in_capital_increase | negative | success | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 223310 | 사토시홀딩스 | paid_in_capital_increase | negative | success | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 012200 | 계양전기 | paid_in_capital_increase | negative | failure | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
