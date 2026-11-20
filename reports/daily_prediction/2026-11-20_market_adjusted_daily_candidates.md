# Market-Adjusted Daily Candidate Report - 2026-11-20

Generated at: 2026-11-20 04:02:13

ML dataset source: `data/processed/ml_dataset_20261120.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261120.csv`

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

- Total rows: **406**
- positive_candidate: **260**
- risk_or_avoid_review: **131**
- watchlist_candidate: **13**
- volatile_watchlist: **2**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 103590 | 일진전기 | supply_contract | positive | failure | market_data_missing | 160.00 | 0.00 | 160.00 | N/A |
| 1970-01-01 | 445090 | 에이직랜드 | supply_contract | positive | failure | market_data_missing | 155.00 | 0.00 | 155.00 | N/A |
| 1970-01-01 | 112610 | 씨에스윈드 | supply_contract | positive | failure | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 115610 | 이미지스 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 025890 | 한국주강 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 013360 | 일성건설 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 013360 | 일성건설 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 042660 | 한화오션 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 013360 | 일성건설 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 013360 | 일성건설 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 286750 | 나노실리칸첨단소재 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 035890 | 서희건설 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 035890 | 서희건설 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 035890 | 서희건설 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 035890 | 서희건설 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 035890 | 서희건설 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 047040 | 대우건설 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 002460 | HS화성 | supply_contract | positive | failure | market_data_missing | 90.00 | 0.00 | 90.00 | N/A |
| 1970-01-01 | 067630 | HLB생명과학 | merger | volatile | success | market_data_missing | 81.00 | 0.00 | 81.00 | N/A |
| 1970-01-01 | 067630 | HLB생명과학 | merger | volatile | success | market_data_missing | 81.00 | 0.00 | 81.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 004990 | 롯데지주 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 007680 | 대원 | merger | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 004090 | 한국석유공업 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 004990 | 롯데지주 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 021050 | 서원 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 263050 | 유틸렉스 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 145720 | 덴티움 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 263050 | 유틸렉스 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 038060 | 루멘스바이오스 | spin_off | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 191410 | 육일씨엔에쓰 | major_shareholder_change | volatile | success | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |
| 1970-01-01 | 105560 | KB금융 | major_shareholder_change | volatile | failure | market_data_missing | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 024070 | WISCOM | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 024070 | WISCOM | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 026910 | 광진실업 | convertible_bond | negative | success | market_data_missing | -5.00 | 0.00 | -5.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | convertible_bond | negative | success | market_data_missing | -5.00 | 0.00 | -5.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | convertible_bond | negative | success | market_data_missing | -5.00 | 0.00 | -5.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | convertible_bond | negative | success | market_data_missing | -5.00 | 0.00 | -5.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | paid_in_capital_increase | negative | success | market_data_missing | -15.00 | 0.00 | -15.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | paid_in_capital_increase | negative | success | market_data_missing | -15.00 | 0.00 | -15.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | paid_in_capital_increase | negative | success | market_data_missing | -15.00 | 0.00 | -15.00 | N/A |
| 1970-01-01 | 026910 | 광진실업 | paid_in_capital_increase | negative | success | market_data_missing | -15.00 | 0.00 | -15.00 | N/A |
| 1970-01-01 | 304840 | 타임X AI | paid_in_capital_increase | negative | failure | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 304840 | 타임X AI | paid_in_capital_increase | negative | failure | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 013360 | 일성건설 | disclosure_violation | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 294630 | 서남 | paid_in_capital_increase | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 013360 | 일성건설 | disclosure_violation | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 013360 | 일성건설 | disclosure_violation | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 013360 | 일성건설 | disclosure_violation | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 900290 | GRT | paid_in_capital_increase | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 294630 | 서남 | paid_in_capital_increase | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | convertible_bond | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
