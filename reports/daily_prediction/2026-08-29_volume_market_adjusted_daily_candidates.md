# Volume + Market-Adjusted Daily Candidate Report - 2026-08-29

Generated at: 2026-08-29 23:19:00

ML dataset source: `data/processed/ml_dataset_20260829.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260829.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20260829.csv`

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

- Total rows: **951**
- watchlist_candidate: **352**
- risk_or_avoid_review: **239**
- strong_volume_market_adjusted_candidate: **236**
- positive_candidate: **105**
- volatile_watchlist: **19**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 002780 | 진흥기업 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 002780 | 진흥기업 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 004440 | 삼일씨엔에스 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | pending | pending | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 001060 | JW중외제약 | investment_decision | volatile | pending | pending | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | pending | pending | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 227610 | 아우딘퓨쳐스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 227610 | 아우딘퓨쳐스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 009290 | 광동제약 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 268280 | 미원에스씨 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 030530 | 원익홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 030530 | 원익홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 030530 | 원익홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 030000 | 제일기획 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 030530 | 원익홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 030530 | 원익홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 030530 | 원익홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 030530 | 원익홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 030530 | 원익홀딩스 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 044380 | 주연테크 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | -4.00 | 0.00 | 0.00 | -4.00 | N/A | N/A | N/A |
| 1970-01-01 | 044380 | 주연테크 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | -4.00 | 0.00 | 0.00 | -4.00 | N/A | N/A | N/A |
| 1970-01-01 | 044380 | 주연테크 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | -4.00 | 0.00 | 0.00 | -4.00 | N/A | N/A | N/A |
| 1970-01-01 | 002360 | SH에너지화학 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | -4.00 | 0.00 | 0.00 | -4.00 | N/A | N/A | N/A |
| 1970-01-01 | 044380 | 주연테크 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | -4.00 | 0.00 | 0.00 | -4.00 | N/A | N/A | N/A |
| 1970-01-01 | 002360 | SH에너지화학 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | -4.00 | 0.00 | 0.00 | -4.00 | N/A | N/A | N/A |
| 1970-01-01 | 044380 | 주연테크 | major_shareholder_change | volatile | pending | pending | insufficient_volume_baseline | -4.00 | 0.00 | 0.00 | -4.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |
| 1970-01-01 | 105550 | 엣지파운드리 | convertible_bond | negative | pending | pending | insufficient_volume_baseline | -30.00 | 0.00 | 0.00 | -30.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
