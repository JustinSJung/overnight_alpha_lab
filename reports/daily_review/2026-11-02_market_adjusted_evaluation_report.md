# Market-Adjusted Evaluation Report - 2026-11-02

Generated at: 2026-11-02 02:02:26

Source feature file: `data/processed/market_adjusted_features_20261102.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **452**
- market_data_missing: **451**
- pending: **1**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 200350 | 아티스트스튜디오 | volatile | success | market_data_missing | 7.00% | N/A | N/A |
| 1970-01-01 | 200350 | 아티스트스튜디오 | volatile | success | market_data_missing | 7.00% | N/A | N/A |
| 1970-01-01 | 200350 | 아티스트스튜디오 | volatile | success | market_data_missing | 7.00% | N/A | N/A |
| 1970-01-01 | 236810 | 엔비티 | positive | failure | market_data_missing | -4.18% | N/A | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | negative | success | market_data_missing | -0.52% | N/A | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | negative | success | market_data_missing | -0.52% | N/A | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | negative | success | market_data_missing | -0.52% | N/A | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | negative | success | market_data_missing | -0.52% | N/A | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | volatile | failure | market_data_missing | -0.52% | N/A | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | volatile | failure | market_data_missing | -0.52% | N/A | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | volatile | failure | market_data_missing | -0.52% | N/A | N/A |
| 1970-01-01 | 439580 | 블루엠텍 | volatile | failure | market_data_missing | -0.52% | N/A | N/A |
| 1970-01-01 | 006370 | 대구백화점 | volatile | failure | market_data_missing | 1.89% | N/A | N/A |
| 1970-01-01 | 006370 | 대구백화점 | volatile | failure | market_data_missing | 1.89% | N/A | N/A |
| 1970-01-01 | 006370 | 대구백화점 | volatile | failure | market_data_missing | 1.89% | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | negative | failure | market_data_missing | 3.07% | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | negative | failure | market_data_missing | 3.07% | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | negative | failure | market_data_missing | 3.07% | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | negative | failure | market_data_missing | 3.07% | N/A | N/A |
| 1970-01-01 | 101000 | KS인더스트리 | negative | failure | market_data_missing | 3.07% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
