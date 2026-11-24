# Market-Adjusted Evaluation Report - 2026-11-24

Generated at: 2026-11-24 06:54:17

Source feature file: `data/processed/market_adjusted_features_20261124.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **221**
- market_data_missing: **221**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 009830 | 한화솔루션 | volatile | success | market_data_missing | 5.26% | N/A | N/A |
| 1970-01-01 | 009830 | 한화솔루션 | volatile | success | market_data_missing | 5.26% | N/A | N/A |
| 1970-01-01 | 290560 | 파라택시스이더리움 | negative | failure | market_data_missing | 0.23% | N/A | N/A |
| 1970-01-01 | 276040 | 스코넥 | negative | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 320000 | 한울반도체 | volatile | success | market_data_missing | 3.49% | N/A | N/A |
| 1970-01-01 | 0153R0 | 바로팜 | volatile | failure | market_data_missing | -0.36% | N/A | N/A |
| 1970-01-01 | 006370 | 대구백화점 | negative | success | market_data_missing | -0.59% | N/A | N/A |
| 1970-01-01 | 262260 | 에이프로 | volatile | success | market_data_missing | 8.15% | N/A | N/A |
| 1970-01-01 | 262260 | 에이프로 | volatile | success | market_data_missing | 8.15% | N/A | N/A |
| 1970-01-01 | 033270 | 유나이티드 | volatile | failure | market_data_missing | 1.85% | N/A | N/A |
| 1970-01-01 | 033270 | 유나이티드 | volatile | failure | market_data_missing | 1.85% | N/A | N/A |
| 1970-01-01 | 0220W0 | 한화머시너리앤서비스홀딩스 | negative | success | market_data_missing | -0.13% | N/A | N/A |
| 1970-01-01 | 053210 | 케이티스카이라이프 | volatile | failure | market_data_missing | 0.55% | N/A | N/A |
| 1970-01-01 | 358570 | 지아이이노베이션 | volatile | success | market_data_missing | 12.93% | N/A | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | success | market_data_missing | -1.97% | N/A | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | success | market_data_missing | -1.97% | N/A | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | success | market_data_missing | -1.97% | N/A | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | success | market_data_missing | -1.97% | N/A | N/A |
| 1970-01-01 | 362990 | 드림인사이트 | volatile | success | market_data_missing | -3.60% | N/A | N/A |
| 1970-01-01 | 000720 | 현대건설 | positive | success | market_data_missing | 4.16% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
