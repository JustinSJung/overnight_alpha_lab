# Trading Volume Feature Report - 2026-11-02

Generated at: 2026-11-02 02:02:28

Source ML dataset: `data/processed/ml_dataset_20261102.csv`

## Purpose

This report measures whether disclosure events were followed by meaningful trading volume changes.

Trading volume helps distinguish events that attracted market attention from events that had weak market response.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Summary

- Total rows: **4840**
- Rows with price file found: **4839**

## Volume Reaction Label Counts

- insufficient_volume_baseline: **4839**
- price_file_missing: **1**

## Interpretation

- `extreme_volume_spike`: event or next-day volume was at least 5x the 20-day average.
- `strong_volume_spike`: event or next-day volume was at least 3x the 20-day average.
- `moderate_volume_increase`: event or next-day volume was at least 1.5x the 20-day average.
- `normal_or_weak_volume`: volume reaction was not meaningfully higher than baseline.
- `price_file_missing`: price data was not available for that stock.

## Sample Rows

| event_date | stock_code | corp_name | event_type | prediction_direction | volume_reaction_label | event_day_volume | avg_volume_20d_before | event_volume_ratio_20d | next_day_volume | next_volume_ratio_20d |
|---|---|---|---|---|---|---|---|---|---|---|
| 20261030 | 200350 | 아티스트스튜디오 | major_shareholder_change | volatile | N/A | 634,445 | N/A | N/A | 534,049 | N/A |
| 20261030 | 236810 | 엔비티 | supply_contract | positive | N/A | 14,315 | N/A | N/A | 17,273 | N/A |
| 20261030 | 439580 | 블루엠텍 | convertible_bond | negative | N/A | 477,500 | N/A | N/A | 4,074,774 | N/A |
| 20261030 | 439580 | 블루엠텍 | convertible_bond | negative | N/A | 477,500 | N/A | N/A | 4,074,774 | N/A |
| 20261030 | 439580 | 블루엠텍 | major_shareholder_change | volatile | N/A | 477,500 | N/A | N/A | 4,074,774 | N/A |
| 20261030 | 439580 | 블루엠텍 | major_shareholder_change | volatile | N/A | 477,500 | N/A | N/A | 4,074,774 | N/A |
| 20261030 | 006370 | 대구백화점 | investment_decision | volatile | N/A | 45,414 | N/A | N/A | 52,879 | N/A |
| 20261030 | 101000 | KS인더스트리 | convertible_bond | negative | N/A | 44,370 | N/A | N/A | 82,459 | N/A |
| 20261030 | 101000 | KS인더스트리 | convertible_bond | negative | N/A | 44,370 | N/A | N/A | 82,459 | N/A |
| 20261030 | 066790 | 씨씨에스 | investment_decision | volatile | N/A | 0 | N/A | N/A | 0 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |
| 20261030 | 487720 | 키움제10호스팩 | merger | volatile | N/A | 2,216 | N/A | N/A | 26,957 | N/A |

## Next Step

The next step is to convert volume reaction labels into score adjustment signals and connect them to the daily candidate report.
