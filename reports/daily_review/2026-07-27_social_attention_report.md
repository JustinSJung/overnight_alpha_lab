# Social Attention Feature Report - 2026-07-27

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **35**
- High attention rows: **1**
- Medium attention rows: **12**
- Rumor-noise detected rows: **0**
- Risk-noise detected rows: **11**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 282720 | 금양그린파워 | supply_contract | 12.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 065420 | 에스아이리소스 | spin_off | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 001630 | 종근당홀딩스 | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 185750 | 종근당 | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 059270 | 해성에어로보틱스 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 062970 | 한국첨단소재 | convertible_bond | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 065650 | 하이퍼코퍼레이션 | convertible_bond | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 475400 | 씨메스로보틱스 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 900120 | 씨엑스아이 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 006060 | 화승인더스트리 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 006060 | 화승인더스트리 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 006060 | 화승인더스트리 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 337840 | 유엑스엔 | convertible_bond | 6.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 290270 | 휴네시온 | disclosure_violation | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 028260 | 삼성물산 | major_shareholder_change | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 006060 | 화승인더스트리 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 006060 | 화승인더스트리 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 006060 | 화승인더스트리 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 006060 | 화승인더스트리 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |
| 006060 | 화승인더스트리 | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
