# Market-Adjusted Evaluation Report - 2026-06-24

Generated at: 2026-06-24 22:05:53

Source feature file: `data/processed/market_adjusted_features_20260624.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **11**
- pending: **11**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 43260 | 성호전자 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 83790 | CG인바이츠 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 61040 | 알에프텍 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 396470 | 워트 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 452260 | 한화갤러리아 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 36620 | 감성코퍼레이션 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 307870 | 비투엔 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 97780 | 에코볼트 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 52710 | 아모텍 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 123690 | 한국화장품 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 3350 | 한국화장품제조 | volatile | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
