# Market-Adjusted Evaluation Report - 2026-11-23

Generated at: 2026-11-23 03:32:59

Source feature file: `data/processed/market_adjusted_features_20261123.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **164**
- market_data_missing: **164**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 142760 | 모아라이프플러스 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 7460 | 에이프로젠 | negative | success | market_data_missing | -1.01% | N/A | N/A |
| 1970-01-01 | 7460 | 에이프로젠 | negative | success | market_data_missing | -1.01% | N/A | N/A |
| 1970-01-01 | 7460 | 에이프로젠 | negative | success | market_data_missing | -1.01% | N/A | N/A |
| 1970-01-01 | 7460 | 에이프로젠 | negative | success | market_data_missing | -1.01% | N/A | N/A |
| 1970-01-01 | 7460 | 에이프로젠 | negative | success | market_data_missing | -1.01% | N/A | N/A |
| 1970-01-01 | 7460 | 에이프로젠 | negative | success | market_data_missing | -1.01% | N/A | N/A |
| 1970-01-01 | 7460 | 에이프로젠 | negative | success | market_data_missing | -1.01% | N/A | N/A |
| 1970-01-01 | 7460 | 에이프로젠 | negative | success | market_data_missing | -1.01% | N/A | N/A |
| 1970-01-01 | 214260 | 라파스 | volatile | success | market_data_missing | -8.74% | N/A | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | volatile | success | market_data_missing | -20.12% | N/A | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | volatile | success | market_data_missing | -20.12% | N/A | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | volatile | success | market_data_missing | -20.12% | N/A | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | volatile | success | market_data_missing | -20.12% | N/A | N/A |
| 1970-01-01 | 9620 | 삼보산업 | negative | success | market_data_missing | -6.30% | N/A | N/A |
| 1970-01-01 | 32350 | 롯데관광개발 | volatile | success | market_data_missing | -3.39% | N/A | N/A |
| 1970-01-01 | 32350 | 롯데관광개발 | volatile | success | market_data_missing | -3.39% | N/A | N/A |
| 1970-01-01 | 32350 | 롯데관광개발 | volatile | success | market_data_missing | -3.39% | N/A | N/A |
| 1970-01-01 | 32350 | 롯데관광개발 | volatile | success | market_data_missing | -3.39% | N/A | N/A |
| 1970-01-01 | 332570 | PS일렉트로닉스 | positive | failure | market_data_missing | -5.79% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
