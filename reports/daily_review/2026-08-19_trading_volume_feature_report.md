# Trading Volume Feature Report - 2026-08-19

Generated at: 2026-08-19 22:48:39

Source ML dataset: `data/processed/ml_dataset_20260819.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **107**
- Rows with price file found: **107**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **107**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20260819 | 322780 | 코퍼스코리아 | major_shareholder_change | volatile | N/A | 97,104 | N/A | N/A | 148,963 | N/A |
| 20260819 | 352940 | 인바이오 | disclosure_violation | negative | N/A | 4,463 | N/A | N/A | 1,662 | N/A |
| 20260819 | 002020 | 코오롱 | supply_contract | positive | N/A | 86,413 | N/A | N/A | 985,819 | N/A |
| 20260819 | 003070 | 코오롱글로벌 | supply_contract | positive | N/A | 28,582 | N/A | N/A | 22,321 | N/A |
| 20260819 | 033530 | SJG세종 | merger | volatile | N/A | 99,035 | N/A | N/A | 73,714 | N/A |
| 20260819 | 033530 | SJG세종 | merger | volatile | N/A | 99,035 | N/A | N/A | 73,714 | N/A |
| 20260819 | 033530 | SJG세종 | merger | volatile | N/A | 99,035 | N/A | N/A | 73,714 | N/A |
| 20260819 | 033530 | SJG세종 | merger | volatile | N/A | 99,035 | N/A | N/A | 73,714 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 073190 | 듀오백 | major_shareholder_change | volatile | N/A | 8,920 | N/A | N/A | 15,679 | N/A |
| 20260819 | 389680 | 유디엠텍 | disclosure_violation | negative | N/A | 35,322 | N/A | N/A | 101,412 | N/A |
| 20260819 | 290270 | 휴네시온 | disclosure_violation | negative | N/A | 7,340 | N/A | N/A | 8,406 | N/A |
| 20260819 | 148250 | 알엔투테크놀로지 | disclosure_violation | negative | N/A | 65,885 | N/A | N/A | 44,916 | N/A |
| 20260819 | 210120 | 캔버스엔 | convertible_bond | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260819 | 210120 | 캔버스엔 | convertible_bond | negative | N/A | 0 | N/A | N/A | 0 | N/A |
| 20260819 | 210120 | 캔버스엔 | convertible_bond | negative | N/A | 0 | N/A | N/A | 0 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
