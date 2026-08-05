# Social Attention Feature Report - 2026-08-05

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **7**
- High attention rows: **0**
- Medium attention rows: **3**
- Rumor-noise detected rows: **2**
- Risk-noise detected rows: **5**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 380540 | 옵티코어 | convertible_bond | 7.5 | 4 | 3 | medium_attention | medium_rumor_noise | risk_noise_detected |
| 276040 | 스코넥 | major_shareholder_change | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 001260 | 남광토건 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 011810 | STX | investment_decision | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 004990 | 롯데지주 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 000950 | 전방 | major_shareholder_change | 3.5 | 4 | 3 | low_attention | medium_rumor_noise | risk_noise_detected |
| 252500 | 세화피앤씨 | spin_off | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
