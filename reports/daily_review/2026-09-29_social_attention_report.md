# Social Attention Feature Report - 2026-09-29

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **97**
- High attention rows: **11**
- Medium attention rows: **32**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **61**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 253590 | 네오셈 | supply_contract | 15.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 253590 | 네오셈 | supply_contract | 15.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 253590 | 네오셈 | supply_contract | 15.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 253590 | 네오셈 | supply_contract | 15.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 302430 | 이노메트리 | supply_contract | 15.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 109670 | 씨싸이트 | major_shareholder_change | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 069260 | 티케이지휴켐스 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 475230 | 엔알비 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 475230 | 엔알비 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 475230 | 엔알비 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 475230 | 엔알비 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 251370 | 와이엠티 | convertible_bond | 11.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 294870 | IPARK현대산업개발 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 096770 | SK이노베이션 | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 222080 | SFA넥셀 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 327260 | RF머트리얼즈 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 950250 | 테라뷰 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 460470 | 아이빔테크놀로지 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 092600 | 앤씨앤 | paid_in_capital_increase | 8.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 092600 | 앤씨앤 | paid_in_capital_increase | 8.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
