# Social Attention Feature Report - 2026-09-24

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **76**
- High attention rows: **1**
- Medium attention rows: **26**
- Rumor-noise detected rows: **2**
- Risk-noise detected rows: **48**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 004440 | 삼일씨엔에스 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 224060 | 더코디 | paid_in_capital_increase | 11.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 109670 | 씨싸이트 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 014790 | HL D&I | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 101360 | 에코앤드림 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 000720 | 현대건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 016740 | 두올 | major_shareholder_change | 7.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 009160 | SIMPAC | investment_decision | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 079940 | 가비아 | major_shareholder_change | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 079940 | 가비아 | major_shareholder_change | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 083650 | 비에이치아이 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 001360 | 삼성제약 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 005250 | 녹십자홀딩스 | major_shareholder_change | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 091590 | 남화토건 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 064350 | 현대로템 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 475400 | 씨메스로보틱스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 068270 | 셀트리온 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 326030 | 에스케이바이오팜 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 377480 | 마음AI | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 347700 | 스피어 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
