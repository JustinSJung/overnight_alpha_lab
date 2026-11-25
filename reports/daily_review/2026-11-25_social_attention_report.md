# Social Attention Feature Report - 2026-11-25

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **73**
- High attention rows: **2**
- Medium attention rows: **35**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **38**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 216400 | 인바이츠바이오코아 | convertible_bond | 14.5 | 0 | 9 | high_attention | no_rumor_signal | high_risk_noise |
| 270520 | 앱튼 | investment_decision | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 347770 | 핌스 | major_shareholder_change | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 080420 | 모다이노칩 | spin_off | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 034730 | SK | merger | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 482680 | 미래에셋비전스팩7호 | merger | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 086390 | 유니테스트 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 122640 | 예스티 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 361610 | SK아이이테크놀로지 | merger | 9.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 010960 | 삼호개발 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 373110 | 엑셀세라퓨틱스 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 097230 | HJ중공업 | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 097230 | HJ중공업 | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 096770 | SK이노베이션 | merger | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 093050 | LF | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 097230 | HJ중공업 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 097230 | HJ중공업 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
