# Market-Adjusted Evaluation Report - 2026-11-10

Generated at: 2026-11-10 05:37:08

Source feature file: `data/processed/market_adjusted_features_20261110.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **197**
- market_data_missing: **196**
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
| 1970-01-01 | 88280 | 쏘닉스 | negative | failure | market_data_missing | 6.06% | N/A | N/A |
| 1970-01-01 | 70300 | 퀀텀레일 | negative | failure | market_data_missing | 0.75% | N/A | N/A |
| 1970-01-01 | 70300 | 퀀텀레일 | negative | failure | market_data_missing | 0.75% | N/A | N/A |
| 1970-01-01 | 950260 | 인제니아테라퓨틱스 | volatile | success | market_data_missing | 5.72% | N/A | N/A |
| 1970-01-01 | 60260 | 뉴보텍 | negative | success | market_data_missing | -2.52% | N/A | N/A |
| 1970-01-01 | 60260 | 뉴보텍 | negative | success | market_data_missing | -2.52% | N/A | N/A |
| 1970-01-01 | 376930 | 노을 | volatile | success | market_data_missing | 21.77% | N/A | N/A |
| 1970-01-01 | 376930 | 노을 | volatile | success | market_data_missing | 21.77% | N/A | N/A |
| 1970-01-01 | 33250 | 체시스 | negative | failure | market_data_missing | 3.84% | N/A | N/A |
| 1970-01-01 | 33250 | 체시스 | negative | failure | market_data_missing | 3.84% | N/A | N/A |
| 1970-01-01 | 33250 | 체시스 | negative | failure | market_data_missing | 3.84% | N/A | N/A |
| 1970-01-01 | 33250 | 체시스 | negative | failure | market_data_missing | 3.84% | N/A | N/A |
| 1970-01-01 | 33250 | 체시스 | negative | failure | market_data_missing | 3.84% | N/A | N/A |
| 1970-01-01 | 33250 | 체시스 | negative | failure | market_data_missing | 3.84% | N/A | N/A |
| 1970-01-01 | 33250 | 체시스 | negative | failure | market_data_missing | 3.84% | N/A | N/A |
| 1970-01-01 | 33250 | 체시스 | negative | failure | market_data_missing | 3.84% | N/A | N/A |
| 1970-01-01 | 33250 | 체시스 | negative | failure | market_data_missing | 3.84% | N/A | N/A |
| 1970-01-01 | 33250 | 체시스 | negative | failure | market_data_missing | 3.84% | N/A | N/A |
| 1970-01-01 | 33250 | 체시스 | negative | failure | market_data_missing | 3.84% | N/A | N/A |
| 1970-01-01 | 33250 | 체시스 | negative | failure | market_data_missing | 3.84% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
