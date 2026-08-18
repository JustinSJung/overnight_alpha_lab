# Market-Adjusted Evaluation Report - 2026-08-18

Generated at: 2026-08-18 22:47:57

Source feature file: `data/processed/market_adjusted_features_20260818.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **34**
- pending: **34**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 033540 | 파라텍 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 0009K0 | 에임드바이오 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 418620 | E8 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 010960 | 삼호개발 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 062970 | 한국첨단소재 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 062970 | 한국첨단소재 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 033310 | 엠투엔 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 001740 | SK네트웍스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 001740 | SK네트웍스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 038880 | 아이에이 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 038880 | 아이에이 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 038880 | 아이에이 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 142760 | 모아라이프플러스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 288980 | 모아데이타 | negative | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
