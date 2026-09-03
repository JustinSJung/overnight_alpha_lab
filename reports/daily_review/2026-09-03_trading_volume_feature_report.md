# Trading Volume Feature Report - 2026-09-03

Generated at: 2026-09-03 00:53:59

Source ML dataset: `data/processed/ml_dataset_20260903.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **2257673**
- Rows with price file found: **2257673**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **2257673**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260902 | 007110 | 일신석재 | supply_contract | positive | N/A | 166,434 | N/A | N/A | 276,992 | N/A |
| 20260902 | 0009K0 | 에임드바이오 | investment_decision | volatile | N/A | 392,787 | N/A | N/A | 186,010 | N/A |
| 20260902 | 066790 | 씨씨에스 | major_shareholder_change | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260902 | 476060 | 온코닉테라퓨틱스 | investment_decision | volatile | N/A | 785,874 | N/A | N/A | 350,568 | N/A |
| 20260902 | 001040 | CJ | lawsuit | negative | N/A | 117,849 | N/A | N/A | 138,862 | N/A |
| 20260902 | 079160 | CJ CGV | lawsuit | negative | N/A | 308,597 | N/A | N/A | 375,772 | N/A |
| 20260902 | 027040 | 서울전자통신 | paid_in_capital_increase | negative | N/A | 26,970 | N/A | N/A | 771,502 | N/A |
| 20260902 | 027040 | 서울전자통신 | paid_in_capital_increase | negative | N/A | 26,970 | N/A | N/A | 771,502 | N/A |
| 20260902 | 027040 | 서울전자통신 | paid_in_capital_increase | negative | N/A | 26,970 | N/A | N/A | 771,502 | N/A |
| 20260902 | 027040 | 서울전자통신 | paid_in_capital_increase | negative | N/A | 26,970 | N/A | N/A | 771,502 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |
| 20260902 | 069920 | 엑시온그룹 | paid_in_capital_increase | negative | N/A | 427,036 | N/A | N/A | 246,053 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
