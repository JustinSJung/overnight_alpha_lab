# Social Attention Feature Report - 2026-08-27

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **4**
- High attention rows: **2**
- Medium attention rows: **1**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **0**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 302430 | 이노메트리 | supply_contract | 16.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 032580 | 피델릭스 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 010400 | 우진아이엔에스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 268280 | 미원에스씨 | major_shareholder_change | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
