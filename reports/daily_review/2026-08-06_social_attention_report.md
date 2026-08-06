# Social Attention Feature Report - 2026-08-06

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **3**
- High attention rows: **1**
- Medium attention rows: **0**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **2**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 028100 | 동아지질 | supply_contract | 19.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 009460 | 한창제지 | lawsuit | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 086820 | 바이오솔루션 | convertible_bond | 3.5 | 0 | 9 | low_attention | no_rumor_signal | high_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
