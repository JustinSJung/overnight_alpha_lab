# Social Attention Feature Report - 2026-08-03

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **20**
- High attention rows: **1**
- Medium attention rows: **12**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **9**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 148250 | 알엔투테크놀로지 | lawsuit | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 032580 | 피델릭스 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 001260 | 남광토건 | investment_decision | 9.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 033310 | 엠투엔 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 031860 | 디에이치엑스컴퍼니 | investment_decision | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 027580 | 상보 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 347700 | 스피어 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 255220 | SG | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 028100 | 동아지질 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 294870 | IPARK현대산업개발 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 227610 | 아우딘퓨쳐스 | convertible_bond | 6.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 047920 | HLB제약 | paid_in_capital_increase | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 060230 | 제이케이시냅스 | convertible_bond | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 223220 | 로지스몬 | lawsuit | 5.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 178320 | 서진시스템 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 012630 | HDC | investment_decision | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 020150 | 롯데에너지머티리얼즈 | major_shareholder_change | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 473980 | 노머스 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 187660 | 페니트리움바이오 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 403490 | 우듬지팜 | spin_off | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
