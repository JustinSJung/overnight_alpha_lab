# Market-Adjusted Evaluation Report - 2026-10-08

Generated at: 2026-10-08 04:05:57

Source feature file: `data/processed/market_adjusted_features_20261008.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **134**
- market_data_missing: **133**
- pending: **1**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 7570 | 일양약품 | negative | failure | market_data_missing | 0.25% | N/A | N/A |
| 1970-01-01 | 203400 | 에이비온 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 203400 | 에이비온 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 35200 | 프럼파스트 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 9190 | 대양금속 | volatile | failure | market_data_missing | -0.15% | N/A | N/A |
| 1970-01-01 | 8930 | 한미사이언스 | volatile | success | market_data_missing | -19.18% | N/A | N/A |
| 1970-01-01 | 8930 | 한미사이언스 | volatile | success | market_data_missing | -19.18% | N/A | N/A |
| 1970-01-01 | 8930 | 한미사이언스 | volatile | success | market_data_missing | -19.18% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | failure | market_data_missing | 29.56% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | failure | market_data_missing | 29.56% | N/A | N/A |
| 1970-01-01 | 128940 | 한미약품 | volatile | success | market_data_missing | -7.16% | N/A | N/A |
| 1970-01-01 | 11000 | 진원생명과학 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | failure | market_data_missing | 15.01% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | failure | market_data_missing | 15.01% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | failure | market_data_missing | 15.01% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | failure | market_data_missing | 15.01% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | failure | market_data_missing | 15.01% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | failure | market_data_missing | 15.01% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | failure | market_data_missing | 15.01% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | failure | market_data_missing | 15.01% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
