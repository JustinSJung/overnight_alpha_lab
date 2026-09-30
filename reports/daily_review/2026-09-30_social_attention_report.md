# Social Attention Feature Report - 2026-09-30

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **102**
- High attention rows: **7**
- Medium attention rows: **41**
- Rumor-noise detected rows: **5**
- Risk-noise detected rows: **45**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 003030 | 세아제강지주 | supply_contract | 18.5 | 4 | 0 | high_attention | medium_rumor_noise | no_risk_noise |
| 306200 | 세아제강 | supply_contract | 18.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 368770 | 파이버프로 | supply_contract | 17.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 469750 | 아이비젼웍스 | supply_contract | 15.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 264450 | 유비쿼스 | supply_contract | 15.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 017000 | 신원종합개발 | supply_contract | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 010580 | 에스엠벡셀 | major_shareholder_change | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 010960 | 삼호개발 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 490470 | 세미파이브 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 302550 | 리메드 | supply_contract | 10.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 069260 | 티케이지휴켐스 | supply_contract | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 032580 | 피델릭스 | supply_contract | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 099750 | 이지케어텍 | investment_decision | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 224110 | 에이텍모빌리티 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 267320 | 나인테크 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 009150 | 삼성전기 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 008930 | 한미사이언스 | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 232140 | 와이씨 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 347700 | 스피어 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 092600 | 앤씨앤 | investment_decision | 8.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
