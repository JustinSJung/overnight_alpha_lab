# Market-Adjusted Evaluation Report - 2026-07-21

Generated at: 2026-07-21 23:15:36

Source feature file: `data/processed/market_adjusted_features_20260721.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **27**
- pending: **27**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 66790 | 씨씨에스 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 348950 | 제이알글로벌리츠 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 397030 | 에이프릴바이오 | volatile | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 6220 | 제주은행 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 66430 | 아이로보틱스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 106240 | 파인테크닉스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 276730 | 한울앤제주 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 53580 | 웹케시 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 71950 | 코아스 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 179530 | 애드바이오텍 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 159910 | 에코글로우 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 119850 | 지엔씨에너지 | positive | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 340810 | 시선AI | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | negative | pending | pending | N/A | N/A | N/A |
| 1970-01-01 | 900120 | 씨엑스아이 | negative | pending | pending | N/A | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
