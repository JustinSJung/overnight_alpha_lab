# Trading Volume Feature Report - 2026-09-15

Generated at: 2026-09-15 01:44:43

Source ML dataset: `data/processed/ml_dataset_20260915.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **344**
- Rows with price file found: **342**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **342**
- price_file_missing: **2**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260914 | 079190 | 케스피온 | major_shareholder_change | volatile | N/A | 1,378,255 | N/A | N/A | 1,980,386 | N/A |
| 20260914 | 079190 | 케스피온 | major_shareholder_change | volatile | N/A | 1,378,255 | N/A | N/A | 1,980,386 | N/A |
| 20260914 | 331920 | 셀레믹스 | paid_in_capital_increase | negative | N/A | 15,961 | N/A | N/A | 34,205 | N/A |
| 20260914 | 340810 | 시선AI | convertible_bond | negative | N/A | 194,583 | N/A | N/A | 148,007 | N/A |
| 20260914 | 032790 | 엠젠솔루션 | lawsuit | negative | N/A | 85,349 | N/A | N/A | 49,466 | N/A |
| 20260914 | 002780 | 진흥기업 | supply_contract | positive | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260914 | 058110 | 멕아이씨에스 | paid_in_capital_increase | negative | N/A | 59,779 | N/A | N/A | 33,228 | N/A |
| 20260914 | 389020 | 자람테크놀로지 | supply_contract | positive | N/A | 45,532 | N/A | N/A | 31,400 | N/A |
| 20260914 | 222080 | SFA넥셀 | supply_contract | positive | N/A | 545,833 | N/A | N/A | 382,466 | N/A |
| 20260914 | 027740 | 마니커 | major_shareholder_change | volatile | N/A | 198,060 | N/A | N/A | 206,002 | N/A |
| 20260914 | 038870 | 에코심플렉스 | supply_contract | positive | N/A | 15,684 | N/A | N/A | 6,313 | N/A |
| 20260914 | 002210 | 동성제약 | lawsuit | negative | N/A | 637,950 | N/A | N/A | 162,921 | N/A |
| 20260914 | 003550 | LG | major_shareholder_change | volatile | N/A | 362,313 | N/A | N/A | 285,777 | N/A |
| 20260914 | 226330 | 신테카바이오 | convertible_bond | negative | N/A | 1,638,923 | N/A | N/A | 1,228,494 | N/A |
| 20260914 | 226330 | 신테카바이오 | convertible_bond | negative | N/A | 1,638,923 | N/A | N/A | 1,228,494 | N/A |
| 20260914 | 226330 | 신테카바이오 | convertible_bond | negative | N/A | 1,638,923 | N/A | N/A | 1,228,494 | N/A |
| 20260914 | 226330 | 신테카바이오 | convertible_bond | negative | N/A | 1,638,923 | N/A | N/A | 1,228,494 | N/A |
| 20260914 | 004800 | 효성 | supply_contract | positive | N/A | 23,981 | N/A | N/A | 14,397 | N/A |
| 20260914 | 005800 | 신영와코루 | disclosure_violation | negative | N/A | 3,391 | N/A | N/A | 7,391 | N/A |
| 20260914 | 298040 | 효성중공업 | supply_contract | positive | N/A | 48,904 | N/A | N/A | 31,283 | N/A |
| 20260914 | 024810 | 이화전기공업 | spin_off | volatile | N/A | N/A | N/A | N/A | N/A | N/A |
| 20260914 | 424870 | 이뮨온시아 | investment_decision | volatile | N/A | 224,268 | N/A | N/A | 140,487 | N/A |
| 20260914 | 424870 | 이뮨온시아 | investment_decision | volatile | N/A | 224,268 | N/A | N/A | 140,487 | N/A |
| 20260914 | 424870 | 이뮨온시아 | investment_decision | volatile | N/A | 224,268 | N/A | N/A | 140,487 | N/A |
| 20260914 | 424870 | 이뮨온시아 | investment_decision | volatile | N/A | 224,268 | N/A | N/A | 140,487 | N/A |
| 20260914 | 424870 | 이뮨온시아 | investment_decision | volatile | N/A | 224,268 | N/A | N/A | 140,487 | N/A |
| 20260914 | 424870 | 이뮨온시아 | investment_decision | volatile | N/A | 224,268 | N/A | N/A | 140,487 | N/A |
| 20260914 | 424870 | 이뮨온시아 | investment_decision | volatile | N/A | 224,268 | N/A | N/A | 140,487 | N/A |
| 20260914 | 424870 | 이뮨온시아 | investment_decision | volatile | N/A | 224,268 | N/A | N/A | 140,487 | N/A |
| 20260914 | 424870 | 이뮨온시아 | investment_decision | volatile | N/A | 224,268 | N/A | N/A | 140,487 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
