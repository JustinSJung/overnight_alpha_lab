# Market-Adjusted Evaluation Report - 2026-09-09

Generated at: 2026-09-09 00:53:42

Source feature file: `data/processed/market_adjusted_features_20260909.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **135**
- market_data_missing: **135**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 203400 | 에이비온 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 5930 | 삼성전자 | volatile | failure | market_data_missing | 0.56% | N/A | N/A |
| 1970-01-01 | 199730 | 바이오인프라 | volatile | failure | market_data_missing | -1.21% | N/A | N/A |
| 1970-01-01 | 199730 | 바이오인프라 | volatile | failure | market_data_missing | -1.21% | N/A | N/A |
| 1970-01-01 | 20120 | 키다리스튜디오 | volatile | failure | market_data_missing | 1.82% | N/A | N/A |
| 1970-01-01 | 9320 | 아진전자부품 | volatile | failure | market_data_missing | 0.43% | N/A | N/A |
| 1970-01-01 | 9320 | 아진전자부품 | volatile | failure | market_data_missing | 0.43% | N/A | N/A |
| 1970-01-01 | 10960 | 삼호개발 | positive | success | market_data_missing | 0.65% | N/A | N/A |
| 1970-01-01 | 27410 | BGF | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 27040 | 서울전자통신 | negative | success | market_data_missing | -0.06% | N/A | N/A |
| 1970-01-01 | 27040 | 서울전자통신 | negative | success | market_data_missing | -0.06% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | success | market_data_missing | -0.90% | N/A | N/A |
| 1970-01-01 | 126600 | BGF에코머티리얼즈 | volatile | failure | market_data_missing | 1.04% | N/A | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | negative | failure | market_data_missing | 1.40% | N/A | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | negative | failure | market_data_missing | 1.40% | N/A | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | negative | failure | market_data_missing | 1.40% | N/A | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | negative | failure | market_data_missing | 1.40% | N/A | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | negative | failure | market_data_missing | 1.40% | N/A | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | negative | failure | market_data_missing | 1.40% | N/A | N/A |
| 1970-01-01 | 247660 | 나노씨엠에스 | negative | failure | market_data_missing | 1.40% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
