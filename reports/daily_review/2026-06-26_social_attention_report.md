# Social Attention Feature Report - 2026-06-26

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **15**
- High attention rows: **1**
- Medium attention rows: **8**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **8**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 033310 | 엠투엔 | major_shareholder_change | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 299660 | 셀리드 | investment_decision | 11.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 007460 | 에이프로젠 | investment_decision | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 013700 | 까뮤이앤씨 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 440110 | 파두 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 005960 | 동부건설 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 300080 | 플리토 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 068270 | 셀트리온 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 054930 | 유신 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 085660 | 차바이오텍 | paid_in_capital_increase | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 001470 | 삼부토건 | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 243070 | 휴온스 | merger | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 211270 | AP위성 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 009730 | 이렘 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 012510 | 더존비즈온 | major_shareholder_change | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
