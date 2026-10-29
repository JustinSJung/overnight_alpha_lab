# Market-Adjusted Evaluation Report - 2026-10-29

Generated at: 2026-10-29 02:25:44

Source feature file: `data/processed/market_adjusted_features_20261029.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **385**
- market_data_missing: **384**
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
| 1970-01-01 | 196170 | 알테오젠 | volatile | success | market_data_missing | -2.46% | N/A | N/A |
| 1970-01-01 | 009190 | 대양금속 | negative | failure | market_data_missing | 1.47% | N/A | N/A |
| 1970-01-01 | 009190 | 대양금속 | negative | failure | market_data_missing | 1.47% | N/A | N/A |
| 1970-01-01 | 002020 | 코오롱 | negative | success | market_data_missing | -4.09% | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | negative | success | market_data_missing | -6.85% | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | negative | success | market_data_missing | -6.85% | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | negative | success | market_data_missing | -6.85% | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | negative | success | market_data_missing | -6.85% | N/A | N/A |
| 1970-01-01 | 065650 | 하이퍼코퍼레이션 | negative | failure | market_data_missing | 0.17% | N/A | N/A |
| 1970-01-01 | 424870 | 이뮨온시아 | negative | success | market_data_missing | -3.86% | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | success | market_data_missing | -9.30% | N/A | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | volatile | success | market_data_missing | -17.51% | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | negative | success | market_data_missing | -0.81% | N/A | N/A |
| 1970-01-01 | 005300 | 롯데칠성음료 | volatile | failure | market_data_missing | 1.47% | N/A | N/A |
| 1970-01-01 | 361610 | SK아이이테크놀로지 | volatile | success | market_data_missing | -4.14% | N/A | N/A |
| 1970-01-01 | 361610 | SK아이이테크놀로지 | volatile | success | market_data_missing | -4.14% | N/A | N/A |
| 1970-01-01 | 065060 | 지엔코 | negative | success | market_data_missing | -2.75% | N/A | N/A |
| 1970-01-01 | 065060 | 지엔코 | negative | success | market_data_missing | -2.75% | N/A | N/A |
| 1970-01-01 | 065060 | 지엔코 | negative | success | market_data_missing | -2.75% | N/A | N/A |
| 1970-01-01 | 065060 | 지엔코 | negative | success | market_data_missing | -2.75% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
