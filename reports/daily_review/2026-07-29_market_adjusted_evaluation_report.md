# Market-Adjusted Evaluation Report - 2026-07-29

Generated at: 2026-07-29 23:18:02

Source feature file: `data/processed/market_adjusted_features_20260729.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **20**
- pending: **20**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 115530 | 씨엔플러스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 115530 | 씨엔플러스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 17810 | 풀무원 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 17810 | 풀무원 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 66790 | 씨씨에스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 43260 | 성호전자 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 47040 | 대우건설 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 54220 | 비츠로시스 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 1260 | 남광토건 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 27040 | 서울전자통신 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 10780 | 아이에스동서 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 340360 | 다보링크 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 340360 | 다보링크 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 114190 | 강원에너지 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 114190 | 강원에너지 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 121440 | 골프존홀딩스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 3470 | 유안타증권 | volatile | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
