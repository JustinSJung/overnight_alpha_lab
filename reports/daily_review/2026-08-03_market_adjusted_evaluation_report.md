# Market-Adjusted Evaluation Report - 2026-08-03

Generated at: 2026-08-03 23:23:52

Source feature file: `data/processed/market_adjusted_features_20260803.csv`

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
| 1970-01-01 | 31860 | 디에이치엑스컴퍼니 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 31860 | 디에이치엑스컴퍼니 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 347700 | 스피어 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 1260 | 남광토건 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 255220 | SG | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 148250 | 알엔투테크놀로지 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 148250 | 알엔투테크놀로지 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 178320 | 서진시스템 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 20150 | 롯데에너지머티리얼즈 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 28100 | 동아지질 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 33310 | 엠투엔 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 27580 | 상보 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 47920 | HLB제약 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 223220 | 로지스몬 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 60230 | 제이케이시냅스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 473980 | 노머스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 473980 | 노머스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 12630 | HDC | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 294870 | IPARK현대산업개발 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 187660 | 페니트리움바이오 | negative | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
