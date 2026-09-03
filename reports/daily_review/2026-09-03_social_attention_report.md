# Social Attention Feature Report - 2026-09-03

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **82**
- High attention rows: **4**
- Medium attention rows: **36**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **48**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 000640 | 동아쏘시오홀딩스 | major_shareholder_change | 15.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 015590 | DKME | lawsuit | 13.5 | 0 | 6 | high_attention | no_rumor_signal | risk_noise_detected |
| 196170 | 알테오젠 | investment_decision | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 469750 | 아이비젼웍스 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 008040 | 사조동아원 | major_shareholder_change | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 493330 | 지에프아이 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 007110 | 일신석재 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 083650 | 비에이치아이 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 036530 | SNT홀딩스 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 336260 | 두산퓨얼셀 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 213420 | 덕산네오룩스 | paid_in_capital_increase | 8.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 090470 | 제이스로보틱스 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 090470 | 제이스로보틱스 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 0009K0 | 에임드바이오 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 476060 | 온코닉테라퓨틱스 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 300080 | 플리토 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 002790 | 아모레퍼시픽홀딩스 | major_shareholder_change | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 060980 | HL홀딩스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 014790 | HL D&I | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 234300 | 에스트래픽 | merger | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
