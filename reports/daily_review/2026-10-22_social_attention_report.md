# Social Attention Feature Report - 2026-10-22

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **90**
- High attention rows: **9**
- Medium attention rows: **40**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **56**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 126340 | 비나텍 | supply_contract | 13.5 | 0 | 6 | high_attention | no_rumor_signal | risk_noise_detected |
| 126340 | 비나텍 | supply_contract | 13.5 | 0 | 6 | high_attention | no_rumor_signal | risk_noise_detected |
| 126340 | 비나텍 | supply_contract | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 126340 | 비나텍 | supply_contract | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 013580 | 계룡건설산업 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 460940 | 피앤에스로보틱스 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 028260 | 삼성물산 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 036190 | 금화피에스시 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 001260 | 남광토건 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 274400 | 이노시뮬레이션 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 043100 | 알파AI | disclosure_violation | 10.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 267250 | HD현대 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003010 | 혜인 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 357880 | SKAI | convertible_bond | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 355390 | 크라우드웍스 | disclosure_violation | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 023350 | 한국종합기술 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 086390 | 유니테스트 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 069920 | 엑시온그룹 | convertible_bond | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 099520 | DGI | major_shareholder_change | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 038060 | 루멘스바이오스 | convertible_bond | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
