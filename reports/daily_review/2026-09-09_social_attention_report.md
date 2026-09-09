# Social Attention Feature Report - 2026-09-09

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **61**
- High attention rows: **1**
- Medium attention rows: **30**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **29**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 148250 | 알엔투테크놀로지 | convertible_bond | 15.5 | 0 | 3 | high_attention | no_rumor_signal | risk_noise_detected |
| 226950 | 올릭스 | investment_decision | 11.5 | 4 | 0 | medium_attention | medium_rumor_noise | no_risk_noise |
| 267250 | HD현대 | supply_contract | 10.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 247660 | 나노씨엠에스 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 247660 | 나노씨엠에스 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 247660 | 나노씨엠에스 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 247660 | 나노씨엠에스 | paid_in_capital_increase | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 010960 | 삼호개발 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 076080 | 웰크론한텍 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 002990 | 금호건설 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 047050 | 포스코인터내셔널 | major_shareholder_change | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 128940 | 한미약품 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 009540 | HD한국조선해양 | supply_contract | 7.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 317400 | 자이에스앤디 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 389260 | 대명에너지 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 490470 | 세미파이브 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 033290 | 로젠 | merger | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 033290 | 로젠 | merger | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 033290 | 로젠 | merger | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 033290 | 로젠 | merger | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
