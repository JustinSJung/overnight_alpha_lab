# Market-Adjusted Evaluation Report - 2026-10-23

Generated at: 2026-10-23 01:25:37

Source feature file: `data/processed/market_adjusted_features_20261023.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **144**
- market_data_missing: **143**
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
| 1970-01-01 | 006370 | 대구백화점 | volatile | success | market_data_missing | -2.53% | N/A | N/A |
| 1970-01-01 | 011560 | 세보엠이씨 | positive | failure | market_data_missing | -2.25% | N/A | N/A |
| 1970-01-01 | 396470 | 워트 | positive | failure | market_data_missing | -2.26% | N/A | N/A |
| 1970-01-01 | 000490 | 대동 | negative | success | market_data_missing | -0.85% | N/A | N/A |
| 1970-01-01 | 002990 | 금호건설 | negative | success | market_data_missing | -4.09% | N/A | N/A |
| 1970-01-01 | 002990 | 금호건설 | negative | success | market_data_missing | -4.09% | N/A | N/A |
| 1970-01-01 | 030610 | 교보증권 | negative | success | market_data_missing | -4.49% | N/A | N/A |
| 1970-01-01 | 030610 | 교보증권 | negative | success | market_data_missing | -4.49% | N/A | N/A |
| 1970-01-01 | 030610 | 교보증권 | negative | success | market_data_missing | -4.49% | N/A | N/A |
| 1970-01-01 | 030610 | 교보증권 | negative | success | market_data_missing | -4.49% | N/A | N/A |
| 1970-01-01 | 030610 | 교보증권 | negative | success | market_data_missing | -4.49% | N/A | N/A |
| 1970-01-01 | 030610 | 교보증권 | negative | success | market_data_missing | -4.49% | N/A | N/A |
| 1970-01-01 | 317770 | 엑스페릭스 | negative | success | market_data_missing | -3.30% | N/A | N/A |
| 1970-01-01 | 317770 | 엑스페릭스 | negative | success | market_data_missing | -3.30% | N/A | N/A |
| 1970-01-01 | 066790 | 씨씨에스 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 066790 | 씨씨에스 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 078130 | 에스엠국일 | volatile | failure | market_data_missing | -0.14% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
