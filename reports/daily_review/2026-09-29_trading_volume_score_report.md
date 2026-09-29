# Trading Volume Score Integration Report - 2026-09-29

Generated at: 2026-09-29 03:32:12

Source trading volume feature file: `data/processed/trading_volume_features_20260929.csv`

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

- Total rows: **598996**
- Total volume adjustment score: **0.00**
- Average volume adjustment score: **0.00**

## Adjustment Label Counts

- neutral_volume_adjustment: **598996**

## Volume Reaction Counts

- insufficient_volume_baseline: **598996**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | volume_reaction_label | event_volume_ratio_20d | next_volume_ratio_20d | trading_volume_score_adjustment | trading_volume_adjustment_label |
|---|---|---|---|---|---|---|---|---|
| 20260928 | 402030 | 코난테크놀로지 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 092040 | 아미코젠 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 206400 | 베노티앤알 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 222080 | SFA넥셀 | positive | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 306620 | 지아이에스 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20260928 | 250030 | 진코스텍 | negative | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |

## Next Step

The next step is to connect trading volume score adjustment to the market-adjusted daily candidate report.
