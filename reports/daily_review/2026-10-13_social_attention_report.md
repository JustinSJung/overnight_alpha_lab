# Social Attention Feature Report - 2026-10-13

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **92**
- High attention rows: **5**
- Medium attention rows: **34**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **52**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 058730 | 다스코 | supply_contract | 16.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 015590 | DKME | supply_contract | 14.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 091590 | 남화토건 | major_shareholder_change | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 282880 | 코윈로보틱스 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 274400 | 이노시뮬레이션 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 475040 | 스트라드비젼 | supply_contract | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 199480 | 뱅크웨어글로벌 | supply_contract | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 010960 | 삼호개발 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 021320 | KCC건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 021320 | KCC건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 126600 | BGF에코머티리얼즈 | merger | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 017040 | 광명전기 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 021320 | KCC건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 021320 | KCC건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 005320 | 온타이드 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 900100 | 파이온엑스 | paid_in_capital_increase | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 226950 | 올릭스 | investment_decision | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 002020 | 코오롱 | disclosure_violation | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 475150 | SK이터닉스 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 291810 | 핀텔 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
