# Social Attention Feature Report - 2026-10-20

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **77**
- High attention rows: **2**
- Medium attention rows: **35**
- Rumor-noise detected rows: **2**
- Risk-noise detected rows: **34**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 033310 | 엠투엔 | major_shareholder_change | 16.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 456160 | 지투지바이오 | investment_decision | 13.5 | 0 | 6 | high_attention | no_rumor_signal | risk_noise_detected |
| 032820 | 우리기술 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010960 | 삼호개발 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 028100 | 동아지질 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 082270 | 젬백스 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 420770 | 기가비스 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 025560 | 미래산업 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 009410 | 태영건설 | investment_decision | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 235980 | 메드팩토 | investment_decision | 7.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 126340 | 비나텍 | supply_contract | 7.5 | 0 | 9 | medium_attention | no_rumor_signal | high_risk_noise |
| 126340 | 비나텍 | supply_contract | 7.5 | 0 | 9 | medium_attention | no_rumor_signal | high_risk_noise |
| 126340 | 비나텍 | supply_contract | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 126340 | 비나텍 | supply_contract | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 009150 | 삼성전기 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 006260 | LS | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 375500 | DL이앤씨 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 025950 | 동신건설 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 032620 | GC메디아이 | major_shareholder_change | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 234300 | 에스트래픽 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
