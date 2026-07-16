# Market-Adjusted Evaluation Report - 2026-07-16

Generated at: 2026-07-16 23:14:05

Source feature file: `data/processed/market_adjusted_features_20260716.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **18**
- pending: **18**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 9320 | 아진전자부품 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 80010 | 이상네트웍스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 11000 | 진원생명과학 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 11000 | 진원생명과학 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 97230 | HJ중공업 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 42940 | 상지건설 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 66790 | 씨씨에스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 11300 | 우성머티리얼스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 11300 | 우성머티리얼스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 54940 | 엑사이엔씨 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 320000 | 한울반도체 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 320000 | 한울반도체 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 320000 | 한울반도체 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 320000 | 한울반도체 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 2810 | 삼영무역 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 2810 | 삼영무역 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 4890 | 동일산업 | volatile | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
