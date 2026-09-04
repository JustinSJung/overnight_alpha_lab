# Volume + Market-Adjusted Daily Candidate Report - 2026-09-04

Generated at: 2026-09-04 00:45:04

ML dataset source: `data/processed/ml_dataset_20260904.csv`
Market-adjusted score source: `data/processed/market_adjusted_score_adjustments_20260904.csv`
Trading volume score source: `data/processed/trading_volume_score_adjustments_20260904.csv`

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

- Total rows: **1547**
- risk_or_avoid_review: **1059**
- volatile_watchlist: **434**
- strong_volume_market_adjusted_candidate: **25**
- positive_candidate: **16**
- watchlist_candidate: **13**

## Strong Volume + Market-Adjusted Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 277880 | 티에스아이 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 140.00 | 0.00 | 0.00 | 140.00 | N/A | N/A | N/A |
| 1970-01-01 | 012170 | 아센디오 | supply_contract | positive | failure | market_data_missing | insufficient_volume_baseline | 135.00 | 0.00 | 0.00 | 135.00 | N/A | N/A | N/A |
| 1970-01-01 | 042660 | 한화오션 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 042660 | 한화오션 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 042660 | 한화오션 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 042660 | 한화오션 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 010960 | 삼호개발 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 120.00 | 0.00 | 0.00 | 120.00 | N/A | N/A | N/A |
| 1970-01-01 | 073490 | LIG아큐버 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 115.00 | 0.00 | 0.00 | 115.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 267850 | 아시아나IDT | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |
| 1970-01-01 | 003070 | 코오롱글로벌 | supply_contract | positive | success | market_data_missing | insufficient_volume_baseline | 100.00 | 0.00 | 0.00 | 100.00 | N/A | N/A | N/A |

## Strong Market-Adjusted Candidates

No candidates in this section.

## Volume-Confirmed Candidates

No candidates in this section.

## Positive Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 003470 | 유안타증권 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 101400 | 엔시트론 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 101400 | 엔시트론 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 56.00 | 0.00 | 0.00 | 56.00 | N/A | N/A | N/A |
| 1970-01-01 | 006340 | 대원전선 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 006340 | 대원전선 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 41.00 | 0.00 | 0.00 | 41.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |
| 1970-01-01 | 267250 | HD현대 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 36.00 | 0.00 | 0.00 | 36.00 | N/A | N/A | N/A |

## Watchlist Candidates

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 002710 | TCC스틸 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 002710 | TCC스틸 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 002710 | TCC스틸 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 268280 | 미원에스씨 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 085620 | 미래에셋생명 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 011780 | 금호석유화학 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 31.00 | 0.00 | 0.00 | 31.00 | N/A | N/A | N/A |
| 1970-01-01 | 096240 | 크레버스 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 096240 | 크레버스 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 096240 | 크레버스 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 340360 | 다보링크 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 340360 | 다보링크 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 340360 | 다보링크 | major_shareholder_change | volatile | success | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |
| 1970-01-01 | 051630 | 진양화학 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 26.00 | 0.00 | 0.00 | 26.00 | N/A | N/A | N/A |

## Volatile Watchlist

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 305090 | 마이크로디지탈 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 305090 | 마이크로디지탈 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |
| 1970-01-01 | 214420 | 토니모리 | major_shareholder_change | volatile | failure | market_data_missing | insufficient_volume_baseline | 16.00 | 0.00 | 0.00 | 16.00 | N/A | N/A | N/A |

## High-Attention Risk Review

No candidates in this section.

## Risk / Avoid Review

| event_date | stock_code | corp_name | event_type | prediction_direction | prediction_result | market_adjusted_result | volume_reaction_label | base_recommendation_score_v3 | market_adjusted_score_adjustment | trading_volume_score_adjustment | final_volume_market_adjusted_score | market_adjusted_next_close_return | event_volume_ratio_20d | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | paid_in_capital_increase | negative | success | market_data_missing | insufficient_volume_baseline | -40.00 | 0.00 | 0.00 | -40.00 | N/A | N/A | N/A |

## General Review

No candidates in this section.

## Next Step

The next step is to compare this v3 report with the existing recommender and decide which score components should be merged into the main daily stock recommender.
