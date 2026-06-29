# Trading Volume Score Integration Report - 2026-06-29

Generated at: 2026-06-29 01:36:33

Source trading volume feature file: `Not found`

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

## Status

No trading volume score adjustment data is available yet.
