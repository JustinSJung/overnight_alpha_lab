# Market-Adjusted Evaluation Report - 2026-07-20

Generated at: 2026-07-20 08:43:29

Source feature file: `data/processed/market_adjusted_features_20260720.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **36**
- pending: **36**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 33310 | 엠투엔 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 290720 | 푸드나무 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 389680 | 유디엠텍 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 144510 | 지씨셀 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 78350 | 한양디지텍 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 224060 | 더코디 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 55550 | 신한지주 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 82270 | 젬백스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 33540 | 파라텍 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 112610 | 씨에스윈드 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 112610 | 씨에스윈드 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 354200 | 엔젠바이오 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 3470 | 유안타증권 | volatile | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
