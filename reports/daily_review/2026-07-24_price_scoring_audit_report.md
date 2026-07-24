# Price Scoring Audit Report - 2026-07-24

This audit documents the conservative v2 price ranker. It is diagnostic only and is not investment advice.
이 문서는 보수적인 v2 가격 랭커를 점검하기 위한 진단 자료이며 투자 조언이 아닙니다.

## Current Score Components

- v1 score: breakout score, 5-day return, 20-day return, volume ratio, volatility penalty, and small social/ML context adjustments.
- v2 score: base momentum plus moderate volume/liquidity confirmation, minus volatility, overextension, reversal, news risk, attention noise, and market regime penalties.
- Score version: **v2_conservative_ranker**
- Broad candidate pool count: **153**
- Selected monitoring picks: **20**

## Suspected Failure Modes

- v1 can over-reward volume spikes and already-exhausted short-term moves.
- v1 has limited penalties for pullback risk after sharp moves.
- News, attention, and social risk are supplementary and may have been too lightly penalized when risk/noise is high.
- Top-ranked buckets have recently underperformed the broad pool, so rank quality needs several more daily observations after v2.

## Conservative Fixes

- Preserve the broad candidate pool for statistical learning.
- Rank selected picks by `final_price_signal_score_v2`, mirrored into existing score columns for evaluator compatibility.
- Reward moderate momentum with volume confirmation instead of automatically favoring the most extreme mover.
- Penalize overextension, reversal risk, attention noise, and risk-heavy news without making news the main engine.
- Avoid stock-specific thresholds, future leakage, or complex ML.

## Component Averages

| Component | Average |
|---|---:|
| final_price_signal_score_v2 | 38.55 |
| base_momentum_score | 47.66 |
| volume_confirmation_score | -1.52 |
| volatility_penalty | 6.19 |
| overextension_penalty | 1.34 |
| reversal_risk_penalty | 1.31 |
| news_risk_penalty | 0.29 |
| attention_noise_penalty | 0.34 |
| market_regime_penalty | 0.01 |

## Notes

V2 scoring impact should be judged after several new daily runs.
V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.