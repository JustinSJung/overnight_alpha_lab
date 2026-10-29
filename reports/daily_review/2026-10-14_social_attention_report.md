# Social Attention Feature Report - 2026-10-14

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **80**
- High attention rows: **7**
- Medium attention rows: **56**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **36**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 320000 | 한울반도체 | paid_in_capital_increase | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 320000 | 한울반도체 | paid_in_capital_increase | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 320000 | 한울반도체 | paid_in_capital_increase | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 320000 | 한울반도체 | paid_in_capital_increase | 13.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 083930 | 아바코 | supply_contract | 13.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 227950 | 엔투텍 | convertible_bond | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 417200 | LS머트리얼즈 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 003580 | HLB글로벌 | merger | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 006260 | LS | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 006740 | 블루산업개발 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 307180 | 아이엘 | convertible_bond | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 047040 | 대우건설 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 010960 | 삼호개발 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 452450 | 피아이이 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 336260 | 두산퓨얼셀 | bond_with_warrant | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 336260 | 두산퓨얼셀 | bond_with_warrant | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 089860 | 롯데렌탈 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 000400 | 롯데손해보험 | investment_decision | 7.5 | 4 | 3 | medium_attention | medium_rumor_noise | risk_noise_detected |
| 363280 | 티와이홀딩스 | supply_contract | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 900100 | 파이온엑스 | paid_in_capital_increase | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
