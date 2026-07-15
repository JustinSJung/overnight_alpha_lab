# Social Attention Feature Report - 2026-07-15

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **28**
- High attention rows: **1**
- Medium attention rows: **5**
- Rumor-noise detected rows: **2**
- Risk-noise detected rows: **12**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 0009K0 | 에임드바이오 | investment_decision | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 004800 | 효성 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 298040 | 효성중공업 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 127120 | 제이에스링크 | paid_in_capital_increase | 8.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 217730 | 강스템바이오텍 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 235980 | 메드팩토 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003470 | 유안타증권 | major_shareholder_change | 5.5 | 4 | 0 | low_attention | medium_rumor_noise | no_risk_noise |
| 296640 | 이노에이엑스 | merger | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 065420 | 에스아이리소스 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 065420 | 에스아이리소스 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 200230 | 텔콘RF제약 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 013810 | 스페코 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 348370 | 엔켐 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 463480 | 모티브링크 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 079950 | 인베니아 | disclosure_violation | 3.5 | 4 | 3 | low_attention | medium_rumor_noise | risk_noise_detected |
| 004780 | 대륙제관 | disclosure_violation | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 002210 | 동성제약 | disclosure_violation | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 065420 | 에스아이리소스 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 065420 | 에스아이리소스 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 069460 | 대호에이엘 | lawsuit | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
