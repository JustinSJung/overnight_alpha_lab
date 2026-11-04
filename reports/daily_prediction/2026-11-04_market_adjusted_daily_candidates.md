# Market-Adjusted Daily Candidate Report - 2026-11-04

Generated at: 2026-11-04 02:54:11

ML dataset source: `data/processed/ml_dataset_20261104.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20261104.csv`

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

- Total rows: **213**
- watchlist_candidate: **115**
- risk_or_avoid_review: **48**
- positive_candidate: **38**
- volatile_watchlist: **12**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 020180 | 대신정보통신 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 207940 | 삼성바이오로직스 | supply_contract | positive | failure | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 000210 | DL | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 000210 | DL | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 005960 | 동부건설 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 171090 | 선익시스템 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 013360 | 일성건설 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 066970 | 엘앤에프 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 375500 | DL이앤씨 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 375500 | DL이앤씨 | supply_contract | positive | failure | market_data_missing | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 440110 | 파두 | supply_contract | positive | failure | market_data_missing | 80.00 | 0.00 | 80.00 | N/A |
| 1970-01-01 | 487720 | 키움제10호스팩 | merger | volatile | failure | market_data_missing | 76.00 | 0.00 | 76.00 | N/A |
| 1970-01-01 | 475040 | 스트라드비젼 | supply_contract | positive | failure | market_data_missing | 75.00 | 0.00 | 75.00 | N/A |
| 1970-01-01 | 016380 | KG스틸 | merger | volatile | failure | market_data_missing | 66.00 | 0.00 | 66.00 | N/A |
| 1970-01-01 | 016380 | KG스틸 | merger | volatile | failure | market_data_missing | 66.00 | 0.00 | 66.00 | N/A |
| 1970-01-01 | 016380 | KG스틸 | merger | volatile | failure | market_data_missing | 66.00 | 0.00 | 66.00 | N/A |
| 1970-01-01 | 016380 | KG스틸 | merger | volatile | failure | market_data_missing | 66.00 | 0.00 | 66.00 | N/A |
| 1970-01-01 | 0126Z0 | 삼성에피스홀딩스 | investment_decision | volatile | failure | market_data_missing | 56.00 | 0.00 | 56.00 | N/A |
| 1970-01-01 | 381970 | KG모빌리티플랫폼 | investment_decision | volatile | failure | market_data_missing | 46.00 | 0.00 | 46.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 012280 | 영화금속 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 012280 | 영화금속 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 002760 | 보락 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 002760 | 보락 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 021050 | 서원 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 248070 | 솔루엠 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 002760 | 보락 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 248070 | 솔루엠 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 248070 | 솔루엠 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 002760 | 보락 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 002760 | 보락 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 012280 | 영화금속 | major_shareholder_change | volatile | failure | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 084680 | 이월드 | major_shareholder_change | volatile | success | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 004770 | 써니전자 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 004770 | 써니전자 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 004770 | 써니전자 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 004770 | 써니전자 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 004770 | 써니전자 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 004770 | 써니전자 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 004770 | 써니전자 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | success | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 034310 | NICE | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 034310 | NICE | major_shareholder_change | volatile | failure | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | success | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 019210 | 와이지-원 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 019210 | 와이지-원 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 450080 | 에코프로머티 | major_shareholder_change | volatile | failure | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 450080 | 에코프로머티 | major_shareholder_change | volatile | failure | market_data_missing | 1.00 | 0.00 | 1.00 | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | -9.00 | 0.00 | -9.00 | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | -9.00 | 0.00 | -9.00 | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | -9.00 | 0.00 | -9.00 | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | major_shareholder_change | volatile | failure | market_data_missing | -9.00 | 0.00 | -9.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 229640 | LS에코에너지 | paid_in_capital_increase | negative | success | market_data_missing | -10.00 | 0.00 | -10.00 | N/A |
| 1970-01-01 | 177350 | 베셀 | convertible_bond | negative | success | market_data_missing | -25.00 | 0.00 | -25.00 | N/A |
| 1970-01-01 | 001360 | 삼성제약 | convertible_bond | negative | failure | market_data_missing | -30.00 | 0.00 | -30.00 | N/A |
| 1970-01-01 | 035420 | NAVER | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 035420 | NAVER | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 066430 | 아이로보틱스 | lawsuit | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | success | market_data_missing | -45.00 | 0.00 | -45.00 | N/A |
| 1970-01-01 | 328130 | 루닛 | convertible_bond | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 223220 | 로지스몬 | lawsuit | negative | success | market_data_missing | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | paid_in_capital_increase | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | paid_in_capital_increase | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | paid_in_capital_increase | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | paid_in_capital_increase | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 067080 | 대화제약 | disclosure_violation | negative | success | market_data_missing | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 040160 | 누리플렉스 | lawsuit | negative | success | market_data_missing | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 108230 | 톱텍 | convertible_bond | negative | success | market_data_missing | -65.00 | 0.00 | -65.00 | N/A |
| 1970-01-01 | 377030 | 비트맥스 | paid_in_capital_increase | negative | failure | market_data_missing | -65.00 | 0.00 | -65.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
