# Market-Adjusted Evaluation Report - 2026-11-25

Generated at: 2026-11-25 05:30:52

Source feature file: `data/processed/market_adjusted_features_20261125.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **130**
- market_data_missing: **130**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 97230 | HJ중공업 | volatile | failure | market_data_missing | 0.29% | N/A | N/A |
| 1970-01-01 | 97230 | HJ중공업 | volatile | failure | market_data_missing | 0.29% | N/A | N/A |
| 1970-01-01 | 97230 | HJ중공업 | volatile | failure | market_data_missing | 0.29% | N/A | N/A |
| 1970-01-01 | 97230 | HJ중공업 | volatile | failure | market_data_missing | 0.29% | N/A | N/A |
| 1970-01-01 | 39200 | 오스코텍 | negative | failure | market_data_missing | 9.73% | N/A | N/A |
| 1970-01-01 | 363250 | 진시스템 | negative | success | market_data_missing | -6.31% | N/A | N/A |
| 1970-01-01 | 363250 | 진시스템 | negative | success | market_data_missing | -6.31% | N/A | N/A |
| 1970-01-01 | 262260 | 에이프로 | volatile | failure | market_data_missing | -1.58% | N/A | N/A |
| 1970-01-01 | 10960 | 삼호개발 | positive | failure | market_data_missing | -0.17% | N/A | N/A |
| 1970-01-01 | 96240 | 크레버스 | volatile | success | market_data_missing | 2.30% | N/A | N/A |
| 1970-01-01 | 270520 | 앱튼 | volatile | failure | market_data_missing | 1.09% | N/A | N/A |
| 1970-01-01 | 34730 | SK | volatile | success | market_data_missing | -7.58% | N/A | N/A |
| 1970-01-01 | 96770 | SK이노베이션 | volatile | failure | market_data_missing | -0.44% | N/A | N/A |
| 1970-01-01 | 65570 | 삼영이엔씨 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 361610 | SK아이이테크놀로지 | volatile | success | market_data_missing | -2.16% | N/A | N/A |
| 1970-01-01 | 361610 | SK아이이테크놀로지 | volatile | success | market_data_missing | -2.16% | N/A | N/A |
| 1970-01-01 | 361610 | SK아이이테크놀로지 | volatile | success | market_data_missing | -2.16% | N/A | N/A |
| 1970-01-01 | 299660 | 셀리드 | negative | success | market_data_missing | -0.99% | N/A | N/A |
| 1970-01-01 | 13580 | 계룡건설산업 | positive | failure | market_data_missing | -0.40% | N/A | N/A |
| 1970-01-01 | 86520 | 에코프로 | negative | failure | market_data_missing | 0.00% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
