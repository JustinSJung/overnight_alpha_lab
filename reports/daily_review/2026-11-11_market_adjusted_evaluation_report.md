# Market-Adjusted Evaluation Report - 2026-11-11

Generated at: 2026-11-11 06:02:41

Source feature file: `data/processed/market_adjusted_features_20261111.csv`

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
| 1970-01-01 | 65420 | 에스아이리소스 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 10960 | 삼호개발 | positive | success | market_data_missing | 0.17% | N/A | N/A |
| 1970-01-01 | 10960 | 삼호개발 | positive | success | market_data_missing | 0.17% | N/A | N/A |
| 1970-01-01 | 247540 | 에코프로비엠 | negative | failure | market_data_missing | 11.82% | N/A | N/A |
| 1970-01-01 | 247540 | 에코프로비엠 | negative | failure | market_data_missing | 11.82% | N/A | N/A |
| 1970-01-01 | 307180 | 아이엘 | negative | failure | market_data_missing | 2.18% | N/A | N/A |
| 1970-01-01 | 66790 | 씨씨에스 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 300080 | 플리토 | positive | success | market_data_missing | 0.65% | N/A | N/A |
| 1970-01-01 | 300080 | 플리토 | positive | success | market_data_missing | 0.65% | N/A | N/A |
| 1970-01-01 | 5880 | 대한해운 | volatile | failure | market_data_missing | -0.21% | N/A | N/A |
| 1970-01-01 | 5880 | 대한해운 | volatile | failure | market_data_missing | -0.21% | N/A | N/A |
| 1970-01-01 | 5880 | 대한해운 | volatile | failure | market_data_missing | -0.21% | N/A | N/A |
| 1970-01-01 | 1200 | 유진증권 | volatile | failure | market_data_missing | 1.44% | N/A | N/A |
| 1970-01-01 | 185490 | 아이진 | volatile | success | market_data_missing | -2.08% | N/A | N/A |
| 1970-01-01 | 124500 | 아이티센글로벌 | volatile | failure | market_data_missing | 1.69% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | failure | market_data_missing | 3.41% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | failure | market_data_missing | 3.41% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | failure | market_data_missing | 3.41% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | failure | market_data_missing | 3.41% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | failure | market_data_missing | 3.41% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
