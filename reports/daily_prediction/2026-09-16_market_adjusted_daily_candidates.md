# Market-Adjusted Daily Candidate Report - 2026-09-16

Generated at: 2026-09-16 01:19:32

ML dataset source: `data/processed/ml_dataset_20260916.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260916.csv`

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

- Total rows: **1362**
- risk_or_avoid_review: **609**
- positive_candidate: **570**
- volatile_watchlist: **137**
- watchlist_candidate: **46**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 095190 | 신화프리텍 | supply_contract | positive | success | market_data_missing | 145.00 | 0.00 | 145.00 | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 081180 | 쎄크 | supply_contract | positive | success | market_data_missing | 140.00 | 0.00 | 140.00 | N/A |
| 1970-01-01 | 298040 | 효성중공업 | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 336260 | 두산퓨얼셀 | supply_contract | positive | failure | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 298040 | 효성중공업 | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 298040 | 효성중공업 | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 298040 | 효성중공업 | supply_contract | positive | success | market_data_missing | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 488900 | 비츠로넥스텍 | supply_contract | positive | success | market_data_missing | 120.00 | 0.00 | 120.00 | N/A |
| 1970-01-01 | 267850 | 아시아나IDT | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 363280 | 티와이홀딩스 | supply_contract | positive | success | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 171090 | 선익시스템 | supply_contract | positive | failure | market_data_missing | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 347700 | 스피어 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 420770 | 기가비스 | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 012630 | HDC | supply_contract | positive | failure | market_data_missing | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 009410 | 태영건설 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 009410 | 태영건설 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 009410 | 태영건설 | supply_contract | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 356890 | 싸이버원 | supply_contract | positive | failure | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 475460 | 미트박스 | bonus_issue | positive | success | market_data_missing | 105.00 | 0.00 | 105.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 084870 | 티비에이치글로벌 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 084870 | 티비에이치글로벌 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 201490 | 미투온 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 201490 | 미투온 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 201490 | 미투온 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 201490 | 미투온 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 201490 | 미투온 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 201490 | 미투온 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 201490 | 미투온 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 201490 | 미투온 | major_shareholder_change | volatile | success | market_data_missing | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 228670 | 레이 | major_shareholder_change | volatile | failure | market_data_missing | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 061250 | 화일약품 | investment_decision | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 010580 | 에스엠벡셀 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 061250 | 화일약품 | investment_decision | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 061250 | 화일약품 | investment_decision | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 061250 | 화일약품 | investment_decision | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 061250 | 화일약품 | investment_decision | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 061250 | 화일약품 | investment_decision | volatile | success | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 326030 | 에스케이바이오팜 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |
| 1970-01-01 | 326030 | 에스케이바이오팜 | major_shareholder_change | volatile | failure | market_data_missing | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 069640 | 한세엠케이 | major_shareholder_change | volatile | success | market_data_missing | 16.00 | 0.00 | 16.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 027740 | 마니커 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 381970 | 케이카 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 381970 | 케이카 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |
| 1970-01-01 | 294090 | 이오플로우 | major_shareholder_change | volatile | failure | market_data_missing | 11.00 | 0.00 | 11.00 | N/A |

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 077360 | 덕산하이메탈 | paid_in_capital_increase | negative | success | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 050090 | 비케이홀딩스 | paid_in_capital_increase | negative | failure | market_data_missing | -35.00 | 0.00 | -35.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 418620 | E8 | paid_in_capital_increase | negative | success | market_data_missing | -40.00 | 0.00 | -40.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
