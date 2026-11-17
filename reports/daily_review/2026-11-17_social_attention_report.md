# Social Attention Feature Report - 2026-11-17

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **80**
- High attention rows: **2**
- Medium attention rows: **38**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **38**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 178320 | 서진시스템 | convertible_bond | 12.5 | 0 | 6 | high_attention | no_rumor_signal | risk_noise_detected |
| 009320 | 아진전자부품 | major_shareholder_change | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 457600 | 벡트로보틱스 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 052460 | 아이크래프트 | supply_contract | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 052460 | 아이크래프트 | supply_contract | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 052460 | 아이크래프트 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 052460 | 아이크래프트 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 299480 | 지앤이헬스케어 | disclosure_violation | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 034020 | 두산에너빌리티 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 226330 | 신테카바이오 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 226330 | 신테카바이오 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 226330 | 신테카바이오 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 226330 | 신테카바이오 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 137080 | 나래나노텍 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 001440 | 대한전선 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 039200 | 오스코텍 | lawsuit | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 090710 | 휴림로봇 | investment_decision | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 358570 | 지아이이노베이션 | investment_decision | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 137400 | 피엔티 | supply_contract | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 340810 | 시선AI | convertible_bond | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
