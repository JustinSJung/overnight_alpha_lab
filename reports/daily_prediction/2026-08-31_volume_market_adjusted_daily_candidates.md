# Volume + Market-Adjusted Daily Candidate Report - 2026-08-31

Generated at: 2026-08-31 01:14:13

ML dataset source: `data/processed/ml_dataset_20260831.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260831.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20260831.csv`

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
- volatile_watchlist: **351**
- strong_volume_market_adjusted_candidate: **245**
- risk_or_avoid_review: **239**
- watchlist_candidate: **81**
- positive_candidate: **35**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 114190 | 강원에너지 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 004440 | 삼일씨엔에스 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 065710 | 서호전기 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 130.00 | 0.00 | 0.00 | 130.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |
| 1970-01-01 | 317400 | 자이에스앤디 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 125.00 | 0.00 | 0.00 | 125.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 208860 | 다산디엠씨 | spin_off | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 208860 | 다산디엠씨 | spin_off | volatile | success | market_data_missing | insufficient_volume_baseline | 51.00 | 0.00 | 0.00 | 51.00 | N/A | N/A | N/A |
| 1970-01-01 | 001060 | JW중외제약 | investment_decision | volatile | failure | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 032350 | 롯데관광개발 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 154040 | 다산솔루에타 | spin_off | volatile | failure | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 032350 | 롯데관광개발 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 154040 | 다산솔루에타 | spin_off | volatile | failure | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 154040 | 다산솔루에타 | spin_off | volatile | failure | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 154040 | 다산솔루에타 | spin_off | volatile | failure | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 032350 | 롯데관광개발 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 46.00 | 0.00 | 0.00 | 46.00 | N/A | N/A | N/A |
| 1970-01-01 | 161890 | 한국콜마 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 161890 | 한국콜마 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 009290 | 광동제약 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 044380 | 주연테크 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 044380 | 주연테크 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 030530 | 원익홀딩스 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 003030 | 세아제강지주 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 090370 | 메타랩스 | merger | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 002920 | 유성기업 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 002920 | 유성기업 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 002920 | 유성기업 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 002920 | 유성기업 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 033920 | 무학 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 033920 | 무학 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 002360 | SH에너지화학 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 002360 | SH에너지화학 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 214330 | 금호에이치티 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 030000 | 제일기획 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 11.00 | 0.00 | 0.00 | 11.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 6.00 | 0.00 | 0.00 | 6.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 6.00 | 0.00 | 0.00 | 6.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 6.00 | 0.00 | 0.00 | 6.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 6.00 | 0.00 | 0.00 | 6.00 | N/A | N/A | N/A |
| 1970-01-01 | 175250 | 아이큐어 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 6.00 | 0.00 | 0.00 | 6.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | convertible_bond | negative | success | market_data_missing | insufficient_volume_baseline | -10.00 | 0.00 | 0.00 | -10.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
