# Market-Adjusted Evaluation Report - 2026-11-19

Generated at: 2026-11-19 04:22:38

Source feature file: `data/processed/market_adjusted_features_20261119.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **121**
- market_data_missing: **121**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 372320 | 큐로셀 | volatile | failure | market_data_missing | -1.86% | N/A | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | failure | market_data_missing | -1.34% | N/A | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | failure | market_data_missing | -1.34% | N/A | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | failure | market_data_missing | -1.34% | N/A | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | failure | market_data_missing | -1.34% | N/A | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | failure | market_data_missing | -1.34% | N/A | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | failure | market_data_missing | -1.34% | N/A | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | failure | market_data_missing | -1.34% | N/A | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | failure | market_data_missing | -1.34% | N/A | N/A |
| 1970-01-01 | 018620 | 우진비앤지 | volatile | failure | market_data_missing | -1.34% | N/A | N/A |
| 1970-01-01 | 032800 | 판타지오 | negative | success | market_data_missing | -2.17% | N/A | N/A |
| 1970-01-01 | 457600 | 벡트로보틱스 | volatile | success | market_data_missing | 8.99% | N/A | N/A |
| 1970-01-01 | 900100 | 파이온엑스 | negative | success | market_data_missing | -10.15% | N/A | N/A |
| 1970-01-01 | 320000 | 한울반도체 | volatile | success | market_data_missing | -3.43% | N/A | N/A |
| 1970-01-01 | 258790 | 소프트캠프 | negative | success | market_data_missing | -5.94% | N/A | N/A |
| 1970-01-01 | 258790 | 소프트캠프 | negative | success | market_data_missing | -5.94% | N/A | N/A |
| 1970-01-01 | 089150 | 케이씨티 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 003470 | 유안타증권 | volatile | failure | market_data_missing | -1.61% | N/A | N/A |
| 1970-01-01 | 003470 | 유안타증권 | volatile | failure | market_data_missing | -1.61% | N/A | N/A |
| 1970-01-01 | 003470 | 유안타증권 | volatile | failure | market_data_missing | -1.61% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
