# Market-Adjusted Evaluation Report - 2026-08-11

Generated at: 2026-08-11 23:08:31

Source feature file: `data/processed/market_adjusted_features_20260811.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **45**
- pending: **45**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 6060 | 화승인더스트리 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 348370 | 엔켐 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 6370 | 대구백화점 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 6370 | 대구백화점 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 263750 | 펄어비스 | neutral_positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 263750 | 펄어비스 | neutral_positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 68240 | 다원시스 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 65420 | 에스아이리소스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 378800 | 샤페론 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 89860 | 롯데렌탈 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 89860 | 롯데렌탈 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 187660 | 페니트리움바이오 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 33270 | 유나이티드 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 60230 | 제이케이시냅스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 60230 | 제이케이시냅스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 272110 | 케이엔제이 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 272110 | 케이엔제이 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 128940 | 한미약품 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 128940 | 한미약품 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 128940 | 한미약품 | volatile | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
