# Price Scoring Audit Report - 2026-08-04

This audit documents the conservative v2 price ranker. It is diagnostic only and is not investment advice.
이 문서는 보수적인 v2 가격 랭커를 점검하기 위한 진단 자료이며 투자 조언이 아닙니다.

## Current Score Components

- v1 score: breakout score, 5-day return, 20-day return, volume ratio, volatility penalty, and small social/ML context adjustments.
- v2 score: base momentum plus moderate volume/liquidity confirmation, minus volatility, overextension, reversal, news risk, attention noise, and market regime penalties.
- v3 experimental score: stability-first diagnostic ranker that favors moderate confirmed momentum and penalizes noisy extremes more strongly.
- Score version: **v2_conservative_ranker**
- Experimental score version: **v3_stability_ranker**
- Broad candidate pool count: **231**
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
| final_price_signal_score_v2 | 44.39 |
| final_price_signal_score_v3 | 43.04 |
| base_momentum_score | 52.08 |
| volume_confirmation_score | -0.41 |
| volatility_penalty | 6.17 |
| overextension_penalty | 1.79 |
| reversal_risk_penalty | 1.23 |
| news_risk_penalty | 0.17 |
| attention_noise_penalty | 0.22 |
| market_regime_penalty | 0.08 |
| v3_momentum_quality_score | 41.51 |
| v3_volume_quality_score | -0.05 |
| v3_liquidity_quality_score | 2.50 |
| v3_stability_score | 6.91 |
| v3_overextension_penalty | 4.44 |
| v3_reversal_penalty | 3.41 |
| v3_noise_penalty | 0.69 |

## Notes

V2 scoring impact should be judged after several new daily runs.
V2 점수 산식 효과는 며칠 이상 신규 데이터가 쌓인 뒤 판단해야 합니다.
V3 is diagnostic only and does not replace selected_pick.
V3는 진단용이며 selected_pick 기준을 대체하지 않습니다.