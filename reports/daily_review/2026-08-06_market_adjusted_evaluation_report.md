# Market-Adjusted Evaluation Report - 2026-08-06

Generated at: 2026-08-06 23:59:34

Source feature file: `data/processed/market_adjusted_features_20260806.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **25**
- pending: **25**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 42370 | 비츠로테크 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 163730 | 핑거 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 64800 | 포니링크 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 457600 | 벡트 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 457600 | 벡트 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 488900 | 비츠로넥스텍 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 9190 | 대양금속 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 9190 | 대양금속 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 9190 | 대양금속 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 9190 | 대양금속 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 79950 | 인베니아 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 215570 | 크로넥스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 9190 | 대양금속 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 9190 | 대양금속 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 9190 | 대양금속 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 9190 | 대양금속 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 115450 | HLB테라퓨틱스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 376270 | HEM파마 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 199800 | 툴젠 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | negative | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
