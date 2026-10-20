# Market-Adjusted Evaluation Report - 2026-10-20

Generated at: 2026-10-20 01:45:21

Source feature file: `data/processed/market_adjusted_features_20261020.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **140**
- market_data_missing: **139**
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
| 1970-01-01 | 059270 | 해성에어로보틱스 | negative | success | market_data_missing | -2.67% | N/A | N/A |
| 1970-01-01 | 302550 | 리메드 | negative | success | market_data_missing | -0.79% | N/A | N/A |
| 1970-01-01 | 302550 | 리메드 | negative | success | market_data_missing | -0.79% | N/A | N/A |
| 1970-01-01 | 207490 | 에이펙스인텍 | negative | failure | market_data_missing | 3.12% | N/A | N/A |
| 1970-01-01 | 032820 | 우리기술 | positive | failure | market_data_missing | -5.67% | N/A | N/A |
| 1970-01-01 | 032820 | 우리기술 | positive | failure | market_data_missing | -5.67% | N/A | N/A |
| 1970-01-01 | 032820 | 우리기술 | positive | failure | market_data_missing | -5.67% | N/A | N/A |
| 1970-01-01 | 032820 | 우리기술 | positive | failure | market_data_missing | -5.67% | N/A | N/A |
| 1970-01-01 | 377450 | 리파인 | negative | failure | market_data_missing | 0.36% | N/A | N/A |
| 1970-01-01 | 018500 | 동원모빌리티 | negative | success | market_data_missing | -0.38% | N/A | N/A |
| 1970-01-01 | 465770 | STX그린로지스 | negative | success | market_data_missing | -2.53% | N/A | N/A |
| 1970-01-01 | 010960 | 삼호개발 | positive | failure | market_data_missing | -0.98% | N/A | N/A |
| 1970-01-01 | 000210 | DL | volatile | success | market_data_missing | -2.68% | N/A | N/A |
| 1970-01-01 | 000210 | DL | volatile | success | market_data_missing | -2.68% | N/A | N/A |
| 1970-01-01 | 000210 | DL | volatile | success | market_data_missing | -2.68% | N/A | N/A |
| 1970-01-01 | 011300 | 우성머티리얼스 | negative | success | market_data_missing | -4.09% | N/A | N/A |
| 1970-01-01 | 375500 | DL이앤씨 | volatile | success | market_data_missing | -5.63% | N/A | N/A |
| 1970-01-01 | 033310 | 엠투엔 | volatile | failure | market_data_missing | -0.73% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | failure | market_data_missing | 0.00% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
