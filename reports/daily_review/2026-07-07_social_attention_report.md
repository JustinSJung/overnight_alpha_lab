# Social Attention Feature Report - 2026-07-07

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **15**
- High attention rows: **0**
- Medium attention rows: **6**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **7**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 101970 | 우양에이치씨 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 047040 | 대우건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 004380 | 삼익THK | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 010140 | 삼성중공업 | major_shareholder_change | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 068240 | 다원시스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 187870 | 디바이스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 253450 | 스튜디오드래곤 | merger | 5.5 | 4 | 0 | low_attention | medium_rumor_noise | no_risk_noise |
| 000720 | 현대건설 | paid_in_capital_increase | 3.5 | 0 | 9 | low_attention | no_rumor_signal | high_risk_noise |
| 019570 | 플루토스 | convertible_bond | 3.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 288980 | 모아데이타 | convertible_bond | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 013520 | 화승코퍼레이션 | major_shareholder_change | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 013720 | 청보 | spin_off | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 368970 | 오에스피 | paid_in_capital_increase | 3.5 | 0 | 3 | low_attention | no_rumor_signal | risk_noise_detected |
| 003070 | 코오롱글로벌 | major_shareholder_change | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 007980 | TP | major_shareholder_change | 3.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
