# Market-Adjusted Evaluation Report - 2026-07-02

Generated at: 2026-07-02 00:00:00

Source feature file: `data/processed/market_adjusted_features_20260702.csv`

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
| 1970-01-01 | 1360 | 삼성제약 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 143210 | 핸즈코퍼레이션 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 143210 | 핸즈코퍼레이션 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 10960 | 삼호개발 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 10960 | 삼호개발 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 10960 | 삼호개발 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 10960 | 삼호개발 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 14680 | 한솔케미칼 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 14680 | 한솔케미칼 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 14680 | 한솔케미칼 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 14680 | 한솔케미칼 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 7280 | 한국특강 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 7280 | 한국특강 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | negative | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
