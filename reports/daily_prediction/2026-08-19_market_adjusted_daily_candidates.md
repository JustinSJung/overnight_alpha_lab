# Market-Adjusted Daily Candidate Report - 2026-08-19

Generated at: 2026-08-19 22:48:38

ML dataset source: `data/processed/ml_dataset_20260819.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260819.csv`

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

- Total rows: **35**
- risk_or_avoid_review: **18**
- positive_candidate: **12**
- watchlist_candidate: **5**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 294870 | IPARK현대산업개발 | supply_contract | positive | pending | pending | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 012630 | HDC | supply_contract | positive | pending | pending | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | supply_contract | positive | pending | pending | 125.00 | 0.00 | 125.00 | N/A |
| 1970-01-01 | 277880 | 티에스아이 | supply_contract | positive | pending | pending | 115.00 | 0.00 | 115.00 | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | pending | pending | 110.00 | 0.00 | 110.00 | N/A |
| 1970-01-01 | 002020 | 코오롱 | supply_contract | positive | pending | pending | 100.00 | 0.00 | 100.00 | N/A |
| 1970-01-01 | 028260 | 삼성물산 | supply_contract | positive | pending | pending | 95.00 | 0.00 | 95.00 | N/A |
| 1970-01-01 | 043090 | 더테크놀로지 | spin_off | volatile | pending | pending | 91.00 | 0.00 | 91.00 | N/A |
| 1970-01-01 | 322780 | 코퍼스코리아 | major_shareholder_change | volatile | pending | pending | 51.00 | 0.00 | 51.00 | N/A |
| 1970-01-01 | 033530 | SJG세종 | merger | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 033530 | SJG세종 | merger | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 073190 | 듀오백 | major_shareholder_change | volatile | pending | pending | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 073190 | 듀오백 | major_shareholder_change | volatile | pending | pending | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 073190 | 듀오백 | major_shareholder_change | volatile | pending | pending | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 073190 | 듀오백 | major_shareholder_change | volatile | pending | pending | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 307870 | 비투엔 | major_shareholder_change | volatile | pending | pending | 21.00 | 0.00 | 21.00 | N/A |

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 351320 | 넥사다이내믹스 | convertible_bond | negative | pending | pending | -20.00 | 0.00 | -20.00 | N/A |
| 1970-01-01 | 352940 | 인바이오 | disclosure_violation | negative | pending | pending | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 389680 | 유디엠텍 | disclosure_violation | negative | pending | pending | -40.00 | 0.00 | -40.00 | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | convertible_bond | negative | pending | pending | -50.00 | 0.00 | -50.00 | N/A |
| 1970-01-01 | 020560 | 아시아나항공 | lawsuit | negative | pending | pending | -55.00 | 0.00 | -55.00 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 009810 | 플레이그램 | paid_in_capital_increase | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 210120 | 캔버스엔 | convertible_bond | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 148250 | 알엔투테크놀로지 | disclosure_violation | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |
| 1970-01-01 | 010130 | 고려아연 | lawsuit | negative | pending | pending | -75.00 | 0.00 | -75.00 | N/A |
| 1970-01-01 | 074610 | 이엔플러스 | lawsuit | negative | pending | pending | -80.00 | 0.00 | -80.00 | N/A |
| 1970-01-01 | 290270 | 휴네시온 | disclosure_violation | negative | pending | pending | -90.00 | 0.00 | -90.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
