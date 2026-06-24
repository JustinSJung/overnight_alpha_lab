# Market-Adjusted Daily Candidate Report - 2026-06-24

Generated at: 2026-06-24 22:40:48

ML dataset source: `data/processed/ml_dataset_20260624.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260624.csv`

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

- Total rows: **11**
- positive_candidate: **5**
- watchlist_candidate: **4**
- risk_or_avoid_review: **2**

## Strong Market-Adjusted Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 396470 | 워트 | supply_contract | positive | pending | pending | 105.00 | 0.00 | 105.00 | N/A |
| 1970-01-01 | 097780 | 에코볼트 | merger | volatile | pending | pending | 86.00 | 0.00 | 86.00 | N/A |
| 1970-01-01 | 061040 | 알에프텍 | merger | volatile | pending | pending | 81.00 | 0.00 | 81.00 | N/A |
| 1970-01-01 | 036620 | 감성코퍼레이션 | spin_off | volatile | pending | pending | 71.00 | 0.00 | 71.00 | N/A |
| 1970-01-01 | 452260 | 한화갤러리아 | investment_decision | volatile | pending | pending | 46.00 | 0.00 | 46.00 | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 043260 | 성호전자 | major_shareholder_change | volatile | pending | pending | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 003350 | 한국화장품제조 | major_shareholder_change | volatile | pending | pending | 36.00 | 0.00 | 36.00 | N/A |
| 1970-01-01 | 123690 | 한국화장품 | major_shareholder_change | volatile | pending | pending | 31.00 | 0.00 | 31.00 | N/A |
| 1970-01-01 | 307870 | 비투엔 | major_shareholder_change | volatile | pending | pending | 26.00 | 0.00 | 26.00 | N/A |

## Volatile Watchlist

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | base_recommendation_score_v2 | market_adjusted_score_adjustment | final_market_adjusted_score | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 083790 | CG인바이츠 | disclosure_violation | negative | pending | pending | -60.00 | 0.00 | -60.00 | N/A |
| 1970-01-01 | 052710 | 아모텍 | paid_in_capital_increase | negative | pending | pending | -70.00 | 0.00 | -70.00 | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v2 report with the existing daily recommender report and decide whether to merge the market-adjusted score into the main recommender.
