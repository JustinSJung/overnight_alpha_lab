# Market-Adjusted Evaluation Report - 2026-09-08

Generated at: 2026-09-08 01:05:16

Source feature file: `data/processed/market_adjusted_features_20260908.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **147**
- market_data_missing: **147**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 294870 | IPARK현대산업개발 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 012630 | HDC | negative | failure | market_data_missing | 1.52% | N/A | N/A |
| 1970-01-01 | 083790 | CG인바이츠 | positive | failure | market_data_missing | -0.76% | N/A | N/A |
| 1970-01-01 | 056090 | 시지메드텍 | volatile | success | market_data_missing | -3.13% | N/A | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | negative | success | market_data_missing | -0.55% | N/A | N/A |
| 1970-01-01 | 320000 | 한울반도체 | volatile | failure | market_data_missing | -1.08% | N/A | N/A |
| 1970-01-01 | 001260 | 남광토건 | volatile | failure | market_data_missing | -0.26% | N/A | N/A |
| 1970-01-01 | 001260 | 남광토건 | volatile | failure | market_data_missing | -0.26% | N/A | N/A |
| 1970-01-01 | 001260 | 남광토건 | volatile | failure | market_data_missing | -0.26% | N/A | N/A |
| 1970-01-01 | 001260 | 남광토건 | volatile | failure | market_data_missing | -0.26% | N/A | N/A |
| 1970-01-01 | 001260 | 남광토건 | volatile | failure | market_data_missing | -0.26% | N/A | N/A |
| 1970-01-01 | 001260 | 남광토건 | volatile | failure | market_data_missing | -0.26% | N/A | N/A |
| 1970-01-01 | 006490 | 프리티 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 078930 | GS | volatile | failure | market_data_missing | 0.88% | N/A | N/A |
| 1970-01-01 | 023440 | 제이스코홀딩스 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | -2.66% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | -2.66% | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | volatile | success | market_data_missing | -2.66% | N/A | N/A |
| 1970-01-01 | 310210 | 보로노이 | volatile | failure | market_data_missing | -1.93% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
