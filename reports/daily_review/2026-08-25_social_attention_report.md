# Social Attention Feature Report - 2026-08-25

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **11**
- High attention rows: **1**
- Medium attention rows: **8**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **4**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 009540 | HD한국조선해양 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 000210 | DL | supply_contract | 11.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 014970 | 삼륭물산 | disclosure_violation | 9.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 069920 | 엑시온그룹 | paid_in_capital_increase | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 034730 | SK | merger | 7.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 000950 | 전방 | major_shareholder_change | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 270520 | 앱튼 | investment_decision | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 375500 | DL이앤씨 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 267250 | HD현대 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 216400 | 인바이츠바이오코아 | disclosure_violation | 5.5 | 0 | 6 | low_attention | no_rumor_signal | risk_noise_detected |
| 006260 | LS | major_shareholder_change | 5.5 | 0 | 0 | low_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
