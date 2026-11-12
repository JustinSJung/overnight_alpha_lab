# Trading Volume Score Integration Report - 2026-11-12

Generated at: 2026-11-12 03:55:00

Source trading volume feature file: `data/processed/trading_volume_features_20261112.csv`

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

- Total rows: **27342**
- Total volume adjustment score: **0.00**
- Average volume adjustment score: **0.00**

## Adjustment Label Counts

- neutral_volume_adjustment: **27342**

## Volume Reaction Counts

- insufficient_volume_baseline: **27342**

## Sample Rows

| event_date | stock_code | corp_name | prediction_direction | volume_reaction_label | event_volume_ratio_20d | next_volume_ratio_20d | trading_volume_score_adjustment | trading_volume_adjustment_label |
|---|---|---|---|---|---|---|---|---|
| 20261111 | 007540 | 샘표 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 248170 | 샘표식품 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 009190 | 대양금속 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |
| 20261111 | 026910 | 광진실업 | volatile | insufficient_volume_baseline | N/A | N/A | 0.00 | neutral_volume_adjustment |

## Next Step

The next step is to connect trading volume score adjustment to the market-adjusted daily candidate report.
