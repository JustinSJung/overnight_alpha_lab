# Social Attention Feature Report - 2026-07-21

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **4**
- High attention rows: **0**
- Medium attention rows: **0**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **3**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 127120 | 제이에스링크 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 215380 | 우정바이오 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 009810 | 플레이그램 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 183490 | 엔지켐생명과학 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
