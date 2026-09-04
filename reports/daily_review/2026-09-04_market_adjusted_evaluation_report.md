# Market-Adjusted Evaluation Report - 2026-09-04

Generated at: 2026-09-04 00:44:37

Source feature file: `data/processed/market_adjusted_features_20260904.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **275**
- market_data_missing: **275**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 50090 | 비케이홀딩스 | negative | failure | market_data_missing | 11.99% | N/A | N/A |
| 1970-01-01 | 50090 | 비케이홀딩스 | negative | failure | market_data_missing | 11.99% | N/A | N/A |
| 1970-01-01 | 50090 | 비케이홀딩스 | negative | failure | market_data_missing | 11.99% | N/A | N/A |
| 1970-01-01 | 50090 | 비케이홀딩스 | negative | failure | market_data_missing | 11.99% | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | success | market_data_missing | -3.98% | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | success | market_data_missing | -3.98% | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | success | market_data_missing | -3.98% | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | success | market_data_missing | -3.98% | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | success | market_data_missing | -3.98% | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | success | market_data_missing | -3.98% | N/A | N/A |
| 1970-01-01 | 226330 | 신테카바이오 | negative | success | market_data_missing | -3.00% | N/A | N/A |
| 1970-01-01 | 3490 | 대한항공 | negative | failure | market_data_missing | 2.74% | N/A | N/A |
| 1970-01-01 | 11090 | 에넥스 | negative | failure | market_data_missing | 12.58% | N/A | N/A |
| 1970-01-01 | 101400 | 엔시트론 | volatile | success | market_data_missing | -3.08% | N/A | N/A |
| 1970-01-01 | 101400 | 엔시트론 | volatile | success | market_data_missing | -3.08% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | failure | market_data_missing | -1.24% | N/A | N/A |
| 1970-01-01 | 229000 | 젠큐릭스 | negative | failure | market_data_missing | 1.94% | N/A | N/A |
| 1970-01-01 | 229000 | 젠큐릭스 | negative | failure | market_data_missing | 1.94% | N/A | N/A |
| 1970-01-01 | 229000 | 젠큐릭스 | negative | failure | market_data_missing | 1.94% | N/A | N/A |
| 1970-01-01 | 229000 | 젠큐릭스 | negative | failure | market_data_missing | 1.94% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
