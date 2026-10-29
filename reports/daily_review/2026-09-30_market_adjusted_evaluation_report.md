# Market-Adjusted Evaluation Report - 2026-09-30

Generated at: 2026-09-30 02:55:23

Source feature file: `data/processed/market_adjusted_features_20260930.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **206**
- market_data_missing: **206**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 079940 | 가비아 | negative | success | market_data_missing | -0.25% | N/A | N/A |
| 1970-01-01 | 079940 | 가비아 | negative | success | market_data_missing | -0.25% | N/A | N/A |
| 1970-01-01 | 079940 | 가비아 | negative | success | market_data_missing | -0.25% | N/A | N/A |
| 1970-01-01 | 079940 | 가비아 | negative | success | market_data_missing | -0.25% | N/A | N/A |
| 1970-01-01 | 079940 | 가비아 | negative | success | market_data_missing | -0.25% | N/A | N/A |
| 1970-01-01 | 079940 | 가비아 | negative | success | market_data_missing | -0.25% | N/A | N/A |
| 1970-01-01 | 010580 | 에스엠벡셀 | volatile | failure | market_data_missing | -0.81% | N/A | N/A |
| 1970-01-01 | 010580 | 에스엠벡셀 | volatile | failure | market_data_missing | -0.81% | N/A | N/A |
| 1970-01-01 | 008930 | 한미사이언스 | volatile | failure | market_data_missing | 1.73% | N/A | N/A |
| 1970-01-01 | 008930 | 한미사이언스 | volatile | failure | market_data_missing | 1.73% | N/A | N/A |
| 1970-01-01 | 128940 | 한미약품 | volatile | failure | market_data_missing | 1.00% | N/A | N/A |
| 1970-01-01 | 128940 | 한미약품 | volatile | failure | market_data_missing | 1.00% | N/A | N/A |
| 1970-01-01 | 128940 | 한미약품 | volatile | failure | market_data_missing | 1.00% | N/A | N/A |
| 1970-01-01 | 089030 | 테크윙 | positive | success | market_data_missing | 0.19% | N/A | N/A |
| 1970-01-01 | 089030 | 테크윙 | positive | success | market_data_missing | 0.19% | N/A | N/A |
| 1970-01-01 | 000430 | 대원강업 | volatile | failure | market_data_missing | -0.75% | N/A | N/A |
| 1970-01-01 | 000430 | 대원강업 | volatile | failure | market_data_missing | -0.75% | N/A | N/A |
| 1970-01-01 | 000430 | 대원강업 | volatile | failure | market_data_missing | -0.75% | N/A | N/A |
| 1970-01-01 | 073570 | 리튬포어스 | negative | failure | market_data_missing | 0.80% | N/A | N/A |
| 1970-01-01 | 066790 | 씨씨에스 | negative | failure | market_data_missing | 0.00% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
