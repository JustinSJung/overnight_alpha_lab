# Social Attention Feature Report - 2026-09-14

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **92**
- High attention rows: **5**
- Medium attention rows: **32**
- Rumor-noise detected rows: **3**
- Risk-noise detected rows: **48**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 056730 | CNT85 | supply_contract | 14.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 013360 | 일성건설 | supply_contract | 14.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 012450 | 한화에어로스페이스 | supply_contract | 13.5 | 4 | 0 | high_attention | medium_rumor_noise | no_risk_noise |
| 389680 | 유디엠텍 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 389680 | 유디엠텍 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 272210 | 한화시스템 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 383310 | 에코프로에이치엔 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 028050 | 삼성E&A | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 282880 | 코윈테크 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 288980 | 모아데이타 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 389680 | 유디엠텍 | disclosure_violation | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 389680 | 유디엠텍 | disclosure_violation | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 347700 | 스피어 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 097230 | HJ중공업 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 101680 | 한국정밀기계 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 004770 | 써니전자 | major_shareholder_change | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 011090 | 에넥스 | investment_decision | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 011090 | 에넥스 | investment_decision | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 026910 | 광진실업 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 307870 | 비투엔 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
