# Trading Volume Score Integration Report - 2026-11-02

Generated at: 2026-11-02 02:02:29

Source trading volume feature file: `data/processed/trading_volume_features_20261102.csv`

## Purpose

This report converts trading volume reaction labels into recommendation score adjustment signals.

The goal is to reward positive events with strong volume confirmation and penalize negative events with strong volume confirmation.

## Important Notice

This report is generated for research and portfolio purposes only. It is not financial advice or a buy/sell recommendation.

## Score Logic

- Positive event + strong volume spike: positive adjustment
- Positive event + weak volume: conservative negative adjustment
- Negative event + strong volume spike: negative risk adjustment
- Volatile event + strong volume spike: volatility confirmation adjustment

## Summary

- Total rows: **4840**
- Total volume adjustment score: **0.00**
- Average volume adjustment score: **0.00**

## Adjustment Label Counts

- neutral_volume_adjustment: **4840**

## Volume Reaction Counts

- insufficient_volume_baseline: **4839**
- price_file_missing: **1**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | volume_reaction_label | event_volume_ratio_20d | next_volume_ratio_20d | trading_volume_score_adjustment | trading_volume_adjustment_label |
|---|---|---|---|---|---|---|---|---|
| 20261030 | 200350 | 아티스트스튜디오 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 236810 | 엔비티 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 439580 | 블루엠텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 439580 | 블루엠텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 439580 | 블루엠텍 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 439580 | 블루엠텍 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 006370 | 대구백화점 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 101000 | KS인더스트리 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 101000 | KS인더스트리 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 066790 | 씨씨에스 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261030 | 487720 | 키움제10호스팩 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |

## Next Step

The next step is to connect trading volume score adjustment to the market-adjusted daily candidate report.
