# Market-Adjusted Evaluation Report - 2026-11-20

Generated at: 2026-11-20 04:02:12

Source feature file: `data/processed/market_adjusted_features_20261120.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **144**
- market_data_missing: **144**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 28300 | HLB | volatile | failure | market_data_missing | -1.25% | N/A | N/A |
| 1970-01-01 | 424870 | 이뮨온시아 | negative | success | market_data_missing | -0.63% | N/A | N/A |
| 1970-01-01 | 900270 | 헝셩그룹 | negative | success | market_data_missing | -6.98% | N/A | N/A |
| 1970-01-01 | 290690 | 아리바이오홀딩스 | negative | success | market_data_missing | -6.71% | N/A | N/A |
| 1970-01-01 | 78350 | 한양디지텍 | negative | success | market_data_missing | -14.60% | N/A | N/A |
| 1970-01-01 | 78350 | 한양디지텍 | negative | success | market_data_missing | -14.60% | N/A | N/A |
| 1970-01-01 | 78350 | 한양디지텍 | negative | success | market_data_missing | -14.60% | N/A | N/A |
| 1970-01-01 | 431190 | 케이쓰리아이 | negative | success | market_data_missing | -3.10% | N/A | N/A |
| 1970-01-01 | 28260 | 삼성물산 | positive | failure | market_data_missing | -6.74% | N/A | N/A |
| 1970-01-01 | 28260 | 삼성물산 | positive | failure | market_data_missing | -6.74% | N/A | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | success | market_data_missing | -28.38% | N/A | N/A |
| 1970-01-01 | 355390 | 크라우드웍스 | negative | success | market_data_missing | -28.38% | N/A | N/A |
| 1970-01-01 | 53210 | 케이티스카이라이프 | volatile | failure | market_data_missing | -0.40% | N/A | N/A |
| 1970-01-01 | 53210 | 케이티스카이라이프 | volatile | failure | market_data_missing | -0.40% | N/A | N/A |
| 1970-01-01 | 53210 | 케이티스카이라이프 | volatile | failure | market_data_missing | -0.40% | N/A | N/A |
| 1970-01-01 | 53210 | 케이티스카이라이프 | volatile | failure | market_data_missing | -0.40% | N/A | N/A |
| 1970-01-01 | 53210 | 케이티스카이라이프 | volatile | failure | market_data_missing | -0.40% | N/A | N/A |
| 1970-01-01 | 53210 | 케이티스카이라이프 | volatile | failure | market_data_missing | -0.40% | N/A | N/A |
| 1970-01-01 | 67630 | HLB생명과학 | volatile | success | market_data_missing | 17.51% | N/A | N/A |
| 1970-01-01 | 67630 | HLB생명과학 | volatile | success | market_data_missing | 17.51% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
