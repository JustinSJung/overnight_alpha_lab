# Market-Adjusted Evaluation Report - 2026-09-03

Generated at: 2026-09-03 00:53:35

Source feature file: `data/processed/market_adjusted_features_20260903.csv`

## Purpose

This report evaluates prediction results using market-adjusted returns. It helps distinguish event-driven stock reactions from broader market movement.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **250**
- market_data_missing: **250**

## Interpretation

- `market_adjusted_success`: stock moved correctly and outperformed the market.
- `market_driven_weak_success`: stock moved correctly but did not outperform the market.
- `relative_success_but_absolute_loss`: stock fell but outperformed a weaker market.
- `market_adjusted_failure`: stock failed after adjusting for market movement.
- `market_driven_volatility`: movement may be mostly explained by market-wide movement.

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | prediction_result | market_adjusted_result | next_close_return | market_next_close_return | market_adjusted_next_close_return |
|---|---|---|---|---|---|---|---|---|
| 1970-01-01 | 007110 | 일신석재 | positive | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 0009K0 | 에임드바이오 | volatile | failure | market_data_missing | -1.08% | N/A | N/A |
| 1970-01-01 | 066790 | 씨씨에스 | volatile | failure | market_data_missing | 0.00% | N/A | N/A |
| 1970-01-01 | 476060 | 온코닉테라퓨틱스 | volatile | failure | market_data_missing | 0.42% | N/A | N/A |
| 1970-01-01 | 001040 | CJ | negative | success | market_data_missing | -1.53% | N/A | N/A |
| 1970-01-01 | 079160 | CJ CGV | negative | failure | market_data_missing | 0.19% | N/A | N/A |
| 1970-01-01 | 027040 | 서울전자통신 | negative | success | market_data_missing | -0.60% | N/A | N/A |
| 1970-01-01 | 027040 | 서울전자통신 | negative | success | market_data_missing | -0.60% | N/A | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | success | market_data_missing | -10.58% | N/A | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | success | market_data_missing | -10.58% | N/A | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | success | market_data_missing | -10.58% | N/A | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | success | market_data_missing | -10.58% | N/A | N/A |
| 1970-01-01 | 268280 | 미원에스씨 | volatile | failure | market_data_missing | -0.85% | N/A | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | success | market_data_missing | -10.58% | N/A | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | success | market_data_missing | -10.58% | N/A | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | success | market_data_missing | -10.58% | N/A | N/A |
| 1970-01-01 | 069920 | 엑시온그룹 | negative | success | market_data_missing | -10.58% | N/A | N/A |
| 1970-01-01 | 086710 | 선진뷰티사이언스 | negative | success | market_data_missing | -0.26% | N/A | N/A |
| 1970-01-01 | 300080 | 플리토 | positive | success | market_data_missing | 0.11% | N/A | N/A |
| 1970-01-01 | 213420 | 덕산네오룩스 | negative | success | market_data_missing | -5.03% | N/A | N/A |

## Next Step

The next step is to use market-adjusted evaluation results in confidence tracking and daily recommendation scoring.
