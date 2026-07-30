# Market-Adjusted Evaluation Report - 2026-07-30

Generated at: 2026-07-30 04:10:02

Source feature file: `data/processed/market_adjusted_features_20260730.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **16**
- pending: **16**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 445090 | 에이직랜드 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 107640 | 한중엔시에스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 107640 | 한중엔시에스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 107640 | 한중엔시에스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 7570 | 일양약품 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 206400 | 베노티앤알 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 80420 | 모다이노칩 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 80420 | 모다이노칩 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 80420 | 모다이노칩 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 420770 | 기가비스 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 25560 | 미래산업 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 460940 | 피앤에스로보틱스 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 11330 | 유니켐 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 402490 | 그린리소스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 402490 | 그린리소스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 104460 | 디와이피엔에프 | positive | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
