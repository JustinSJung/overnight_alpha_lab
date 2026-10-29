# Market-Adjusted Evaluation Report - 2026-10-13

Generated at: 2026-10-13 03:53:59

Source feature file: `data/processed/market_adjusted_features_20261013.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **189**
- market_data_missing: **189**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 142760 | 모아라이프플러스 | negative | failure | market_data_missing | 15.88% | N/A | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | negative | failure | market_data_missing | 15.88% | N/A | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | negative | failure | market_data_missing | 15.88% | N/A | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | negative | failure | market_data_missing | 15.88% | N/A | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | negative | failure | market_data_missing | 15.88% | N/A | N/A |
| 1970-01-01 | 34730 | SK | positive | failure | market_data_missing | -7.28% | N/A | N/A |
| 1970-01-01 | 6490 | 프리티 | negative | success | market_data_missing | -8.30% | N/A | N/A |
| 1970-01-01 | 6490 | 프리티 | negative | success | market_data_missing | -8.30% | N/A | N/A |
| 1970-01-01 | 6490 | 프리티 | negative | success | market_data_missing | -8.30% | N/A | N/A |
| 1970-01-01 | 6490 | 프리티 | negative | success | market_data_missing | -8.30% | N/A | N/A |
| 1970-01-01 | 91590 | 남화토건 | volatile | success | market_data_missing | -4.76% | N/A | N/A |
| 1970-01-01 | 96770 | SK이노베이션 | positive | failure | market_data_missing | -0.98% | N/A | N/A |
| 1970-01-01 | 226340 | 본느 | volatile | success | market_data_missing | -9.60% | N/A | N/A |
| 1970-01-01 | 6490 | 프리티 | negative | success | market_data_missing | -8.30% | N/A | N/A |
| 1970-01-01 | 6490 | 프리티 | negative | success | market_data_missing | -8.30% | N/A | N/A |
| 1970-01-01 | 6490 | 프리티 | negative | success | market_data_missing | -8.30% | N/A | N/A |
| 1970-01-01 | 6490 | 프리티 | negative | success | market_data_missing | -8.30% | N/A | N/A |
| 1970-01-01 | 2020 | 코오롱 | negative | success | market_data_missing | -5.00% | N/A | N/A |
| 1970-01-01 | 2020 | 코오롱 | negative | success | market_data_missing | -5.00% | N/A | N/A |
| 1970-01-01 | 5940 | NH투자증권 | volatile | success | market_data_missing | -2.05% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
