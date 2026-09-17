# Market-Adjusted Evaluation Report - 2026-09-17

Generated at: 2026-09-17 01:41:21

Source feature file: `data/processed/market_adjusted_features_20260917.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **212**
- market_data_missing: **212**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 261200 | 덴티스 | negative | success | market_data_missing | -0.58% | N/A | N/A |
| 1970-01-01 | 261200 | 덴티스 | negative | success | market_data_missing | -0.58% | N/A | N/A |
| 1970-01-01 | 261200 | 덴티스 | negative | success | market_data_missing | -0.58% | N/A | N/A |
| 1970-01-01 | 261200 | 덴티스 | negative | success | market_data_missing | -0.58% | N/A | N/A |
| 1970-01-01 | 261200 | 덴티스 | negative | success | market_data_missing | -0.58% | N/A | N/A |
| 1970-01-01 | 261200 | 덴티스 | negative | success | market_data_missing | -0.58% | N/A | N/A |
| 1970-01-01 | 226950 | 올릭스 | volatile | success | market_data_missing | 4.33% | N/A | N/A |
| 1970-01-01 | 443250 | 레뷰코퍼레이션 | volatile | failure | market_data_missing | 0.57% | N/A | N/A |
| 1970-01-01 | 092600 | 앤씨앤 | negative | failure | market_data_missing | 29.89% | N/A | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | negative | success | market_data_missing | -7.98% | N/A | N/A |
| 1970-01-01 | 014970 | 삼륭물산 | negative | failure | market_data_missing | 0.56% | N/A | N/A |
| 1970-01-01 | 079940 | 가비아 | negative | failure | market_data_missing | 4.63% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -4.44% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -4.44% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -4.44% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -4.44% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -4.44% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -4.44% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -4.44% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -4.44% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
