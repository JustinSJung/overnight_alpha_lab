# Social Attention Feature Report - 2026-10-09

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **95**
- High attention rows: **6**
- Medium attention rows: **36**
- Rumor-noise detected rows: **4**
- Risk-noise detected rows: **66**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 007820 | 엠엑스로보틱스 | supply_contract | 17.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 058730 | 다스코 | supply_contract | 16.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 057680 | 티사이언티픽 | supply_contract | 13.5 | 0 | 6 | high_attention | no_rumor_signal | risk_noise_detected |
| 399720 | 가온칩스 | supply_contract | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 147760 | 피엠티 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 282720 | 금양그린파워 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 148250 | 알엔투테크놀로지 | major_shareholder_change | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 046940 | 우원개발 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 082740 | 한화엔진 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 119650 | KC코트렐 | supply_contract | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 210120 | 빅텐츠 | disclosure_violation | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 210120 | 빅텐츠 | disclosure_violation | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 210120 | 빅텐츠 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 210120 | 빅텐츠 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 043340 | 에쎈테크 | spin_off | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 226950 | 올릭스 | investment_decision | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 340360 | 다보링크 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 340360 | 다보링크 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 340360 | 다보링크 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 340360 | 다보링크 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
