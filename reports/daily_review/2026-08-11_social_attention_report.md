# Social Attention Feature Report - 2026-08-11

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **6**
- High attention rows: **1**
- Medium attention rows: **5**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **3**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 420770 | 기가비스 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 126880 | 제이엔케이글로벌 | supply_contract | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 126880 | 제이엔케이글로벌 | supply_contract | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 126880 | 제이엔케이글로벌 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 126880 | 제이엔케이글로벌 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 060230 | 제이케이시냅스 | convertible_bond | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
