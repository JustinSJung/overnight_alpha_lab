# Market-Adjusted Evaluation Report - 2026-10-16

Generated at: 2026-10-16 00:50:06

Source feature file: `data/processed/market_adjusted_features_20261016.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **243**
- market_data_missing: **243**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 019570 | GMI벤처 | volatile | success | market_data_missing | 4.18% | N/A | N/A |
| 1970-01-01 | 019570 | GMI벤처 | volatile | success | market_data_missing | 4.18% | N/A | N/A |
| 1970-01-01 | 033310 | 엠투엔 | volatile | failure | market_data_missing | 0.22% | N/A | N/A |
| 1970-01-01 | 031860 | 디에이치엑스컴퍼니 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 336570 | 원텍 | negative | failure | market_data_missing | 5.79% | N/A | N/A |
| 1970-01-01 | 336570 | 원텍 | negative | failure | market_data_missing | 5.79% | N/A | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | volatile | success | market_data_missing | 23.96% | N/A | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | volatile | success | market_data_missing | 23.96% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | 6.76% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | 6.76% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | 6.76% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | 6.76% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | 6.76% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | 6.76% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | 6.76% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | 6.76% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | 6.76% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | 6.76% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | 6.76% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | 6.76% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
