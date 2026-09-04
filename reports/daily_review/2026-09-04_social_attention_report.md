# Social Attention Feature Report - 2026-09-04

## Purpose

This report summarizes investor attention, rumor-noise, and risk-noise signals derived from existing disclosure and news text.

This layer does not treat rumors as facts. It only treats rumor-like language as a noise and attention feature for research purposes.

## Summary

- Total rows: **102**
- High attention rows: **1**
- Medium attention rows: **28**
- Rumor-noise detected rows: **1**
- Risk-noise detected rows: **73**

## Top Social Attention Signals

| stock_code | corp_name | event_type | social_attention_score | rumor_noise_score | risk_noise_score | attention_label | rumor_label | risk_label |
|---|---|---|---|---|---|---|---|---|
| 073490 | LIG아큐버 | supply_contract | 12.5 | 0 | 0 | high_attention | no_rumor_signal | no_risk_noise |
| 340360 | 다보링크 | major_shareholder_change | 10.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 012170 | 아센디오 | supply_contract | 9.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 010960 | 삼호개발 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 002460 | HS화성 | supply_contract | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 187660 | 페니트리움바이오 | investment_decision | 9.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 413630 | 씨피시스템 | convertible_bond | 8.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 011090 | 에넥스 | paid_in_capital_increase | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 003470 | 유안타증권 | major_shareholder_change | 8.5 | 0 | 3 | medium_attention | no_rumor_signal | risk_noise_detected |
| 288980 | 모아데이타 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 006340 | 대원전선 | major_shareholder_change | 8.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 002020 | 코오롱 | supply_contract | 7.5 | 0 | 6 | medium_attention | no_rumor_signal | risk_noise_detected |
| 267250 | HD현대 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 267250 | HD현대 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 267850 | 아시아나IDT | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 009540 | HD한국조선해양 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 002990 | 금호건설 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 003070 | 코오롱글로벌 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 277880 | 티에스아이 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |
| 042660 | 한화오션 | supply_contract | 7.5 | 0 | 0 | medium_attention | no_rumor_signal | no_risk_noise |

## Interpretation

- High social attention may indicate stronger short-term investor interest.
- Rumor-noise should not be interpreted as truth. It is only a noise signal.
- Risk-noise may help explain why seemingly positive events fail.
- This layer should be combined with event score, market-adjusted return, and trading volume reaction.
